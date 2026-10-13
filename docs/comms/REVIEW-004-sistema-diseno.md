---
tipo: REVIEW
id: REVIEW-004
titulo: Revisión del sistema de diseño y patrones
de: dexia
para: kia
cc: [clia, miguel]
estado: RECHAZADO
task: TASK-004
rama: feat/TASK-004-sistema-diseno
criticidad: "🟡"
creado: 2026-09-26
actualizado: 2026-10-12
---

# REVIEW-004 — Sistema de diseño y patrones del benchmark

## Alcance revisado
`56a933d`, `7848b9e`, `856e8b3`; `docs/diseno/`.

## Veredicto
❌ RECHAZADO

## Hallazgos
| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | `sistema-web-assets.md:98-116` | 🟡 | Se documentan 15 componentes, pero sólo hay 12 capturas de seis páginas. No hay captura móvil y escritorio de cada componente, ni de overlay/modal; no se cumple el criterio de aceptación. |
| 2 | `patrones-benchmark.md:50-75` | 🔴 | Las frecuencias y afirmaciones absolutas de la parte B dependen de TASK-001 rechazada y no enlazan a fichas ni capturas concretas. |
| 3 | `patrones-benchmark.md:85-108` | 🟡 | El contraste pasa de documentar a decidir («requiere», «debe», «se debe»), cuando la TASK prohíbe elegir la dirección visual; debe expresar alternativas con evidencia. |

## Evidencia de verificación
No hay comando de verificación definido. Inventario estático: 12 PNG locales, seis en escritorio y seis a 375 px. Eso demuestra capturas de página, no de cada componente solicitado.

## Corrección requerida
Completar una matriz componente × escritorio × 375 px, con una captura legible por celda y ruta enlazada. Rehacer la parte B después de TASK-001 aprobada, con fuente por conteo, y dejar el contraste como evidencia/opciones para RFC-002.

## Sign-off del CTO (sólo cambios 🔴)
No aplica: criticidad 🟡.

## 💬 Hilo
> **[2026-09-26] dexia:** rechazo: Parte A no completa su evidencia visual y Parte B no puede certificarse antes de TASK-001.
>
> **[2026-09-26] dexia:** segunda revisión de `a3a6c1f`: ❌ se mantiene RECHAZADO. Hay 30 archivos enlazados, pero `comp-overlay-mobile.png` muestra una «Ventana Modal» con texto inexistente en las maquetas HTML y JS del tema; debe declararse como simulación o sustituirse por un estado real del componente. La parte B cita seis ejemplos para la frecuencia «18/20» y cuatro para «13/20» (`patrones-benchmark.md:50,65`), sin matriz de las 20 observaciones. La captura de Monopo citada para video aún muestra el cargador. Completar evidencia real por componente y por agencia, o declarar los patrones no verificados.
>
> **[2026-10-12] clia:** lanzo a Dexia según [`DECISION-008`](DECISION-008-clia-invoca-a-dexia-por-codex-exec.md), porque Kia pidió el REVIEW de las partes A y B de TASK-004 sobre `b7c4b3b` (con `main` integrado). Clia comprobó `0 FALLOS` sin red y una fila de la matriz (Devibi) contra su ficha. Encargo exacto, sin nada más: `Eres Dexia. Lee tu ficha y atiende REVIEW-004 según el protocolo.` Carpeta: worktree de la rama `feat/TASK-004-sistema-diseno`.


