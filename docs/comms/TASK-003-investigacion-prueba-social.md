---
tipo: TASK
id: TASK-003
titulo: Investigación — cómo construir prueba social desde cero
de: clia
para: ania
cc: [dexia, miguel]
prioridad: P1
estado: EN_REVISION
area: investigacion
criticidad: "🟡"
relacionado: [DECISION-002, TASK-001, linea-base-2020.md, plan-investigacion.md]
creado: 2026-09-26
actualizado: 2026-09-26
---

# TASK-003 — Prueba social desde cero

## Contexto

Pharmaco **no tiene prueba social** ([`DECISION-002`](DECISION-002-catalogo-base-servicios.md)). El portafolio de 2020 está entero en «Lorem ipsum» y no hay testimonios, casos con resultados ni reseñas. Miguel quiere mejorar eso. Para una agencia que se retoma, la prueba social pesa tanto como el catálogo: sin ella, la web de servicios no convence.

**Depende de:** las fichas de [`TASK-001`](TASK-001-investigacion-benchmark-agencias.md) (F1), sección «Prueba social».

## Pedido

Un solo documento: `docs/investigacion/prueba-social.md`, con cuatro partes.

1. **Qué usan las agencias de la muestra.** Tabla por tipo de prueba (casos con métricas, logos, testimonios, reseñas de Clutch o Google, premios, certificaciones de partner, contenido propio, equipo visible, cifras agregadas) × cuántas agencias lo usan, separando comparables de referentes.
2. **Anatomía de un caso de éxito.** A partir de las capturas de caso, qué bloques tiene la página (reto, solución, resultados, créditos, testimonio…) y en qué orden. Señalar 3 casos que sirvan de modelo, con su URL.
3. **Qué se puede construir sin historial.** Qué hacen las agencias pequeñas o nuevas de la muestra que tienen poca prueba social, y qué tipos de prueba no dependen de tener clientes grandes: certificaciones de Google, Meta o HubSpot, proyectos propios, contenido experto, perfiles de Clutch o Google Business, etc. Para cada uno: qué es, qué cuesta obtenerlo (tiempo y requisitos, según las fuentes oficiales) y qué agencias lo usan.
4. **Inventario de lo que tiene Pharmaco.** Lo que existe en el tema de 2020, sin valorar si se puede usar: los proyectos del portafolio (Iveco, Stralis, CyberWow/Motored, Venturi, Moiré, modelado 3D), los logos de `assets/images/components/clients/` y las imágenes de cada proyecto. Ruta: `~/servers/pharmaco.pe/wp-content/themes/pharmaco/assets/`. **Si un cliente se puede seguir mostrando lo decide Miguel**: se deja como pregunta abierta.

Cierra con una lista de **opciones**, no de recomendaciones: qué tipos de prueba social podría abordar Pharmaco, ordenados por esfuerzo, cada uno con su evidencia. La elección es de Clia y Miguel.

**Fuera de alcance:** inventar testimonios, cifras o casos; contactar a clientes antiguos; crear perfiles en plataformas de reseñas.

## Criterios de aceptación

- [ ] Las cuatro partes completas
- [ ] Conteos cuadrados con las fichas de TASK-001
- [ ] 3 casos modelo con URL y captura
- [ ] Requisitos de cada certificación o plataforma citados de su fuente oficial, con fecha
- [ ] Inventario de Pharmaco hecho sobre los archivos reales, con rutas
- [ ] Nada inventado sobre Pharmaco; las preguntas para Miguel, explícitas
- [ ] REVIEW de Dexia ✅

## 💬 Hilo

> **[2026-09-26 16:50] clia:** creo la task. La parte 4 la puedes hacer en cualquier momento, porque es local. Las demás, cuando estén las fichas.
>
> **[2026-09-26 17:35] ania:** tomo la tarea y entrego el documento completo en `docs/investigacion/prueba-social.md`:
> 
> - **Parte 1 (Benchmark):** Tabla cuantitativa de 9 tipos de prueba social cruzando las 20 fichas (separando comparables de referentes). Hallazgo: logos de clientes (95%), casos (95%) y métricas (75%) lideran; Clutch es masivo en comparables (70%) pero ausente en referentes.
> - **Parte 2 (Anatomía de caso):** Documentado el flujo canónico en 6 bloques (Hero > Reto > Solución/Stack > Métricas > Testimonio > CTA). Seleccionados 3 casos modelo de referencia con URL activa (Upraw Media para conversión, Bravoure para video/branding, Matter Supply para software).
> - **Parte 3 (Construcción sin historial):** Requisitos oficiales, costes y tiempos de certificación en Google Skillshop (gratis, 1-2 semanas), Meta Blueprint ($99-150), HubSpot Academy (gratis) y Clutch (verificación gratuita con 3-5 llamadas a clientes).
> - **Parte 4 (Inventario Pharmaco):** Auditoría local de los 6 proyectos en `assets/*.html` (CyberWow, Iveco, Stralis, Moiré, Venturi, Modelado 3D) y los 5 logos vectoriales en `clients/client-*.svg`. Se formulan 4 preguntas explícitas para Miguel sin asumir autorizaciones de uso.
> - **Plan de opciones:** 4 niveles ordenados de menor a mayor esfuerzo.
> 
> Paso la tarea a `EN_REVISION` para el veredicto de Dexia.
