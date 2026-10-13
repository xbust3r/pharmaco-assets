/**
 * Descarga los assets exportados desde Figma y los deja listos para el core.
 *
 *     pnpm figma:assets                    # lee figma-assets.json
 *     pnpm figma:assets otra-campana.json  # lee otro manifiesto
 *
 * El script es genérico: todo lo que cambia entre proyectos vive en el
 * manifiesto, que es un JSON con esta forma.
 *
 *     {
 *         "baseUrl": "https://www.figma.com/api/mcp/asset/",
 *         "file": "gs9lgkXozC8JyZpRGgHpoR",
 *         "generated": "2026-08-21",
 *         "assets": [
 *             {
 *                 "nodeId": "171:571",
 *                 "asset": "97687e1c-....svg",
 *                 "target": "src/assets/icons/icon-phone.svg",
 *                 "currentColor": "white"
 *             }
 *         ]
 *     }
 *
 * Campos de cada asset:
 *
 *     nodeId        nodo de Figma del que sale, para poder regenerar la URL.
 *     asset         identificador temporal que devuelve el MCP de Figma.
 *     target        ruta de destino relativa a la raíz del repositorio.
 *     strip         false para guardar el SVG tal cual llega. Por defecto se
 *                   limpian los fondos que Figma hornea.
 *     keepGroup     id de capa: conserva sólo ese grupo y descarta el resto.
 *     dropGroup     id de capa: elimina ese grupo y conserva el resto.
 *     onlyPaths     conserva solo los trazos. Para los iconos del sprite.
 *     currentColor  color, o lista de colores, que pasan a heredarse con
 *                   currentColor. Para los iconos que van al sprite.
 *
 * Las URLs del MCP son temporales: caducan unos siete días después de haberse
 * generado. Si alguna responde 403 o 404 hay que volver a exportarla desde
 * Figma y actualizar su campo `asset`; el campo `nodeId` está para eso.
 */

import { mkdir, rm, writeFile } from 'node:fs/promises';
import { readFileSync } from 'node:fs';
import { dirname, extname, resolve } from 'node:path';
import pc from 'picocolors';

const root = process.cwd();
const manifestPath = resolve(root, process.argv[2] || 'figma-assets.json');

/**
 * Cada export de Figma llega envuelto en el contexto de la página: un rect
 * opaco #1E1E1E, el rect del artboard y los de la tarjeta que contiene la capa.
 * Guardados tal cual, el icono se pinta sobre una caja sólida.
 *
 * Sólo se recorre el cuerpo del SVG. Dentro de <defs> hay rects que definen los
 * clipPath, y borrarlos deja el recorte vacío: el icono desaparece entero.
 */
const stripBackgrounds = (svg) => {
    const box = svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);

    if (!box) return svg;

    const [width, height] = [Number(box[1]), Number(box[2])];
    let inDefs = false;

    return svg
        .split('\n')
        .filter((line) => {
            const l = line.trim();

            if (l.startsWith('<defs')) inDefs = true;
            if (l.startsWith('</defs')) inDefs = false;
            if (inDefs || !l.startsWith('<rect')) return true;
            if (/fill="#1E1E1E"/i.test(l)) return false;
            if (/transform="translate/.test(l)) return false;

            const w = Number((l.match(/\swidth="([\d.]+)"/) || [])[1]);
            const h = Number((l.match(/\sheight="([\d.]+)"/) || [])[1]);

            return !(w > width || h > height);
        })
        .join('\n');
};

/** Localiza el rango de líneas que ocupa un grupo, contando anidamiento. */
const groupRange = (lines, id, opcional = false) => {
    const start = lines.findIndex((line) => line.includes(`<g id="${id}"`));

    if (start === -1 && opcional) return null;

    if (start === -1) throw new Error(`no existe la capa "${id}"`);

    let depth = 0;

    for (let i = start; i < lines.length; i += 1) {
        depth += (lines[i].match(/<g[\s>]/g) || []).length - (lines[i].match(/<\/g>/g) || []).length;
        if (depth === 0) return [start, i];
    }

    throw new Error(`la capa "${id}" no cierra`);
};

