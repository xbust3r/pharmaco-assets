---
tipo: TASK
id: TASK-002
titulo: Investigación — cómo actualizar y presentar los 11 servicios
de: clia
para: ania
cc: [dexia, miguel]
prioridad: P0
estado: ABIERTA
area: investigacion
criticidad: "🟡"
relacionado: [DECISION-002, TASK-001, plan-investigacion.md, plantilla-servicio.md, linea-base-2020.md]
creado: 2026-09-26
actualizado: 2026-09-26
---

# TASK-002 — Cómo actualizar y presentar los 11 servicios

## Contexto

Miguel decidió el catálogo ([`DECISION-002`](DECISION-002-catalogo-base-servicios.md)): los 6 servicios de 2020, actualizados, más Fotografía y video, Inteligencia artificial, SEO y GEO, CRO, y Datos y automatización. Hay que saber cómo nombran, qué incluyen y cómo presentan hoy esos servicios las agencias de referencia, para que Clia redacte `RFC-002`.

**Depende de:** las fichas de [`TASK-001`](TASK-001-investigacion-benchmark-agencias.md) (F1). No empezar antes.

## Pedido

1. **Una ficha por servicio** en `docs/investigacion/servicios/{nn-slug}.md` (de `01-branding.md` a `11-datos-automatizacion.md`), con la [plantilla de servicio](../investigacion/plantilla-servicio.md). Se construye cruzando las 20 fichas de agencia; si hace falta, se amplía con las páginas de servicio de esas mismas agencias.
2. **Para los 6 de 2020:** la sección «Qué cambió desde 2020» es obligatoria. Compárala contra la [línea base](../linea-base-2020.md).
3. **Para Fotografía y video:** distinguir qué es producción (foto, video, rodaje) y qué es postproducción (edición, motion, color), y si las agencias lo venden suelto o como parte de las campañas.
4. **Para los servicios 8 a 11:** anotar qué agencias los ofrecen juntos o separados (¿SEO y GEO van juntos o son dos servicios? ¿Datos va con automatización?). Esto decide la agrupación final.
5. **`servicios/resumen.md`:** una tabla con los 11 servicios × nº de agencias que lo ofrecen × los 3 nombres más usados × cómo se agrupan en pilares. Y aparte, **los servicios que aparecen en ≥ 5 agencias y no están en nuestro catálogo**, como información para Miguel, no como propuesta.
6. Pedir el REVIEW a Dexia.

**Fuera de alcance:** redactar textos o descripciones para la web de Pharmaco, proponer precios, decidir nombres. Eso sale de `RFC-002`.

## Criterios de aceptación

- [ ] 11 fichas de servicio completas con la plantilla
- [ ] Cada afirmación enlaza a las fichas de agencia o a las URLs que la sostienen
- [ ] Conteos cuadrados con las 20 fichas de TASK-001 (Dexia lo comprueba)
- [ ] «Qué cambió desde 2020» en los 6 servicios de 2020
- [ ] Producción y postproducción separadas en Fotografía y video
- [ ] Evidencia sobre la agrupación de los servicios 8 a 11
- [ ] `resumen.md` con la tabla y la lista de servicios fuera de catálogo
- [ ] Vacíos declarados
- [ ] REVIEW de Dexia ✅

## 💬 Hilo

> **[2026-09-26 16:50] clia:** creo la task. Ania: no es un trabajo de redacción. Si al terminar la ficha de Branding sientes que tienes el texto para la web, te has pasado de alcance. Lo que necesito es qué nombres usan, qué incluyen y con qué frecuencia.
