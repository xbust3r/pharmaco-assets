import fs from 'node:fs';
import path from 'node:path';

/**
 * Deja el HTML construido abrible con doble clic.
 *
 * Vite asume que el resultado se sirve por HTTP y emite dos cosas que el
 * navegador bloquea bajo `file://`:
 *
 *   - `crossorigin` en la hoja de estilos y en el script, que dispara una
 *     comprobación CORS que `file://` no puede pasar;
 *   - `type="module"`, que además exige un origen.
 *
 * El resultado es una página sin estilos y sin comportamiento, sin un solo
 * error visible salvo en la consola. Esto quita lo uno y convierte lo otro en un
 * `defer`, que hace lo mismo —ejecutar tras el parseo, en orden— sin exigir
 * origen. Para que eso sea válido, el bundle se genera como `iife` desde
 * `vite.config.js`: un script clásico no entiende `import`.
 *
 * Servido por HTTP el resultado es idéntico; lo que se gana es que también
 * funcione sin servidor.
 */
export default function htmlAutonomo(dist = 'dist') {
    let salida = dist;

    return {
        name: 'html-autonomo',
        apply: 'build',
        configResolved(config) {
            salida = path.resolve(config.root, dist || config.build.outDir);
        },
        // `writeBundle` y no `closeBundle`: reescribe archivos ya emitidos, y es
        // este el hook que corre justo después de escribirlos.
        writeBundle(opciones, bundle) {
            // El cambio a `defer` sólo es válido si todo el JavaScript cabe en
            // un archivo. Hoy cabe, pero un `import()` dinámico partiría el
            // bundle y los trozos dejarían de cargarse en silencio. Se lee del
            // propio bundle, que es quien lo sabe, y no del texto del archivo:
            // un `import()` dentro de una flecha no lo ve ninguna expresión
            // regular razonable.
            const trozos = Object.values(bundle).filter((s) => s.type === 'chunk');

            if (trozos.length > 1) {
                this.error(
                    `El JavaScript se partió en ${trozos.length} archivos (${trozos.map((t) => t.fileName).join(', ')}). `
                    + 'Un script clásico no puede cargar trozos y `file://` no admite módulos: la página se abriría '
                    + 'sin comportamiento. Quitar el `import()` dinámico, o retirar este plugin y servir `dist/` por HTTP.'
                );
            }

            const quitarCrossorigin = (etiqueta) =>
                etiqueta.replace(/\s+crossorigin(=(["'])[^"']*\2)?/g, '');

            const procesar = (archivo) => {
                const original = fs.readFileSync(archivo, 'utf-8');

                // Sólo se retira `crossorigin` de las hojas de estilo y scripts
                // emitidos por Vite, donde el atributo bloquea la carga bajo
                // `file://`. No se retira de preloads de fuentes u otros
                // recursos donde `crossorigin` es requerido por el navegador.
                const nuevo = original
                    .replace(/<script\b[^>]*>/gi, (match) =>
                        quitarCrossorigin(match).replace(/<script\s+type="module"/g, '<script defer')
                    )
                    .replace(/<link\b(?=[^>]*\brel=["']stylesheet["'])[^>]*>/gi, (match) =>
                        quitarCrossorigin(match)
                    );

                if (nuevo !== original) fs.writeFileSync(archivo, nuevo, 'utf-8');
            };

            const recorrer = (dir) => {
                for (const entrada of fs.readdirSync(dir, { withFileTypes: true })) {
                    const completa = path.join(dir, entrada.name);

                    if (entrada.isDirectory()) recorrer(completa);
                    else if (path.extname(completa) === '.html') procesar(completa);
                }
            };

            if (fs.existsSync(salida)) recorrer(salida);
        },
    };
}
