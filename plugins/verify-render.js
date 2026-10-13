/**
 * Comprobaciones que `pnpm validate` no puede hacer.
 *
 * `validate-assets` confirma que un archivo referenciado existe. Esto verifica
 * cosas que un archivo existente todavía puede hacer mal: no pintar nada,
 * declarar una proporción que no es la suya, precargarse dos veces, nombrar una
 * fuente que nadie sirve, o resolver con un valor inventado lo que debería ser
 * un token. Trabaja sobre `dist/`, así que se ejecuta después del build.
 *
 *     node plugins/verify-render.js
 */

import { readFileSync, existsSync } from 'node:fs';
import { resolve, join, basename } from 'node:path';
import { glob } from 'glob';
import sharp from 'sharp';
import pc from 'picocolors';

const raiz = process.cwd();
const dist = resolve(raiz, 'dist');

const fallos = [];
const avisos = [];
const falla = (archivo, mensaje) => fallos.push({ archivo, mensaje });
const avisa = (archivo, mensaje) => avisos.push({ archivo, mensaje });

if (!existsSync(dist)) {
    console.error(pc.red('No hay dist/. Ejecutar `pnpm build` antes.'));
    process.exit(1);
}

// ── utilidades de parseo ───────────────────────────────────────────────────
// Basta una expresión regular: el marcado lo genera el build, no una persona.
const etiquetas = (html, nombre) => [...html.matchAll(new RegExp(`<${nombre}\\b[^>]*>`, 'gi'))].map(m => m[0]);
const atributo = (etiqueta, nombre) => etiqueta.match(new RegExp(`\\b${nombre}=["']([^"']*)["']`, 'i'))?.[1] ?? null;
const rutas = (srcset) => (srcset || '').split(',').map(c => c.trim().split(/\s+/)[0]).filter(Boolean);

