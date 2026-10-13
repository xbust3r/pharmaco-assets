---
tipo: REVIEW
id: REVIEW-006
titulo: Checkpoint de fases 0–2 de la migración Blackgrow
de: dexia
para: kia
cc: [clia, miguel]
estado: APROBADO
task: TASK-006
rama: feat/TASK-006-migracion-blackgrow
criticidad: "🔴"
creado: 2026-10-12
actualizado: 2026-10-12
---

# REVIEW-006 — Checkpoint de fases 0–2

## Alcance revisado

Commits `6f5843e` (inventario), `946de89` (infraestructura) y `aa3aad6` (tokens), sobre `cb2b014`. También las decisiones posteriores de Clia en el hilo de TASK-006. Revisé `docs/migracion/inventario.md`, la configuración de Vite, pnpm y lint, los verificadores copiados, `src/styles/styles.css`, las fuentes y la página provisional. No es la revisión final de las diez páginas.

## Veredicto

✅ **APROBADO el checkpoint de fases 0–2**, sobre `aa3aad6`. Clia puede hacer el sign-off 🔴 de ese estado concreto. La fase 3 puede comenzar después de su firma. Este veredicto no habilita el merge de TASK-006: falta la verificación completa en verde y el REVIEW final.

## Hallazgos y seguimiento

| # | Archivo:línea | Severidad | Hallazgo y condición |
| --- | --- | --- | --- |
| 1 | `plugins/validate-origen.js:33` | 🔴 para el merge; fase 7 | Lee `docs/migracion/origen-comportamientos.json`, que no existe, y conserva el contrato de Playgrow. `pnpm validate:origen` acaba en `ENOENT`. La TASK asigna su adaptación a la fase 7. El gate completo deberá pasar contra `assets/` antes del REVIEW final. |
| 2 | `.husky/pre-commit:1` | 🔴 para el merge | Invoca `pnpm exec lint-staged` sin comprobar la presencia de `node_modules` ni si el stage sólo contiene `docs/`. Clia ya exigió corregirlo y probar un commit de documentación en un worktree sin instalación. |
| 3 | `.gitignore`, `src/assets/images/sprite.svg` | 🟢 | El build deja `src/assets/images/` sin seguimiento; el sprite está vacío porque aún no hay iconos. Kia debe dejar claro si ese archivo generado se versiona o se ignora, para evitar incluirlo por accidente. |
| 4 | `docs/migracion/inventario.md:19,325` | 🟢 | El inventario aún llama «pregunta abierta» a las diez páginas y a los `@media`; Clia ya decidió ambas cosas en TASK-006. Agregar una nota de resolución al documento propio antes del informe final. |

Los nombres semánticos de color son una decisión de migración, porque el mapa Sass no contiene sus nombres originales. No encontré un nombre que atribuya al origen un valor distinto. Las cinco desviaciones de Blackgrow declaradas por Kia (sin preflight, `import-notation`, `--weight-*`, minúsculas en la pila de fuentes y precisión local de sombra) tienen motivo técnico y no cambian los valores comprobados.

## Evidencia de verificación

Comprobación directa de Dexia sobre `assets/css/main.css` y los archivos de fuente:

```text
hex source 57 tokens 57 missing [] extra []
Poppins-SemiBold.woff True
Poppins-Medium.woff2 True
Poppins-Medium.woff True
Poppins-Regular.woff True
Poppins-Regular.woff2 True
Poppins-SemiBold.woff2 True
```

`git diff main -- assets/` no produjo salida. El preview respondió `HTTP/1.1 200 OK` en `127.0.0.1:5274` y sirvió la página provisional con `lang="es"`, viewport y el texto de fase 1. No hay páginas de producto para comparar visualmente a 375 px o escritorio en este checkpoint; esa comparación corresponde a la fase 7.

Dexia ejecutó `pnpm optimize && pnpm lint && pnpm validate && pnpm build && pnpm verify:render && pnpm validate:origen`. La salida real completa de la misma secuencia, ejecutada por Kia sobre `aa3aad6`, se pega a continuación. La repetición de Dexia dio el mismo resultado: comandos hasta `verify:render` con código 0, `validate:origen` con código 1 y `ENOENT` sobre el mismo archivo. `verify:render` revisa sólo una página provisional y cero assets, por lo que aún no acredita fidelidad visual.

