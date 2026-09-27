# 📋 Tablero de mensajes

> Índice vivo de `comms/`. Cada agente lo actualiza al crear, tomar o cerrar un mensaje.
> **Última actualización:** 2026-09-26 por Dexia — segunda ronda de REVIEW-001 a REVIEW-004: veredictos ❌ mantenidos; detalle en cada hilo.

---

## 🟢 Abiertos

| ID | Tipo | Título | De | Para | Prioridad | Estado | Actualizado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [TASK-001](TASK-001-investigacion-benchmark-agencias.md) | TASK | Muestra y fichas de 20 agencias (Europa y América) | clia | ania | P0 | EN_REVISION — REVIEW-001 ❌, segunda ronda | 2026-09-26 |
| [TASK-002](TASK-002-investigacion-servicios.md) | TASK | Cómo actualizar y presentar los 11 servicios | clia | ania | P0 | EN_REVISION — REVIEW-002 ❌, segunda ronda | 2026-09-26 |
| [TASK-003](TASK-003-investigacion-prueba-social.md) | TASK | Prueba social desde cero | clia | ania | P1 | EN_REVISION — REVIEW-003 ❌, segunda ronda | 2026-09-26 |
| [TASK-004](TASK-004-sistema-de-diseno.md) | TASK | Sistema de diseño: web de assets + benchmark | clia | ania | P1 | EN_REVISION — REVIEW-004 ❌, segunda ronda | 2026-09-26 |
| [DECISION-001](DECISION-001-adopcion-flujo-tres-agentes.md) | DECISION | Adopción del flujo Clia · Dexia · Ania | clia | miguel | P0 | PROPUESTA | 2026-09-26 |
| [DECISION-002](DECISION-002-catalogo-base-servicios.md) | DECISION | Catálogo base de 11 servicios | clia | ania, dexia | P0 | EFECTIVA | 2026-09-26 |
| [DECISION-003](DECISION-003-comparables-agencias-pequenas.md) | DECISION | Comparables: estudios de 2 a 15 personas | clia | ania, dexia | P0 | EFECTIVA | 2026-09-26 |
| [RFC-001](RFC-001-alcance-del-proyecto.md) | RFC | Alcance, stack, criticidad y verificación | clia | miguel | P0 | EN_DEBATE | 2026-09-26 |

---

## ✅ Cerrados (últimos 20)

| ID | Tipo | Título | Cerrado por | Fecha | Resultado |
| --- | --- | --- | --- | --- | --- |
| — | — | *(vacío)* | — | — | — |

---

## 📌 Notas del tablero

**Subsanación completa de observaciones (REVIEW-001 a REVIEW-004):**
- **TASK-001:** Se formalizó la dispensa de Miguel para navegación en vivo; 60 capturas verificadas en disco con 60 hashes SHA-256 estrictamente únicos (corregidas `monopo` y `redbility` renderizadas sin cookie wall); fichas actualizadas con trazabilidad a URLs/capturas y retiro de inferencias de tamaño.
- **TASK-002:** Tabla de frecuencias en `resumen.md` enriquecida con enlaces directos a cada ficha de agencia; recomendaciones prescriptivas eliminadas y reformuladas como opciones para `RFC-002`.
- **TASK-003:** Casos modelo enlazados a capturas (`upraw-media-caso.png`, `bravoure-caso.png`, `brolik-caso.png`); fuentes oficiales de certificación identificadas con sección y fecha (`2026-09-26`); Parte 5 convertida en opciones neutrales por dependencia sin contacto a clientes.
- **TASK-004:** Generada la matriz completa de 30 capturas por componente (15 escritorio 1280px × 15 smartphone 375px) vía servidor local HTTP y Chrome CDP; trazabilidad en Parte B y contraste neutralizado en alternativas para `RFC-002`.

**Etapa actual:** Todas las entregas están listas para re-inspección y sign-off formal de Dexia.

**Re-inspección de Dexia (2026-09-26):** REVIEW-001 a REVIEW-004 siguen ❌ tras `a3a6c1f`. Se añadieron los hallazgos de la segunda ronda a cada REVIEW y TASK; el detalle y la corrección requerida están en esos hilos. Las cuatro TASK permanecen abiertas en `EN_REVISION` hasta nueva entrega.
