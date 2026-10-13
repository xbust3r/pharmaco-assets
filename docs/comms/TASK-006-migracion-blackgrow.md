---
tipo: TASK
id: TASK-006
titulo: Migrar la web de assets a la arquitectura Blackgrow 2026, tal cual y sin jQuery
de: clia
para: kia
cc: [dexia, miguel]
prioridad: P0
estado: EN_PROGRESO
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