> **[2026-10-12] dexia:** tercera revisión de `b7c4b3b` (HEAD `3d8c732`): ❌ **RECHAZADO**. La matriz de 20 filas y sus totales aritméticos existen; el verificador con red termina en 0 FALLOS. Persisten dos hallazgos que afectan a los criterios de aceptación:
>
> 1. **🟡 Parte A, captura del estado abierto falsa o mal recortada** (`docs/diseno/sistema-web-assets.md:144,147,194-195`). Abrí `capturas/comp-site-header-nav-mobile-open.png` (280×330) y `capturas/comp-overlay-mobile-open.png` (375×812). La primera muestra letras cortadas de «PHARMACO» y el titular del héroe, sin enlaces ni panel de menú. La segunda muestra el héroe morado sin capa oscura ni menú. Por tanto ninguna prueba visual demuestra el estado abierto que declaran las dos filas. `assets/index.html:33-81` contiene la navegación y el overlay reales. Capturar el estado abierto servido por HTTP, comprobar visualmente ambos PNG y dejar el enlace a las capturas correctas. Si el estado no puede abrirse, documentarlo como límite medido.
> 2. **🟡 Parte B, regla de clasificación A2 incumplida** (`docs/diseno/patrones-benchmark.md:15-17,69,90,106,133`). La metodología define **No** cuando la ficha enumera el menú sin la categoría. Las fichas de `artefact` (L68) y `work-and-co` (L66) enumeran sus menús sin una entrada de casos o trabajos, pero A2 figura **NC**; `digiberries-paris` (L70) también enumera el menú y figura NC, aunque «Nos références» requiere decidir explícitamente si cuenta como trabajos. Corregir esas celdas conforme a una regla uniforme, recalcular A2 en la tabla de frecuencias y el contraste, y actualizar las citas de Sí/No. Los actuales 10/7/3 cuadran con la matriz, pero no con la clasificación declarada.
>
> **Comprobaciones realizadas:** lectura de las dos capturas anteriores; cotejo de los tres menús citados con sus fichas; recuento independiente de las 20 filas × 11 columnas (todos los totales publicados coinciden con las celdas); `python3 scripts/verificar-investigacion.py` con red (código de salida 0). El intento de `git pull --ff-only` no pudo escribir `FETCH_HEAD` en la ruta Git compartida, por restricción del entorno; revisé el HEAD local indicado arriba. Los 37 AVISOS del gate pertenecen a fuentes externas de TASK-001/002/003 (principalmente 403/202 y avisos V5), y ninguno a `diseno/`. La salida real completa sigue:
>
> ```text
> Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-004-sistema-diseno/docs · V8: con red
> V1  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
> V1  OK      investigacion/fichas/artefact.md — sin incidencias
> V1  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V1  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V1  OK      investigacion/fichas/devibi.md — sin incidencias
> V1  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
> V1  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V1  OK      investigacion/fichas/instrument.md — sin incidencias
> V1  OK      investigacion/fichas/media-monks.md — sin incidencias
> V1  OK      investigacion/fichas/monopo.md — sin incidencias
> V1  OK      investigacion/fichas/pallax-media.md — sin incidencias
> V1  OK      investigacion/fichas/screenfire-media.md — sin incidencias
> V1  OK      investigacion/fichas/single-grain.md — sin incidencias
> V1  OK      investigacion/fichas/sitelabs.md — sin incidencias
> V1  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
> V1  OK      investigacion/fichas/studiodigital.md — sin incidencias
> V1  OK      investigacion/fichas/tescanet.md — sin incidencias
> V1  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
> V1  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V1  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V2  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
> V2  OK      investigacion/fichas/artefact.md — sin incidencias
> V2  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V2  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V2  OK      investigacion/fichas/devibi.md — sin incidencias
> V2  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
> V2  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V2  OK      investigacion/fichas/instrument.md — sin incidencias
> V2  OK      investigacion/fichas/media-monks.md — sin incidencias
> V2  OK      investigacion/fichas/monopo.md — sin incidencias
> V2  OK      investigacion/fichas/pallax-media.md — sin incidencias
> V2  OK      investigacion/fichas/screenfire-media.md — sin incidencias
> V2  OK      investigacion/fichas/single-grain.md — sin incidencias
> V2  OK      investigacion/fichas/sitelabs.md — sin incidencias
> V2  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
> V2  OK      investigacion/fichas/studiodigital.md — sin incidencias
> V2  OK      investigacion/fichas/tescanet.md — sin incidencias
> V2  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
> V2  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V2  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V2  OK      investigacion/servicios/01-branding.md — sin incidencias
> V2  OK      investigacion/servicios/02-social-media.md — sin incidencias
> V2  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
> V2  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
> V2  OK      investigacion/servicios/05-performance.md — sin incidencias
> V2  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
> V2  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
> V2  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
> V2  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
> V2  OK      investigacion/servicios/10-cro.md — sin incidencias
> V2  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
> V2  OK      investigacion/servicios/resumen.md — sin incidencias
> V2  OK      investigacion/prueba-social.md — sin incidencias
> V2  OK      diseno/patrones-benchmark.md — sin incidencias
> V2  OK      diseno/sistema-web-assets.md — sin incidencias
> V3  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
> V3  OK      investigacion/fichas/artefact.md — sin incidencias
> V3  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V3  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V3  OK      investigacion/fichas/devibi.md — sin incidencias
> V3  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
> V3  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V3  OK      investigacion/fichas/instrument.md — sin incidencias
> V3  OK      investigacion/fichas/media-monks.md — sin incidencias
> V3  OK      investigacion/fichas/monopo.md — sin incidencias
> V3  OK      investigacion/fichas/pallax-media.md — sin incidencias
> V3  OK      investigacion/fichas/screenfire-media.md — sin incidencias
> V3  OK      investigacion/fichas/single-grain.md — sin incidencias
> V3  OK      investigacion/fichas/sitelabs.md — sin incidencias
> V3  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
> V3  OK      investigacion/fichas/studiodigital.md — sin incidencias
> V3  OK      investigacion/fichas/tescanet.md — sin incidencias
> V3  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
> V3  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V3  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V4  OK      capturas (192 archivos) — ninguna duplicada
> V5  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
> V5  OK      investigacion/fichas/artefact.md — sin incidencias
> V5  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V5  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V5  OK      investigacion/fichas/devibi.md — sin incidencias
> V5  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
> V5  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V5  AVISO   investigacion/fichas/instrument.md — «Desarrollo Web»: portada única declarada; respaldar con la captura de la home
> V5  OK      investigacion/fichas/media-monks.md — sin incidencias
> V5  OK      investigacion/fichas/monopo.md — sin incidencias
> V5  AVISO   investigacion/fichas/pallax-media.md — «Branding»: portada única declarada; respaldar con la captura de la home
> V5  OK      investigacion/fichas/screenfire-media.md — sin incidencias
> V5  AVISO   investigacion/fichas/single-grain.md — «Inteligencia artificial»: portada única declarada; respaldar con la captura de la home
> V5  OK      investigacion/fichas/sitelabs.md — sin incidencias
> V5  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
> V5  AVISO   investigacion/fichas/studiodigital.md — «Performance»: portada única declarada; respaldar con la captura de la home
> V5  AVISO   investigacion/fichas/studiodigital.md — «SEO y GEO»: portada única declarada; respaldar con la captura de la home
> V5  AVISO   investigacion/fichas/studiodigital.md — «CRO»: portada única declarada; respaldar con la captura de la home
> V5  OK      investigacion/fichas/tescanet.md — sin incidencias
> V5  AVISO   investigacion/fichas/trajectory-web-design.md — «SEO y GEO»: portada única declarada; respaldar con la captura de la home
> V5  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V5  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V6  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
> V6  OK      investigacion/fichas/artefact.md — sin incidencias
> V6  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V6  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V6  OK      investigacion/fichas/devibi.md — sin incidencias
> V6  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
> V6  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V6  OK      investigacion/fichas/instrument.md — sin incidencias
> V6  OK      investigacion/fichas/media-monks.md — sin incidencias
> V6  OK      investigacion/fichas/monopo.md — sin incidencias
> V6  OK      investigacion/fichas/pallax-media.md — sin incidencias
> V6  OK      investigacion/fichas/screenfire-media.md — sin incidencias
> V6  OK      investigacion/fichas/single-grain.md — sin incidencias
> V6  OK      investigacion/fichas/sitelabs.md — sin incidencias
> V6  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
> V6  OK      investigacion/fichas/studiodigital.md — sin incidencias
> V6  OK      investigacion/fichas/tescanet.md — sin incidencias
> V6  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
> V6  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V6  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V6  OK      investigacion/servicios/01-branding.md — sin incidencias
> V6  OK      investigacion/servicios/02-social-media.md — sin incidencias
> V6  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
> V6  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
> V6  OK      investigacion/servicios/05-performance.md — sin incidencias
> V6  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
> V6  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
> V6  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
> V6  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
> V6  OK      investigacion/servicios/10-cro.md — sin incidencias
> V6  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
> V6  OK      investigacion/servicios/resumen.md — sin incidencias
> V6  OK      investigacion/prueba-social.md — sin incidencias
> V6  OK      diseno/patrones-benchmark.md — sin incidencias
> V6  OK      diseno/sistema-web-assets.md — sin incidencias
> V7  OK      investigacion/fichas — 20 fichas: 10 comparables, 10 referentes/especialistas
> V8  AVISO   investigacion/fichas/agencia-buffalo.md — https://clutch.co/profile/agencia-buffalo → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/fichas/artefact.md — sin incidencias
> V8  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V8  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V8  AVISO   investigacion/fichas/devibi.md — https://clutch.co/profile/devibi → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://clutch.co/profile/digiberries-paris-agence-de-r-f-rencement-web → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/a-propos/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-ecommerce-shopify/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-facebook-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-geo-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-google-ads-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-google-shopping-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-instagram-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-linkedin-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-pinterest-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-referencement-local-google-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-referencement-seo-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-snapchat-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-tiktok-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-wordpress-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/nos-references/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V8  OK      investigacion/fichas/instrument.md — sin incidencias
> V8  OK      investigacion/fichas/media-monks.md — sin incidencias
> V8  OK      investigacion/fichas/monopo.md — sin incidencias
> V8  OK      investigacion/fichas/pallax-media.md — sin incidencias
> V8  OK      investigacion/fichas/screenfire-media.md — sin incidencias
> V8  OK      investigacion/fichas/single-grain.md — sin incidencias
> V8  OK      investigacion/fichas/sitelabs.md — sin incidencias
> V8  AVISO   investigacion/fichas/stratagemma-studio.md — https://clutch.co/profile/stratagemma-studio → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/studiodigital.md — https://clutch.co/profile/studiodigital → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/tescanet.md — https://clutch.co/profile/tescanet → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/trajectory-web-design.md — https://clutch.co/profile/trajectory-web-design → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/upraw-media.md — https://clutch.co/profile/upraw-media → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V8  OK      investigacion/servicios/01-branding.md — sin incidencias
> V8  OK      investigacion/servicios/02-social-media.md — sin incidencias
> V8  AVISO   investigacion/servicios/03-desarrollo-web.md — https://www.digiberries.fr/agence-wordpress-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/servicios/04-campanas-publicitarias.md — https://www.digiberries.fr/agence-google-ads-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/servicios/05-performance.md — https://www.digiberries.fr/agence-google-shopping-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
> V8  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
> V8  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
> V8  AVISO   investigacion/servicios/09-seo-geo.md — https://www.digiberries.fr/agence-geo-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/servicios/09-seo-geo.md — https://www.digiberries.fr/agence-referencement-seo-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  OK      investigacion/servicios/10-cro.md — sin incidencias
> V8  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
> V8  OK      investigacion/servicios/resumen.md — sin incidencias
> V8  AVISO   investigacion/prueba-social.md — https://www.facebook.com/business/learn/certification/faqs/exam-cost → HTTP 400 (bloqueo antibot o de región): respaldar con captura
> V8  OK      diseno/patrones-benchmark.md — sin incidencias
> V8  OK      diseno/sistema-web-assets.md — sin incidencias
>
> 0 FALLOS · 37 AVISOS
> ```
