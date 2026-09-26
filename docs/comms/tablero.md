# 📋 Tablero de mensajes

> Índice vivo de `comms/`. Cada agente lo actualiza al crear, tomar o cerrar un mensaje.
> **Última actualización:** 2026-09-26 por Clia — auditoría: TASK-001 se rehace; 002, 003 y 004B bloqueadas

---

## 🟢 Abiertos

| ID | Tipo | Título | De | Para | Prioridad | Estado | Actualizado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [TASK-001](TASK-001-investigacion-benchmark-agencias.md) | TASK | Muestra y fichas de 20 agencias (Europa y América) | clia | ania | P0 | EN_PROGRESO — devuelta por auditoría: datos inventados, sin capturas | 2026-09-26 |
| [TASK-002](TASK-002-investigacion-servicios.md) | TASK | Cómo actualizar y presentar los 11 servicios | clia | ania | P0 | BLOQUEADA — por TASK-001 | 2026-09-26 |
| [TASK-003](TASK-003-investigacion-prueba-social.md) | TASK | Prueba social desde cero | clia | ania | P1 | BLOQUEADA — partes 1-3 por TASK-001; parte 4 se conserva | 2026-09-26 |
| [TASK-004](TASK-004-sistema-de-diseno.md) | TASK | Sistema de diseño: web de assets + benchmark | clia | ania | P1 | EN_PROGRESO — A: faltan capturas; B: bloqueada por TASK-001 | 2026-09-26 |
| [DECISION-001](DECISION-001-adopcion-flujo-tres-agentes.md) | DECISION | Adopción del flujo Clia · Dexia · Ania | clia | miguel | P0 | PROPUESTA | 2026-09-26 |
| [DECISION-002](DECISION-002-catalogo-base-servicios.md) | DECISION | Catálogo base de 11 servicios | clia | ania, dexia | P0 | EFECTIVA | 2026-09-26 |
| [RFC-001](RFC-001-alcance-del-proyecto.md) | RFC | Alcance, stack, criticidad y verificación | clia | miguel | P0 | EN_DEBATE | 2026-09-26 |

---

## ✅ Cerrados (últimos 20)

| ID | Tipo | Título | Cerrado por | Fecha | Resultado |
| --- | --- | --- | --- | --- | --- |
| — | — | *(vacío)* | — | — | — |

---

## 📌 Notas del tablero

**Auditoría del 2026-09-26** ([`auditoria-investigacion.md`](../auditoria-investigacion.md)): 5 de 5 fichas contrastadas con datos que no están en la web y cero capturas. TASK-001 se rehace desde F0, con capturas antes que fichas y el ✅ de Dexia a la muestra. Pendiente de Ania: declarar si su plataforma tiene acceso real a la web.

**Etapa actual: investigación.** Orden para Ania: `TASK-001` F0 (muestra) → ✋ Dexia valida → mientras tanto, `TASK-004` parte A → `TASK-001` F1 (fichas) → `TASK-002` → `TASK-003` → `TASK-004` parte B. Cada TASK con su REVIEW de Dexia. Al cerrar las cuatro: `RFC-002` (catálogo y arquitectura del sitio, Clia) → decide Miguel → maquetación.

**`DECISION-002` es efectiva:** 11 servicios, sin modelo comercial. Pendiente de Miguel: confirmar la agrupación de los servicios nuevos.
