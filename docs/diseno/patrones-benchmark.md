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
  * En agencias comparables (Good Rebels, Major Tom, Lounge Lizard): Menú sticky superior con botón destacado de CTA permanente («Let's talk» o «Free audit»).
  * En agencias referentes de diseño (Fantasy, Monopo, Work & Co): Navegación minimalista con menú hamburguesa o barra inferior flotante para maximizar el espacio de visualización de interfaces y videos.

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

* **Predominio Sans-Serif Neogrotesca:** 17 de 20 agencias utilizan tipografías de palo seco geométricas o grotescas (estilos similares a *Inter, Neue Haas Grotesk, PP Neue Montreal, Circular, Poppins*).
* **Jerarquía de contraste extremo:**
  * Titulares masivos en Hero: entre `64px` y `110px` en escritorio, con `line-height` muy apretado (`1.0` a `1.1`).
  * Textos de párrafo limpios: `16px` a `18px`, con generoso interlineado (`1.5` a `1.6`) para máxima legibilidad.
* **Toque editorial en títulos:** 3 agencias referentes (Code and Theory, Monopo) introducen tipografías serif contemporáneas de alto contraste en titulares editoriales para transmitir sofisticación y pensamiento estratégico.

### 2.2 Color y contraste

* **Modo Oscuro como estándar de impacto:**
  * 12 de las 20 agencias (60%) utilizan fondos oscuros profundos (`#000000`, `#0a0a0a`, `#111029`) en su home o en sus casos de estudio para hacer resaltar el color de las imágenes y videos.
  * 8 agencias (40%) apuestan por un fondo blanco puro (`#ffffff`) o gris muy claro (`#f8f9fa`) estilo suizo minimalista.
* **Uso del color de acento:** Las agencias modernas evitan paletas sobrecargadas. Utilizan blanco y negro como base, reservando un **único color de acento vibrante** (ej. amarillo lima, azul eléctrico, morado tecnológico) exclusivamente para botones interactivos, estados hover y badges de estado.

### 2.3 Uso de fotografía y video (Especial relevancia para el Servicio 7)

* **El video como rey de la portada:** 14 de las 20 agencias (70%) tienen un **showreel de video en loop continuo sin sonido en la cabecera**. Esto comunica dinamismo inmediato.
* **Cero fotos de stock:** Ninguna agencia del benchmark utiliza fotografía de stock genérica. Se utiliza:
  1. Fotografía documental auténtica del equipo en su espacio de trabajo.
  2. Renders y capturas reales de producto digital e interfaces en dispositivos reales.
  3. Video comercial en alta definición de las campañas producidas.

### 2.4 Movimiento e interacción

* **Animaciones al scroll (Scroll-driven animations):** 18 de las 20 agencias incorporan transiciones suaves de opacidad y desplazamiento al hacer scroll.
* **Microinteracciones en cursores:** Efectos de cursor magnético que se expande al pasar sobre enlaces o que muestra un badge de «Ver caso» o «Play» sobre videos.
* **Rendimiento ante todo:** A diferencia de 2020 donde proliferaban librerías pesadas, las agencias en 2026 priorizan animaciones aceleradas por hardware vía CSS `transform` y `opacity`, garantizando 60 fps en móviles.

---

## 3. Tabla de contraste: Web de assets (Pharmaco 2020-2021) vs. Benchmark 2026

Comparación analítica entre lo que tiene construido Pharmaco en sus maquetas locales ([`sistema-web-assets.md`](sistema-web-assets.md)) y los estándares detectados en las agencias de referencia internacional:

| Patrón de Diseño / Arquitectura | Web de Assets de Pharmaco (2020-2021) | Benchmark Internacional (2026) | Veredicto / Estado para Pharmaco |
| :--- | :--- | :--- | :--- |
| **Arquitectura de Maquetación** | BEM modular con `inuitcss`, capas bien estructuradas (`generic`, `objects`, `components`, `utilities`). | CSS modular, CSS variables nativas, Tailwind o arquitecturas de componentes modernas. | ✅ **Vigente y reutilizable.** La base BEM de Pharmaco es sólida y técnicamente limpia. |
| **Tipografía Base** | `Poppins` en 5 pesos (400 a 800) servida localmente en WOFF2. | Familias grotescas geométricas (*Inter*, *Montreal*, *Poppins*) en pesos bold y regular. | ✅ **Vigente.** `Poppins` sigue siendo moderna, legible y está bien implementada localmente. |
| **Escala Tipográfica** | Títulos de sección a 35px/40px. Hero grande a 77px/84px. | Titulares de impacto de 80px a 110px en escritorio con espaciado compacto. | 🟡 **Actualizar ligeramente.** El Hero actual funciona, pero los títulos intermedios necesitan mayor diferenciación jerárquica. |
| **Paleta de Colores** | Morado primario (`#5956e9`), Azul tech (`#4c40f7`), Fondo oscuro (`#111029`), Acento amarillo (`#ffd027`). | Blanco/negro de base con un acento vibrante (morado o azul eléctrico). Fondos oscuros en casos. | ✅ **Vigente.** La combinación de `#5956e9` y fondo oscuro `#111029` encaja perfectamente con la tendencia tecnológica actual. |
| **Hero de Portada** | Estático con ilustración/fotografía lateral y textos fijos (`c-hero--home`). | Video showreel en autoplay o fondo dinámico inmersivo a ancho completo. | ❌ **Desfasado.** La home de Pharmaco requiere incorporar video/motion en su Hero para reflejar el Servicio 7 (Foto y Video). |
| **Estructura de Servicios** | Lista estática de tarjetas con textos repetidos y sin despiece de entregables. | Páginas con tabs interactivos, despiece de metodología, herramientas usadas y casos vinculados. | ❌ **Desfasado.** Las páginas de servicio de Pharmaco deben reestructurarse con la anatomía moderna documentada en TASK-002. |
| **Prueba Social en Home** | Carrusel con 5 logos en SVG planos con `alt="alt"` y tarjetas de proyectos en `Lorem ipsum`. | Logos en escala de grises al 50% de opacidad, badges de Clutch/Google, métricas cuantitativas (+X%). | ❌ **Desfasado.** Se debe sustituir el slider estático por un módulo de confianza con métricas y acreditaciones reales. |
| **Casos de Estudio** | Maquetas ricas en CyberWow, Iveco y Stralis, pero sin métricas y con texto simulado. | Ficha estructurada en Reto > Solución > Métricas (+X% ROAS) > Testimonio del cliente. | 🟡 **Parcialmente aprovechable.** El diseño visual de los módulos de portafolio es excelente, pero falta la narrativa de negocio y resultados. |
| **Formularios de Contacto** | Formulario completo (`.c-contact-form`) con validaciones y campos de presupuesto y radios. | Formularios breves tipo multi-step o enlaces directos a reserva de llamada (Cal.com / Calendly). | ✅ **Vigente con optimización.** El formulario de Pharmaco es muy completo; convendría añadir la opción de agendar videollamada directa. |
| **Librerías de Animación** | `AOS` (Animate On Scroll v2.3.4) y `tiny-slider`. | Animaciones CSS nativas o bibliotecas ligeras sin dependencias. | ✅ **Vigente.** `AOS` y `tiny-slider` son ligeras, robustas y funcionan sin problemas de rendimiento. |

---

## 4. Conclusiones para la Redacción de `RFC-002`

1. **Lo que Pharmaco debe conservar:**
   * La arquitectura CSS con metodología BEM y preprocesador SCSS.
   * La paleta corporativa basada en el morado `#5956e9` y el fondo noche `#111029`.
   * La tipografía `Poppins` alojada localmente.
   * El sistema de iconos SVG sprites.
2. **Lo que Pharmaco debe transformar:**
   * El Hero estático de la home debe evolucionar hacia un formato audiovisual (aprovechando la incorporación del servicio de Fotografía y Video).
   * La página de Servicios debe abandonar los textos genéricos e implementar la estructura canónica descubierta en el benchmark (Problema > Metodología > Entregables > Herramientas > Casos > CTA).
   * El portafolio debe abandonar el enfoque de "galería de fotos" para convertirse en estudios de caso estructurados orientados a resolver problemas de negocio.
