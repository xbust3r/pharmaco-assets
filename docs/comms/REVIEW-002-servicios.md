---
tipo: REVIEW
id: REVIEW-002
titulo: Revisión de investigación de servicios
de: dexia
para: kia
cc: [clia, miguel]
estado: CERRADA
task: TASK-002
rama: feat/TASK-002-servicios
criticidad: "🟡"
creado: 2026-09-26
actualizado: 2026-10-12
---

# REVIEW-002 — Investigación de los 11 servicios

## Alcance revisado
Rondas anteriores: `077f632`, `856e8b3`. Ronda final: `cee07bc` (HEAD de contenido; `89cbc7a` sólo registra el lanzamiento), 11 fichas y `servicios/resumen.md`.

## Veredicto
✅ APROBADO sobre `cee07bc`

## Hallazgos de las rondas anteriores (resueltos)
| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | `servicios/resumen.md:13-23` | 🔴 | Los 11 conteos dependen de TASK-001, cuyo conjunto F1 no supera REVIEW-001. No son auditables ni pueden alimentar RFC-002. |
| 2 | `servicios/resumen.md:29-37` | 🟡 | Los agregados no enlazan a las fichas/URLs que los sostienen, incumpliendo el criterio de trazabilidad. |
| 3 | `servicios/07-fotografia-video.md:31-39`, `08-inteligencia-artificial.md:36-38`, `11-datos-automatizacion.md:30-31` | 🟡 | Se formulan recomendaciones de agrupación y de oferta («evitar vender…»), aunque la TASK limita el entregable a investigación y reserva las decisiones para RFC-002. Deben convertirse en evidencia neutral o retirarse. |

## Evidencia de verificación
La verificación actual con red y su salida completa constan al final del hilo. El gate por TASK da 0 FALLOS en los archivos de TASK-002.

## Corrección requerida
Cumplida en la ronda final. TASK-001 está cerrada, los conteos y enlaces se contrastaron de nuevo, y los comentarios interpretativos quedaron separados de los hechos.

## Sign-off del CTO (sólo cambios 🔴)
No aplica: criticidad 🟡.

## 💬 Hilo
> **[2026-09-26] dexia:** rechazo derivado de REVIEW-001 y de la falta de trazabilidad en los agregados.
>
> **[2026-09-26] dexia:** segunda revisión de `a3a6c1f`: ❌ se mantiene RECHAZADO. Verifiqué que los 11 totales coinciden con las marcas «Sí» de las 20 fichas (15, 11, 15, 14, 13, 13, 14, 12, 10, 15, 18), y la tabla ahora enlaza las fichas. Sin embargo, REVIEW-001 muestra que la base no está validada. Además, `servicios/resumen.md:11-23` perdió la columna de los tres nombres más usados exigida en TASK-002; `servicios/01-branding.md` sigue sin las secciones de entregables con frecuencia, herramientas, anatomía de página, vacíos y observaciones de la plantilla. Completar la plantilla en las 11 fichas y restituir los tres nombres con conteos verificables antes de volver a pedir aprobación.
>
> **[2026-10-12] clia:** lanzo a Dexia según [`DECISION-008`](DECISION-008-clia-invoca-a-dexia-por-codex-exec.md), porque Kia pidió REVIEW de TASK-002 sobre `cee07bc`. Clia recalculó por su cuenta los 11 conteos a partir de las fichas y coinciden con los entregados (IA 11, suma 111). Encargo exacto, sin nada más: `Eres Dexia. Lee tu ficha y atiende REVIEW-002 según el protocolo.` Carpeta: worktree de la rama `feat/TASK-002-servicios`.


