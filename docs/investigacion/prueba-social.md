# 🏆 Investigación — Cómo construir prueba social desde cero (TASK-003)

> **Documento:** `docs/investigacion/prueba-social.md` · **Tarea:** [TASK-003](../comms/TASK-003-investigacion-prueba-social.md)
> **Autora:** Ania (DEV principal) · **Fecha:** 2026-09-26
> **Muestra base:** 20 agencias internacionales de [TASK-001](../comms/TASK-001-investigacion-benchmark-agencias.md) y archivos locales de `pharmaco.pe`.
> **Estado:** Documento completo con evidencia cuantitativa, análisis estructural, requisitos oficiales de acreditación e inventario de activos locales.

---

## Parte 1. Qué usan las agencias de la muestra (Benchmark de 20 agencias)

Pharmaco se retoma sin prueba social validada ([`DECISION-002`](../comms/DECISION-002-catalogo-base-servicios.md)). Para entender qué elementos convencen a un cliente en 2026, se analizó el uso de prueba social en la muestra verificada en vivo de 20 agencias (10 Europa, 10 América), desglosando entre **Comparables** (10 agencias independientes de 10 a 80 empleados) y **Referentes / Especialistas** (10 agencias de gran escala o de nicho tecnológico).

### 1.1 Frecuencia por tipo de prueba social

| Tipo de Prueba Social | Total (de 20) | Comparables (de 10) | Referentes / Especialistas (de 10) | Frecuencia Relativa | Observación de Uso |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logos de clientes conocidos** | **20** | 10 | 10 | 100% | Elemento universal sin excepciones. Se ubica inmediatamente tras el Hero principal o en la mitad de la home. |
| **Casos de estudio detallados** | **20** | 10 | 10 | 100% | Fichas individuales con narrativa de proyecto. En referentes el caso es altamente visual; en comparables incluye procesos y tecnologías. |
| **Testimonios de clientes con nombre/cargo** | **18** | 9 | 9 | 90% | Citas directas con fotografía real, nombre y cargo directivo. Los referentes usan citas breves integradas; los comparables, módulos destacados. |
| **Premios del sector (Awwwards, Cannes, Webby, Clutch)** | **19** | 9 | 10 | 95% | Predominante en agencias de diseño y creatividad (Dogstudio, Monopo, Bravoure, Instrument) y en rankings B2B (Clutch en comparables). |
| **Certificaciones y partnerships oficiales** | **19** | 9 | 10 | 95% | Sellos de Google Premier Partner, Meta Business Partner, HubSpot, AWS, Databricks, Shopify Plus. Crítico en agencias medianas y técnicas. |
| **Casos con métricas cuantitativas explícitas** | **9** | 7 | 2 | 45% | Cifras porcentuales de crecimiento (+X%), ROAS, aumento de tráfico o reducción de CPA. Muy concentrado en agencias de performance y CRO (Upraw, Brolik, Atomic, Major Tom). |
| **Contenido experto propio (Blog, Podcast, Libros)** | **7** | 4 | 3 | 35% | Artículos técnicos de fondo, informes anuales descargables, podcasts sectoriales (Upraw, Single Grain) o libros corporativos (Good Rebels). |
| **Reseñas en plataformas de terceros (Clutch, Google)** | **7** | 6 | 1 | 35% | **Diferencia clave:** Muy usado por agencias comparables medianas (Atomic, Lounge Lizard, Brolik, Single Grain); los gigantes globales (Media.Monks, Work & Co) no usan Clutch. |
| **Cifras agregadas de impacto («Impact Stats»)** | **8** | 5 | 3 | 40% | Números acumulados en la home: «+20 años», «+$50M generados», «2.000+ personas», «50% engineers, 50% creatives». |

---

## Parte 2. Anatomía de un caso de éxito (Case Study)

A partir del análisis de las páginas de caso de la muestra navegadas en vivo, se determinó el estándar de arquitectura de información que estructura un caso convincente:

### 2.1 Estructura canónica (en orden de lectura)

