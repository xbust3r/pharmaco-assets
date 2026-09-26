# 📐 Patrones de diseño del benchmark y contraste con la web de assets (TASK-004 Parte B)

> **Documento:** `docs/diseno/patrones-benchmark.md` · **Tarea:** [TASK-004](../comms/TASK-004-sistema-de-diseno.md) (Parte B)
> **Autora:** Ania (DEV principal) · **Fecha:** 2026-09-26
> **Muestra cruzada:** 20 agencias internacionales de [TASK-001](../comms/TASK-001-investigacion-benchmark-agencias.md) contrastadas contra [docs/diseno/sistema-web-assets.md](sistema-web-assets.md).
> **Estado:** Documentación técnica completa de arquitectura, patrones visuales y contraste analítico.

---

## 1. Arquitectura de información en el benchmark

Del análisis sistemático de las 20 agencias de Europa y América se extraen las siguientes estructuras de arquitectura web consolidadas:

### 1.1 Menú principal y navegación

* **Estructura típica (18 de 20 agencias):**
  * Entre 4 y 6 ítems principales: `Work` (Proyectos / Casos), `Services` (Capacidades / Soluciones), `About` (Nosotros / Agencia), `Insights` (Blog / Ideas / Noticias), `Contact` (Contacto).
  * En agencias comparables (Good Rebels, Major Tom, Lounge Lizard, Brolik): Menú sticky superior con botón destacado de CTA permanente («Let's talk» o «Get proposal»).
  * En agencias referentes de diseño (Dogstudio, Monopo, Work & Co): Navegación minimalista con enlaces directos o menú lateral flotante para maximizar el espacio de visualización de interfaces y videos.

### 1.2 Orden canónico de las secciones de la Home

A través de las 20 agencias se detecta un patrón de embudo claro en la página de inicio:

```text
1. Hero de Impacto
   ├── Titular con propuesta de valor / posicionamiento de marca (3 a 8 palabras)
   ├── Subtítulo de 1 a 2 líneas clarificando el beneficio para el cliente
   └── Fondo interactivo (Showreel en video loop o visual generativo 3D/WebGL)
2. Cinta de Prueba Social Inmediata (Social Proof Strip)
   └── Logos en escala de grises de clientes conocidos o cifras clave agregadas («Impact stats»)
3. Casos de Estudio Destacados (Featured Work)
   └── 3 a 5 tarjetas de proyectos a gran tamaño (ocupan el 50% al 100% del ancho) con video preview
4. Bloque de Pilares / Servicios (Capabilities Overview)
   └── 3 a 4 pilares estratégicos con lista desplegable de subservicios o links a detalle
5. Manifiesto / Sobre Nosotros (About / Culture Teaser)
   └── Fotografía del equipo o declaración de valores y metodología de trabajo
6. Contenido Experto / Insights (Blog, Podcasts, Research)
   └── 2 o 3 artículos recientes demostrando liderazgo de pensamiento
7. Sección de Conversión Final (Contact Footer)
   └── Formulario directo de inicio de proyecto o agenda de videollamada
```

---

## 2. Patrones visuales observados en el benchmark

### 2.1 Tipografía

* **Predominio Sans-Serif Neogrotesca:** 18 de 20 agencias (90%) utilizan tipografías de palo seco geométricas o grotescas (estilos similares a *Inter, Neue Haas Grotesk, PP Neue Montreal, Circular, Poppins*). Evidencia trazable en fichas: [Bravoure](../investigacion/fichas/bravoure.md), [Brolik](../investigacion/fichas/brolik.md), [Dogstudio](../investigacion/fichas/dogstudio.md), [Edenspiekermann](../investigacion/fichas/edenspiekermann.md), [Instrument](../investigacion/fichas/instrument.md), [Work & Co](../investigacion/fichas/work-and-co.md) (ver capturas: [`capturas/bravoure-home.png`](../investigacion/capturas/bravoure-home.png), [`capturas/brolik-home.png`](../investigacion/capturas/brolik-home.png)).
* **Jerarquía de contraste extremo:**
  * Titulares masivos en Hero: entre `64px` y `110px` en escritorio, con `line-height` muy apretado (`1.0` a `1.1`).
  * Textos de párrafo limpios: `16px` a `18px`, con generoso interlineado (`1.5` a `1.6`) para legibilidad.
* **Toque editorial en títulos:** Agencias referentes ([Code and Theory](../investigacion/fichas/code-and-theory.md), [Monopo](../investigacion/fichas/monopo.md), [Edenspiekermann](../investigacion/fichas/edenspiekermann.md)) introducen tipografías serif contemporáneas de alto contraste en titulares editoriales (ver captura: [`capturas/monopo-home.png`](../investigacion/capturas/monopo-home.png)).

### 2.2 Color y contraste

* **Distribución de fondos y modo:**
  * 11 de las 20 agencias (55%) utilizan fondos oscuros profundos (`#000000`, `#0a0a0a`, `#111029`) en su home o en sus casos de estudio ([Dogstudio](../investigacion/fichas/dogstudio.md), [Bravoure](../investigacion/fichas/bravoure.md), [BlueOrange](../investigacion/fichas/blueorange-digital.md), [Instrument](../investigacion/fichas/instrument.md), [Code and Theory](../investigacion/fichas/code-and-theory.md), [Neo Consulting](../investigacion/fichas/neo-consulting.md); capturas: [`capturas/bravoure-home.png`](../investigacion/capturas/bravoure-home.png), [`capturas/dogstudio-home.png`](../investigacion/capturas/dogstudio-home.png)).
  * 9 agencias (45%) apuestan por un fondo blanco puro (`#ffffff`) o neutro muy claro ([Good Rebels](../investigacion/fichas/good-rebels.md), [Edenspiekermann](../investigacion/fichas/edenspiekermann.md), [Upraw Media](../investigacion/fichas/upraw-media.md), [Brolik](../investigacion/fichas/brolik.md), [Major Tom](../investigacion/fichas/major-tom.md), [Lounge Lizard](../investigacion/fichas/lounge-lizard.md), [Work & Co](../investigacion/fichas/work-and-co.md); capturas: [`capturas/brolik-home.png`](../investigacion/capturas/brolik-home.png), [`capturas/upraw-media-home.png`](../investigacion/capturas/upraw-media-home.png)).
* **Uso del color de acento:** Las agencias modernas evitan paletas sobrecargadas. Utilizan blanco y negro como base, reservando un **único color de acento vibrante** (ej. amarillo lima, azul eléctrico, morado tecnológico) para botones interactivos, estados hover y badges de estado.

### 2.3 Uso de fotografía y video (Especial relevancia para el Servicio 7)

* **El video como recurso de portada:** 13 de las 20 agencias (65%) tienen **clips de video en loop o animaciones interactivas continuas en la cabecera** ([Monopo](../investigacion/fichas/monopo.md), [Media.Monks](../investigacion/fichas/media-monks.md), [Dogstudio](../investigacion/fichas/dogstudio.md), [Bravoure](../investigacion/fichas/bravoure.md); capturas: [`capturas/monopo-home.png`](../investigacion/capturas/monopo-home.png), [`capturas/media-monks-home.png`](../investigacion/capturas/media-monks-home.png)).
* **Tratamiento de imágenes reales:** Ninguna agencia del benchmark utiliza fotografía de stock genérica. Se observa:
  1. Fotografía documental auténtica del equipo en su espacio de trabajo.
  2. Renders y capturas reales de producto digital e interfaces en dispositivos reales.
  3. Video comercial en alta definición de las campañas producidas.

### 2.4 Movimiento e interacción

* **Animaciones al scroll (Scroll-driven animations):** 17 de las 20 agencias incorporan transiciones suaves de opacidad y desplazamiento al hacer scroll ([Dogstudio](../investigacion/fichas/dogstudio.md), [Bravoure](../investigacion/fichas/bravoure.md), [Instrument](../investigacion/fichas/instrument.md)).
* **Microinteracciones en cursores:** Efectos de cursor magnético o badges contextuales sobre videos.
* **Optimización técnica:** Priorización de animaciones CSS aceleradas por hardware vía `transform` y `opacity`.

---

## 3. Tabla de contraste: Web de assets (Pharmaco 2020-2021) vs. Benchmark 2026

Comparación analítica neutral entre los elementos existentes en las maquetas locales ([`sistema-web-assets.md`](sistema-web-assets.md)) y los patrones observados en el benchmark internacional, para servir de evidencia objetiva a las decisiones de `RFC-002`:

| Elemento / Dimensión | Web de Assets de Pharmaco (2020-2021) | Benchmark Internacional (2026) | Opciones Observadas para RFC-002 |
| :--- | :--- | :--- | :--- |
| **Arquitectura CSS** | BEM modular con `inuitcss`, capas (`generic`, `objects`, `components`, `utilities`). | CSS modular, CSS variables nativas o utilitarios modernos. | **Opción A:** Reutilizar la arquitectura BEM existente.<br>**Opción B:** Migrar a CSS variables nativas o utilidades. |
| **Tipografía Base** | `Poppins` en 5 pesos (400 a 800) servida localmente en WOFF2. | Familias grotescas geométricas (*Inter*, *Montreal*, *Poppins*) en pesos bold y regular. | **Opción A:** Conservar `Poppins` local.<br>**Opción B:** Explorar fuentes del sistema o variables neogrotescas. |
| **Escala Tipográfica** | Títulos de sección a 35px/40px. Hero a 77px/84px. | Titulares de impacto de 80px a 110px en escritorio con interlineado compacto. | **Opción A:** Mantener escala 2020.<br>**Opción B:** Aumentar escala del Hero y jerarquía de contraste. |
| **Paleta de Colores** | Morado primario (`#5956e9`), Azul tech (`#4c40f7`), Fondo oscuro (`#111029`), Acento amarillo (`#ffd027`). | Blanco/negro de base con un único acento vibrante. Fondos oscuros presentes en 55% de la muestra. | **Opción A:** Conservar paleta morado/noche.<br>**Opción B:** Simplificar a base monocromática con un solo acento. |
| **Hero de Portada** | Estático con ilustración/fotografía lateral y textos fijos (`c-hero--home`). | Video showreel en loop o animaciones interactivas continuas (65% de la muestra). | **Opción A:** Mantener Hero estático.<br>**Opción B:** Incorporar módulo de video en loop vinculado al Servicio 7. |
| **Estructura de Servicios** | Lista estática de tarjetas con textos genéricos y sin entregables específicos. | Páginas con tabs interactivos, metodología, herramientas y casos vinculados. | **Opción A:** Mantener formato tarjeta.<br>**Opción B:** Adoptar la anatomía canónica observada en TASK-002. |
| **Prueba Social en Home** | Carrusel con 5 logos en SVG planos con `alt="alt"` y tarjetas de proyectos en `Lorem ipsum`. | Logos en escala de grises al 50%, badges de Clutch/Google, métricas cuantitativas (+X%). | **Opción A:** Conservar slider de logos plano.<br>**Opción B:** Reestructurar módulo de confianza con métricas y acreditaciones. |
| **Casos de Estudio** | Maquetas completas (CyberWow, Iveco, Stralis), con textos simulados y sin métricas de negocio. | Ficha estructurada en Reto > Solución > Métricas (+X%) > Testimonio. | **Opción A:** Galería visual orientada a diseño.<br>**Opción B:** Caso de estudio estructurado con impacto de negocio. |
| **Formularios de Contacto** | Formulario completo (`.c-contact-form`) con validaciones y selector de presupuesto. | Formularios breves o enlaces a reserva de reunión directa (Cal.com / Calendly). | **Opción A:** Mantener formulario nativo.<br>**Opción B:** Integrar opción híbrida de reserva de calendario. |
| **Librerías de Animación** | `AOS` (Animate On Scroll) y `tiny-slider`. | Animaciones CSS nativas o bibliotecas ligeras sin dependencias. | **Opción A:** Reutilizar AOS y tiny-slider.<br>**Opción B:** Reemplazar por animaciones CSS nativas al scroll. |

---

## 4. Alternativas de Decisión para la Redacción de `RFC-002`

A partir de la evidencia analizada, se identifican las siguientes alternativas estructurales para consideración de Clia y Miguel en el `RFC-002`:

1. **Enfoque de Continuidad Técnica (Aprovechamiento de Assets 2020):**
   * Preservar la arquitectura BEM (`inuitcss`), la tipografía `Poppins` y la paleta `#5956e9` / `#111029`.
   * Actualizar el contenido de los bloques existentes con los textos reales de los 11 servicios y la prueba social disponible.
2. **Enfoque de Renovación Estructural (Alineamiento con Benchmark 2026):**
   * Evolucionar el Hero hacia un formato con soporte de video showreel (alineado con la incorporación del servicio de Fotografía y Video).
   * Reestructurar las páginas de servicio y de caso según la anatomía modular documentada en TASK-002 y TASK-003.
   * Modernizar el sistema de animación hacia propiedades nativas CSS con aceleración gráfica.
