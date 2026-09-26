---
tipo: REVIEW
id: REVIEW-003
titulo: Revisión de investigación de prueba social
de: dexia
para: ania
cc: [clia, miguel]
estado: RECHAZADO
task: TASK-003
rama: main
criticidad: "🟡"
creado: 2026-09-26
actualizado: 2026-09-26
---

# REVIEW-003 — Investigación de prueba social

## Alcance revisado
`430cda9`, `856e8b3`; `docs/investigacion/prueba-social.md`.

## Veredicto
❌ RECHAZADO

## Hallazgos
| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | `prueba-social.md:18-26` | 🔴 | Todos los conteos de benchmark dependen de las fichas no aprobadas en REVIEW-001; no se pueden certificar como cuadrados. |
| 2 | `prueba-social.md:57-70` | 🟡 | Los tres casos tienen URL, pero no hay enlaces a las capturas exigidas ni evidencia asociada que permita revisar la anatomía descrita. |
| 3 | `prueba-social.md:82-101` | 🟡 | Las fuentes oficiales se enlazan, pero las afirmaciones de requisitos, coste y tiempos no identifican sección/fecha de consulta por fuente; no alcanzan el criterio de evidencia verificable. |
| 4 | `prueba-social.md:177-180` | 🟡 | La lista de opciones cruza a recomendaciones y acciones concretas —incluye solicitar reseñas a clientes—, pese a que la TASK excluye contactos y pide opciones, no recomendaciones. |

## Evidencia de verificación
No hay comando de verificación definido. La parte 4 conserva preguntas explícitas a Miguel y no ha sido objeto de este rechazo; el rechazo afecta a la entrega completa porque las partes 1–3 no satisfacen la evidencia requerida.

## Corrección requerida
Recalcular partes 1–2 desde TASK-001 aprobada, enlazar las tres capturas de caso, citar sección y fecha de cada fuente oficial y reescribir la parte 5 como opciones neutrales sin prescribir ni contactar.

## Sign-off del CTO (sólo cambios 🔴)
No aplica: criticidad 🟡.

## 💬 Hilo
> **[2026-09-26] dexia:** rechazo por dependencia no validada, evidencia incompleta y salida de alcance.
