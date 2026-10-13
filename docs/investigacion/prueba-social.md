# Prueba social desde cero — investigación (TASK-003)

> **Tarea:** [TASK-003](../comms/TASK-003-investigacion-prueba-social.md) · **Autora:** Kia · **Fecha de consulta:** 2026-10-10
> **Base de conteo:** las 20 fichas de [`fichas/`](fichas/) de esta rama (10 comparables, 10 referentes y especialistas). `fichas/anexo-medianas/` no cuenta.
> **Hechos y opciones van separados.** La parte 5 son opciones, no recomendaciones; la elección es de Clia y Miguel (RFC-002).

---

## Parte 1. Qué usan las agencias de la muestra

Cómo se cuenta: cada tipo se cuenta **sólo si la ficha lo documenta**. «No publicado» o «no documentado en la ficha» no suma; no equivale a «la agencia no lo tiene», porque la ficha sólo recoge lo que se revisó.

| Tipo de prueba social | Comparables (de 10) | Referentes y especialistas (de 10) | Qué cuenta |
| --- | :---: | :---: | --- |
| Caso con página propia | **4**: agencia-buffalo, sitelabs, screenfire-media, trajectory-web-design | **10**: todas | Página individual de un proyecto. Sin página propia (listado de trabajos o de clientes): devibi, digiberries-paris y tescanet, todas comparables |
| Caso con cifra de resultado | **1**: trajectory-web-design | **4**: dogstudio (cifras de alcance), media-monks, single-grain, upraw-media | Cifra de resultado en la página del caso |
| Logos o nombres de clientes | **4**: digiberries-paris, sitelabs, screenfire-media (nombres en texto, no logos), trajectory-web-design | **4**: artefact, instrument (carrusel), single-grain, upraw-media | Logos o lista de nombres en la web |
| Testimonio con nombre y cargo o actividad | **2**: digiberries-paris, sitelabs (nombre y actividad, sin cargo empresarial) | **1**: dogstudio | Cita de cliente con nombre |
| Reseña de terceros visible | **2**: digiberries-paris (Google, 4,9), pallax-media (Google, ProvenExpert y Sortlist) | **1**: upraw-media (dos plataformas sin identificar) | Valoración de plataforma externa |
| Premio o ranking | **0** | **3**: code-and-theory, dogstudio, instrument | Premio o ranking de la industria |
| Certificación o partnership declarado | **4**: digiberries-paris y sitelabs (Google Partner); tescanet («W3C Certifica nuestra calidad», sin programa nombrado); trajectory-web-design («Strategic partnership», sin programa nombrado) | **3**: artefact («Tech Partners' Certifications», sin programa nombrado); blueorange-digital (SOC 2 Type II; Databricks y Claude); work-and-co («Accenture Song», sin programa nombrado) | Lo declara la web. Sólo digiberries-paris, sitelabs y blueorange-digital nombran un programa de plataforma o un informe de auditoría |
| Contenido propio en el menú (Blog, Podcast, News, Insights, Learn) | **5**: agencia-buffalo, devibi, screenfire-media, tescanet, trajectory-web-design | **5**: artefact (Insights), code-and-theory (Latest News), single-grain (Learn), upraw-media (Blog, Podcast), work-and-co (News & Insights) | Sección de contenido visible en el menú principal. No se ha evaluado su contenido. Quedan fuera «Latest» (instrument) y «Resources» (blueorange-digital), por ambiguos |
| Personas con nombre y cargo visibles | **1**: screenfire-media | **0** documentados | Equipo con nombres y cargos en la web revisada |
| Cifra agregada propia (proyectos, clientes, resultado o rendimiento declarado) | **5**: devibi («87+ projects shipped»), digiberries-paris («10M€ de budgets»), sitelabs («170+ PROYECTOS»), studiodigital (rendimiento declarado, sin cliente), trajectory-web-design («200+ projects») | **3**: blueorange-digital, single-grain («500+ Companies»), upraw-media | Cifra que la agencia publica sobre sí misma. Los años de antigüedad no se cuentan |

**Lectura de los conteos, sin interpretarlos:**
- Los casos con página propia aparecen en 14 de 20 fichas. Las 10 referentes y especialistas los tienen; entre las comparables, 4 de 10.
- Los premios aparecen sólo en referentes y especialistas (3 de 10). Ninguna comparable lo documenta.
- Las reseñas de terceros aparecen en 3 de 20 fichas, y las certificaciones con programa nombrado en 3 de 20 (digiberries-paris, sitelabs, blueorange-digital).
- Los testimonios con nombre aparecen en 3 de 20 fichas.

Fuentes de los conteos: las fichas de [`fichas/`](fichas/), sección «Prueba social». Las capturas de cada ficha están en [`capturas/`](capturas/).

---

## Parte 2. Anatomía de un caso de éxito

Se han abierto las tres páginas en esta sesión (2026-10-10) y se han hecho capturas con Chrome headless. La anatomía se describe **sólo de lo que se ve en la captura** y, cuando un bloque sólo aparece en la lectura de la página (WebFetch) y no en la captura, se marca como AVISO.

### 2.1 Bloques observados, en orden

Trajectory PRAXIS3 (captura completa, sin banner):

1. Cabecera: etiqueta «CASE STUDY», título del cliente (`PRAXIS3`), párrafo de presentación y bloque «Key outcomes» con tres resultados en viñetas.
2. Imagen de la web del cliente.
3. «The Challenge: Balancing Breadth and Focus» (el reto).
4. «Our Approach: Strategy First» (proceso: descubrimiento, estrategia de contenidos, arquitectura de información).
5. «The Solution: Purposeful Design» (la solución, con capturas).
6. «Results: Measurable Impact» (resultados en texto y capturas).
7. Llamada a la acción: «Ready for a website that actually works?».

No tiene testimonio ni bloque de créditos.

SEON / Upraw Media (captura de la parte superior; un banner de cookies cubre parte de «Approach»):

1. Titular con el resultado: «How we increased SEON's high-intent landing page conversion rates by 46%».
2. «The Situation» (contexto del cliente).
3. «Challenges» (lista de problemas, sin cifras).
4. «Approach» (lista de actividades, con «AB testing assessment, strategy & education»).
5. «The results speak for themselves» (cuatro tarjetas de resultado).
6. «Hero Section Before» (comparación antes y después de la portada del cliente).

**AVISO:** la captura no llega al testimonio ni a la llamada a la acción. Ambos bloques sólo se han leído con WebFetch: testimonio de «Dorottya Kiss, Performance Marketing Team Lead» y llamada «Talk to the founder».

Monks / Boomtown (captura en 4600 px):

1. Titular: «Boomtown Unboxed • Driving Record Sales for Boomtown with Personalized Video».
2. Etiquetas de cliente y servicios (Client: «Boomtown, Amplify»).
3. Vídeo con reproductor («Watch video 01:44»).
4. «The goal: turn post-event buzz into early ticket sales.» (el reto).

**AVISO:** el resto de la página no se renderiza en la captura (contenido cargado en diferido) y aparece en blanco bajo el banner de cookies. Los bloques de solución y resultados sólo se han leído con WebFetch: «88% average completion rate» y «over 40% of viewers downloaded or shared their personal video». Este caso queda como modelo **parcial**.

### 2.2 Tres casos modelo

| # | Tipo de agencia | Caso y URL | Captura | Qué muestra la captura | Estado |
| --- | --- | --- | --- | --- | --- |
| 1 | Comparable (trajectory-web-design) | PRAXIS3 · `https://www.trajectorywebdesign.com/work/praxis3/` | [`capturas/prueba-social-praxis3-caso.png`](capturas/prueba-social-praxis3-caso.png) | Los siete bloques de la lista anterior, excepto el texto completo del bloque de resultados | Completo. Métricas visibles: «Page load speeds improved by 85% and mobile engagement increased by 60%» |
| 2 | Especialista (upraw-media) | SEON · `https://www.uprawmedia.com/seon-cro-case-study` | [`capturas/prueba-social-seon-caso.png`](capturas/prueba-social-seon-caso.png) | Titular, situación, retos, enfoque, resultados (cuatro tarjetas) y antes/después de la portada | Parcial: sin testimonio ni CTA en la captura. Métrica visible: «A huge +46% increase on high intent landing page conversion rates reported by the client» |
| 3 | Referente (media-monks) | Boomtown · `https://www.monks.com/case-studies/boomtown-amplify-ai-powered-platform` | [`capturas/prueba-social-boomtown-caso.png`](capturas/prueba-social-boomtown-caso.png) | Titular, etiquetas, vídeo y reto | **AVISO:** sin bloque de resultados en la captura. Las cifras sólo vienen de WebFetch |

Los casos de la muestra que **no** se han usado como modelo, y por qué: Schumacher (single-grain) tiene un pop-up que tapa el caso, y su captura no sirve; ServiceNow (instrument) muestra titular, reto y visual, pero no los resultados ni el testimonio en la captura, y tampoco tiene cifras en la captura. Ninguno de los dos se cita como modelo.

---

## Parte 3. Qué se puede construir sin historial de clientes grandes

Cada fila tiene la fuente oficial que se ha abierto, la sección, la cita literal de **una frase** y la captura. Lo que no aparece en la fuente se escribe «no publicado en la página consultada». La fecha de consulta es 2026-10-10.

### 3.1 Google Partner (insignia de empresa en Google Ads)

- **Qué es:** insignia que Google concede a la empresa, no a una persona. Exige rendimiento, gasto y certificaciones.
- **Fuente:** [How to become a Google Partner or Premier Partner](https://support.google.com/google-ads/answer/9702452?hl=en). Sección «How to become a Google Partner», tabla de requisitos. Captura: [`capturas/prueba-social-fuente-google-partner.png`](capturas/prueba-social-fuente-google-partner.png).
- **Requisitos (citas literales, visibles en la captura):**
  - Rendimiento: «Your Google Partners registered Ads manager account needs to have a minimum optimization score of 70%».
  - Gasto: «Your Google Partners registered Ads manager account needs to maintain a 90-day ad spend of $10,000 USD across managed accounts.»
  - Certificaciones: «Your Google Partners registered Ads manager account needs to have a minimum of 50% of your account strategists certified in Google Ads (capped at 100 users)…»
  - Frecuencia: «The Google Partner requirements are checked on a daily basis.»
- **Coste:** no publicado en la página consultada. **Tiempo:** no publicado.
- **Lo que implica el requisito de gasto:** exige gasto gestionado de cuentas de clientes; no es un requisito que se cumpla sin clientes.
- **Agencias que lo declaran:** digiberries-paris, sitelabs.

### 3.2 Google Analytics: curso y certificación en Skillshop

- **Qué es:** curso y evaluación en Skillshop sobre Google Analytics.
- **Fuente 1:** [Analytics Academy](https://support.google.com/analytics/answer/15440208?hl=en). Captura: [`capturas/prueba-social-fuente-ga-academy.png`](capturas/prueba-social-fuente-ga-academy.png). Cita visible: «Google Analytics currently offers 4 training courses and a certification.» Y de la misma sección: «Analytics Academy on Skillshop is a collection of free e-learning courses designed by Analytics experts…» (el coste gratuito se dice de los cursos, no de la certificación).
- **Fuente 2:** [Certifications for Skillshop Google Ads/GMP/GA](https://support.google.com/skillshop/answer/14744470?hl=en). Sección «To earn an achievement or a certification». Captura: [`capturas/prueba-social-fuente-skillshop-certificacion.png`](capturas/prueba-social-fuente-skillshop-certificacion.png). Cita visible: «Prepare for the assessment by performing the activities contained within the path.» y «Complete any associated certification assessment(s).»
- **Requisitos de aprobación (AVISO):** la [FAQ de Skillshop](https://support.google.com/skillshop/answer/14739859?hl=en-AU) indica en la lectura de la página (WebFetch) «you'll need a score of 80% or greater to pass», «you’ll need to wait 24 hours before you can take it again» y «There's no limit to the number of attempts you can have.». **La captura de esa FAQ muestra el índice con los apartados plegados** (captura: [`capturas/prueba-social-fuente-skillshop-faq.png`](capturas/prueba-social-fuente-skillshop-faq.png)), así que estas tres frases no están verificadas visualmente.
- **Coste de la certificación:** no publicado en las páginas consultadas. **Tiempo:** no publicado.
- **Agencias que lo declaran:** ninguna ficha lo documenta.

### 3.3 Meta Blueprint (certificaciones de medios y marketing)

- **Qué es:** exámenes oficiales de Meta sobre planificación y compra de medios, entre otros.
- **Fuente:** [¿Cuánto cuestan los exámenes?](https://www.facebook.com/business/learn/certification/faqs/exam-cost). Sección «Programar Tu Examen», apartado «¿Cuánto cuestan los exámenes?». Captura: [`capturas/prueba-social-fuente-meta-costo.png`](capturas/prueba-social-fuente-meta-costo.png). Cita literal, visible: «El costo de los exámenes de certificación de Meta varía entre el equivalente a 99 y 150 dólares estadounidenses (USD).» Y: «El costo real puede variar según el país.»
- **Coste:** entre 99 y 150 USD según la página, variable por país. **Tiempo de preparación:** no publicado en la página consultada.
- **Agencias que lo declaran:** ninguna ficha lo documenta.

### 3.4 HubSpot Solutions Partner

- **Qué es:** programa de partners de HubSpot; exige que una persona de la organización apruebe un examen y lo renueve.
- **Fuente:** [HubSpot Solutions Partner onboarding resource center](https://www.hubspot.com/partner-onboarding-resource-center). Sección «Onboarding Milestones». Captura: [`capturas/prueba-social-fuente-hubspot.png`](capturas/prueba-social-fuente-hubspot.png). Cita visible: «These milestones are the top six major tasks and accomplishments to complete in your first 90 days, in order.»
- **Requisito de examen y renovación (AVISO):** en la lectura de la página (WebFetch) aparece «Every partner organization needs one individual to take and pass the Solutions Partner Certification exam…» y «Note: this must be renewed every two years.». **Estas frases están en apartados plegados y no aparecen en la captura**, así que no están verificadas visualmente.
- **Coste:** no publicado en la página consultada. **Tamaño mínimo de equipo:** no publicado en la página consultada.
- **Agencias que lo declaran:** ninguna ficha lo documenta.

### 3.5 Clutch (perfil y reseñas verificadas)

- **Qué es:** directorio B2B de agencias. Las reseñas pasan por verificación de identidad e historial de trabajo.
- **Fuente:** [How Does Clutch Verify Reviews?](https://help.clutch.co/en/knowledge/how-clutch-verifies-reviews). Sección «Review Verification & Publishing» (Help Center › For Buyers). Captura: [`capturas/prueba-social-fuente-clutch.png`](capturas/prueba-social-fuente-clutch.png). Citas visibles: «Clutch verifies reviews using reviewer-provided information & online research.» y «To leave a review on Clutch, you’ll need a LinkedIn, Google account, or company email address.»
- **Sin verificar:** si no puede verificar identidad o proyecto, la página dice que publica la reseña como «Not Verified» (visible en la captura).
- **Coste del perfil:** no publicado en la página consultada. La URL `clutch.co/how-it-works` devolvió 404 en WebFetch el 2026-10-10 y no se ha usado.
- **Agencias:** 10 fichas enlazan un perfil de Clutch (agencia-buffalo, devibi, digiberries-paris, pallax-media, sitelabs, stratagemma-studio, studiodigital, tescanet, trajectory-web-design, upraw-media). screenfire-media indica que su perfil devuelve 404. **En ninguna ficha se ha revisado una reseña de Clutch.**

### 3.6 Google Business Profile

- **Qué es:** perfil de empresa en Google. Requiere verificar la empresa.
- **Fuente:** [Verifica tu empresa en Google](https://support.google.com/business/answer/7107242). Sección «Paso 2: Verifica tu empresa» y «Paso 3». Captura: [`capturas/prueba-social-fuente-gbp.png`](capturas/prueba-social-fuente-gbp.png) (página en español). Citas visibles: «Paso 3: Espera hasta 5 días hábiles para que se complete la verificación» y los métodos «Teléfono o mensaje de texto», «Correo electrónico», «Videollamada en vivo» y «Correo».
- **Coste:** no publicado en la página consultada.
- **Agencias:** ninguna ficha documenta un perfil de Google Business. Las fichas de digiberries-paris y pallax-media citan valoraciones de Google sin indicar de qué perfil proceden.

### 3.7 Contenido propio (blog, podcast, noticias)

- **Qué es:** artículos, pódcast o noticias publicados por la agencia.
- **Fuente:** no hay fuente oficial externa. Es un hecho de la muestra: la sección aparece en el menú principal de 10 de 20 agencias (ver Parte 1).
- **Coste y tiempo:** no hay dato de la muestra ni de fuente oficial. No se ha medido el coste de producir contenido.

### 3.8 Proyectos propios

- **Qué es:** trabajos propios que la agencia publica como caso.
- **Fuente:** no hay fuente externa. Ninguna ficha documenta un proyecto propio publicado como caso. No se ha buscado esto fuera de las fichas.
- **Coste y tiempo:** no publicado.

---

## Parte 4. Inventario de lo que tiene Pharmaco

Ruta revisada: `~/servers/pharmaco.pe/wp-content/themes/pharmaco/assets/`. Inventario de archivos reales (2026-10-10). **No se valora si se puede usar.** Los textos de `Lorem ipsum` del sitio de 2020 se citan entre comillas invertidas.

### 4.1 Proyectos del portafolio

| Proyecto | Página | Marca indicada en la página | Carpeta de imágenes (archivos) | Imágenes referenciadas (únicas) | Referencias rotas | Texto |
| --- | --- | --- | --- | :---: | :---: | --- |
| Campaña CyberWow | `campana-cyberwow.html` | «Brand: Motored» (línea 124) | `images/components/portafolio/campaña-cyberwow/` (108) | 70 | 1: `video1-l.webp` (línea 377) | `Lorem ipsum` en 4 líneas |
| Campaña Iveco | `campana-iveco.html` | «Brand: Iveco» (línea 124) | `images/components/portafolio/campaña-iveco/` (72) | 40 | 1: `publicacion-revista-revista1-lg.webp` (línea 204) | `Lorem ipsum` en 4 líneas |
| Campaña Stralis | `campana-stralis.html` | «Brand: Iveco» (línea 124) | `images/components/portafolio/campaña-stralis/` (116) | 57 | 0 | `Lorem ipsum` en 4 líneas |
| Diseño de personajes | `diseño-de-personajes.html` | «Brand: Moiré» (línea 122) | `images/components/portafolio/diseño-de-personajes/` (38) | 24 | 0 | `Lorem ipsum` en 4 líneas |
| Branding Venturi | No existe página de detalle. Tarjeta en `index.html` (línea 220) y `portafolio.html` (líneas 181 y 226) | No aplica | Ninguna. Usa `images/components/projects/project-1.webp` | — | El enlace `portafolio-detalle.html` no existe | No aplica |
| Modelado 3D | No existe página de detalle. Tarjeta en `index.html` (línea 205) y `portafolio.html` (línea 211) | No aplica | Ninguna. Usa `images/components/projects/project-1.webp` | — | El enlace `portafolio-detalle.html` no existe | No aplica |

Notas:
- Las cuatro páginas de proyecto existen y sus imágenes están en disco. Los números de la columna «Imágenes» cuentan referencias únicas de `src` en el HTML; la carpeta cuenta todos los archivos (PNG, JPG y WebP, en varios tamaños).
- Las tarjetas de Venturi y Modelado 3D usan `alt="alt"` y la misma imagen de marcador.
- `Lorem ipsum` aparece además en `index.html` (3 líneas), `portafolio.html` (9) y `servicio-detalle.html` (1).
- En `campana-stralis.html` y `campana-iveco.html` la marca es la misma (Iveco). Los archivos no documentan qué relación hay entre el proyecto Stralis y la marca Iveco.
- La página `diseño-de-personajes.html` usa en la línea 228 el texto «Moiré, es una agencia digital que realiza vídeos en 2D ó 3D» para describir al proyecto. No se documenta si Moiré es cliente, colaborador o autor.

### 4.2 Logos de clientes

- Carpeta: `images/components/clients/`. Hay cinco SVG (`client-1.svg` a `client-5.svg`), cada uno con viewBox de 206 × 46, y cinco PNG de 210 × 60 px. Los SVG son sólo trazos vectoriales: no contienen texto (`<text>`), así que **el archivo no dice qué marca es cada logo**.
- En `index.html` (líneas 256 a 268) y `nosotros.html` (líneas 177 a 189) los cinco logos usan `alt="alt"`.

### 4.3 Preguntas abiertas para Miguel

Estas preguntas no se resuelven con los archivos. Ninguna se da por supuesta.

1. ¿Puede Pharmaco seguir mostrando en la nueva web los proyectos de Iveco, Motored (CyberWow) y Moiré?
2. Stralis e Iveco aparecen con la misma marca. ¿Es el mismo cliente, y se pueden mostrar como dos casos separados?
3. Venturi y Modelado 3D no tienen página de detalle ni imágenes propias. ¿Existe material real para ellos?
4. ¿Cuáles son las marcas de los logos `client-1.svg` a `client-5.svg`? Los archivos no lo dicen.
5. ¿Existen métricas reales de esas campañas que se puedan publicar? Sin ellas, los casos no tienen cifras.
6. ¿Hay clientes de los últimos años (2022 a 2026) que puedan figurar como caso o como testimonio?
7. ¿Moiré es cliente, colaborador o autor de los renders de la página de diseño de personajes?

---

## Parte 5. Opciones de prueba social para Pharmaco

Son **opciones**, no recomendaciones. Van ordenadas de menor a mayor dependencia de terceros. El esfuerzo en horas no está publicado en las fuentes, así que el criterio de orden es la dependencia de terceros y el tiempo que declaran las fuentes. Cada opción tiene su evidencia. La elección es de Clia y Miguel.

| # | Opción | Qué implica (según fuente) | Dependencia de terceros | Evidencia |
| :---: | --- | --- | --- | --- |
| A | Contenido propio en el sitio (blog, pódcast o noticias) | Sección de contenido en el menú. Coste y tiempo no publicados | Ninguna | 10 de 20 agencias lo muestran en el menú (Parte 1, fila «Contenido propio») |
| B | Curso y certificación gratuitos de Google Analytics en Skillshop | Cursos gratuitos; aprobación con 80 % según la FAQ (AVISO); coste de la certificación no publicado | Ninguna (persona individual) | [Analytics Academy](https://support.google.com/analytics/answer/15440208?hl=en); [certificaciones](https://support.google.com/skillshop/answer/14744470?hl=en). Ninguna ficha lo declara |
| C | Perfil verificado en Google Business Profile | Verificación en hasta 5 días hábiles (Paso 3); métodos: teléfono, correo, videollamada o correo postal | Verificación de Google | [Verifica tu empresa en Google](https://support.google.com/business/answer/7107242). Ninguna ficha lo declara |
| D | Certificaciones de plataforma individuales: Meta Blueprint | Examen entre 99 y 150 USD según país | Ninguna (persona individual) | [Meta, costo de exámenes](https://www.facebook.com/business/learn/certification/faqs/exam-cost). Ninguna ficha lo declara |
| E | HubSpot Solutions Partner | Una persona aprueba el examen; se renueva cada dos años (AVISO: no visible en captura) | Requiere programa de partner | [HubSpot](https://www.hubspot.com/partner-onboarding-resource-center). Ninguna ficha lo declara |
| F | Perfil de Clutch con reseñas verificadas | Perfil sin coste publicado (no publicado); reseñas verificadas por identidad e historial de trabajo | Reseñas de clientes que deben escribirlas | [Clutch](https://help.clutch.co/en/knowledge/how-clutch-verifies-reviews). 10 fichas enlazan perfil; ninguna reseña revisada |
| G | Google Partner (empresa) | 70 % de optimización, 10 000 USD de gasto gestionado en 90 días, 50 % de estrategas certificados | Cuentas de clientes con gasto | [Google Partner](https://support.google.com/google-ads/answer/9702452?hl=en). Declarado por digiberries-paris y sitelabs |
| H | Casos con página propia y cifras de resultado | Un caso con página propia y cifra de resultado en la web | Datos y permiso de clientes | Caso con cifra: trajectory-web-design, upraw-media (y referentes, Parte 1). Pregunta 5 de Miguel |
| I | Activos del portafolio de 2020 (campañas, diseño, logos) | Material existente con textos de `Lorem ipsum` y marcas no confirmadas | Autorización de Miguel | Parte 4. Preguntas 1 a 4 y 7 |

---

## Avisos y lo que queda sin verificar

- **AVISO, captura de Boomtown:** sin bloque de resultados (Parte 2).
- **AVISO, captura de SEON:** sin testimonio ni llamada a la acción en la captura (Parte 2).
- **AVISO, Skillshop FAQ:** las frases de 80 %, 24 horas y número ilimitado de intentos vienen de WebFetch; la captura muestra la FAQ plegada (Parte 3.2).
- **AVISO, HubSpot:** la frase sobre examen y renovación cada dos años viene de WebFetch; la captura muestra el apartado plegado (Parte 3.4).
- **Clutch:** `clutch.co/how-it-works` devolvió 404 en WebFetch; no se ha usado como fuente.
- **Sin verificar en la muestra:** las reseñas de Clutch de cualquier agencia, por ausencia de revisión; el contenido de los blogs; y los proyectos propios fuera de las fichas.
- **Descartado de la versión anterior:** «60 % más de confianza»; la fila de Shopify y Webflow; los «Pharmaco Lab» y otros proyectos propuestos, que no son datos de la muestra; el caso de Matter Supply, que no estaba en la muestra.
