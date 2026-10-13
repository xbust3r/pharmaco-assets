import path from 'path';

export default function watchIcons(relativePath = 'src/assets/icons') {
    return {
        name: 'vite-plugin-watch-icons',
        configureServer(server) {
            const folderPath = path.resolve(process.cwd(), relativePath);

            server.watcher.add(folderPath);

            server.watcher.on('all', (eventName, file) => {
                if (file.startsWith(folderPath) && (eventName === 'add' || eventName === 'unlink')) {
                    console.log(`Changes detected (${eventName}), restart server...`);

                    server.restart();
                }
            });
        }
    };
}