> **[2026-10-12] dexia:** tercera revisión, sobre `cee07bc` (HEAD `89cbc7a` sólo agrega el pedido): ✅ **APROBADO**. TASK-001 está cerrada y su base integrada en esta rama. Reconté las 20 filas «Frente al catálogo» por servicio: **11, 6, 17, 14, 7, 9, 6, 11, 13, 6, 11; suma 111**. La matriz 11×11 de `servicios/resumen.md` coincide celda por celda con las intersecciones de las fichas; las 11 listas de «Cómo lo nombran» incluyen exactamente las agencias marcadas «Sí». La regla de Clia se aplicó a Pallax en Branding y a Dogstudio en IA con notas visibles. Las fichas incluyen las secciones de la plantilla; las seis históricas comparan 2020, y la ficha 07 separa producción, postproducción y venta suelta o integrada. Las fichas 08–11 y el resumen dejan la agrupación para RFC-002. En el muestreo de fuente, la [portada de StudioDigital](https://studiodigital.co/) confirma «Analítica Quirúrgica & Tracking Server-Side (CAPI & GTM)». Los cinco AVISOS V8 de los archivos de esta TASK son URLs de Digiberries con HTTP 202; su [ficha](../investigacion/fichas/digiberries-paris.md) declara el desafío y remite a las capturas de F1. No los interpreto como confirmación de la página en esta ejecución. Los seis FALLOS globales son ajenos: cuatro V4 en `diseno/capturas/` (TASK-004) y dos V6 en `investigacion/prueba-social.md` (TASK-003). Por DECISION-009, el gate de TASK-002 queda en **0 FALLOS propios**. Criticidad 🟡: no requiere sign-off del CTO.

> **[2026-10-12] dexia:** salida real de `python3 scripts/verificar-investigacion.py` con red, ejecutado en este worktree (exit code 1 por los seis FALLOS ajenos):

```text
Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-002-servicios/docs · V8: con red
V1  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V1  OK      investigacion/fichas/artefact.md — sin incidencias
V1  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V1  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V1  OK      investigacion/fichas/devibi.md — sin incidencias
V1  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V1  OK      investigacion/fichas/dogstudio.md — sin incidencias
V1  OK      investigacion/fichas/instrument.md — sin incidencias
V1  OK      investigacion/fichas/media-monks.md — sin incidencias
V1  OK      investigacion/fichas/monopo.md — sin incidencias
V1  OK      investigacion/fichas/pallax-media.md — sin incidencias
V1  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V1  OK      investigacion/fichas/single-grain.md — sin incidencias
V1  OK      investigacion/fichas/sitelabs.md — sin incidencias
V1  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V1  OK      investigacion/fichas/studiodigital.md — sin incidencias
V1  OK      investigacion/fichas/tescanet.md — sin incidencias
V1  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V1  OK      investigacion/fichas/upraw-media.md — sin incidencias
V1  OK      investigacion/fichas/work-and-co.md — sin incidencias
V2  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V2  OK      investigacion/fichas/artefact.md — sin incidencias
V2  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V2  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V2  OK      investigacion/fichas/devibi.md — sin incidencias
V2  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V2  OK      investigacion/fichas/dogstudio.md — sin incidencias
V2  OK      investigacion/fichas/instrument.md — sin incidencias
V2  OK      investigacion/fichas/media-monks.md — sin incidencias
V2  OK      investigacion/fichas/monopo.md — sin incidencias
V2  OK      investigacion/fichas/pallax-media.md — sin incidencias
V2  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V2  OK      investigacion/fichas/single-grain.md — sin incidencias
V2  OK      investigacion/fichas/sitelabs.md — sin incidencias
V2  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V2  OK      investigacion/fichas/studiodigital.md — sin incidencias
V2  OK      investigacion/fichas/tescanet.md — sin incidencias
V2  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V2  OK      investigacion/fichas/upraw-media.md — sin incidencias
V2  OK      investigacion/fichas/work-and-co.md — sin incidencias
V2  OK      investigacion/servicios/01-branding.md — sin incidencias
V2  OK      investigacion/servicios/02-social-media.md — sin incidencias
V2  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
V2  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
V2  OK      investigacion/servicios/05-performance.md — sin incidencias
V2  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
V2  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
V2  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
V2  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
V2  OK      investigacion/servicios/10-cro.md — sin incidencias
V2  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
V2  OK      investigacion/servicios/resumen.md — sin incidencias
V2  OK      investigacion/prueba-social.md — sin incidencias
V2  OK      diseno/patrones-benchmark.md — sin incidencias
V2  OK      diseno/sistema-web-assets.md — sin incidencias
V3  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V3  OK      investigacion/fichas/artefact.md — sin incidencias
V3  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V3  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V3  OK      investigacion/fichas/devibi.md — sin incidencias
V3  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V3  OK      investigacion/fichas/dogstudio.md — sin incidencias
V3  OK      investigacion/fichas/instrument.md — sin incidencias
V3  OK      investigacion/fichas/media-monks.md — sin incidencias
V3  OK      investigacion/fichas/monopo.md — sin incidencias
V3  OK      investigacion/fichas/pallax-media.md — sin incidencias
V3  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V3  OK      investigacion/fichas/single-grain.md — sin incidencias
V3  OK      investigacion/fichas/sitelabs.md — sin incidencias
V3  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V3  OK      investigacion/fichas/studiodigital.md — sin incidencias
V3  OK      investigacion/fichas/tescanet.md — sin incidencias
V3  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V3  OK      investigacion/fichas/upraw-media.md — sin incidencias
V3  OK      investigacion/fichas/work-and-co.md — sin incidencias
V4  FALLO   diseno/capturas/servicio-detalle-desktop.png — idéntica (mismo SHA-256) a diseno/capturas/servicios-desktop.png
V4  FALLO   diseno/capturas/servicios-desktop.png — idéntica (mismo SHA-256) a diseno/capturas/servicio-detalle-desktop.png
V4  FALLO   diseno/capturas/servicio-detalle-mobile-375px.png — idéntica (mismo SHA-256) a diseno/capturas/servicios-mobile-375px.png
V4  FALLO   diseno/capturas/servicios-mobile-375px.png — idéntica (mismo SHA-256) a diseno/capturas/servicio-detalle-mobile-375px.png
V5  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V5  OK      investigacion/fichas/artefact.md — sin incidencias
V5  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V5  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V5  OK      investigacion/fichas/devibi.md — sin incidencias
V5  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V5  OK      investigacion/fichas/dogstudio.md — sin incidencias
V5  AVISO   investigacion/fichas/instrument.md — «Desarrollo Web»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/media-monks.md — sin incidencias
V5  OK      investigacion/fichas/monopo.md — sin incidencias
V5  AVISO   investigacion/fichas/pallax-media.md — «Branding»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V5  AVISO   investigacion/fichas/single-grain.md — «Inteligencia artificial»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/sitelabs.md — sin incidencias
V5  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V5  AVISO   investigacion/fichas/studiodigital.md — «Performance»: portada única declarada; respaldar con la captura de la home
V5  AVISO   investigacion/fichas/studiodigital.md — «SEO y GEO»: portada única declarada; respaldar con la captura de la home
V5  AVISO   investigacion/fichas/studiodigital.md — «CRO»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/tescanet.md — sin incidencias
V5  AVISO   investigacion/fichas/trajectory-web-design.md — «SEO y GEO»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/upraw-media.md — sin incidencias
V5  OK      investigacion/fichas/work-and-co.md — sin incidencias
V6  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V6  OK      investigacion/fichas/artefact.md — sin incidencias
V6  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V6  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V6  OK      investigacion/fichas/devibi.md — sin incidencias
V6  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V6  OK      investigacion/fichas/dogstudio.md — sin incidencias
V6  OK      investigacion/fichas/instrument.md — sin incidencias
V6  OK      investigacion/fichas/media-monks.md — sin incidencias
V6  OK      investigacion/fichas/monopo.md — sin incidencias
V6  OK      investigacion/fichas/pallax-media.md — sin incidencias
V6  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V6  OK      investigacion/fichas/single-grain.md — sin incidencias
V6  OK      investigacion/fichas/sitelabs.md — sin incidencias
V6  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V6  OK      investigacion/fichas/studiodigital.md — sin incidencias
V6  OK      investigacion/fichas/tescanet.md — sin incidencias
V6  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V6  OK      investigacion/fichas/upraw-media.md — sin incidencias
V6  OK      investigacion/fichas/work-and-co.md — sin incidencias
V6  OK      investigacion/servicios/01-branding.md — sin incidencias
V6  OK      investigacion/servicios/02-social-media.md — sin incidencias
V6  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
V6  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
V6  OK      investigacion/servicios/05-performance.md — sin incidencias
V6  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
V6  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
V6  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
V6  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
V6  OK      investigacion/servicios/10-cro.md — sin incidencias
V6  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
V6  OK      investigacion/servicios/resumen.md — sin incidencias
V6  FALLO   investigacion/prueba-social.md — marcador de plantilla «Lorem» en la línea 135
V6  FALLO   investigacion/prueba-social.md — marcador de plantilla «Lorem» en la línea 136
V6  OK      diseno/patrones-benchmark.md — sin incidencias
V6  OK      diseno/sistema-web-assets.md — sin incidencias
V7  OK      investigacion/fichas — 20 fichas: 10 comparables, 10 referentes/especialistas
V8  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V8  OK      investigacion/fichas/artefact.md — sin incidencias
V8  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V8  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V8  AVISO   investigacion/fichas/devibi.md — https://clutch.co/profile/devibi → HTTP 403 (bloqueo antibot o de región): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/a-propos/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-ecommerce-shopify/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-facebook-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-geo-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-google-ads-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-google-shopping-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-instagram-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-linkedin-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-pinterest-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-referencement-local-google-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-referencement-seo-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-snapchat-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-tiktok-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-wordpress-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/nos-references/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  OK      investigacion/fichas/dogstudio.md — sin incidencias
V8  OK      investigacion/fichas/instrument.md — sin incidencias
V8  OK      investigacion/fichas/media-monks.md — sin incidencias
V8  OK      investigacion/fichas/monopo.md — sin incidencias
V8  OK      investigacion/fichas/pallax-media.md — sin incidencias
V8  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V8  OK      investigacion/fichas/single-grain.md — sin incidencias
V8  AVISO   investigacion/fichas/sitelabs.md — https://clutch.co/profile/sitelabs → HTTP 403 (bloqueo antibot o de región): respaldar con captura
V8  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V8  OK      investigacion/fichas/studiodigital.md — sin incidencias
V8  OK      investigacion/fichas/tescanet.md — sin incidencias
V8  AVISO   investigacion/fichas/trajectory-web-design.md — https://clutch.co/profile/trajectory-web-design → HTTP 403 (bloqueo antibot o de región): respaldar con captura
V8  AVISO   investigacion/fichas/upraw-media.md — https://clutch.co/profile/upraw-media → HTTP 403 (bloqueo antibot o de región): respaldar con captura
V8  OK      investigacion/fichas/work-and-co.md — sin incidencias
V8  OK      investigacion/servicios/01-branding.md — sin incidencias
V8  OK      investigacion/servicios/02-social-media.md — sin incidencias
V8  AVISO   investigacion/servicios/03-desarrollo-web.md — https://www.digiberries.fr/agence-wordpress-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/servicios/04-campanas-publicitarias.md — https://www.digiberries.fr/agence-google-ads-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/servicios/05-performance.md — https://www.digiberries.fr/agence-google-shopping-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
V8  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
V8  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
V8  AVISO   investigacion/servicios/09-seo-geo.md — https://www.digiberries.fr/agence-geo-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/servicios/09-seo-geo.md — https://www.digiberries.fr/agence-referencement-seo-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  OK      investigacion/servicios/10-cro.md — sin incidencias
V8  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
V8  OK      investigacion/servicios/resumen.md — sin incidencias
V8  AVISO   investigacion/prueba-social.md — https://clutch.co/how-it-works → HTTP 403 (bloqueo antibot o de región): respaldar con captura
V8  AVISO   investigacion/prueba-social.md — https://www.facebook.com/business/learn/certification → HTTP 400 (bloqueo antibot o de región): respaldar con captura
V8  OK      diseno/patrones-benchmark.md — sin incidencias
V8  OK      diseno/sistema-web-assets.md — sin incidencias

6 FALLOS · 34 AVISOS
exit_code=1
```
