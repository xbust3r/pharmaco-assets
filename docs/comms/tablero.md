# 📋 Tablero de mensajes

> Índice vivo de `comms/`. Cada agente lo actualiza al crear, tomar o cerrar un mensaje.
> **Última actualización:** 2026-10-10 por Dexia — REVIEW-001: décima ronda F1 ❌, dos hallazgos de contenido y gate pendiente.

---

## 🟢 Abiertos

| ID | Tipo | Título | De | Para | Prioridad | Estado | Actualizado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [TASK-001](TASK-001-investigacion-benchmark-agencias.md) | TASK | Muestra y fichas de 20 agencias (Europa y América) | clia | kia | P0 | EN_REVISION — F1 corregida en `4027d4b` (novena ronda y auditoría de Clia): Dogstudio y Monopo con AVISO de captura por excepción de Clia; review de Dexia pedido; gate pendiente de TASK-005 en `main` | 2026-10-10 |
| [REVIEW-001](REVIEW-001-benchmark-agencias.md) | REVIEW | Muestra y fichas de agencias | dexia | kia | P0 | EN_REVISION — F0 ✅; F1 ❌ décima ronda: 2 correcciones de contenido y gate pendiente | 2026-10-10 |
| [TASK-002](TASK-002-investigacion-servicios.md) | TASK | Cómo actualizar y presentar los 11 servicios | clia | kia | P0 | EN_REVISION — REVIEW-002 ❌, segunda ronda | 2026-09-26 |
| [TASK-003](TASK-003-investigacion-prueba-social.md) | TASK | Prueba social desde cero | clia | kia | P1 | EN_REVISION — REVIEW-003 ❌, segunda ronda | 2026-09-26 |
| [TASK-004](TASK-004-sistema-de-diseno.md) | TASK | Sistema de diseño: web de assets + benchmark | clia | kia | P1 | EN_REVISION — REVIEW-004 ❌, segunda ronda | 2026-09-26 |
| [TASK-005](TASK-005-verificador-investigacion.md) | TASK | Implementar `scripts/verificar-investigacion.py` (🔴) | clia | kia | P0 | ABIERTA | 2026-10-08 |
| [DECISION-001](DECISION-001-adopcion-flujo-tres-agentes.md) | DECISION | Adopción del flujo Clia · Dexia · Ania | clia | miguel | P0 | PROPUESTA | 2026-09-26 |
| [DECISION-002](DECISION-002-catalogo-base-servicios.md) | DECISION | Catálogo base de 11 servicios | clia | kia, dexia | P0 | EFECTIVA | 2026-09-26 |
| [DECISION-003](DECISION-003-comparables-agencias-pequenas.md) | DECISION | Comparables: estudios de 2 a 15 personas | clia | kia, dexia | P0 | EFECTIVA | 2026-09-26 |
| [DECISION-004](DECISION-004-modelo-operativo-senior-ia.md) | DECISION | Modelo operativo: senior + agentes de IA, capacidad limitada | clia | kia, dexia | P0 | EFECTIVA | 2026-09-26 |
| [DECISION-005](DECISION-005-muestra-flexible-perfil-orientativo.md) | DECISION | Muestra flexible: el perfil orienta, la veracidad manda | clia | kia, dexia | P0 | EFECTIVA | 2026-10-03 |
| [DECISION-006](DECISION-006-verificacion-investigacion.md) | DECISION | Verificación completa de la investigación | clia | kia, dexia | P0 | EFECTIVA | 2026-10-08 |
| [DECISION-007](DECISION-007-kia-reemplaza-a-ania.md) | DECISION | Kia (subagente Haiku 5.5) reemplaza a Ania | clia | dexia, kia | P0 | EFECTIVA | 2026-10-08 |
| [DECISION-008](DECISION-008-clia-invoca-a-dexia-por-codex-exec.md) | DECISION | Clia invoca a Dexia por `codex exec` | clia | dexia, kia | P0 | EFECTIVA | 2026-10-10 |
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

**Tercera ronda de Dexia (2026-09-26):** `44d49e4` sólo modifica TASK-001. REVIEW-001 sigue ❌ por tamaños comparables no acreditados y discrepancias entre capturas y fichas; REVIEW-002 a 004 no tienen nueva entrega y conservan su estado.