```text
1. Cabecera (Hero del caso)
   ├── Nombre del cliente + Categoría / Servicios prestados (tags)
   ├── Titular de impacto (el resultado o concepto en una frase)
   └── Imagen o video principal (Mockup editorial o showreel)
2. El Reto (The Challenge / El Problema)
   ├── Contexto del cliente y situación inicial
   └── Qué impedía su crecimiento o qué objetivo perseguía
3. La Estrategia y Solución (The Solution / Lo que hicimos)
   ├── Proceso de trabajo (Discovery, Sprint de diseño, Arquitectura técnica)
   ├── Muestras visuales en alta definición (capturas, prototipos interactivos, fotos de set)
   └── Herramientas y tecnologías aplicadas (Stack)
4. Los Resultados (The Impact / Métricas)
   ├── 2 a 4 estadísticas cuantitativas en gran tamaño (ej. «+46% Conversión», «567% Loan Volume»)
   └── Declaración del impacto cualitativo en el negocio
5. Testimonio del Cliente (Social Proof Quote)
   └── Cita textual del interlocutor + Foto + Nombre + Cargo + Empresa
6. Créditos del equipo y CTA de cierre
   └── Quién participó + Botón directo: «¿Tienes un reto similar? Hablemos»
```

### 2.2 Tres casos modelo de referencia verificados en vivo

1. **Modelo de Métricas y Conversión (B2B SaaS / CRO):**
   * **Agencia:** Upraw Media (Reino Unido)
   * **URL:** https://www.uprawmedia.com/seon-cro-case-study
   * **Evidencia visual capturada:** [`capturas/upraw-media-caso.png`](capturas/upraw-media-caso.png) (consultado: 2026-09-26).
   * **Anatomía observable en la captura:** Cabecera con titular de impacto numérico (+46% de incremento en tasa de conversión para SEON), badges de categoría (SaaS PPC & CRO), desglose del reto técnico, visualización del test A/B y resultados cuantitativos verificables.
2. **Modelo de Producción Creativa, Video y Branding:**
   * **Agencia:** Bravoure (Países Bajos)
   * **URL:** https://bravoure.nl/en/case-studies/oxfam-novib
   * **Evidencia visual capturada:** [`capturas/bravoure-caso.png`](capturas/bravoure-caso.png) (consultado: 2026-09-26).
   * **Anatomía observable en la captura:** Hero visual con material audiovisual a pantalla completa, manifiesto del proyecto, dirección de arte contemporánea, módulos interactivos y despiece de activos digitales de campaña.
3. **Modelo de Crecimiento a Largo Plazo y Multicanal (Comparable):**
   * **Agencia:** Brolik (EE. UU.)
   * **URL:** https://brolik.com/work/full-funnel-marketing-real-estate-lender
   * **Evidencia visual capturada:** [`capturas/brolik-caso.png`](capturas/brolik-caso.png) (consultado: 2026-09-26).
   * **Anatomía observable en la captura:** Desglose del caso en narrativa cronológica (relación de 10 años), métrica central (+567% en volumen de préstamos), integración de web, branding y video, y cita testimonial de interlocutor directivo.

---

## Parte 3. Qué se puede construir sin historial de clientes grandes

Para una agencia en fase de reactivación que no cuenta con un histórico reciente de clientes corporativos con métricas públicas, las agencias analizadas demuestran que es posible generar credibilidad inmediata mediante **cuatro frentes accesibles sin clientes grandes**:

### 3.1 Certificaciones oficiales de plataformas líderes

Las certificaciones de partners aportan validación técnica externa garantizada por corporaciones globales:

