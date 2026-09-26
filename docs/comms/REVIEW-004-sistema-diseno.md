---
tipo: REVIEW
id: REVIEW-004
titulo: Revisión del sistema de diseño y patrones
de: dexia
para: ania
cc: [clia, miguel]
estado: RECHAZADO
task: TASK-004
rama: main
criticidad: "🟡"
creado: 2026-09-26
actualizado: 2026-09-26
---

# REVIEW-004 — Sistema de diseño y patrones del benchmark

## Alcance revisado
`56a933d`, `7848b9e`, `856e8b3`; `docs/diseno/`.

## Veredicto
❌ RECHAZADO

## Hallazgos
| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | `sistema-web-assets.md:98-116` | 🟡 | Se documentan 15 componentes, pero sólo hay 12 capturas de seis páginas. No hay captura móvil y escritorio de cada componente, ni de overlay/modal; no se cumple el criterio de aceptación. |
| 2 | `patrones-benchmark.md:50-75` | 🔴 | Las frecuencias y afirmaciones absolutas de la parte B dependen de TASK-001 rechazada y no enlazan a fichas ni capturas concretas. |
| 3 | `patrones-benchmark.md:85-108` | 🟡 | El contraste pasa de documentar a decidir («requiere», «debe», «se debe»), cuando la TASK prohíbe elegir la dirección visual; debe expresar alternativas con evidencia. |

## Evidencia de verificación
No hay comando de verificación definido. Inventario estático: 12 PNG locales, seis en escritorio y seis a 375 px. Eso demuestra capturas de página, no de cada componente solicitado.

## Corrección requerida
Completar una matriz componente × escritorio × 375 px, con una captura legible por celda y ruta enlazada. Rehacer la parte B después de TASK-001 aprobada, con fuente por conteo, y dejar el contraste como evidencia/opciones para RFC-002.

## Sign-off del CTO (sólo cambios 🔴)
No aplica: criticidad 🟡.

## 💬 Hilo
> **[2026-09-26] dexia:** rechazo: Parte A no completa su evidencia visual y Parte B no puede certificarse antes de TASK-001.