const resolverDesdeDist = (ruta) => {
    if (!ruta || /^(https?:|data:|#)/.test(ruta)) return null;
    return resolve(dist, ruta.replace(/^\.?\//, ''));
};

// ── 1. ¿el asset pinta algo? ───────────────────────────────────────────────
// Un SVG con un clipPath vacío es un archivo válido, con peso y sin errores,
// que no dibuja nada. Sólo se distingue rasterizándolo y midiendo.
const pintados = new Map();

const pinta = async (archivo) => {
    if (pintados.has(archivo)) return pintados.get(archivo);

    let resultado;

    try {
        const { data, info } = await sharp(archivo, { density: 72 })
            .resize(64, 64, { fit: 'inside', withoutEnlargement: true })
            .ensureAlpha()
            .raw()
            .toBuffer({ resolveWithObject: true });

        let visibles = 0;

        for (let i = 3; i < data.length; i += info.channels) {
            if (data[i] > 8) visibles += 1;
        }

        resultado = visibles;
    } catch {
        resultado = null; // sharp no lo entiende; no es asunto de esta comprobación
    }

    pintados.set(archivo, resultado);

    return resultado;
};

// ── 2. proporción declarada contra proporción real ─────────────────────────
const proporcion = async (archivo) => {
    try {
        const { width, height } = await sharp(archivo).metadata();

        return width && height ? width / height : null;
    } catch {
        return null;
    }
};

// ── recorrido de las páginas construidas ───────────────────────────────────
// Una imagen la puede servir el marcado o el CSS: un LCP de fondo se declara en
// una regla `background-image`, y precargarlo es justo lo que hay que hacer.
// Mirar solo el marcado convierte esa práctica en un fallo. Las rutas del CSS
// son relativas a su propia carpeta, así que la comparación va por nombre.
const hojas = (await glob('assets/styles/*.css', { cwd: dist, absolute: true }))
    .map(f => readFileSync(f, 'utf8'))
    .join('\n');

let spriteVacioAvisado = false;

const paginas = await glob('**/*.html', { cwd: dist, absolute: true });

// Cadenas de clases del marcado construido, para las comprobaciones 7 y 8.
const clases = [];

for (const pagina of paginas) {
    const html = readFileSync(pagina, 'utf8');
    const nombre = basename(pagina);

    for (const [, valor] of html.matchAll(/\bclass=["']([^"']+)["']/g)) {
        clases.push({ nombre, valor });
    }

    // imágenes y sus candidatos
    for (const etiqueta of [...etiquetas(html, 'img'), ...etiquetas(html, 'source')]) {
        const candidatos = [
            ...(atributo(etiqueta, 'src') ? [atributo(etiqueta, 'src')] : []),
            ...rutas(atributo(etiqueta, 'srcset')),
        ];

        for (const candidato of candidatos) {
            const archivo = resolverDesdeDist(candidato);

            if (!archivo || !existsSync(archivo)) continue;

            const visibles = await pinta(archivo);

            if (visibles === 0) {
                falla(nombre, `${candidato} no pinta ningún píxel; el archivo existe pero está vacío`);
            }
        }

        // La proporción se compara contra el primer candidato, que es el que el
        // navegador usa para reservar el hueco.
        const ancho = Number(atributo(etiqueta, 'width'));
        const alto = Number(atributo(etiqueta, 'height'));
        const primero = resolverDesdeDist(candidatos[0]);

        if (ancho && alto && primero && existsSync(primero)) {
            const real = await proporcion(primero);

            // Lo que importa no es la diferencia de proporción sino el salto que
            // produce: el navegador reserva `alto` y lo corrige a `ancho / real`
            // al cargar. Hacen falta las dos condiciones, no una. La proporción
            // sola marca iconos diminutos donde medio píxel ya es un 6%; los
            // píxeles solos marcan el redondeo del `viewBox` de un logotipo, que
            // no descuadra nada. Un export que no corresponde al frame cruza las
            // dos: 320×200 declarados sobre un archivo de 320×286.
            if (real) {
                const corregido = ancho / real;
                const salto = Math.abs(alto - corregido);
                const desvio = (salto / alto) * 100;

                if (salto > 2 && desvio > 5) {
                    falla(nombre, `${candidatos[0]} declara ${ancho}×${alto} pero el archivo obliga a ${corregido.toFixed(1)} de alto:`
                        + ` ${salto.toFixed(1)}px de desvío (${desvio.toFixed(0)}%). El export no corresponde al frame`);
                }
            }
        }
    }

    // preload de imagen: su media y su imagesrcset tienen que existir en un
    // picture. La búsqueda se hace sobre el marcado sin los `link`, porque si no
    // el propio preload se encuentra a sí mismo y la comprobación no prueba nada.
    const marcado = html.replace(/<link\s[^>]*>/gi, '');

    for (const enlace of etiquetas(html, 'link')) {
        if (!/rel=["']preload["']/i.test(enlace) || !/as=["']image["']/i.test(enlace)) continue;

        const media = atributo(enlace, 'media');
        const juego = atributo(enlace, 'imagesrcset') || atributo(enlace, 'href');

        if (!juego) continue;

        const primera = rutas(juego)[0] || juego;

        if (!marcado.includes(primera) && !hojas.includes(basename(primera))) {
            falla(nombre, `se precarga ${primera} y no la sirve ni un picture de la página ni una regla del CSS; se descargará dos veces`);
        }

        // El espejo del `media` sólo se le puede exigir a un `source`. Si la
        // imagen precargada es la que sirve el `img`, es el candidato por
        // defecto y no lleva `media` por definición: su rango es el complemento
        // de todos los `source`, y eso no se comprueba leyendo una etiqueta.
        const laSirveUnSource = etiquetas(marcado, 'source').some(t => t.includes(primera));

        if (media && laSirveUnSource && !etiquetas(marcado, 'source').some(t => t.includes(primera) && t.includes(media))) {
            falla(nombre, `el preload usa media="${media}" y el source que sirve ${primera} no lo replica; los rangos no coinciden y se descargarán dos archivos`);
        }
    }

    // símbolos del sprite
    const usos = [...html.matchAll(/(?:xlink:)?href=["']([^"']*)#(icon-[^"']+)["']/gi)];

    for (const [, archivoSprite, simbolo] of usos) {
        const sprite = resolverDesdeDist(archivoSprite) || join(dist, 'assets/images/sprite.svg');

        if (!existsSync(sprite)) continue;

        const contenido = readFileSync(sprite, 'utf8');
        const simbolos = (contenido.match(/id="/g) || []).length;

        // Un sprite vacío es el estado de partida: el core referencia iconos que
        // todavía no se han exportado del diseño. Eso es un pendiente, no un
        // error. Un sprite con símbolos al que le falta el que se usa sí lo es.
        if (!simbolos) {
            if (!spriteVacioAvisado) {
                avisa('sprite', 'el sprite no tiene ningún símbolo: los iconos del diseño aún no se han exportado a `src/assets/icons/`');
                spriteVacioAvisado = true;
            }

            continue;
        }

        if (!contenido.includes(`id="${simbolo}"`)) {
            falla(nombre, `usa #${simbolo} y el sprite tiene ${simbolos} símbolos pero no ese; revisar el prefijo que añade el generador`);
        }
    }
}

// ── 3. marcadores de posición sin reemplazar ───────────────────────────────
// El core trae plantillas comentadas para que se rellenen. Que sigan comentadas
// no rompe nada, pero tampoco protesta nadie: el preload del LCP es el que más
// veces se queda sin aplicar. Esto lo recuerda al terminar.
const pugCrudo = (await glob('src/**/*.pug', { cwd: raiz, absolute: true }))
    .map(f => readFileSync(f, 'utf8'))
    .join('\n');

const plantillaPreload = /\/\/\s*link\([^)]*as=['"]image['"]/s.test(pugCrudo);
const preloadReal = paginas.some(p => /rel=["']preload["'][^>]*as=["']image["']/.test(readFileSync(p, 'utf8')));

if (plantillaPreload && !preloadReal) {
    avisa('preload', 'la plantilla del preload sigue comentada y ninguna página precarga una imagen: si hay candidata a LCP, hay que aplicarla');
}

// ── 4. la fuente del diseño se nombra pero no se entrega ───────────────────
// `validate-assets` comprueba que el archivo de un `@font-face` declarado
// exista, pero no dice nada si no se declara ninguno: el token de `@theme`
// nombra la familia, nadie la sirve, y la página cae en una fuente de
// sustitución sin que ningún comando lo note. Es la mayor diferencia visual que
// puede tener una página.
const sinComentarios = (css) => css.replace(/\/\*[\s\S]*?\*\//g, '');

const estilos = await glob('src/**/*.css', { cwd: raiz, absolute: true });

const servidas = new Set();
const nombradas = new Map();

for (const archivo of estilos) {
    const css = sinComentarios(readFileSync(archivo, 'utf8'));

    for (const [, familia] of css.matchAll(/@font-face\s*\{[^}]*?font-family\s*:\s*['"]?([^'";]+)['"]?\s*;/g)) {
        servidas.add(familia.trim().toLowerCase());
    }

    // `--font-main: 'Jost', sans-serif` nombra Jost: la primera familia de la
    // pila es la que el diseño pide, el resto son sustitutos declarados a
    // propósito y no hay que servirlos.
    for (const [, token, valor] of css.matchAll(/(--font-[\w-]+)\s*:\s*([^;]+);/g)) {
        const primera = valor.split(',')[0].trim().replace(/^['"]|['"]$/g, '');

        if (!primera || /^(var|inherit|initial|ui-|system-|sans-serif|serif|monospace)/.test(primera)) continue;
        if (!nombradas.has(primera)) nombradas.set(primera, token);
    }
}

for (const [familia, token] of nombradas) {
    if (!servidas.has(familia.toLowerCase())) {
        falla('fuentes', `\`${token}\` nombra \`${familia}\` y ningún \`@font-face\` la sirve: la página se pinta con una fuente de sustitución`);
    }
}

if (!nombradas.size && !servidas.size) {
    avisa('fuentes', 'ningún token de `@theme` nombra una familia y no hay ningún `@font-face`: si el diseño lleva fuente propia, todavía no se ha entregado');
}

// ── 5. valores arbitrarios donde debería haber un token ────────────────────
// Tailwind acepta `bg-[#0a0a0a]` y `text-[13px]`, y ahí está su trampa: cuando
// un agente no encuentra el token, no pregunta, lo inventa entre corchetes. El
// valor queda correcto en pantalla y fuera del sistema, así que la siguiente
// sección lo vuelve a inventar con otro número.
//
// Un color siempre es un token: no hay color de un solo uso en un diseño. Una
// medida puede serlo legítimamente —un desplazamiento de 3px para alinear un
// icono—, así que sólo se señala cuando se repite.
const arbitrarios = new Map();

for (const { nombre, valor } of clases) {
    for (const [, utilidad, dentro] of valor.matchAll(/(?:^|\s)(?:[\w-]+:)*([a-z-]+)-\[([^\]]+)\]/g)) {
        const clave = `${utilidad}-[${dentro}]`;
        const entrada = arbitrarios.get(clave) || { veces: 0, nombre, color: /^(#|rgb|hsl|oklch)/i.test(dentro) };

        entrada.veces += 1;
        arbitrarios.set(clave, entrada);
    }
}

for (const [clase, { veces, nombre, color }] of arbitrarios) {
    if (color) {
        falla(nombre, `\`${clase}\` fija un color en el marcado: los colores son tokens de \`@theme\`, no valores sueltos`);
    } else if (veces >= 3) {
        avisa(nombre, `\`${clase}\` aparece ${veces} veces: un valor repetido es un token que falta en \`@theme\``);
    }
}

// ── 6. la misma cadena de clases repetida ──────────────────────────────────
// Con utilidades, repetir es lo normal y no hay que perseguirlo. Lo que sí
// importa es la cadena larga e idéntica que aparece tres veces: eso ya no es
// una coincidencia de spacing, es un componente sin nombre, y el sitio de un
// componente es un mixin de Pug.
//
// El recuento va por página: el header aparece en las tres y eso no es una
// repeticion, es el mismo componente incluido tres veces. Lo que se busca son
// tres hermanos dentro de un documento.
const repetidas = new Map();

for (const { nombre, valor } of clases) {
    const normalizada = valor.trim().split(/\s+/).sort().join(' ');

    if (normalizada.split(' ').length < 6) continue;

    const clave = `${nombre}\u0000${normalizada}`;
    const entrada = repetidas.get(clave) || { veces: 0, nombre, cadena: normalizada };

    entrada.veces += 1;
    repetidas.set(clave, entrada);
}

for (const { veces, nombre, cadena } of repetidas.values()) {
    if (veces >= 3) {
        const corta = cadena.length > 70 ? `${cadena.slice(0, 70)}…` : cadena;

        avisa(nombre, `${veces} elementos comparten las mismas ${cadena.split(' ').length} clases (\`${corta}\`): eso es un componente, va en un mixin de \`src/components/\``);
    }
}

// ── informe ────────────────────────────────────────────────────────────────
console.log(pc.cyan(pc.bold('Comprobación de render')));
console.log(pc.gray('------------------------------------------------'));

for (const { archivo, mensaje } of avisos) {
    console.log(`${pc.yellow('AVISO')} ${pc.dim(archivo)}  ${mensaje}`);
}

for (const { archivo, mensaje } of fallos) {
    console.log(`${pc.red('FALLO')} ${pc.dim(archivo)}  ${mensaje}`);
}

if (!fallos.length && !avisos.length) {
    console.log(pc.green('Todo correcto: los assets pintan, las proporciones cuadran y no hay valores fuera del sistema.'));
}

console.log(pc.gray('------------------------------------------------'));
console.log(`Páginas revisadas: ${pc.bold(paginas.length)}  ·  assets medidos: ${pc.bold(pintados.size)}`);

process.exit(fallos.length ? 1 : 0);
