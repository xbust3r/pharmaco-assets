---
tipo: DECISION
id: DECISION-009
titulo: El gate de la investigación se evalúa por TASK; la etapa cierra con 0 FALLOS globales
de: clia
para: [dexia, kia]
cc: [miguel]
estado: EFECTIVA
estrategica: false
relacionado: [AGENTS.md, DECISION-006, TASK-001, TASK-002, TASK-003, TASK-004, REVIEW-001]
creado: 2026-10-10
actualizado: 2026-10-10
---

# DECISION-009 — Gate por TASK

## Contexto

En la undécima ronda de `REVIEW-001`, Dexia acepta el contenido de F1 pero rechaza la excepción de alcance que Clia escribió en el hilo de TASK-001. Tiene razón: `AGENTS.md` exige **0 FALLOS** en la ejecución completa, y una entrada en un hilo no puede contradecir a `AGENTS.md`.

Aplicado al pie de la letra, `AGENTS.md` produce un **bloqueo circular**:

- TASK-001 no puede cerrar mientras haya FALLOS en `prueba-social.md` (TASK-003) y en `diseno/` (TASK-004).
- TASK-003 y TASK-004 no pueden rehacerse hasta que TASK-001 cierre, porque sus conteos salen de las fichas aprobadas.

## Decisión

1. **El gate de cada TASK de investigación exige 0 FALLOS en sus propios archivos:**

   | TASK | Archivos que cuentan |
   | --- | --- |
   | TASK-001 | `investigacion/fichas/*.md` (sin `anexo-medianas/`), las capturas que citan y V7 |
   | TASK-002 | `investigacion/servicios/*.md` y las capturas que citan |
   | TASK-003 | `investigacion/prueba-social.md` y las capturas que cita |
   | TASK-004 | `diseno/*.md` y `diseno/capturas/` |

2. **La salida que se pega sigue siendo la completa, con red.** Cada FALLO fuera de alcance se lista en el hilo con su archivo y la TASK a la que pertenece. Dexia lo comprueba por el nombre del archivo: es mecánico, no una interpretación.
3. **La etapa de investigación cierra con 0 FALLOS globales.** Antes de `RFC-002`, la ejecución completa sobre `docs/` tiene que salir en verde. El rigor no baja; solo se ordena.
4. **El verificador tiene que estar en `main`** para que cualquier gate valga. Eso sigue dependiendo de TASK-005.
5. Se añade a `AGENTS.md`, en «Verificación de la investigación».

## Motivo

Sin esto, ninguna TASK de investigación puede cerrar. Con esto, cada TASK responde solo de lo suyo y el cierre de la etapa conserva el requisito global de `AGENTS.md`.

## Consecuencias

- Mi excepción en el hilo de TASK-001 queda sustituida por esta decisión; deja de valer como entrada suelta.
- **Sugerencia para TASK-005, no requisito:** una opción `--task TASK-00X` en el verificador haría mecánico el punto 2. La decide quien lleva TASK-005.

## Vigencia

**Efectiva desde el 2026-10-10**, con el ✅ de Miguel.

## 💬 Hilo

> **[2026-10-10] clia:** emito la propuesta. Dexia hizo bien en no aceptar una excepción escrita solo en un hilo; esta es la vía formal.
>
> **[2026-10-10] miguel:** (transcrito por Clia) sí, apruebo ambas (DECISION-008 y DECISION-009); pásala a main.
>
> **[2026-10-10] clia:** EFECTIVA. DECISION-008 pasa a `main` con sus dos commits originales (cherry-pick) y ya rige desde aquí para todas las ramas.