/**
 * Elimina un grupo entero. Sirve cuando el nodo que interesa no existe como
 * capa propia pero sí como "el frame menos una de sus partes": por ejemplo una
 * escena ilustrada de la que hay que descartar el panel de texto, porque ese
 * texto se marca en HTML y no puede venir horneado en la imagen.
 */
const dropGroup = (id, opcional = false) => (svg) => {
    const lines = svg.split('\n');
    const rango = groupRange(lines, id, opcional);

    // Que no esté no siempre es un error. Casi todos los `dropGroup` se
    // escribieron contra la exportación del MCP, que envuelve el nodo en el
    // contexto de la página; la de la API REST no lleva ese envoltorio, así que
    // la capa que había que quitar sencillamente no viene. Quitar algo que no
    // está es el resultado que se buscaba.
    if (!rango) {
        console.log(pc.dim(`      la capa "${id}" no está en el SVG de la API REST; no hay nada que quitar`));

        return svg;
    }

    const [start, end] = rango;

    return [...lines.slice(0, start), ...lines.slice(end + 1)].join('\n');
};

/**
 * Conserva sólo un grupo. Hace falta cuando lo que sobra no es un rect sino una
 * forma —un path con gradiente, por ejemplo—, que `stripBackgrounds` no puede
 * distinguir de la ilustración.
 */
const keepGroup = (id) => (svg) => {
    const lines = svg.split('\n');
    const [start, end] = groupRange(lines, id);
    const defsStart = lines.findIndex((line) => line.includes('<defs>'));
    const defs = defsStart === -1
        ? []
        : lines.slice(defsStart, lines.findIndex((line) => line.includes('</defs>')) + 1);

    return [lines[0], ...lines.slice(start, end + 1), ...defs, '</svg>'].join('\n');
};

/** Deja que el icono herede el color del componente que lo usa. */
const useCurrentColor = (colors) => (svg) =>
    [colors].flat().reduce((acc, color) => acc.replaceAll(`fill="${color}"`, 'fill="currentColor"'), svg);

/**
 * Conserva únicamente los trazos. Es lo que necesita un icono destinado al
 * sprite: el generador descarta los rellenos fijos y sube `fill="currentColor"`
 * al símbolo, así que cualquier forma de adorno —el círculo blanco de un
 * chevron— acabaría del mismo color que el trazo y lo taparía. De paso
 * descarta los filtros que Figma arrastra del contenedor, como la sombra de la
 * tarjeta en la que estaba dibujado el icono.
 */
const onlyPaths = () => (svg) => {
    const lines = svg.split('\n');
    return [lines[0], ...lines.filter((l) => l.trim().startsWith('<path')), '</svg>'].join('\n');
};

// `origen` distingue de dónde vino el SVG. Importa para una sola decisión: si
// una capa que había que quitar no aparece, con el MCP es un manifiesto
// desactualizado y con la API REST es que ese envoltorio no existe allí.
const clean = (svg, spec, origen = 'mcp') => {
    let out = spec.strip === false ? svg : stripBackgrounds(svg);

    // `keepGroup` no admite esa tolerancia: si falta la capa que hay que
    // conservar, no queda nada que guardar y el archivo saldría vacío.
    if (spec.keepGroup) out = keepGroup(spec.keepGroup)(out);
    if (spec.dropGroup) out = dropGroup(spec.dropGroup, origen === 'rest')(out);
    if (spec.onlyPaths) out = onlyPaths()(out);
    if (spec.currentColor) out = useCurrentColor(spec.currentColor)(out);

    return out;
};

/**
 * Windows bloquea el archivo mientras otro proceso lo tiene abierto —el
 * servidor de desarrollo o el optimizador de imágenes—, así que conviene
 * reintentar antes de darlo por fallido.
 */
