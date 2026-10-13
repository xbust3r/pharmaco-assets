import vituum from 'vituum';
import pug from '@vituum/vite-plugin-pug';
import ViteSvgSpriteWrapper from 'vite-svg-sprite-wrapper';
import { ViteImageOptimizer } from 'vite-plugin-image-optimizer';
import devWebpProxy from './plugins/devWebpProxy.js';
import getAssetFileName from './plugins/assetFileNames.js';
import watchIcons from './plugins/watchIcons.js';
import htmlAutonomo from './plugins/htmlAutonomo.js';

// La salida es HTML y CSS estáticos. `base: './'` deja rutas relativas, así que
// el `dist/` funciona tanto servido desde cualquier subcarpeta como abierto con
// doble clic. Lo segundo pide además el formato `iife` y el plugin
// `htmlAutonomo`: ver su cabecera.
// Puertos fijos y `strictPort`. Sin declararlos, Vite usa 5173 —su valor por
// defecto, que colisiona con cualquier otro proyecto Vite— y **se desplaza solo
// al siguiente libre**: el servidor sigue arrancando, pero en otra dirección, y
// los enlaces y capturas que alguien pegó en un hilo dejan de valer. Con
// `strictPort` el arranque falla en voz alta si el puerto está ocupado, que es
// lo que se quiere: enterarse.
const DEV_PORT = 5273;
const PREVIEW_PORT = 5274;

export default {
    base: './',
    server: {
        port: DEV_PORT,
        strictPort: true
    },
    preview: {
        port: PREVIEW_PORT,
        strictPort: true
    },
    plugins: [
        devWebpProxy(),
        vituum({
            pages: {
                normalizeBasePath: true
            },
            imports: {
                paths: [],
                filenamePattern: {}
            }
        }),
        pug({ options: { pretty: true } }),
        ViteSvgSpriteWrapper({
            icons: './src/assets/icons/*.svg',
            outputDir: './src/assets/images/'
        }),
        ViteImageOptimizer({
            test: /^(?!.*sprite\.svg$).*\.svg$/i,
            cache: true,
            cacheLocation: 'node_modules/.cache/image-optimizer'
        }),
        watchIcons('src/assets/icons'),
        htmlAutonomo('dist')
    ],
    build: {
        // Sin módulos no hay nada que precargar.
        modulePreload: false,
        assetsInlineLimit: 0,
        rollupOptions: {
            output: {
                assetFileNames: getAssetFileName,
                entryFileNames: 'assets/scripts/[name].js',
                chunkFileNames: 'assets/scripts/[name].js'
            }
        }
    },
    css: {
        devSourcemap: true
    }
};
