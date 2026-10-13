export default function getAssetFileName(assetInfo) {
    const fileName = assetInfo.name || (assetInfo.names && assetInfo.names[0]) || 'asset';
    const extType = fileName.split('.').pop();

    if (/sprite\.svg$/i.test(fileName)) {
        return 'assets/images/[name][extname]';
    }

    const originalName = assetInfo.originalFileName || (assetInfo.originalFileNames && assetInfo.originalFileNames[0]);

    if (originalName) {
        const relativePath = originalName.replace(/^src\//, '');
        if (!/css|js/i.test(extType)) {
            return `${relativePath}`;
        }
    }

    if (/css/i.test(extType)) {
        return 'assets/styles/[name][extname]';
    }

    if (/js/i.test(extType)) {
        return 'assets/scripts/[name][extname]';
    }

    return `assets/[name][extname]`;
};