```text
# Salida real de la verificacion de AGENTS.md, fase 2 de TASK-006 (2026-10-12 22:59)

$ pnpm optimize
$ node plugins/convertWebp.js
Start image optimization
------------------------------------------------
✅  Completed in 0.01s
   • Processed: 0
   • Skipped:  0
------------------------------------------------
[exit 0]

$ pnpm lint
$ run-p lint:pug lint:css lint:js
$ markuplint "src/**/*.pug"
$ stylelint "src/**/*.css" --fix --cache --cache-location .stylelintcache
$ eslint "src/**/*.js" --fix --cache --cache-location .eslintcache
<markuplint> passed /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion/src/pages/index.pug
[exit 0]

$ pnpm validate
$ node plugins/validate-assets.js
🔍 Iniciando validación estricta de assets...
✔ Todos los assets existen. Procediendo...

[exit 0]

$ pnpm build
$ npm-run-all optimize --parallel lint validate
$ node plugins/convertWebp.js
Start image optimization
------------------------------------------------
✅  Completed in 0.01s
   • Processed: 0
   • Skipped:  0
------------------------------------------------
$ run-p lint:pug lint:css lint:js
$ node plugins/validate-assets.js
🔍 Iniciando validación estricta de assets...
✔ Todos los assets existen. Procediendo...

$ markuplint "src/**/*.pug"
$ stylelint "src/**/*.css" --fix --cache --cache-location .stylelintcache
$ eslint "src/**/*.js" --fix --cache --cache-location .eslintcache
<markuplint> passed /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion/src/pages/index.pug
$ vite build
vite v8.2.2 building client environment for production...
[vite-plugin-svg-sprite] Sprite generated /src/assets/images/sprite.svg
transforming...
✓ 4 modules transformed.
rendering chunks...
computing gzip size...
dist/assets/images/sprite.svg              0.08 kB │ gzip: 0.08 kB
dist/index.html                            0.34 kB │ gzip: 0.24 kB
dist/assets/fonts/Poppins-Medium.woff2    51.69 kB
dist/assets/fonts/Poppins-SemiBold.woff2  52.40 kB
dist/assets/fonts/Poppins-Regular.woff2   52.45 kB
dist/assets/fonts/Poppins-Medium.woff     72.66 kB
dist/assets/fonts/Poppins-SemiBold.woff   73.20 kB
dist/assets/fonts/Poppins-Regular.woff    73.51 kB
dist/assets/styles/styles.css              6.87 kB │ gzip: 1.65 kB
dist/assets/scripts/main.js                0.00 kB │ gzip: 0.02 kB

✓ built in 532ms
$ node plugins/verify-render.js
Comprobación de render
------------------------------------------------
Todo correcto: los assets pintan, las proporciones cuadran y no hay valores fuera del sistema.
------------------------------------------------
Páginas revisadas: 1  ·  assets medidos: 0
[exit 0]

$ pnpm verify:render
$ node plugins/verify-render.js
Comprobación de render
------------------------------------------------
Todo correcto: los assets pintan, las proporciones cuadran y no hay valores fuera del sistema.
------------------------------------------------
Páginas revisadas: 1  ·  assets medidos: 0
[exit 0]

$ pnpm validate:origen
$ node plugins/validate-origen.js
node:fs:436
    return binding.readFileUtf8(path, stringToFlags(options.flag));
                   ^

Error: ENOENT: no such file or directory, open '/Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion/docs/migracion/origen-comportamientos.json'
    at readFileSync (node:fs:436:20)
    at file:///Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion/plugins/validate-origen.js:33:5
    at ModuleJob.run (node:internal/modules/esm/module_job:437:25)
    at async onImport.tracePromise.__proto__ (node:internal/modules/esm/loader:642:26)
    at async asyncRunEntryPointWithESMLoader (node:internal/modules/run_main:101:5) {
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: '/Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-006-migracion/docs/migracion/origen-comportamientos.json'
}

Node.js v26.0.0
[ELIFECYCLE] Command failed with exit code 1.
[exit 1]
```

## Sign-off del CTO (cambios 🔴)

- [x] **Clia (CTO): FIRMADO — 2026-10-12, checkpoint de fases 0–2 sobre `aa3aad6`.** Verificación propia en el hilo. Vale para ese estado del código.

## 💬 Hilo

> **[2026-10-12 23:04] dexia:** emito ✅ para el checkpoint de fases 0–2. Los 57 hex y las seis fuentes coinciden con `assets/`; el build y `verify:render` pasan para la página provisional. `validate:origen` sigue en rojo por el catálogo de Playgrow, cuya adaptación está prevista en fase 7. Antes del merge hacen falta esa adaptación, el hook seguro para commits de `docs/`, la comparación visual y el REVIEW final. Solicito el sign-off 🔴 de Clia sobre `aa3aad6` para que Kia continúe con la fase 3.
>
> **[2026-10-12] clia:** **sign-off 🔴 FIRMADO para el checkpoint de fases 0–2** (`946de89`, `aa3aad6`). Comprobado por mi cuenta:
>
> 1. `git diff main -- assets/`: vacío. El origen está intacto.
> 2. `pnpm run lint`, `validate`, `build` y `verify:render`: **exit 0** en los cuatro. `verify:render`: «Todo correcto».
> 3. Colores: los 57 hex distintos de `assets/css/*.css` están todos en `@theme` (57 = 57, ninguno falta).
> 4. Las cinco desviaciones de Blackgrow (sin preflight, `import-notation`, `--weight-*`, `--font-sans` en minúsculas y `number-max-precision` local) quedan **aprobadas**, con la justificación de Kia en el hilo.
>
> **Esta firma no habilita el merge:** antes del final siguen pendientes `validate:origen` (fase 7) y el arreglo del hook de husky. Kia: puedes empezar la fase 3.
