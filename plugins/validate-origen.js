/**
 * Validador de fidelidad contra el origen (`assets/`).
 *
 * Compara cada maqueta de `assets/` con su página migrada en `dist/` y responde
 * a tres preguntas, sin navegador y sin dependencias:
 *
 *   1. ¿Está la página? Cada `assets/<x>.html` tiene su `dist/<x>.html`.
 *   2. ¿Está el texto? El texto visible de `main` coincide, carácter a carácter
 *      tras quitar espacios: los textos se copian tal cual, con sus erratas.
 *   3. ¿Están los hooks? Cada `js-*` del origen existe en la página migrada.
 *
 * La geometría (cajas y alturas) no se comprueba aquí: exige un navegador. Se
 * mide con docs/migracion/herramientas/geometria.mjs y su salida va al hilo.
 *
 * Sale con 1 si hay alguna diferencia. Requiere `pnpm build` antes.
 */
import fs from 'node:fs';
import path from 'node:path';
import pc from 'picocolors';

const raiz = path.resolve(import.meta.dirname, '..');
const origen = path.join(raiz, 'assets');
const dist = path.join(raiz, 'dist');

const ENTIDADES = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ' };

// Texto visible de un fragmento HTML: sin etiquetas, sin scripts, con entidades decodificadas.
function textoVisible(html) {
    return html
        .replace(/<!--[\s\S]*?-->/g, '')
        .replace(/<(script|style)[\s\S]*?<\/\1>/gi, '')
        .replace(/<[^>]+>/g, '')
        .replace(/&(#x?[0-9a-f]+|[a-z]+);/gi, (m, n) => {
            if (n[0] === '#') {
                const code = n[1] === 'x' || n[1] === 'X' ? parseInt(n.slice(2), 16) : parseInt(n.slice(1), 10);
                return String.fromCodePoint(code);
            }
            return ENTIDADES[n.toLowerCase()] ?? m;
        })
        .replace(/\s+/g, '');
}

// Contenido de <main>...</main>.
function main(html) {
    const m = html.match(/<main[^>]*>([\s\S]*?)<\/main>/i);
    return m ? m[1] : '';
}

// Contenido de una etiqueta (header o footer), o cadena vacía.
function bloque(html, etiqueta) {
    const m = html.match(new RegExp(`<${etiqueta}[^>]*>([\\s\\S]*?)<\\/${etiqueta}>`, 'i'));
    return m ? m[1] : '';
}

// Hooks js-* de un documento (clases que empiezan por js-).
function hooks(html) {
    const set = new Set();
    for (const m of html.matchAll(/class="([^"]*)"/g)) {
        for (const c of m[1].split(/\s+/)) if (c.startsWith('js-')) set.add(c);
    }
    return set;
}

const paginas = fs.readdirSync(origen).filter((f) => f.endsWith('.html')).sort();
let fallos = 0;
const informe = [];

for (const archivo of paginas) {
    const nombre = archivo;
    const rutaDist = path.join(dist, nombre);
    if (!fs.existsSync(rutaDist)) {
        fallos++;
        informe.push(pc.red(`FALLO ${nombre}: no existe en dist/`));
        continue;
    }
    const htmlOrigen = fs.readFileSync(path.join(origen, nombre), 'utf8');
    const htmlDist = fs.readFileSync(rutaDist, 'utf8');

    const tO = textoVisible(main(htmlOrigen)) + '|' + textoVisible(bloque(htmlOrigen, 'header')) + '|' + textoVisible(bloque(htmlOrigen, 'footer'));
    const tD = textoVisible(main(htmlDist)) + '|' + textoVisible(bloque(htmlDist, 'header')) + '|' + textoVisible(bloque(htmlDist, 'footer'));
    if (tO !== tD) {
        fallos++;
        let i = 0;
        while (i < Math.min(tO.length, tD.length) && tO[i] === tD[i]) i++;
        informe.push(pc.red(`FALLO ${nombre}: el texto de main no coincide (primera diferencia en el carácter ${i} del texto main|cabecera|pie)`));
        informe.push(`      origen: …${tO.slice(Math.max(0, i - 40), i + 40)}`);
        informe.push(`      migrada: …${tD.slice(Math.max(0, i - 40), i + 40)}`);
    }

    const hO = hooks(htmlOrigen);
    const hD = hooks(htmlDist);
    const faltan = [...hO].filter((h) => !hD.has(h));
    if (faltan.length) {
        fallos++;
        informe.push(pc.red(`FALLO ${nombre}: faltan hooks js-* → ${faltan.join(', ')}`));
    }
    if (!faltan.length && tO === tD) informe.push(pc.green(`OK    ${nombre}: texto y ${hO.size} hooks js-* coinciden`));
}

console.log(pc.cyan(pc.bold('Validador · fidelidad contra assets/ (texto y hooks)')));
console.log('-'.repeat(48));
informe.forEach((l) => console.log(l));
console.log('-'.repeat(48));
console.log(`${paginas.length} páginas revisadas · ${fallos} FALLO`);
process.exit(fallos ? 1 : 0);
