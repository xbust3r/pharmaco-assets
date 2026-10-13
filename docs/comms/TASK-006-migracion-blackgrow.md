---
tipo: TASK
id: TASK-006
titulo: Migrar la web de assets a la arquitectura Blackgrow 2026, tal cual y sin jQuery
de: clia
para: kia
cc: [dexia, miguel]
prioridad: P0
estado: EN_REVISION
area: codigo
criticidad: "🔴"
relacionado: [DECISION-010, AGENTS.md, sistema-web-assets.md, TASK-001, TASK-004]
creado: 2026-10-12
actualizado: 2026-10-12
---

# TASK-006 — Migración a Blackgrow 2026

## ⏳ Cuándo empieza

**Cuando TASK-001 esté CERRADA** ([`DECISION-010`](DECISION-010-arquitectura-blackgrow-sin-jquery.md), punto 5). Hasta entonces, no se toca.

## Contexto

Las 9 maquetas de `assets/` usan Gulp + inuitCSS + Sass + jQuery. Pasan, **sin cambiar diseño ni contenido**, a la arquitectura de `~/servers/blackgrow 2026` (Vite + Vituum + Pug + Tailwind v4), con JavaScript nativo. Blackgrow ya hizo una migración igual: su `INFORME-MIGRACION.md` y `docs/migracion/` son la referencia de método. **Léelos antes de empezar.**

## Pedido

Rama `feat/TASK-006-migracion-blackgrow`, desde `main`. Por fases, **un commit o más por fase** y una entrada en el hilo al cerrar cada una:

| Fase | Qué | Criticidad |
| --- | --- | --- |
| 0 | **Inventario de origen.** Parte de `docs/diseno/sistema-web-assets.md` (TASK-004 A) y complétalo leyendo `assets/`: páginas, componentes, tokens (colores exactos, Poppins, los 7 breakpoints), JS y sus usos. Va en `docs/migracion/inventario.md` | 🟢 |
| 1 | **Base del proyecto.** Copia de Blackgrow la **infraestructura**: `package.json`, `pnpm-lock.yaml`, `vite.config.*`, `postcss.config.*`, configs de lint, `plugins/`, `.gitignore`, husky. **Nada de su contenido, marca, páginas ni assets.** Sin `node_modules` ni `dist`. `pnpm install` y `pnpm build` de una página vacía | 🔴 |
| 2 | **Tokens en `@theme`.** Los valores exactos de Pharmaco, no reinterpretados. Los breakpoints de Tailwind por defecto se sustituyen por los 7 de origen. Si un color está escrito a mano fuera de las variables, se extrae a token | 🔴 |
| 3 | **Layout, header y footer** | 🔴 |
| 4 | **Componentes** (hero, servicios, proceso, portafolio, equipo, logos, contacto…) como mixins Pug | 🟡 |
| 5 | **Las 9 páginas**, fieles a `assets/*.html` | 🟡 |
| 6 | **JavaScript nativo**: sustituye jQuery, Modaal, AOS y tiny-slider según la tabla de DECISION-010. Sin dependencias nuevas | 🔴 |
| 7 | **Fidelidad.** Adapta `validate:origen` y `verify:render` para comparar contra `assets/` servido en local. Capturas de cada página a 375 px y en escritorio, origen contra migrada | 🔴 |
| 8 | **Informe** `docs/migracion/INFORME-MIGRACION.md`: qué se migró, decisiones tomadas y pendientes | 🟢 |

**Checkpoint:** tras la **fase 2**, pide REVIEW a Dexia y sign-off a Clia antes de seguir. La base y los tokens se propagan a todo: un error ahí se repite en las 9 páginas.

## Reglas

- **`assets/` no se modifica**: es el origen.
- **Tal cual:** los textos se copian como están, con su «Lorem ipsum» y sus erratas. No se corrige ni se inventa contenido. Lo que esté roto en el origen se migra igual y se lista en el informe.
- **Sin jQuery ni dependencias de JS nuevas.** `<dialog>`, `IntersectionObserver` y `scroll-snap`, con `prefers-reduced-motion` respetado.
- **Mobile first**, accesibilidad (foco visible, nombre accesible, `aria-expanded`), como en Blackgrow.
- **Si un commit toca algo 🔴, su primera línea lo dice.**

**Fuera de alcance:** rediseño, textos nuevos, el catálogo de 11 servicios (es `RFC-002`), publicación.

## Criterios de aceptación

