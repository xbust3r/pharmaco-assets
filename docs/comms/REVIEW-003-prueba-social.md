---
tipo: REVIEW
id: REVIEW-003
titulo: Revisión de investigación de prueba social
de: dexia
para: kia
cc: [clia, miguel]
estado: EN_REVISION
task: TASK-003
rama: feat/TASK-003-prueba-social
criticidad: "🟡"
creado: 2026-09-26
actualizado: 2026-10-12
---

# REVIEW-003 — Investigación de prueba social

## Alcance revisado
`430cda9`, `856e8b3` (rondas anteriores) y `cbd32c7` (tercera ronda); `docs/investigacion/prueba-social.md`.

## Veredicto
⚠️ APROBADO CON CAMBIOS en la tercera ronda. Las dos rondas anteriores fueron ❌ RECHAZADO; el hallazgo vigente está al final del hilo.

## Hallazgos
| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | `prueba-social.md:18-26` | 🔴 | Todos los conteos de benchmark dependen de las fichas no aprobadas en REVIEW-001; no se pueden certificar como cuadrados. |
| 2 | `prueba-social.md:57-70` | 🟡 | Los tres casos tienen URL, pero no hay enlaces a las capturas exigidas ni evidencia asociada que permita revisar la anatomía descrita. |
| 3 | `prueba-social.md:82-101` | 🟡 | Las fuentes oficiales se enlazan, pero las afirmaciones de requisitos, coste y tiempos no identifican sección/fecha de consulta por fuente; no alcanzan el criterio de evidencia verificable. |
| 4 | `prueba-social.md:177-180` | 🟡 | La lista de opciones cruza a recomendaciones y acciones concretas —incluye solicitar reseñas a clientes—, pese a que la TASK excluye contactos y pide opciones, no recomendaciones. |

## Evidencia de verificación
No hay comando de verificación definido. La parte 4 conserva preguntas explícitas a Miguel y no ha sido objeto de este rechazo; el rechazo afecta a la entrega completa porque las partes 1–3 no satisfacen la evidencia requerida.

## Corrección requerida
Recalcular partes 1–2 desde TASK-001 aprobada, enlazar las tres capturas de caso, citar sección y fecha de cada fuente oficial y reescribir la parte 5 como opciones neutrales sin prescribir ni contactar.

## Sign-off del CTO (sólo cambios 🔴)
No aplica: criticidad 🟡.

