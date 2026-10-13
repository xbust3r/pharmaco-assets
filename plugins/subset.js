import { spawnSync } from 'child_process';
import fs from 'fs';
import path from 'path';
import pc from 'picocolors';

const fontsDir = path.resolve('src/assets/fonts');
const unicodeRanges = [
    'U+0000-024F', // Basic Latin, Latin-1, Latin Extended A/B e IPA
    'U+1E00-1EFF', // Latin Extended Additional
    'U+2000-206F', // Puntuación general
    'U+20A0-20CF', // Símbolos monetarios
    'U+2C60-2C7F', // Latin Extended C
    'U+A720-A7FF', // Latin Extended D
    'U+AB30-AB6F', // Latin Extended E
    'U+FB00-FB06', // Ligaduras latinas
].join(',');

function getPythonCandidates() {
    if (process.env.FONT_SUBSET_PYTHON) {
        return [{ command: process.env.FONT_SUBSET_PYTHON, prefixArgs: [] }];
    }

    return [
        { command: 'python', prefixArgs: [] },
        { command: 'py', prefixArgs: ['-3'] },
        { command: 'python3', prefixArgs: [] },
    ];
}

function findPython() {
    for (const candidate of getPythonCandidates()) {
        const check = spawnSync(
            candidate.command,
            [
                ...candidate.prefixArgs,
                '-c',
                'import fontTools.subset; import brotli',
            ],
            { encoding: 'utf8' },
        );

        if (check.status === 0) return candidate;
    }

    console.error(pc.red(pc.bold('No se encontró una instalación compatible de Python.')));
    console.error('Instala Python, fontTools y Brotli antes de convertir fuentes:');
    console.error(pc.cyan('python -m pip install -r requirements-fonts.txt'));
    console.error('Si Python usa otra ruta, defínela en FONT_SUBSET_PYTHON.');
    process.exit(1);
}

function getOutputFileName(ttfFile) {
    const baseName = path.basename(ttfFile, path.extname(ttfFile));
    const normalizedName = baseName
        .trim()
        .replace(/[\s_]+/g, '-')
        .replace(/[^a-zA-Z0-9.-]+/g, '-')
        .replace(/-+/g, '-')
        .replace(/^-|-$/g, '')
        .toLowerCase();

    return `${normalizedName}.woff2`;
}

function findOutputCollisions(ttfFiles) {
    const outputs = new Map();

    for (const ttfFile of ttfFiles) {
        const outputFile = getOutputFileName(ttfFile);
        const sources = outputs.get(outputFile) ?? [];
        sources.push(ttfFile);
        outputs.set(outputFile, sources);
    }

    return [...outputs.entries()].filter(([, sources]) => sources.length > 1);
}

function convertFont(python, ttfFile) {
    const inputPath = path.join(fontsDir, ttfFile);
    const outputFile = getOutputFileName(ttfFile);
    const outputPath = path.join(fontsDir, outputFile);
    const temporaryPath = `${outputPath}.${process.pid}.tmp`;

    console.log(`${pc.blue('Procesando:')} ${pc.yellow(ttfFile)}...`);

    const conversion = spawnSync(
        python.command,
        [
            ...python.prefixArgs,
            '-m',
            'fontTools.subset',
            inputPath,
            `--unicodes=${unicodeRanges}`,
            '--flavor=woff2',
            '--layout-features=*',
            `--output-file=${temporaryPath}`,
        ],
        { encoding: 'utf8' },
    );

    if (conversion.status !== 0) {
        fs.rmSync(temporaryPath, { force: true });
        const details = conversion.stderr?.trim() || conversion.error?.message || 'Error desconocido';
        throw new Error(details);
    }

    if (!fs.existsSync(temporaryPath) || fs.statSync(temporaryPath).size === 0) {
        fs.rmSync(temporaryPath, { force: true });
        throw new Error('fontTools no generó un archivo WOFF2 válido.');
    }

    fs.rmSync(outputPath, { force: true });
    fs.renameSync(temporaryPath, outputPath);

    console.log(`  ${pc.green('✓')} Generado con éxito: ${pc.magenta(outputFile)}\n`);
}

if (!fs.existsSync(fontsDir)) {
    console.error(pc.red(pc.bold(`No se encontró la carpeta ${fontsDir}`)));
    process.exit(1);
}

const ttfFiles = fs.readdirSync(fontsDir)
    .filter((file) => path.extname(file).toLowerCase() === '.ttf')
    .sort((first, second) => first.localeCompare(second));

if (ttfFiles.length === 0) {
    console.error(pc.red(pc.bold(`No se encontró ningún archivo TTF en la carpeta ${fontsDir}`)));
    process.exit(1);
}

const collisions = findOutputCollisions(ttfFiles);

if (collisions.length > 0) {
    console.error(pc.red(pc.bold('Hay fuentes que generarían el mismo archivo de salida:')));
    collisions.forEach(([outputFile, sources]) => {
        console.error(`  ${pc.yellow(outputFile)}: ${sources.join(', ')}`);
    });
    process.exit(1);
}

const python = findPython();
let failures = 0;

for (const ttfFile of ttfFiles) {
    try {
        convertFont(python, ttfFile);
    } catch (error) {
        failures++;
        console.error(`  ${pc.red('✗ Error')} al procesar ${pc.yellow(ttfFile)}:`);
        console.error(`  ${pc.red(error.message)}\n`);
    }
}

console.log(pc.dim('--------------------------------------------'));

if (failures > 0) {
    console.error(pc.red(pc.bold(`Conversión incompleta: ${failures} fuente(s) fallaron.`)));
    process.exit(1);
}

console.log(pc.green(pc.bold(`¡${ttfFiles.length} fuente(s) optimizadas correctamente!`)));
