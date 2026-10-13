// scripts/convert-images.js
import sharp from 'sharp';
import fs from 'fs';
import path from 'path';
import { glob } from 'glob';
import pc from 'picocolors';

async function convert() {
    const startTime = Date.now();

    console.log(pc.cyan(pc.bold('Start image optimization')));

    const files = await glob('src/**/*.{png,jpg,jpeg,gif}', {
        ignore: '**/favicon/**'
    });

    let processedCount = 0;
    let skippedCount = 0;

    for (const file of files) {
        const ext = path.extname(file);
        const newFile = file.replace(ext, '.webp');
        const fileName = path.basename(file);

        const sourceStats = fs.statSync(file);
        let needsConversion = true;

        if (fs.existsSync(newFile)) {
            const destStats = fs.statSync(newFile);
            if (sourceStats.mtime <= destStats.mtime) {
                needsConversion = false;
            }
        }

        if (!needsConversion) {
            console.log(pc.dim(`Skip: ${fileName}`)); 
            skippedCount++;
            continue;
        }

        try {
            console.log(`${pc.blue('Convert:')} ${pc.white(fileName)}`);

            await sharp(file)
                .webp({ quality: 85, animated: true })
                .toFile(newFile);

            const time = new Date();
            fs.utimesSync(newFile, time, time);

            processedCount++;
        } catch (error) {
            console.error(pc.red(pc.bold(`❌  Error on ${fileName}:`)), error.message);
        }
    }

    const duration = ((Date.now() - startTime) / 1000).toFixed(2);

    // Resumen final
    console.log(pc.gray('------------------------------------------------'));
    console.log(pc.green(pc.bold(`✅  Completed in ${duration}s`)));
    console.log(`   ${pc.magenta('•')} Processed: ${pc.bold(processedCount)}`);
    console.log(`   ${pc.magenta('•')} Skipped:  ${pc.bold(skippedCount)}`);
    console.log(pc.gray('------------------------------------------------'));
}

convert();