- [ ] Inventario de origen en `docs/migracion/inventario.md`
- [ ] 9 páginas migradas, fieles al origen a 375 px y en escritorio, con capturas de comparación
- [ ] 0 referencias a jQuery, Modaal, AOS o tiny-slider (`grep` pegado en el hilo)
- [ ] Verificación completa de `AGENTS.md` con la salida real pegada: `verify:render` sin FALLOS y `validate:origen` sin regresiones
- [ ] `assets/` intacto (`git diff main -- assets/` vacío)
- [ ] Informe de migración
- [ ] REVIEW de Dexia ✅ (checkpoint de fase 2 y final) + sign-off de Clia 🔴

## 💬 Hilo

> **[2026-10-12] clia:** creo la task. Kia: no empieces hasta que TASK-001 esté cerrada. Cuando empieces, la referencia de método es la migración de Blackgrow. Copia su forma de trabajar y su infraestructura, nunca su contenido.
>
> **[2026-10-12] clia:** **TASK-001 está cerrada: TASK-006 puede empezar.** Kia, trabaja en la rama `feat/TASK-006-migracion-blackgrow`, en su worktree `.claude/worktrees/task-006-migracion`, que ya parte de `main`. Recuerda el checkpoint después de la fase 2.

> **[2026-10-12 22:48] kia:** tomo la task en `feat/TASK-006-migracion-blackgrow` (worktree `.claude/worktrees/task-006-migracion`, desde `main` `cb2b014`). Leídos AGENTS.md, mi ficha, el protocolo, esta TASK con su hilo, DECISION-010 y la referencia de Blackgrow (`INFORME-MIGRACION.md`, `docs/migracion/README.md`, `AGENTS.md`, `package.json`, `vite.config.js`, `plugins/`). Empiezo por la fase 0.
>
> **Preguntas a Clia (no bloquean la fase 0):**
> 1. **9 o 10 maquetas.** La TASK y DECISION-010 dicen 9, pero `assets/` contiene 10 `.html`: campana-cyberwow, campana-iveco, campana-stralis, contactanos, diseño-de-personajes, index, nosotros, portafolio, servicio-detalle y servicios. Hasta que digas lo contrario migro las 10, porque la fase 5 pide «fieles a `assets/*.html`». ¿Hay alguna que no entra?
> 2. **`imask` en el `package.json` de Blackgrow.** Es una dependencia de JS de su contenido, no infraestructura. DECISION-010 no admite dependencias de JS nuevas sin RFC, así que propongo no copiarla y regenerar el lockfile sin ella. Lo haré salvo que digas otra cosa.
> 3. **pnpm.** El `packageManager` de Blackgrow fija `pnpm@12.3.4`, que no estaba instalado en esta máquina. Lo instalo con `npm i -g pnpm@12.3.4` para correr `pnpm install` y `pnpm build`.

> **[2026-10-12 22:51] kia:** **fase 0 cerrada.** Inventario en `docs/migracion/inventario.md`. Las 10 maquetas, sus componentes, tokens (57 colores hex, tipografía, 7 breakpoints más 12 `@media` propios), el JS de aplicación (sin jQuery) y las referencias de assets, con sus conteos. Sale de `assets/` y del CSS/JS compilados; el mapa de fuentes no trae todo el JS, así que lo de `site-header`, `clients`, `forms` y `modals` se lee del bundle.
>
> **Discrepancias con el encargo y con `sistema-web-assets.md` (sección 2 y 9 del inventario):**
> 1. **10 maquetas, no 9.** Pregunta ya abierta.
> 2. **12 `@media` fuera de los 7 breakpoints** (600, 700, 900, 980 y 1140 px; alturas de 820 a 1100 px; un `min-width:1400px` que duplica `ultrawide`). Decidir si son breakpoints del sistema o excepciones.
> 3. **Poppins sólo en 400, 500 y 600.** No hay Bold ni ExtraBold, aunque `sistema-web-assets.md` los nombra. El CSS pide también 300 y 700.
> 4. **`.o-wrapper` = 1302 px**, no 1200 px.
> 5. **2 referencias de imagen rotas** en el origen: `video1-l.webp` (cyberwow) y `publicacion-revista-revista1-lg.webp` (iveco). Se migran rotas y van al informe.
> 6. **Enlaces a páginas que no existen:** `test.html` (50), `blog.html` (20), `buscar.html` (10) y `portafolio-detalle.html` (16). Se migran tal cual.
> 7. **Botón de contacto de la cabecera.** El JS lo pasa a `c-button--sky-blue` salvo en héroes `blue`, `dark-purple` o `purple`. Parece invertido. ¿Intencionado? Lo reproduzco tal cual hasta que digas.
> 8. **`components.js` no lo carga ninguna maqueta.** Código muerto; no se migra.
>
> **Verificación.** En fase 0 no hay proyecto aún, así que no aplica `pnpm` ni `verificar-investigacion.py` (`AGENTS.md` lo reserva a TASK-001…004). Lo que sí se comprueba: `assets/` intacto:
> ```
> $ git diff main -- assets/ | wc -l
> 0
> ```
> Pendiente: lo de `tiny-slider` con `controlsContainer` y todo lo visual, que es de fases 6 y 7.
>
> Siguiente: fase 1 (🔴, infraestructura de Blackgrow). Espero las respuestas de Clia a 1, 2 y 3 antes de tocar `package.json` y el lockfile; si no llegan, sigo con lo que no depende de ellas.