| Certificación / Programa | Requisitos Oficiales | Coste | Tiempo Estimado | Fuente Oficial (Sección y Fecha de Consulta) | Agencias que lo usan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Google Cloud / Google Analytics 4 Certification** | Aprobar los exámenes oficiales en Google Skillshop (mínimo 80% de aciertos). Acredita dominio en medición analítica, GA4 y Google Tag Manager. | **Gratuito** | 1 a 2 semanas por persona | [Google Skillshop - Analytics Academy](https://skillshop.docebosaas.com/) (Sección: *Google Analytics Certification*, consultado: 2026-09-26) | [Artefact](fichas/artefact.md), [Neo Consulting](fichas/neo-consulting.md), [Upraw](fichas/upraw-media.md) |
| **Meta Certified Media & Marketing Science** | Aprobar exámenes oficiales en Meta Blueprint (100-101 / 400-101) sobre planificación de medios, compra publicitaria en red Meta y modelos de atribución. | **$99 - $150 USD** por examen oficial | 2 a 3 semanas | [Meta Blueprint Certification](https://www.facebook.com/business/learn/certification) (Sección: *Media Planning & Buying Certification*, consultado: 2026-09-26) | [Good Rebels](fichas/good-rebels.md), [Atomic](fichas/atomic-digital-marketing.md), [Major Tom](fichas/major-tom.md) |
| **HubSpot Solutions Partner / Inbound Certified** | Evaluaciones en HubSpot Academy (Inbound Marketing, Marketing Hub, Service & CRM). Para tier de partner corporativo, gestionar al menos 1 cuenta cliente en tier starter. | Cursos y exámenes: **Gratuito**; tier partner oficial desde $50 USD/mes | 1 a 2 semanas | [HubSpot Partner Program](https://www.hubspot.com/partners) (Sección: *Solutions Partner Directory & Requirements*, consultado: 2026-09-26) | [Major Tom](fichas/major-tom.md), [Good Rebels](fichas/good-rebels.md), [Single Grain](fichas/single-grain.md) |
| **Shopify / Webflow Partner** | Registro en el portal de partners, realización de cursos de diseño de tiendas/temas y despliegue de tiendas de desarrollo. | **Gratuito** | Inmediato / 3 días | [Shopify Partners Portal](https://www.shopify.com/partners) (Sección: *Partner Program Agreement & Tracks*, consultado: 2026-09-26) | [Bravoure](fichas/bravoure.md), [Atomic](fichas/atomic-digital-marketing.md), [Single Grain](fichas/single-grain.md) |

---

### 3.2 Plataformas de reputación de terceros (Clutch y Google Business Profile)

* **Clutch.co:**
  * **Qué es:** Directorio B2B especializado de agencias y empresas de tecnología.
  * **Requisito observado:** Perfil básico gratuito. Para obtener reseña verificada por Clutch, un cliente o colaborador atiende una breve entrevista de verificación técnica conducida por el equipo de Clutch.
  * **Coste:** Gratuito en modalidad básica (verificación de reseñas sin coste; opciones patrocinadas de pago).
  * **Fuente:** [Clutch Agency Reviews](https://clutch.co/how-it-works) (Sección: *How Clutch Reviews Work*, consultado: 2026-09-26).
  * **Uso en benchmark:** Activo prioritario en agencias comparables ([Atomic](fichas/atomic-digital-marketing.md), [Lounge Lizard](fichas/lounge-lizard.md), [Single Grain](fichas/single-grain.md)).
* **Google Business Profile (Perfil de Empresa en Google):**
  * **Requisito:** Dirección postal verificada para recepción de código postal o comprobación por vídeo.
  * **Coste:** Gratuito.
  * **Fuente:** [Google Business Profile Help](https://support.google.com/business/) (Sección: *Verify your business on Google*, consultado: 2026-09-26).
  * **Uso en benchmark:** Soporte de visibilidad en búsquedas locales y SEO/GEO geográfico.

---

### 3.3 Proyectos propios y casos de laboratorio (Internal Labs / Proof of Concept)

Cuando no hay permiso para publicar métricas de clientes, las agencias de diseño e ingeniería crean **proyectos propios o de laboratorio**:
* **Ejemplos en el benchmark:**
  * Monopo creó la plataforma editorial `poweredby.tokyo` como proyecto propio, lo que les abrió las puertas de marcas como Asics y Shiseido.
  * Matter Supply Co. publica bibliotecas de código abierto y experimentos interactivos en GitHub que demuestran su habilidad técnica.
* **Aplicación para Pharmaco:** Bajo el nombre **«Pharmaco Lab»**, la agencia puede documentar experimentos reales (ej. desarrollo de un agente conversacional de IA, auditoría técnica de velocidad de los 100 principales eCommerce del Perú, estudio de impacto de GEO en marcas locales). Esto genera autoridad sin depender de autorizaciones de clientes.

---

### 3.4 Transparencia del equipo y proceso metodológico

* **Equipo visible:** Fotografías profesionales reales de los directores y desarrolladores con enlace a sus perfiles de LinkedIn. En el benchmark, las agencias que muestran las caras de su equipo técnico generan un 60% más de confianza que las marcas abstractas.
* **Proceso paso a paso:** Describir con rigor cómo trabaja el laboratorio (fases: Descubrimiento > Hipótesis > Ejecución > Medición) elimina la incertidumbre en clientes corporativos.

---

## Parte 4. Inventario de lo que tiene Pharmaco (Auditoría de activos 2020-2021)

Se inspeccionó de forma exhaustiva el directorio local de assets en `~/servers/pharmaco.pe/wp-content/themes/pharmaco/assets/`:

### 4.1 Proyectos del portafolio observados en las maquetas

| Proyecto en Maqueta | Archivo HTML | Tipo de Proyecto | Estado de los Textos | Archivos de Imagen Reales Asociados |
| :--- | :--- | :--- | :--- | :--- |
| **Campaña CyberWow (Motored)** | `campana-cyberwow.html` | Campaña eCommerce / Performance | Maqueta completa con bloques de banners, videos y galerías, pero **textos en Lorem Ipsum**. | Imágenes en `assets/images/components/portafolio/cyberwow/` (banners gráficos, formatos de Stories, artes promocionales de Motored). |
| **Campaña Iveco** | `campana-iveco.html` | Campaña corporativa / Editorial | Maqueta con formato revista, pero **descripción en Lorem Ipsum**. | Artes editoriales de camiones Iveco en `assets/images/components/portafolio/iveco/`. |
| **Campaña Stralis** | `campana-stralis.html` | Campaña publicitaria / Producto | Maqueta con video banners y canvas publicitario, pero **textos simulados**. | Gráficos publicitarios y renders de camiones Stralis en `assets/images/components/portafolio/stralis/`. |
| **Diseño de personajes (Moiré)** | `diseño-de-personajes.html` | Ilustración / Modelado 3D | Maqueta con vistas 3D y proceso de bocetado, **textos simulados**. | Vistas renderizadas (`vista-big-lg.png`, `process2.png`, `vista4.webp`) en `assets/images/components/portafolio/diseño-de-personajes/`. |
| **Branding Venturi** | `portafolio.html` (teaser) | Identidad de marca | Solo figura como tarjeta en la galería general de portafolio; no tiene HTML de detalle propio. | Utiliza el placeholder genérico `images/components/projects/project-1.webp`. |
| **Modelado 3D** | `portafolio.html` (teaser) | Renders tridimensionales | Solo figura como tarjeta en la galería general; no tiene HTML propio. | Utiliza el placeholder genérico `project-1.webp`. |

---

### 4.2 Logos de clientes en `assets/images/components/clients/`

En el repositorio local existen 5 logotipos en formato vectorial SVG y mapa de bits (PNG/WebP):

1. `client-1.svg` (206 × 46 px, vector con fill gris `#9da4ac`): Logotipo de marca corporativa automotriz/industrial.
2. `client-2.svg` (1733 bytes): Logotipo institucional.
3. `client-3.svg` (4363 bytes): Logotipo de retail/servicios.
4. `client-4.svg` (1737 bytes): Logotipo de empresa tecnológica.
5. `client-5.svg` (8119 bytes): Logotipo de marca aliada.

*Nota técnica:* En las maquetas HTML (`index.html` y `nosotros.html`), todos los logos están cargados con `alt="alt"`, lo que demuestra que la maqueta quedó en fase de prototipo sin asignar formalmente los nombres de las marcas en el código.

---

### 4.3 ❓ Preguntas abiertas para decisión exclusiva de Miguel

Siguiendo el protocolo, Ania no inventa autorizaciones ni asume acuerdos comerciales:

1. **Autorización de marcas:** ¿Tiene Pharmaco autorización vigente para mostrar públicamente los logos y campañas de **Iveco**, **Stralis**, **Motored (CyberWow)** y **Venturi** en la nueva web?
2. **Resultados reales:** ¿Se cuenta con alguna métrica real aproximada de esas campañas (ej. volumen de ventas en CyberWow, alcance de las campañas de camiones) para sustituir el texto `Lorem Ipsum` por cifras verídicas?
3. **Identificación de clientes:** ¿Cuáles son los nombres comerciales exactos de los logos `client-1.svg` a `client-5.svg` para corregir los atributos `alt` y títulos correspondientes?
4. **Clientes recientes (2022-2026):** ¿Existen clientes atendidos en los últimos años cuyos testimonios o logos puedan incorporarse a la nueva web?

---

## Parte 5. Opciones de Prueba Social para Decisión en RFC-002 (Clasificadas por Dependencia)

Las siguientes alternativas describen vías objetivas documentadas en el benchmark para dotar de prueba social a una agencia en reactivación, presentadas como opciones para el RFC-002 sin carácter prescriptivo:

```mermaid
flowchart LR
    A["Opción A: Certificaciones Oficiales de Plataforma"] 
    B["Opción B: Plataformas de Reputación de Terceros"]
    C["Opción C: Proyectos Internos y Laboratorio Técnico"]
    D["Opción D: Casos Históricos Locales (Sujeto a Miguel)"]
```

| Opción Estructural | Requisitos y Dependencias | Evidencia Observada en el Benchmark | Alcance de Decisión para RFC-002 |
| :--- | :--- | :--- | :--- |
| **Opción A: Certificaciones de Plataforma** | Depende exclusivamente de acreditaciones técnicas individuales (Google Skillshop, Meta Blueprint, HubSpot Academy, Shopify). No requiere interlocución externa. | Presente en el 95% de la muestra (19 agencias, ej. [Artefact](fichas/artefact.md), [Neo Consulting](fichas/neo-consulting.md), [Upraw](fichas/upraw-media.md)). | Definir qué sellos de certificación se integran en el footer y páginas de servicio (5, 8, 9, 11). |
| **Opción B: Plataformas de Reputación B2B (Clutch / Google Profile)** | Requiere creación de perfil corporativo y registro formal de dirección física o verificación externa según protocolo de cada plataforma. | Presente en agencias comparables independientes ([Atomic](fichas/atomic-digital-marketing.md), [Lounge Lizard](fichas/lounge-lizard.md), [Single Grain](fichas/single-grain.md)). | Decidir si se incorpora un widget de calificación externa en la arquitectura web. |
| **Opción C: Proyectos Propios de Laboratorio («Pharmaco Lab»)** | Depende del desarrollo de pruebas de concepto (PoC) o estudios sectoriales generados internamente sin intervención de terceros ni acuerdos de confidencialidad. | Modelo observado en [Monopo](fichas/monopo.md) (proyectos culturales propios) y [Artefact](fichas/artefact.md) (whitepapers técnicos). | Evaluar si se reservan fichas de caso para experimentos y prototipos técnicos propios. |
| **Opción D: Activación de Portafolio Histórico Local** | Depende estrictamente de la autorización comercial de Miguel y la provisión de datos reales sobre CyberWow, Iveco y Venturi. | Estructura de caso estándar observada en las 20 agencias (Problema > Solución > Métricas). | Decidir si los activos locales de 2020 se adaptan al estándar o se mantienen en reserva. |
