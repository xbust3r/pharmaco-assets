# Herramientas de la migración (TASK-006)

Auditoría del trabajo, no parte del producto. No se ejecutan en `pnpm build`.

## Generador de páginas (`generador/`)

Las páginas de `src/pages/` salen de `assets/*.html` por este orden:

1. `gen_tokens.py` y `gen_base.py`: tokens de `src/styles/styles.css` y reset de `@layer base`, con los valores de `assets/css/main.css`.
2. `extract_icons.py`: iconos de `assets/images/icons/icons.svg` a `src/assets/icons/`.
3. `build_page.py <pagina>`: compila el `<main>` del origen a Pug (`compile.py`, cascada de `main.css` en `cssparse.py` y `dom.py`).
4. `mixinize.py`: extrae los bloques repetidos a `src/components/repetidos.pug`.

Las rutas son absolutas al repositorio de este worktree. Para regenerar, ajustar `REPO` en cada script.

## Geometría (`geometria.mjs`)

Compara cajas (tag, x, y, ancho, alto) de los elementos de `main` del origen frente a la página migrada, en orden de DOM, con Chrome real. Necesita `puppeteer-core` (instalar fuera del repositorio) y el origen servido en un puerto y la migración con `pnpm preview`:

    node geometria.mjs index.html 1280 900

Variables: `DUMP=ruta.json` vuelca las cajas; `STYLE_IDX=26,27` vuelca estilos computados; `N=40` cuántos desalineados listar.
