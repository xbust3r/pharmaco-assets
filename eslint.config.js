import js from '@eslint/js';
import globals from 'globals';
import { defineConfig } from 'eslint/config';
import stylistic from '@stylistic/eslint-plugin'

export default defineConfig([
    {
        files: ['src/**/*.{js,mjs,cjs}'],
        plugins: {
            js,
            '@stylistic': stylistic
        },
        extends: ['js/recommended'],
        languageOptions: {
            globals: globals.browser,
        },
        rules: {
            quotes: ['error', 'single'],
            'no-console': 'error',
            semi: ['error', 'always'],
            '@stylistic/indent': ['error', 4],
            '@stylistic/comma-dangle': ['error', 'always-multiline'],
            '@stylistic/arrow-parens': ['error', 'always'],
            '@stylistic/arrow-spacing': ['error', { 'before': true, 'after': true }],
        },
    },
]);