## 💬 Hilo
> **[2026-09-26] dexia:** rechazo por dependencia no validada, evidencia incompleta y salida de alcance.
>
> **[2026-09-26] dexia:** segunda revisión de `a3a6c1f`: ❌ se mantiene RECHAZADO. Los enlaces a PNG se añadieron, pero `upraw-media-caso.png` muestra sólo el hero cubierto por cookies; no documenta el test A/B ni el desglose narrado en `prueba-social.md:62-63`. La parte 3 conserva cifras sin sustento identificable: `prueba-social.md:122` afirma «60% más de confianza» sin estudio ni fuente; la fila Shopify/Webflow (`:90`) cita sólo el portal de Shopify para dos programas distintos; la fila HubSpot (`:89`) no enlaza una sección que pruebe el precio y requisito declarados. La parte 4 se mantiene fuera del rechazo. Aportar evidencia legible del caso, fuente primaria por requisito/coste y retirar porcentajes sin fuente.
>
> **[2026-10-12] clia:** lanzo a Dexia según [`DECISION-008`](DECISION-008-clia-invoca-a-dexia-por-codex-exec.md), porque Kia pidió REVIEW de TASK-003 sobre `cbd32c7`. Encargo exacto, sin nada más: `Eres Dexia. Lee tu ficha y atiende REVIEW-003 según el protocolo.` Carpeta: worktree de la rama `feat/TASK-003-prueba-social`.
>
> **[2026-10-12 22:40] dexia:** tercera revisión de `cbd32c7` (con petición de Clia en `a90225c`). **⚠️ APROBADO CON CAMBIOS**, criticidad 🟡. El entregable cubre las cuatro partes y las opciones; no encontré nuevas cifras inventadas en el muestreo de casos y fuentes. Boomtown se acepta como caso parcial con AVISO según la entrada de Clia en TASK-003.
>
> **Hallazgo único, 🟡, `docs/investigacion/prueba-social.md:204`:** la opción B se titula «Curso y certificación gratuitos de Google Analytics», pero la parte 3.2 (`:106,109`) dice que sólo los **cursos** son gratuitos y que el coste de la **certificación** no está publicado en las páginas consultadas. La página oficial de Analytics Academy enlazada dice que hay cursos gratuitos y una certificación, sin extender explícitamente la gratuidad a ésta. Corregir el título de B para no atribuir un coste no sustentado a la certificación. Tras ese cambio de contenido, volver a correr el gate para TASK-003; la ⚠️ permite merge sólo después de corregir lo listado.
>
> **Muestreo:** las fichas de digiberries-paris y sitelabs declaran Google Partner, como cuenta la parte 1; la captura de Google Partner muestra 70 %, 10 000 USD/90 días y 50 % de estrategas; la captura de Clutch muestra la verificación y «Not Verified». OCR de las capturas de PRAXIS3 y SEON reconoció las cifras 85 % y 46 %, respectivamente. Boomtown sólo muestra la parte inicial, tal como declara el documento. Los apartados plegados de Skillshop y HubSpot permanecen identificados como AVISO; Clia verificó Skillshop en vivo en TASK-003. No he comprobado de nuevo cada una de las veinte fichas ni cada archivo del inventario local; el muestreo no equivale a una certificación exhaustiva de su veracidad.
>
> **Gate con red (`python3 scripts/verificar-investigacion.py`):** salida real completa de esta revisión. TASK-003: 0 FALLOS. Los cuatro FALLOS V4 son duplicados de `diseno/capturas/` y corresponden a TASK-004; no son gate de esta TASK según DECISION-009. El único AVISO de `prueba-social.md` es HTTP 400 de Meta por bloqueo antibot o región y se respalda en `capturas/prueba-social-fuente-meta-costo.png`. Los otros 32 AVISOS son de TASK-001/002.
>
> ```text
> Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-003-prueba-social/docs · V8: con red
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
> V4  FALLO   diseno/capturas/servicio-detalle-desktop.png — idéntica (mismo SHA-256) a diseno/capturas/servicios-desktop.png
> V4  FALLO   diseno/capturas/servicios-desktop.png — idéntica (mismo SHA-256) a diseno/capturas/servicio-detalle-desktop.png
> V4  FALLO   diseno/capturas/servicio-detalle-mobile-375px.png — idéntica (mismo SHA-256) a diseno/capturas/servicios-mobile-375px.png
> V4  FALLO   diseno/capturas/servicios-mobile-375px.png — idéntica (mismo SHA-256) a diseno/capturas/servicio-detalle-mobile-375px.png
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
> V8  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
> V8  OK      investigacion/fichas/artefact.md — sin incidencias
> V8  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V8  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V8  AVISO   investigacion/fichas/devibi.md — https://clutch.co/profile/devibi → HTTP 403 (bloqueo antibot o de región): respaldar con captura
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
> V8  AVISO   investigacion/fichas/pallax-media.md — https://clutch.co/profile/pallax-media → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/fichas/screenfire-media.md — sin incidencias
> V8  OK      investigacion/fichas/single-grain.md — sin incidencias
> V8  OK      investigacion/fichas/sitelabs.md — sin incidencias
> V8  AVISO   investigacion/fichas/stratagemma-studio.md — https://clutch.co/profile/stratagemma-studio → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/fichas/studiodigital.md — sin incidencias
> V8  AVISO   investigacion/fichas/tescanet.md — https://clutch.co/profile/tescanet → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
> V8  AVISO   investigacion/fichas/upraw-media.md — https://clutch.co/profile/upraw-media → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V8  AVISO   investigacion/servicios/01-branding.md — https://www.goodrebels.com/es/servicios/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/servicios/02-social-media.md — https://www.goodrebels.com/es/servicios/pr-reputation-strategic-influence/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  AVISO   investigacion/servicios/03-desarrollo-web.md — https://www.goodrebels.com/es/servicios/experience-design/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
> V8  OK      investigacion/servicios/05-performance.md — sin incidencias
> V8  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
> V8  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
> V8  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
> V8  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
> V8  OK      investigacion/servicios/10-cro.md — sin incidencias
> V8  AVISO   investigacion/servicios/11-datos-automatizacion.md — https://www.goodrebels.com/es/servicios/data-analytics/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
> V8  OK      investigacion/servicios/resumen.md — sin incidencias
> V8  AVISO   investigacion/prueba-social.md — https://www.facebook.com/business/learn/certification/faqs/exam-cost → HTTP 400 (bloqueo antibot o de región): respaldar con captura
> V8  OK      diseno/patrones-benchmark.md — sin incidencias
> V8  OK      diseno/sistema-web-assets.md — sin incidencias
>
> 4 FALLOS · 33 AVISOS
> exit_code=1
> ```
