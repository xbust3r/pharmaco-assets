---
tipo: REVIEW
id: REVIEW-002
titulo: Revisión de investigación de servicios
de: dexia
para: ania
cc: [clia, miguel]
estado: RECHAZADO
task: TASK-002
rama: main
criticidad: "🟡"
creado: 2026-09-26
actualizado: 2026-09-26
---

# REVIEW-002 — Investigación de los 11 servicios

## Alcance revisado
`077f632`, `856e8b3`; 11 fichas y `servicios/resumen.md`.

## Veredicto
❌ RECHAZADO

## Hallazgos
| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | `servicios/resumen.md:13-23` | 🔴 | Los 11 conteos dependen de TASK-001, cuyo conjunto F1 no supera REVIEW-001. No son auditables ni pueden alimentar RFC-002. |
| 2 | `servicios/resumen.md:29-37` | 🟡 | Los agregados no enlazan a las fichas/URLs que los sostienen, incumpliendo el criterio de trazabilidad. |
| 3 | `servicios/07-fotografia-video.md:31-39`, `08-inteligencia-artificial.md:36-38`, `11-datos-automatizacion.md:30-31` | 🟡 | Se formulan recomendaciones de agrupación y de oferta («evitar vender…»), aunque la TASK limita el entregable a investigación y reserva las decisiones para RFC-002. Deben convertirse en evidencia neutral o retirarse. |

## Evidencia de verificación
No hay comando de verificación definido. La revisión estática confirmó 11 fichas, pero no puede validar sus frecuencias porque la fuente dependiente fue rechazada.

## Corrección requerida
Tras aprobar TASK-001, recalcular cada conteo desde las 20 fichas, enlazar cada agregado a su conjunto de fuentes y sustituir recomendaciones por opciones/evidencia.

## Sign-off del CTO (sólo cambios 🔴)
No aplica: criticidad 🟡.

## 💬 Hilo
> **[2026-09-26] dexia:** rechazo derivado de REVIEW-001 y de la falta de trazabilidad en los agregados.
