# 📋 Status: Kia (DEV principal)

> **Proyecto:** Pharmaco Assets
> **Última actualización:** 2026-10-12

---

## 📝 Forma de trabajo

Subagente de Claude Code (Haiku 5.5), lanzado por Clia con el ID de la TASK. Escribe código, investiga y hace capturas; no hace push.

**Canal de activación:** mensajes dirigidos a `kia` en [`comms/tablero.md`](../comms/tablero.md).

---

## 🎯 Trabajo reciente

| Tarea | Estado | Notas |
| --- | --- | --- |
| TASK-006 · migración a Blackgrow 2026 sin jQuery (🔴) | EN_PROGRESO | Rama `feat/TASK-006-migracion-blackgrow`, worktree `.claude/worktrees/task-006-migracion`. Tomada el 2026-10-12 desde `main` `cb2b014`. Fase 0 cerrada (`6f5843e`, inventario en `docs/migracion/inventario.md`). Fase 1 hecha: infraestructura de Blackgrow sin contenido, `pnpm install` y `pnpm build` verdes sobre una página vacía; `validate:origen` falla hasta la fase 7. Tres preguntas a Clia en el hilo, sin bloquear |
| TASK-001 · merge a `main` | EN_REVISION | REVIEW-001 ✅ de Dexia sobre `5cacb1e`. Merge `--no-ff` en `main`: `aa77063`, sin conflictos. `git diff 5cacb1e main` sobre fichas y capturas vacío. Verificador sobre `main`: 0 FALLOS en TASK-001 (6 fuera de alcance: TASK-003 y TASK-004). Salida pegada en el hilo. No hice push. Anterior, F1: `5cacb1e`: decisiones de Clia del 2026-10-10 aplicadas: Pallax fila 1 (Branding) a «Sí» como tema del formulario, con portada única; Digiberries, AVISO de las 16 URL con desafío en las filas 2, 3, 4, 5, 8, 9 y 10. Gate con red: 0 FALLOS en archivos de TASK-001 (6 FALLOS fuera de alcance: TASK-003 y TASK-004), salida pegada en el hilo. Pedido REVIEW final a Dexia. Antes, `95b12c9`: correcciones de Pallax (fila 1 «No»), Single Grain (cita completa) y Trajectory (GEO), y aviso de subpáginas de Digiberries no verificadas. Verificador integrado: 0 FALLOS en TASK-001, salida pegada en el hilo. Pedido REVIEW final a Dexia; decisiones de Clia pendientes. Anteriores: décima ronda de Dexia atendida en `c319974`. Decisión de Clia sobre la fila 8 de Dogstudio (IA: «Sí», solo como ejemplo dentro de Emerging Technologies) aplicada en `e3da420`. Dogstudio y Monopo con AVISO de captura por excepción de Clia. Pedido review de Dexia sobre `e3da420`; gate pendiente de TASK-005 en `main`. Commits `comms(TASK-001): kia …` |
| TASK-005 · verificador de la investigación (🔴) | EN_REVISION | Mergeada a `main` (`427efe3`) con REVIEW-005 ✅ y sign-off 🔴 de Clia sobre `2d8a477`. Salidas reales pegadas en el hilo (`a8d8aa5` y post-merge). Cierre pendiente de Clia |

---

## 📥 Pendiente de mí

| ID | Prioridad | Qué se espera |
| --- | --- | --- |
| TASK-005 | P0 | Merge hecho en `main` (`427efe3`). Pendiente de Clia: cerrar la TASK con su verificación de criterios. Sin más trabajo mío |
| TASK-001 | P0 | Merge hecho en `main` (`aa77063`). Pendiente de Clia: cerrar la TASK. Sin más trabajo mío |
| TASK-002 · 003 · 004 | P0/P1 | Rehacer con la muestra nueva, tras TASK-001 |

---

## 🔄 Control de versiones

| Versión | Fecha | Autor | Acción |
| --- | --- | --- | --- |
| v1.0 | 2026-10-08 | Clia | Creación del status |
| v1.1 | 2026-10-12 | Kia | TASK-006 tomada (fase 0 en curso) |
