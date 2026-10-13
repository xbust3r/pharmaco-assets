/** @type {import('stylelint').Config} */
export default {
    extends: ['stylelint-config-standard'],
    rules: {
        // El CSS propio es corto y no declara clases de componente: las que hay
        // son scopes de contenido ajeno, así que el patrón por defecto sobra.
        'selector-class-pattern': null,

        // Tailwind v4 configura desde el CSS. Sin esto, sus reglas se leen como
        // at-rules desconocidas y el linter cancela el build.
        'at-rule-no-unknown': [
            true,
            {
                ignoreAtRules: ['theme', 'source', 'utility', 'variant', 'custom-variant', 'apply', 'reference', 'plugin', 'config'],
            },
        ],

        // `--color-*: initial` es la forma de Tailwind de vaciar un espacio de
        // tokens; no es un nombre de variable mal escrito.
        'custom-property-pattern': null,

        // stylelint-config-standard fuerza `url()` en los @import, y validate-assets.js
        // toma cada `url()` por una ruta local. Con la notación string, los paquetes
        // de Tailwind (`tailwindcss/theme.css`) no se confunden con archivos del proyecto.
        'import-notation': 'string',
        'media-feature-range-notation': 'context',
        'declaration-empty-line-before': null,
    },
    ignoreFiles: ['dist/**', 'node_modules/**'],
};
