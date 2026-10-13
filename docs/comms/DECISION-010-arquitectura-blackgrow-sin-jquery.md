---
tipo: DECISION
id: DECISION-010
titulo: El HTML se migra tal cual a la arquitectura Blackgrow 2026, sin jQuery y con JavaScript nativo
de: clia
para: [kia, dexia]
cc: [miguel]
estado: EFECTIVA
estrategica: true
relacionado: [RFC-001, AGENTS.md, protocolo.md, TASK-006, sistema-web-assets.md]
creado: 2026-10-12
actualizado: 2026-10-12
---

# DECISION-010 — Arquitectura del HTML

## Contexto

La web de assets de Pharmaco (`assets/`, 9 maquetas) está hecha con el stack antiguo del equipo, la plantilla *front-end-core*: Gulp + inuitCSS + Sass + sass-mq, con **jQuery** y tres librerías (**Modaal**, plugin de jQuery para modales; **AOS**; **tiny-slider**). `RFC-001` tenía abierta la pregunta del stack.

## Decisión

Por decisión de Miguel:

1. **Arquitectura: Blackgrow 2026** (`~/servers/blackgrow 2026`): Vite + Vituum + **Pug** + **Tailwind v4**, con pnpm, lint (markuplint, stylelint, eslint), `validate`, `verify:render` y `validate:origen`. Se toma su **infraestructura**, no su contenido ni su marca.
2. **Alcance: migrar tal cual.** Las 9 maquetas pasan a la nueva arquitectura **sin cambiar diseño ni contenido**: mismos textos, incluso el «Lorem ipsum» y los restos de plantilla, que se conservan y se listan como pendientes. El rediseño y los textos nuevos llegan después, con `RFC-002`.
3. **Sin jQuery. JavaScript nativo:**

   | Hoy | Nativo |
   | --- | --- |
   | jQuery | `querySelector`, `addEventListener`, `classList`, `dataset` |
   | Modaal | `<dialog>` + `showModal()` + `inert` en el fondo |
   | AOS | `IntersectionObserver` + CSS, sin animación con `prefers-reduced-motion` |
   | tiny-slider | `scroll-snap` de CSS + botones propios, con fallback a fila desplazable si el JS no carga |

   **No entra ninguna dependencia de JavaScript nueva** sin un RFC aprobado.
4. **`assets/` es el origen y no se modifica.** Es contra lo que se valida la fidelidad (`validate:origen`).
5. **Empieza cuando TASK-001 esté cerrada**, como pidió Miguel. No depende de TASK-002 a TASK-004, que siguen en paralelo.

## Motivo

- Blackgrow 2026 ya hizo esta misma migración (Playgrow → Blackgrow), con verificador de fidelidad y bajo el mismo flujo de tres agentes. Es la base probada más reciente del equipo.
- Migrar tal cual separa dos riesgos que juntos se enmascaran: «¿se rompió algo al cambiar de arquitectura?» y «¿el diseño nuevo es el correcto?».
- Las cuatro piezas de JS tienen equivalente nativo con mejor accesibilidad (`<dialog>` gestiona el foco; `scroll-snap` funciona sin JS).

## Consecuencias

- `RFC-001`: queda resuelto el stack. La criticidad y la verificación del código pasan a `AGENTS.md` y al protocolo.
- `AGENTS.md`: «Verificación completa» con los comandos reales de Blackgrow.
- Nace `TASK-006` (migración), para Kia, 🔴.
- `TASK-004` parte A, que documenta el sistema de la web de assets, pasa a ser el **inventario de origen** de la migración.

## Vigencia

Efectiva desde el 2026-10-12, por decisión directa de Miguel.

## 💬 Hilo

> **[2026-10-12] miguel:** (transcrito por Clia) después de TASK-001 hay que pasar el HTML a una nueva arquitectura. → Blackgrow 2026, migrar tal cual. Matamos jQuery y usamos JS nativo.
>
> **[2026-10-12] clia:** registrada como EFECTIVA. Medí la dependencia actual: `assets/js/main.js` incluye jQuery, Modaal (199 referencias), AOS y tiny-slider, según su source map. Las cuatro tienen equivalente nativo.