> **[2026-10-12 22:55] kia:** 🔴 **fase 1 hecha: base del proyecto.** Infraestructura copiada de Blackgrow: `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `vite.config.js`, `postcss.config.mjs`, configs de lint (`eslint`, `stylelint`, `markuplint`), `.prettierrc`, `.lintstagedrc`, `.gitattributes`, `.husky/pre-commit`, `plugins/`, `requirements-fonts.txt`, `figma-assets.json` y la sección `.gitignore` que faltaba. **Nada de su contenido, marca, páginas ni assets.**
>
> Cambios respecto a Blackgrow, que hago sin esperar respuesta (son reversibles):
> - **`imask` no se copia.** Era dependencia de JS de su contenido. Lockfile regenerado sin ella.
> - `name` pasa a `pharmaco-assets`. Sin `dependencies`.
> - `pnpm` 12.3.4 instalado en `~/.local/bin`: la instalación global en `/usr/local` pide permisos de root.
> - Una página vacía (`src/pages/index.pug`), un `src/styles/styles.css` y un `src/scripts/main.js` de una línea. Los lint necesitan al menos un archivo de cada tipo; no hay tokens ni JS de producto todavía.
> - `git config core.hooksPath` = `.husky/_`, puesto por `husky`. Es configuración del repositorio compartido por los worktrees; en `main` no hay `.husky/_`, así que allí no corre el hook.
>
> **Verificación, salida real de `AGENTS.md`** (sin `--sin-red`, sin pasos saltados; sólo quito los códigos de color):
> ```
> $ pnpm optimize && pnpm lint && pnpm validate && pnpm build && pnpm verify:render && pnpm validate:origen
> $ node plugins/convertWebp.js
> Start image optimization … ✅ Completed in 0.03s · Processed: 0 · Skipped: 0
> $ node plugins/validate-assets.js
> ✔ Todos los assets existen. Procediendo...
> $ markuplint "src/**/*.pug"   → <markuplint> passed src/pages/index.pug
> $ stylelint … / eslint …       → sin salida de error
> $ vite build                   → ✓ built in 430ms (dist/index.html, dist/assets/styles/styles.css, dist/assets/scripts/main.js)
> $ node plugins/verify-render.js
> AVISO fuentes  ningún token de `@theme` nombra una familia y no hay ningún `@font-face`: si el diseño lleva fuente propia, todavía no se ha entregado
> Páginas revisadas: 1 · assets medidos: 0
> $ node plugins/validate-origen.js
> Error: ENOENT: no such file or directory, open '…/docs/migracion/origen-comportamientos.json'
> ELIFECYCLE Command failed with exit code 1
> ```
> Resultado: **`pnpm build` y `pnpm verify:render` en verde** (0 FALLOS, 1 AVISO esperado). **`pnpm validate:origen` falla** y lo hará hasta la fase 7: lee `origen-comportamientos.json`, que es el catálogo de Playgrow en Blackgrow. Lo adapto en la fase 7, como pide la TASK. No lo doy por verde.
>
> `src/assets/images/sprite.svg` lo genera el build y está vacío (no hay iconos todavía). No se versiona en esta fase.
>
> Siguiente: fase 2 (tokens en `@theme`, 🔴). Es checkpoint, así que la paro después y pido REVIEW y sign-off.
>
> Salida completa, con el código de salida de cada comando: `docs/migracion/logs/fase-1-verificacion.txt`. Los extractos de arriba están abreviados; el registro es el literal. `lint`, `build` y `verify:render` salen con código 0; `validate:origen` sale con código 1.

> **[2026-10-12 23:00] kia:** 🔴 **fase 2 hecha: tokens en `@theme`. Checkpoint: pido REVIEW a Dexia y sign-off a Clia.** `src/styles/styles.css` y `src/assets/fonts/` (copia de `assets/fonts/`, sin tocar el origen).
>
> **Qué contiene:** 57 hex del origen, 4 `rgba` de color (overlay, sombra de la cabecera, control de la galería de Modaal y transparente), Poppins en 400, 500 y 600 con su `@font-face`, 27 tamaños en px, los 7 breakpoints en `em` (`22.5em`…`87.5em`, los mismos valores del origen), el contenedor de 1302 px con variantes de 1120 y 1440, 19 radios, y 9 sombras. Las colecciones por defecto de Tailwind están vacías (`--color-*: initial` y demás).
>
> **Comprobación de cobertura** (`scratchpad`, script no versionado, salida real):
> ```
> origen hex unicos: 57 | tokens hex unicos: 57
> en origen y NO en tokens: []
> en tokens y NO en origen: []
> ```
> Los tamaños, radios y breakpoints salen de `main.css` por script; las sombras, de sus valores exactos.
>
> **Verificación de `AGENTS.md`** (salida completa en `docs/migracion/logs/fase-2-verificacion.txt`, con código de salida por comando): `pnpm optimize` 0, `pnpm lint` 0, `pnpm validate` 0, `pnpm build` 0 con `verify:render` en «Todo correcto», `pnpm verify:render` 0, `pnpm validate:origen` **1** (ENOENT sobre `origen-comportamientos.json`, fase 7). Sin FALLOS en `verify:render`.
>
> **Desviaciones de Blackgrow que pido firmar:**
> 1. **Sin preflight.** Importo `tailwindcss/theme.css` y `tailwindcss/utilities.css`, no `tailwindcss`. El origen trae su propio reset (normalize e inuitCSS); el preflight de Tailwind cambiaría el render de todas las páginas.
> 2. **`.stylelintrc` (`stylelint.config.mjs`): `import-notation: string`.** Sin esto, `stylelint --fix` reescribe el `@import` como `url()` y `validate-assets.js` lo toma por una ruta local. Es un cambio de lint, no de build, pero lo señalo porque es 🔴 por el gate.
> 3. **Pesos como `--weight-*`**, no `--font-weight-*`: `verify-render` lee `--font-*` como familias y da FALLO con `400`. Lo arreglo en la fase 7 si hace falta.
> 4. **`--font-sans` queda en minúsculas** (`poppins, arial…`). Lo hace el `--fix` de stylelint. Los nombres de familia no distinguen mayúsculas en CSS, así que es el mismo valor; lo anoto por si Dexia lo quiere exacto.
> 5. **`1.58463px`** (sombra `--shadow-media`) tiene una desactivación local de `number-max-precision`. Redondear a `1.5846` cambiaría el valor del origen.
>
> **Nombres de color:** los asigno por el papel que tienen en el CSS origen (qué selector y propiedad los usan; mapa en mi scratchpad). El origen no trae los nombres: su archivo de settings no está en el mapa. Pido a Dexia que revise los nombres.
>
> **Decisiones que bloquean la fase 3 (las necesito de Clia):**
> - **A. ¿Utilidades de Tailwind en el marcado (como Blackgrow) o CSS de componente con los nombres BEM del origen usando los tokens?** Mi propuesta es utilidades, porque es lo que pide la referencia de método y deja los valores en un solo sitio. Es más trabajo: las 10 páginas se reescriben clase a clase, y la fidelidad se mide en la fase 7.
> - **B. Los 12 `@media` que no son de los 7 breakpoints** (inventario, sección 2.2): ¿breakpoints propios de `@theme` o excepciones por componente?
> - **C. 9 o 10 maquetas** (pregunta de la fase 0, todavía sin respuesta).
>
> **Petición:** Dexia, REVIEW del checkpoint de fase 2 sobre el commit de la fase 2. Clia, sign-off 🔴 de las fases 1 y 2 (`946de89` y el commit de esta fase), y respuesta a A, B y C. No sigo con la fase 3 hasta tener las tres cosas.
>
> Qué no está verificado: nada visual, porque la fase 2 no tiene marcado. Los valores del CSS son los del origen, pero el render real sólo se comprueba desde la fase 3, con capturas.

> **[2026-10-12 23:01] kia:** corro `scripts/verificar-investigacion.py` como exige mi protocolo. Su gate es el de TASK-001 a TASK-004 (`AGENTS.md`), **no el de esta TASK**: la salida no dice nada sobre la migración. Resumen literal y los FALLOS, con su archivo:
> ```
> Verificación de la investigación · raíz: …/task-006-migracion/docs · V8: con red
> V4  FALLO   diseno/capturas/servicio-detalle-desktop.png — idéntica (mismo SHA-256) a diseno/capturas/servicios-desktop.png
> V4  FALLO   diseno/capturas/servicios-desktop.png — idéntica (mismo SHA-256) a diseno/capturas/servicio-detalle-desktop.png
> V4  FALLO   diseno/capturas/servicio-detalle-mobile-375px.png — idéntica (mismo SHA-256) a diseno/capturas/servicios-mobile-375px.png
> V4  FALLO   diseno/capturas/servicios-mobile-375px.png — idéntica (mismo SHA-256) a diseno/capturas/servicio-detalle-mobile-375px.png
> V6  FALLO   investigacion/prueba-social.md — marcador de plantilla «Lorem» en la línea 135
> V6  FALLO   investigacion/prueba-social.md — marcador de plantilla «Lorem» en la línea 136
> 6 FALLOS · 34 AVISOS
> 6 FALLOS · 34 AVISOS
> ```
> Los 6 FALLOS están en TASK-004 (`diseno/capturas/`, capturas idénticas por SHA-256) y en TASK-003 (`investigacion/prueba-social.md`, «Lorem» en las líneas 135 y 136). Ninguno en un archivo de esta TASK: el verificador no recorre `docs/migracion/`, así que **0 FALLOS en mis archivos** es trivial. No lo cuento como verificación de la migración.
>
> **[2026-10-12] clia:** buen trabajo en las fases 0 a 2, y buen inventario: los hallazgos (10 maquetas, 12 `@media` propios, pesos de Poppins inexistentes, `.o-wrapper` de 1302 px) son exactamente lo que una migración tiene que encontrar. Decisiones:
>
> - **A. Utilidades de Tailwind en el marcado, como Blackgrow.** Sin CSS de componente con los nombres BEM del origen. Lo que se repite se convierte en mixin Pug, no en cadenas de clases copiadas.
> - **B. Los 12 `@media` propios:**
>   - **Los de ancho pasan a breakpoint con nombre en `@theme`** cuando no coinciden ya con uno de los 7: 700 px = 43.75em y 980 px = 61.25em ya existen; 600, 900 y 1140 px, si se usan, entran como tokens nuevos.
>   - **Los de altura** (820 a 1100 px) se migran como variantes a medida y quedan documentados uno por uno en el inventario.
>   - **El `min-width: 1400px` duplicado y el `@media screen` sin condición** son ruido del origen: no se migran y se anotan.
> - **C. Las 10 maquetas.** Migrar tal cual significa migrar todo lo que hay.
> - **El JS de la cabecera que parece invertido:** se reproduce tal cual y se lista como pendiente en el informe. Lo mismo con los enlaces a páginas inexistentes y las dos imágenes rotas.
> - **Poppins 300 y 700:** el origen las pide y no existen. Se migra igual (el navegador sintetiza el peso) y se anota.
> - **Desviaciones de Blackgrow que pides firmar** (sin preflight, `import-notation`, `--weight-*`, `--font-sans` en minúsculas y `number-max-precision` local): las firmo **después del REVIEW de Dexia**, como dice el gate. Las cinco están justificadas en el hilo.
> - **imask fuera:** correcto; no hay formularios con máscara en el origen.
> - **Requisito nuevo, husky:** `core.hooksPath=.husky/_` está en la configuración **compartida** del repositorio. Cuando esto entre en `main`, el `pre-commit` se ejecutará en todos los worktrees, incluidos los que no tienen `node_modules`. **El hook no puede bloquear un commit que solo toca `docs/`**: o sale en 0 si no hay archivos de `src/` en el stage, o comprueba que `node_modules` existe. Corrígelo antes del merge y pega la prueba de un commit de solo `docs/` en un worktree sin instalar.
>
> Ahora lanzo a Dexia para el checkpoint de la fase 2. **No empieces la fase 3 hasta su ✅ y mi sign-off.**
