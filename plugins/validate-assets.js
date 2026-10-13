import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');
const srcDir = path.join(rootDir, 'src');
const distDir = path.join(rootDir, 'dist');

console.log('\x1b[36m%s\x1b[0m', '🔍 Iniciando validación estricta de assets...');

let hasErrors = false;

function getFiles(dir, extensions, fileList = []) {
    if (!fs.existsSync(dir)) return fileList;
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const filePath = path.join(dir, file);
        if (fs.statSync(filePath).isDirectory()) {
            getFiles(filePath, extensions, fileList);
        } else if (extensions.some(ext => filePath.endsWith(ext))) {
            fileList.push(filePath);
        }
    });
    return fileList;
}

const filesToAudit = getFiles(srcDir, ['.css', '.pug', '.js']);

// Un ejemplo comentado no es una referencia real. Sin esto, una línea como
// `// @include font-face.font-face('Poppins', 'poppins-light', 300);` exige un
// archivo que nadie usa y cancela el build.
//
// Solo cuentan los comentarios de línea completa, para no tocar el `//` que
// aparece dentro de una URL. En Pug se descarta además el bloque sangrado que
// cuelga del comentario, porque ahí viven los atributos del marcado comentado.
function stripComments(content, ext) {
    const lines = content.replace(/\/\*[\s\S]*?\*\//g, '').split('\n');

    if (ext !== '.pug') {
        return lines.map(line => (line.trim().startsWith('//') ? '' : line)).join('\n');
    }

    // En Pug el comentario no es una línea sino un bloque: abarca todo lo que
    // venga con mayor sangría. Un marcado comentado arrastra ahí sus atributos,
    // y descartando solo la primera línea sus rutas se leen como reales.
    let sangriaComentario = null;

    return lines
        .map(line => {
            const sangria = line.length - line.trimStart().length;

            if (sangriaComentario !== null) {
                if (line.trim() === '' || sangria > sangriaComentario) return '';
                sangriaComentario = null;
            }

            if (line.trim().startsWith('//')) {
                sangriaComentario = sangria;
                return '';
            }

            return line;
        })
        .join('\n');
}

filesToAudit.forEach(file => {
    const ext = path.extname(file);
    const content = stripComments(fs.readFileSync(file, 'utf-8'), ext);
    const foundAssets = [];

    if (ext === '.css') {
        const regex = /url\(['"]?([^'")]*)['"]?\)/g;
        let match; while ((match = regex.exec(content)) !== null) foundAssets.push(match[1]);
    }
    else if (ext === '.pug') {
        const regex = /(?:src|href|include|srcset|imagesrcset)\s*[\(=]\s*['"]([^'"]+)['"]/g;
        let match;
        while ((match = regex.exec(content)) !== null) {
            const rawValue = match[1].trim();
            const cleanUrls = rawValue.split(',').map(item => {
                return item.trim().split(/\s+/)[0];
            });

            cleanUrls.forEach(url => {
                if (url) foundAssets.push(url);
            });
        }

        const fontsArrayRegex = /let\s+fonts\s*=\s*\[([\s\S]*?)\]/g;
        let matchFontsArray;

        while ((matchFontsArray = fontsArrayRegex.exec(content)) !== null) {
            const arrayContent = matchFontsArray[1];
            const fontNameRegex = /['"]([^'"]+)['"]/g;
            let matchFontName;

            while ((matchFontName = fontNameRegex.exec(arrayContent)) !== null) {
                const fontFileName = matchFontName[1];
                const fontDir = path.join(rootDir, 'src', 'assets', 'fonts');
                const expectedPath = path.join(fontDir, fontFileName + '.woff2');

                if (!fs.existsSync(expectedPath)) {
                    hasErrors = true;
                    console.error('\n\x1b[41m\x1b[37m %s \x1b[0m', ' Error de preload de fuente (pug) ');
                    console.error(`\x1b[31mArchivo Pug:\x1b[0m ${path.relative(rootDir, file)}`);
                    console.error(`\x1b[31mFuente declarada en array:\x1b[0m ${fontFileName}`);
                    console.error(`\x1b[33mNo se encontró el archivo:\x1b[0m ${expectedPath}`);
                }
            }
        }
    }
    else if (ext === '.js') {
        const regex = /['"]([^'"]+\.(?:png|jpe?g|svg|webp|gif))['"]/gi;
        let match; while ((match = regex.exec(content)) !== null) foundAssets.push(match[1]);
    }

    foundAssets.forEach(assetPath => {
        const cleanPath = assetPath.trim();
        if (!cleanPath) return;
        if (/^(https?:|data:|tel:|mailto:|sms:|#|\$|\/\/)/.test(cleanPath)) return;

        const pathWithoutQuery = cleanPath.split(/[?#]/)[0];
        const assetExt = path.extname(pathWithoutQuery).toLowerCase();
        if (['.html', '.php', '.xml', '.txt'].includes(assetExt)) return;
        if (assetExt === '') return;

        let absolutePath;

        if (pathWithoutQuery.startsWith('/src/')) {
            absolutePath = path.join(rootDir, pathWithoutQuery.substring(1));
        } else if (pathWithoutQuery.startsWith('src/')) {
            absolutePath = path.join(rootDir, pathWithoutQuery);
        } else if (pathWithoutQuery.startsWith('/')) {
            absolutePath = path.join(rootDir, pathWithoutQuery);
        } else {
            absolutePath = path.resolve(path.dirname(file), pathWithoutQuery);
        }

        if (!fs.existsSync(absolutePath)) {
            hasErrors = true;
            console.error('\n\x1b[41m\x1b[37m %s \x1b[0m', ' Error de asset ');
            console.error(`\x1b[31mArchivo:\x1b[0m ${path.relative(rootDir, file)}`);
            console.error(`\x1b[31mRuta escrita:\x1b[0m ${cleanPath}`);
            console.error(`\x1b[33mBuscado en:\x1b[0m ${absolutePath}`);
        }
    });
});

if (hasErrors) {
    console.error('\n\x1b[31m❌ Validación fallida. El proceso de Build ha sido cancelado.\x1b[0m');
    process.exit(1);
} else {
    console.log('\x1b[32m✔ Todos los assets existen. Procediendo...\x1b[0m\n');
}