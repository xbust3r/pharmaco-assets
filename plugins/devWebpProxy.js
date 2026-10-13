import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

export default function devWebpProxy() {
    return {
        name: 'vite-plugin-dev-webp-proxy',
        apply: 'serve', 
        
        configureServer(server) {
            server.middlewares.use(async (req, res, next) => {
                if (req.method === 'GET' && req.url.endsWith('.webp')) {
                    const cleanUrl = decodeURIComponent(req.url.split('?')[0]);
                    
                    const possibleRoots = [
                        process.cwd(),
                        path.join(process.cwd(), 'src')
                    ];

                    let pngPath = null;

                    for (const root of possibleRoots) {
                        const absolutePath = path.join(root, cleanUrl);
                        const tryPng = absolutePath.replace(/\.webp$/, '.png');
                        const tryJpg = absolutePath.replace(/\.webp$/, '.jpg');
                        const tryJpeg = absolutePath.replace(/\.webp$/, '.jpeg');
                        const tryGif = absolutePath.replace(/\.webp$/, '.gif');

                        if (fs.existsSync(tryPng)) { pngPath = tryPng; break; }
                        if (fs.existsSync(tryJpg)) { pngPath = tryJpg; break; }
                        if (fs.existsSync(tryJpeg)) { pngPath = tryJpeg; break; }
                        if (fs.existsSync(tryGif)) { pngPath = tryGif; break; }
                    }

                    if (pngPath) {
                        try {
                            const buffer = await sharp(pngPath)
                                .webp({ quality: 85, animated: true })
                                .toBuffer();
                            res.setHeader('Content-Type', 'image/webp');
                            res.setHeader('Cache-Control', 'no-store');
                            res.end(buffer);
                            return;
                        } catch (e) {
                            console.error('Error convirtiendo imagen en dev:', e);
                        }
                    }
                }
                next();
            });
        }
    };
}