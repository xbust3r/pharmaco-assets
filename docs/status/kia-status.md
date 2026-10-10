# 📋 Status: Kia (DEV principal)

> **Proyecto:** Pharmaco Assets
> **Última actualización:** 2026-10-10

---

## 📝 Forma de trabajo

Subagente de Claude Code (Haiku 5.5), lanzado por Clia con el ID de la TASK. Escribe código, investiga y hace capturas; no hace push.

**Canal de activación:** mensajes dirigidos a `kia` en [`comms/tablero.md`](../comms/tablero.md).

---

## 🎯 Trabajo reciente

| Tarea | Estado | Notas |
| --- | --- | --- |
| TASK-005 · verificador de la investigación (🔴) | EN_REVISION | Segunda ronda de REVIEW-005 (`20854d3` 🔴): V2 valida VP8/VP8L/ANMF y el filtro PNG; regresiones `falla-v2c`, `falla-v2d`, `falla-v2e` y `correcta-formatos`; salida con red pegada en el hilo |
| — | — | Hereda el trabajo de Ania (ver [`ania-status.md`](ania-status.md)) |

---

## 📥 Pendiente de mí

| ID | Prioridad | Qué se espera |
| --- | --- | --- |
| TASK-005 | P0 | EN_REVISION. Enmienda 6 aplicada en `ba46de7`: contenedor PNG/WebP cerrado, datos de imagen en VP8 y VP8L, mínimo 320×200 px. Pendiente: cuarta ronda de REVIEW-005 de Dexia sobre `ba46de7`; decisión de Clia sobre si el mínimo aplica a las 16 capturas de componentes de `diseno/`; después, sign-off (🔴) |
| TASK-001 | P0 | F1: las 10 fichas de comparables pequeñas y corrección de las 10 grandes |
| TASK-002 · 003 · 004 | P0/P1 | Rehacer con la muestra nueva, tras TASK-001 |

---

## 🔄 Control de versiones

| Versión | Fecha | Autor | Acción |
| --- | --- | --- | --- |
| v1.0 | 2026-10-08 | Clia | Creación del status |
