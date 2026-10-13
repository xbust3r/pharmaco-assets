# 📋 Status: Dexia (Lead Dev / Reviews)

> **Proyecto:** Pharmaco Assets
> **Última actualización:** 2026-10-12

---

## 📝 Forma de trabajo

ChatGPT (Codex). Emite REVIEWs en exclusiva. En esta sesión dispone del repositorio y puede correr comprobaciones; pega la salida real en el REVIEW.

**Canal de activación:** mensajes dirigidos a `dexia` en [`comms/tablero.md`](../comms/tablero.md).

---

## 🎯 Trabajo reciente

| Tarea | Estado | Notas |
| --- | --- | --- |
| TASK-001 | REVIEW-001 ✅; F0 y F1 aprobadas | Verificador con red: 0 FALLOS en archivos de TASK-001; 6 FALLOS ajenos (TASK-003/004). Muestreo de Pallax y Digiberries contrastado. |
| TASK-002 | REVIEW-002 ❌, segunda ronda | Conteos internos correctos; fuente F1 y plantilla de servicio pendientes. |
| TASK-003 | REVIEW-003 ✅, cuarta ronda | Opción B corregida, `main` integrado; gate con red: 0 FALLOS de TASK-003. Kia puede mergear según el protocolo. |
| TASK-004 | REVIEW-004 ❌, tercera ronda | Gate con red: 0 FALLOS; capturas de menú/overlay abierto no muestran el estado declarado; A2 clasifica NC contra la regla escrita. |
| TASK-005 | REVIEW-005 ✅, cuarta ronda | V2 conforme a la enmienda 6; salidas con red pegadas por Kia. Sign-off 🔴 de Clia pendiente. |

---

## 📥 Pendiente de mí

| ID | Prioridad | Qué se espera |
| --- | --- | --- |
| TASK-004 | P1 | Nueva revisión cuando Kia corrija las dos capturas de estado abierto y la clasificación A2 |
| TASK-005 | P0 | Esperar sign-off 🔴 de Clia; no queda revisión de implementación pendiente |
| RFC-001 | P2 | Opinar sobre la calibración de la criticidad |

---

## 🔄 Control de versiones

| Versión | Fecha | Autor | Acción |
| --- | --- | --- | --- |
| v1.0 | 2026-09-26 | Clia | Creación del status |
