---
tipo: DECISION
id: DECISION-003
titulo: Las agencias comparables son estudios de 2 a 15 personas, no de 10 a 80
de: clia
para: [ania, dexia]
cc: [miguel]
estado: EFECTIVA
estrategica: false
relacionado: [TASK-001, REVIEW-001, plan-investigacion.md, DECISION-002]
creado: 2026-09-26
actualizado: 2026-09-26
---

# DECISION-003 — Comparables: estudios pequeños

## Contexto

El plan de investigación definía como «comparables» a las agencias independientes de **10 a 80 personas**. Ese criterio tenía dos fallos:

1. **No se puede comprobar.** Clutch y LinkedIn publican rangos (10–49, 50–249), no cifras. En la tercera ronda de `REVIEW-001`, Dexia rechazó con razón que se presentaran «~55» o «~65» personas como datos verificados.
2. **No es la escala de Pharmaco.** Miguel lo aclara: *«mi agencia a la justa tendrá 5 personas, así que no sé qué tan bueno sea comparar con agencias de 250 personas».* El fallo es del criterio que escribió Clia, no de la muestra de Ania.

Las 10 comparables actuales tienen entre ~20 (sin verificar) y 50–249 personas. **Ninguna es de la escala de Pharmaco.**

## Decisión

### 1. Nuevo criterio de «comparable»

Estudio **independiente** (no pertenece a un holding ni a una red), que hace **marketing y desarrollo**, de **2 a 15 personas**, acreditado con **una** de estas evidencias:

| Evidencia | Vale como prueba |
| --- | --- |
| Clutch «2–9 employees» o «Freelancer» | ✅ Directa |
| LinkedIn «2–10 employees» | ✅ Directa |
| Página de equipo con las personas visibles y contadas (≤ 15), con captura | ✅ Directa |
| Clutch o LinkedIn en la franja «10–49» / «11–50» | ⚠️ Solo junto con una página de equipo que muestre ≤ 15 personas |
| Una cifra estimada («~12») | ❌ No vale |

### 2. Nueva composición de la muestra

| Perfil | Por bloque | Para qué sirve |
| --- | --- | --- |
| **Comparables pequeñas** (criterio nuevo) | 5 | **Modelo de escala**: qué ofrece y cómo se presenta un estudio del tamaño de Pharmaco |
| **Referentes** | 3 | Tendencia. No son modelo de escala |
| **Especialistas** | 2 | Referencia de los servicios 8 a 11. No son modelo de escala |

- **Se sustituyen las 10 comparables.** Las nuevas deben incluir al menos 2 de Latinoamérica (competencia real de Pharmaco).
- **Las 10 fichas de comparables actuales no se tiran:** pasan a `fichas/anexo-medianas/` como contexto y **no cuentan en los conteos** de TASK-002, 003 y 004.
- **Referentes y especialistas se mantienen**, con las correcciones pendientes de `REVIEW-001`.

### 3. Una pregunta nueva: cómo cubre un estudio pequeño un catálogo amplio

Pharmaco va a ofrecer 11 servicios con unas 5 personas (`DECISION-002`). Para cada comparable pequeña se documenta además cómo lo resuelve: red de freelancers o partners, marca blanca, servicios empaquetados, especialización en pocos servicios, alianzas con productoras, etc. **Solo lo que la web diga**; si no lo dice, «no publicado».

## Motivo

Un estudio de 200 personas puede tener un departamento para cada uno de los 11 servicios; uno de 5, no. Copiar la presentación de una agencia grande con un equipo pequeño crea una promesa que no se puede cumplir. Además, el nuevo criterio se comprueba con una captura, y el anterior no.

## Consecuencias

- **TASK-001:** hay que rehacer F0 **solo para las 10 comparables**. **El checkpoint vuelve a aplicarse**: la excepción que ratificó Miguel cubre la muestra anterior, no estas 10 nuevas. Dexia las valida antes de fichar.
- **Plan de investigación** a v2.3 y **plantilla de ficha** con la sección nueva.
- **TASK-002, 003 y 004 (parte B):** los conteos se recalculan con la muestra nueva.
- **Para `RFC-002`**, no para ahora: queda anotado que 11 servicios con 5 personas es la tensión central del catálogo. La evidencia de esta pregunta nueva es la que la resolverá.

## Vigencia

Efectiva desde el 2026-09-26. Nace de la indicación de Miguel sobre el tamaño de su agencia. No es estratégica porque no cambia el catálogo, solo el método de investigación. Miguel puede vetarla.

## 💬 Hilo

> **[2026-09-26 20:30] miguel:** (transcrito por Clia) mi agencia a la justa tendrá 5 personas, así que no sé qué tan bueno sea comparar con agencias de 250 personas.
>
> **[2026-09-26 20:30] clia:** tiene razón, y el error de base es mío: definí «comparable» como 10–80 personas sin preguntar el tamaño real. Emito la decisión. Ania, Dexia: las comparables nuevas se validan en F0 **antes** de fichar.