// En Windows, sobrescribir un archivo existente puede fallar con EBUSY, EPERM o
// UNKNOWN aunque nadie lo tenga abierto: basta con que el servidor de desarrollo
// lo haya leido, o que el antivirus lo este inspeccionando. Reintentar no siempre
// basta, pero borrar y volver a crear si: el error es de la escritura sobre el
// archivo, no del directorio.
const writeWithRetry = async (destination, body, attempts = 3) => {
    for (let i = 1; ; i += 1) {
        try {
            await writeFile(destination, body);
            return;
        } catch (error) {
            const locked = ['EBUSY', 'EPERM', 'UNKNOWN'].includes(error.code);

            if (!locked || i === attempts) throw error;

            await new Promise((r) => { setTimeout(r, 300 * i); });

            // Ultimo intento: quitar el archivo de en medio y escribirlo de cero.
            if (i === attempts - 1) await rm(destination, { force: true });
        }
    }
};

let manifest;

try {
    manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
} catch (error) {
    console.error(pc.red(pc.bold(`No se pudo leer el manifiesto ${manifestPath}`)));
    console.error(pc.red(error.message));
    console.error('\nCada proyecto declara sus propios assets. Crear el archivo con esta forma:');
    console.error(pc.cyan(`
{
    "generated": "AAAA-MM-DD",
    "assets": [
        {
            "nodeId": "123:456",
            "asset": "<identificador que devuelve el MCP de Figma>.svg",
            "target": "src/assets/images/<seccion>/<nombre>.svg"
        }
    ]
}`));
    console.error('\nLos campos disponibles están documentados en la cabecera de este script.');
    process.exit(1);
}

const baseUrl = manifest.baseUrl || 'https://www.figma.com/api/mcp/asset/';
const assets = manifest.assets || [];

// Las URLs del MCP caducan a los siete dias y llevan el formato ya fijado, asi
// que con ellas el manifiesto solo sirve durante esa ventana y cambiar de SVG a
// PNG exige una exportacion nueva. La API REST de Figma no tiene ninguno de los
// dos problemas: resuelve una URL fresca a partir del nodo, y el formato y la
// escala son parametros. Se activa sola cuando hay token y `file` en el
// manifiesto; si no, se usan las URLs del MCP como hasta ahora.
const token = process.env.FIGMA_TOKEN || process.env.FIGMA_ACCESS_TOKEN;
const porRest = Boolean(token && manifest.file);

// De la extension del `target` sale lo que se le pide a Figma. El `-2x` del
// nombre indica la escala, que es como el core nombra las variantes de densidad.
const exportacion = (spec) => {
    const formato = extname(spec.target).slice(1).toLowerCase();

    return {
        formato: formato === 'jpeg' ? 'jpg' : formato,
        escala: spec.scale || (/-2x\.[a-z]+$/i.test(spec.target) ? 2 : 1),
    };
};

// Lo unico que Figma exporta. `webp` no esta, y no es un olvido: lo genera
// `pnpm optimize` a partir del PNG, asi que declararlo aqui es el error.
const FORMATOS_REST = new Set(['jpg', 'png', 'svg', 'pdf']);

// La API rinde los nodos de una peticion antes de contestarla, y un lote grande
// agota el tiempo. Cuarenta por tanda sobra para una landing page.
const TANDA = 40;

const resolverPorRest = async (lote) => {
    const urls = new Map();
    const sinResolver = [];

    // Un grupo por combinacion de formato y escala: la API los toma como
    // parametros de la peticion, no por nodo.
    const grupos = new Map();

    for (const spec of lote) {
        const { formato, escala } = exportacion(spec);

        if (!FORMATOS_REST.has(formato)) {
            sinResolver.push(`${spec.target}: Figma no exporta \`${formato}\` (solo ${[...FORMATOS_REST].join(', ')})`);
            continue;
        }

        const clave = `${formato}@${escala}`;

        if (!grupos.has(clave)) grupos.set(clave, []);
        grupos.get(clave).push(spec);
    }

    for (const [clave, specs] of grupos) {
        const [formato, escala] = clave.split('@');

        for (let i = 0; i < specs.length; i += TANDA) {
            const tanda = specs.slice(i, i + TANDA);
            const ids = tanda.map((s) => s.nodeId).filter(Boolean);

            if (!ids.length) continue;

            const consulta = new URLSearchParams({ ids: ids.join(','), format: formato, scale: escala });
            const respuesta = await fetch(`https://api.figma.com/v1/images/${manifest.file}?${consulta}`, {
                headers: { 'X-Figma-Token': token },
            });
            const datos = await respuesta.json().catch(() => null);

            // El motivo va en el cuerpo, no en el codigo: un token invalido
            // responde 403 con `{"err":"Invalid token"}`, y quedarse con el 403
            // esconde justo el dato que hace falta para arreglarlo.
            if (!respuesta.ok || datos?.err) {
                throw new Error(datos?.err || `${respuesta.status} ${respuesta.statusText}`);
            }

            for (const spec of tanda) {
                const url = datos.images?.[spec.nodeId];

                if (url) urls.set(spec.target, url);
                else sinResolver.push(`${spec.target}: la API no devolvio imagen para el nodo ${spec.nodeId}`);
            }
        }
    }

    if (sinResolver.length) {
        console.error(pc.yellow('Nodos que la API REST no resolvio; se intentara con la URL del manifiesto:'));
        for (const linea of sinResolver) console.error(pc.yellow(`  ${linea}`));
    }

    return urls;
};

