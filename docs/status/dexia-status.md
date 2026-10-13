# 📋 Status: Dexia (Lead Dev / Reviews)

> **Proyecto:** Pharmaco Assets
> **Última actualización:** 2026-10-13

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
| TASK-004 | REVIEW-004 ✅, cuarta ronda | Capturas de menú y overlay abierto verificadas; A2 uniforme (10/10/0); gate con red: 0 FALLOS y 37 AVISOS ajenos a `diseno/`. |
| TASK-005 | REVIEW-005 ✅, cuarta ronda | V2 conforme a la enmienda 6; salidas con red pegadas por Kia. Sign-off 🔴 de Clia pendiente. |
| TASK-006 | REVIEW-006 ✅, checkpoint fases 0–2 | Inventario, infraestructura y tokens aprobados sobre `aa3aad6`; sign-off 🔴 de Clia pendiente. Gate completo aún rojo en `validate:origen`, previsto para fase 7. |
| TASK-007 | REVIEW-007 ❌, primera ronda | Dos fallos 🔴 en V8: URL mal formada aborta el lote y redirecciones superan el tiempo por intento. 16 tests existentes OK; Kia debe corregir y pedir nueva ronda. |

---

## 📥 Pendiente de mí

| ID | Prioridad | Qué se espera |
| --- | --- | --- |
| TASK-005 | P0 | Esperar sign-off 🔴 de Clia; no queda revisión de implementación pendiente |
| TASK-006 | P0 | Esperar sign-off 🔴 de Clia para el checkpoint; revisar fases 3–8 y el gate completo al final |
| REVIEW-007 | P1 | Revisar correcciones y regresiones de Kia; sign-off 🔴 de Clia pendiente |
| RFC-001 | P2 | Opinar sobre la calibración de la criticidad |

---

## 🔄 Control de versiones

| Versión | Fecha | Autor | Acción |
| --- | --- | --- | --- |
| v1.0 | 2026-09-26 | Clia | Creación del status |
