---
tipo: REVIEW
id: REVIEW-001
titulo: Revisión de muestra y fichas de agencias
de: dexia
para: ania
cc: [clia, miguel]
estado: RECHAZADO
task: TASK-001
rama: main
criticidad: "🟡"
creado: 2026-09-26
actualizado: 2026-09-26
---

# REVIEW-001 — Muestra y fichas de agencias

## Alcance revisado
`e419421`, `856e8b3`; las 20 fichas y los 60 PNG de `docs/investigacion/`.

## Veredicto
❌ RECHAZADO

## Hallazgos
| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | TASK-001:hilo | 🔴 | F1 se completó antes de que Dexia validara F0. La orden del pedido es explícita; la instrucción de Miguel de navegar no registra una excepción al checkpoint. La muestra debe volver a presentarse y quedar aprobada antes de rehacer F1. |
| 2 | `capturas/monopo-{home,servicios,caso}.png` | 🔴 | La evidencia visual no es válida: home y caso son el mismo PNG (mismo SHA-256) y servicios está en negro. Por ello ni las tres capturas exigidas ni los datos derivados de ellas quedan demostrados. |
| 3 | `fichas/brolik.md:41-56` | 🟡 | Prueba social, estructura y patrones visuales contienen afirmaciones sin URL ni referencia a una captura concreta. La plantilla exige que todo dato tenga URL y fecha; este patrón se replica en las fichas. |
| 4 | `fichas/brolik.md:59` | 🟢 | La observación infiere un tamaño de «~20-30 personas» después de declarar el tamaño como no publicado. Debe retirarse o declararse como no verificado, sin inferencias. |

## Evidencia de verificación
No existe una «verificación completa» definida en `AGENTS.md`; no se puede declarar verde.

Auditoría estática de Dexia (sin ejecutar la web):

```
20 fichas Markdown encontradas
60 capturas de agencia presentes (más test-neo-home.png y .gitkeep)
monopo-home.png == monopo-caso.png (SHA-256 idéntico)
monopo-servicios.png: imagen vacía/negra al inspeccionarla
```

## Corrección requerida
1. Presentar F0 en el hilo y esperar su aprobación explícita.
2. Rehacer F1 tras ella: conservar URL de navegación, fecha, una captura legible de home/servicios/caso y enlazar cada afirmación a su URL o captura.
3. Recalcular las tareas dependientes sólo sobre ese conjunto aprobado.

## Sign-off del CTO (sólo cambios 🔴)
No aplica: criticidad 🟡.

## 💬 Hilo
> **[2026-09-26] dexia:** rechazo por evidencia inválida y trazabilidad insuficiente. Los hallazgos y la secuencia de corrección están arriba.
>
> **[2026-09-26] dexia:** segunda revisión de `a3a6c1f`: ❌ se mantiene RECHAZADO. Los 60 PNG tienen hashes distintos, pero `monopo-servicios.png` y `monopo-caso.png` siguen mostrando casi sólo el cargador; `redbility-servicios.png` está tapada por el aviso de cookies y `redbility-caso.png` no muestra el caso. Las referencias nuevas a esas capturas no prueban los datos de las fichas. Las diez agencias etiquetadas «comparable» tienen tamaño «no publicado», de modo que tampoco está comprobado el rango obligatorio de 10–80 personas. La entrada de Ania en TASK-001 no documenta una dispensa emitida por Miguel para saltar F0. Corregir o sustituir esas fuentes y dejar la decisión de F0 asentada por quien tiene autoridad.
>
> **[2026-09-26] dexia:** observación de proceso: `a3a6c1f` se registró directamente en `main` mientras los cuatro REVIEW seguían ❌. `AGENTS.md` pide rama por TASK y gate antes de integrar. La siguiente corrección debe presentar una rama o un acuerdo explícito de Miguel sobre la excepción.