console.log(pc.cyan(pc.bold(`Descargando ${assets.length} assets de Figma`)));

let urlsRest = new Map();

if (porRest) {
    console.log(pc.dim('Resolviendo URLs con la API REST a partir de los nodos.'));

    try {
        urlsRest = await resolverPorRest(assets);
    } catch (error) {
        console.error(pc.yellow(`No se pudo usar la API REST (${error.message}); se intentara con las URLs del manifiesto.`));
    }
} else if (manifest.generated) {
    const dias = Math.floor((Date.now() - Date.parse(manifest.generated)) / 86400000);
    const caducadas = Number.isFinite(dias) && dias >= 7;

    console.log(pc[caducadas ? 'yellow' : 'dim'](`URLs generadas el ${manifest.generated}`
        + `${Number.isFinite(dias) ? ` (hace ${dias} dias)` : ''}. Caducan a los siete.`));

    // El manifiesto ya trae `file` y `nodeId`: lo unico que falta para dejar de
    // depender de una URL que caduca es la variable de entorno.
    if (!token) {
        console.log(pc.dim('Sin caducidad: exportar FIGMA_TOKEN con un token personal de Figma'));
        console.log(pc.dim('(figma.com -> Settings -> Security -> Personal access tokens, alcance file_content de solo lectura).'));
    } else if (!manifest.file) {
        console.log(pc.dim('Hay FIGMA_TOKEN pero al manifiesto le falta `file`: sin el file key no se puede resolver el nodo.'));
    }
}

const failures = [];
let ok = 0;

for (const spec of assets) {
    const destination = resolve(root, spec.target);

    try {
        const url = urlsRest.get(spec.target) || (spec.asset && baseUrl + spec.asset);

        if (!url) throw new Error('sin URL: falta `asset` en el manifiesto y la API REST no resolvio este nodo');

        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status} ${response.statusText}`);
        }

        let body = Buffer.from(await response.arrayBuffer());

        if (body.length === 0) throw new Error('la respuesta llegó vacía');

        if (spec.target.endsWith('.svg')) {
            body = Buffer.from(clean(body.toString('utf8'), spec, urlsRest.has(spec.target) ? 'rest' : 'mcp'), 'utf8');
        }

        await mkdir(dirname(destination), { recursive: true });
        await writeWithRetry(destination, body);

        ok += 1;
        console.log(`${pc.green('OK')}    ${spec.target}  ${pc.dim(`(${(body.length / 1024).toFixed(1)} KB)`)}`);
    } catch (error) {
        failures.push({ ...spec, message: error.message });
        console.error(`${pc.red('FALLO')} ${spec.target}  ->  ${error.message}`);
    }
}

console.log(pc.gray('------------------------------------------------'));
console.log(`Descargados: ${pc.bold(ok)} de ${pc.bold(assets.length)}`);

if (failures.length > 0) {
    console.error(pc.red('\nHay que regenerar la URL de estos assets desde Figma:'));
    failures.forEach(({ nodeId, target, message }) => {
        console.error(`  ${target}  ${pc.dim(`(nodo ${nodeId})`)} -> ${message}`);
    });
    process.exitCode = 1;
} else {
    console.log(pc.green('\nTodo listo. Siguiente paso: pnpm optimize && pnpm build'));
}
