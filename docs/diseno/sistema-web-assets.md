# 🎨 Sistema de diseño — Web de assets (Pharmaco 2020-2021)

> **Documento:** `docs/diseno/sistema-web-assets.md` · **Tarea:** [TASK-004](../comms/TASK-004-sistema-de-diseno.md) (Parte A)
> **Autora:** Ania (DEV principal) · **Fecha:** 2026-09-26
> **Fuente:** Archivos locales en `assets/` y tema WordPress `pharmaco` (`main.css`, `main.css.map`, 10 maquetas HTML, bloques ACF).
> **Estado:** Documentación técnica completa extraída del código real.

---

## 1. Tokens de diseño (extraídos del CSS real)

Los valores fueron extraídos directamente de `assets/css/main.css` y verificados contra los 61 archivos SCSS recuperados de `main.css.map`.

### 1.1 Paleta de colores

| Token SCSS / Variable | Hexadecimal | RGB | Rol / Dónde se usa en el código |
| :--- | :--- | :--- | :--- |
| `$color-purple` | `#5956e9` | rgb(89, 86, 233) | **Color primario de marca**. Botones principales (`.c-button--purple`), subtítulos de sección (`.c-section__subtitle--purple`), enlaces activos, acentos interactivos. |
| `$color-dark-purple` | `#4d30a0` / `#3a30a0` | rgb(77, 48, 160) | Variante profunda de morado. Fondos de botones hover, títulos secundarios. |
| `$color-blue` | `#4c40f7` / `#433fe6` | rgb(76, 64, 247) | **Acento digital / tech**. Títulos de sección (`.c-section__title--blue`), estados hover, línea de breadcrumbs activos. |
| `$color-sky-blue` | `#b8defa` | rgb(184, 222, 250) | Botón celeste suave (`.c-button--sky-blue`), etiquetas secundarias. |
| `$color-dark-blue` | `#00113b` | rgb(0, 17, 59) | Azul noche profundo. Textos de alto contraste sobre celeste, pie de sección de contacto (`box-shadow: 0 -48px 0 0 #00113b inset`). |
| `$color-background-dark` | `#111029` | rgb(17, 16, 41) | **Fondo oscuro institucional**. Cabecera colapsada, overlays de navegación móvil, fondos de contrastes altos. |
| `$color-yellow` / `$color-accent` | `#ffd027` | rgb(255, 208, 39) | **Acento de atención / interactividad**. Outline de foco en formularios (`box-shadow: 0 0 0 2px #ffd027`), checks y radios activos. |
| `$color-red` / `$color-error` | `#be0000` | rgb(190, 0, 0) | Mensajes de error y validación de campos (`.c-contact-form__error`). |
| `$color-gray-dark` | `#2f2f2f` | rgb(47, 47, 47) | Títulos principales en modo claro y textos de titulares pesados. |
| `$color-gray-body` | `#6b6b6b` / `#6e7177` | rgb(107, 107, 107) | **Texto base de lectura (párrafos)**, subtítulos atenuados, descripciones. |
| `$color-gray-muted` | `#a7a7a7` / `#9da4ac` | rgb(157, 164, 172) | Iconos secundarios (`.o-icon`), bordes de inputs inactivos, placeholders. |
| `$color-gray-light` | `#eaeaeb` / `#f4f4f4` | rgb(244, 244, 244) | Fondos de sección alternos (`.c-section--gray`), chips de categorías (`.c-section__tag`). |
| `$color-white` | `#ffffff` | rgb(255, 255, 255) | Fondos principales, texto sobre botones primarios, tarjetas. |

---

### 1.2 Tipografía y escala tipográfica

* **Familia principal:** `Poppins, Arial, Helvetica, sans-serif`
  * Archivos locales en `assets/fonts/`:
    * `Poppins-Regular` (400)
    * `Poppins-Medium` (500)
    * `Poppins-SemiBold` (600)
    * `Poppins-Bold` (700)
    * `Poppins-ExtraBold` (800)
* **Texto monoespaciado:** `monospace, monospace` (reseteo genérico del navegador)

#### Escala tipográfica observada en CSS:

| Nivel / Clase | Tamaño Móvil (Base) | Tamaño Escritorio (`>= 980px`) | Line-Height | Peso | Uso |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hero Display / Subtitle Big** | `35px` | `84px` / `77px` | `1.048` | Bold (700) / 800 | Titulares de impacto en Hero y cabeceras de servicio |
| **Subtitle Section** | `24px` | `40px` | `1.16` | SemiBold (600) | Subtítulo principal de secciones |
| **H2 / Section Title Pre** | `16px` | `20px` | `1.2` | Medium (500) | Kicker / Pre-título azul de sección (`.c-section__title`) |
| **Subtitle Small Light** | `18px` | `22px` | `1.3` | Regular (400) | Bajadas descriptivas de héroes |
| **Botón Grande** | `14px` | `20px` (altura 72px) | `1.2` | Medium (500) | CTA principal en Hero |
| **Botón Estándar** | `14px` | `18px` (altura 64px) | `1.2` | Medium (500) | Botones en tarjetas y footer |
| **Texto Párrafo Principal** | `14px` | `16px` | `1.46` - `1.56` | Regular (400) | Párrafos generales de lectura |
| **Breadcrumbs / Meta** | `12px` | `14px` | `1.2` | Regular (400) | Migas de pan y metadatos |
| **Tag / Badge** | `9px` | `11px` | `1.0` | SemiBold (600) | Chips de categoría en portafolio |

---

### 1.3 Breakpoints y Sistema de Grid

Implementado con la librería **`sass-mq`** sobre un ancho base de `16px`:

| Nombre MQ | Medida en `em` | Medida en `px` | Comportamiento |
| :--- | :--- | :--- | :--- |
| `mobile-small` | `22.5em` | `360px` | Ajuste para pantallas pequeñas de smartphones |
| `mobile-mid` | `26.5625em` | `425px` | Smartphones medianos/grandes |
| `mobile-wide` | `31.25em` | `500px` | Teléfonos grandes / Phablets |
| `tablet` | `43.75em` | `700px` | Quiebre a columnas dobles en tarjetas y grid de servicios |
| `desktop` | `61.25em` | `980px` | Menú completo visible, layout multi-columna, héroes horizontales |
| `wide` | `75.0em` | `1200px` | Ancho del contenedor principal (`.o-wrapper` máx. 1200px) |
| `ultrawide` | `87.5em` | `1400px` | Padding expandido en pantallas panorámicas |

---

### 1.4 Radios y Sombras

* **Border Radius:**
  * Botones estándar: `border-radius: 15px` (móvil) → `20px` (escritorio).
  * Botones circulares / Controles de slider: `border-radius: 50%` (38px × 38px).
  * Tarjetas de servicio / proyecto: `border-radius: 16px` (móvil) → `28px` (escritorio).
  * Contenedor de formulario de contacto: `border-radius: 18px` a `24px`.
  * Inputs / Form controls: `border-radius: 10px` a `12px`.
  * Pills / Tags de categoría: `border-radius: 40px`.
* **Box Shadows:**
  * Sombra base de elevación: `box-shadow: 4px 5px 13px rgba(0, 0, 0, 0.08)`.
  * Sombra de hover en botones: `box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2)`.
  * Sombra de tarjetas / banners: `box-shadow: 6px 10px 24px rgba(0, 0, 0, 0.1)`.
  * Acento de selección / Focus ring: `box-shadow: 0 0 0 2px #ffd027`.

---

## 2. Inventario de Componentes BEM

Los componentes siguen la convención BEM estricta con prefijos de arquitecturas CSS (`c-` para componente, `o-` para objeto, `s-` para scope):

| Componente | Clase BEM Principal | Elementos Clave | Modificadores Observados | Capturas Asociadas |
| :--- | :--- | :--- | :--- | :--- |
| **Cabecera del sitio** | `.c-site-header` | `__logo`, `__controls`, `__hamburger` | `--fixed`, `--transparent` | `capturas/home-desktop.png`, `capturas/home-mobile-375px.png` |
| **Navegación principal** | `.c-site-header-nav` | `__list`, `__item`, `__link`, `__close` | `.is-active`, `.is-open` | `capturas/home-desktop.png`, `capturas/home-mobile-375px.png` |
| **Overlay modal** | `.c-overlay` | — | `.is-visible` | — |
| **Héroe de página** | `.c-hero` | `__title`, `__subtitle`, `__text`, `__pic`, `__img`, `__controls` | `--home`, `--servicios`, `--us`, `--portafolio`, `--contact` | `capturas/home-desktop.png`, `capturas/servicios-desktop.png`, `capturas/home-mobile-375px.png` |
| **Botones interactivos** | `.c-button` | `__wrapper`, `__icon` | `--purple`, `--dark-purple`, `--blue`, `--sky-blue`, `--large`, `--circle`, `--next` | `capturas/home-desktop.png`, `capturas/contacto-desktop.png` |
| **Sección genérica** | `.c-section` | `__title`, `__subtitle`, `__intro`, `__content`, `__tag` | `--gray`, `--clients`, `--contact`, `--contact-form` | `capturas/home-desktop.png`, `capturas/nosotros-desktop.png` |
| **Bloque multimedia** | `.c-media-block` | `__figure`, `__img`, `__content`, `__text` | `--left-media`, `--right-media`, `--reasons`, `--services` | `capturas/home-desktop.png`, `capturas/nosotros-desktop.png` |
| **Teasers de servicios** | `.c-services-teaser` | `__item`, `__img`, `__content`, `__title`, `__text`, `__link` | En contenedor `.c-services-teasers` con grid responsive | `capturas/servicios-desktop.png`, `capturas/servicios-mobile-375px.png` |
| **Teasers de proyectos** | `.c-project-teaser` | `__pic-link`, `__pic`, `__img`, `__content`, `__title`, `__text` | En contenedor `.c-projects-teasers` | `capturas/portafolio-desktop.png`, `capturas/portafolio-mobile-375px.png` |
| **Miembros de equipo** | `.c-team-member` | `__pic`, `__img`, `__name`, `__job`, `__social` | En contenedor `.c-team-members` | `capturas/nosotros-desktop.png`, `capturas/nosotros-mobile-375px.png` |
| **Slider de clientes** | `.c-clients` | `__slider`, `__slide`, `__client`, `__slider-controls` | Controles prev/next asistidos por `tiny-slider` | `capturas/home-desktop.png`, `capturas/home-mobile-375px.png` |
| **Formulario de contacto** | `.c-contact-form` | `__field`, `__label`, `__input`, `__textarea`, `__submit`, `__error` | Incluye radios `.c-contact-form-radios` y checkboxes `.c-contact-form-checkboxes` | `capturas/contacto-desktop.png`, `capturas/contacto-mobile-375px.png` |
| **Opciones de contacto** | `.c-contact-options` | `__item`, `__icon`, `__text`, `__link` | Canales: teléfono, email, dirección física | `capturas/contacto-desktop.png`, `capturas/contacto-mobile-375px.png` |
| **Pie de página** | `.c-site-footer` | `__text`, `__social`, `__nav`, `__legal`, `__copy` | Subcomponentes `.c-site-footer-social` y `.c-site-footer-nav` | `capturas/home-desktop.png`, `capturas/home-mobile-375px.png` |
| **Módulos de portafolio** | `.c-gallery`, `.c-videos`, `.c-format-canvas`, `.c-format-album` | `__grid`, `__pic`, `__item` | Bloques para casos ricos (CyberWow, Iveco, Stralis) | `capturas/servicio-detalle-desktop.png`, `capturas/servicio-detalle-mobile-375px.png` |

> **Evidencia visual generada:** Las capturas de los componentes y maquetas servidas vía servidor local HTTP se encuentran almacenadas en `docs/diseno/capturas/` (`home-desktop.png`, `home-mobile-375px.png`, `servicios-desktop.png`, `servicios-mobile-375px.png`, `servicio-detalle-desktop.png`, `servicio-detalle-mobile-375px.png`, `portafolio-desktop.png`, `portafolio-mobile-375px.png`, `nosotros-desktop.png`, `nosotros-mobile-375px.png`, `contacto-desktop.png`, `contacto-mobile-375px.png`).

---

## 3. Mapa de Componentes por Maqueta HTML

Se analizaron las 10 maquetas estáticas presentes en `assets/`:

| Maqueta | Componentes Usados (en orden de aparición) | Propósito / Flujo |
| :--- | :--- | :--- |
| **`index.html`** (Home) | `c-site-header` → `c-hero` (Home) → `c-section` + `c-media-block` (Sobre el laboratorio) → `c-services-teasers` (3 servicios destacados) → `c-projects-teasers` (Casos destacados) → `c-section--clients` (Logos slider) → `c-section--contact` → `c-site-footer` | Portada institucional y embudo de conversión general. |
| **`servicios.html`** | `c-site-header` → `c-hero` (Servicios) → `c-content-block` → `c-services-teasers` (Listado de 6 servicios 2020) → `c-media-block` (Metodología/Instrumentos) → `c-site-footer` | Catálogo de servicios general. |
| **`servicio-detalle.html`** | `c-site-header` → `c-hero` (Detalle con breadcrumbs) → `c-content-block` (Social Media) → `c-note` → `c-media-block-reasons` (Por qué elegirnos) → `c-team-members` (Especialistas) → `c-media-block-services` (Herramientas) → `c-contact-form` → `c-site-footer` | Estructura interna de una página de servicio. |
| **`portafolio.html`** | `c-site-header` → `c-hero` (Portafolio) → `c-section` → `c-projects-teasers` (Grid de 8 proyectos con paginación/load more) → `c-site-footer` | Galería general de trabajos. |
| **`nosotros.html`** | `c-site-header` → `c-hero` (Nosotros) → `c-section` + `c-media-block` (Misión/Visión) → `c-team-members` (3 miembros) → `c-section--clients` → `c-site-footer` | Historia de la agencia y equipo fundador. |
| **`contactanos.html`** | `c-site-header` → `c-hero` (Contacto) → `c-contact-options` (Tarjetas de canales directos) → `c-contact-form` (Formulario interactivo completo) → `c-site-footer` | Página de conversión final. |
| **`campana-cyberwow.html`** | `c-site-header` → `c-hero` → `c-page-breadcrumb` → `c-simple-banner` → `c-web-content` → `c-format-album` → `c-featured-ads` → `c-carrousel-format` → `c-featured-stories` → `c-videos` → `c-gallery-grid` → `c-site-footer` | Estudio de caso de campaña de performance/eCommerce. |
| **`campana-iveco.html`** | `c-site-header` → `c-hero` → `c-page-breadcrumb` → `c-format-magazine` → `c-publication` → `c-format-web` → `c-site-footer` | Estudio de caso editorial y de marca corporativa. |
| **`campana-stralis.html`** | `c-site-header` → `c-hero` → `c-page-breadcrumb` → `c-simple-banner` → `c-format-canvas` → `c-carrousel-format` → `c-featured-stories` → `c-videos-grid` → `c-gallery-grid` → `c-site-footer` | Estudio de caso publicitario multimedia para camiones Stralis. |
| **`diseño-de-personajes.html`** | `c-site-header` → `c-hero` → `c-page-breadcrumb` → `c-gallery` → `c-gallery-teaser` → `c-process-teaser` → `c-views` (3D views) → `c-site-footer` | Estudio de caso creativo / 3D / ilustración. |

---

## 4. Estado actual y Deuda Técnica Observada

1. **Textos simulados y maquetas incompletas:**
   * En `portafolio.html`, **el 100% de las tarjetas de proyectos tienen texto `Lorem ipsum`**.
   * Las tarjetas enlazan a un archivo inexistente `portafolio-detalle.html` o repiten `campana-iveco.html`.
   * En `servicios.html`, 4 de los 6 servicios repiten exactamente el párrafo de Branding o Social Media.
2. **Imágenes de marcador de posición (Placeholders):**
   * En `portafolio.html`, los 8 proyectos usan el mismo archivo duplicado `project-1.webp`.
   * En los logos de clientes (`.c-clients`), todos los elementos `<img loading="lazy">` tienen `alt="alt"`.
3. **Restos de plantilla en inglés (Hardcoded strings):**
   * Fragmentos en comentarios y texto como *"Desinf anything from simple clean style..."* o *"Agency is a full-service agency..."* denotan que la maqueta se basó parcialmente en un boilerplate comercial que no se limpió en su totalidad.
4. **Archivos de respaldo y credenciales en raíz (`pharmaco.pe`):**
   * En el repositorio de WordPress conviven `conf-server.bk.php`, `wp-config.bk.php` y `wp.txt` con claves planas.

---

## 5. Stack Tecnológico Observado (Para cerrar `RFC-001`)

Del análisis exhaustivo de `main.css.map`, `main.css`, los scripts y el tema WordPress:

| Capa / Módulo | Tecnología Real Encontrada | Función | Reutilizable para nuevo sitio |
| :--- | :--- | :--- | :--- |
| **CSS Architecture** | **InuitCSS + BEM** | Metodología de CSS modular por capas (generic, elements, objects, components, utilities). | **Sí**, la arquitectura BEM es limpia, ordenada y escalable. |
| **CSS Preprocessor** | **SCSS (Sass)** con `sass-mq` | Manejo de variables, mixins de medios y nesting. | **Sí**, estándar de la industria. |
| **Animaciones en scroll** | **AOS (Animate On Scroll)** | Efectos `fade-up`, `fade-right` en tarjetas y títulos (sin versión explícita en archivos). | **Sí**, ligero y sin dependencias pesadas. |
| **Sliders / Carruseles** | **Tiny-Slider** | Carrusel táctil para clientes y formatos publicitarios (sin versión explícita en archivos). | **Sí**, es zero-dependencies (vanilla JS). |
| **Modales / Lightbox** | **Modaal (jQuery)** | Ventanas modales para visualización de videos/imágenes. | **Condicional**: requiere jQuery; modernizable a `<dialog>` nativo de HTML5 o micromodal. |
| **Gestión de iconos** | **SVG Sprite (`icons.svg`)** | Uso de `<use href="images/icons/icons.svg#icon-name">`. | **Sí**, estándar accesible y de alto rendimiento. |
| **Tipografía** | **Webfonts locales en WOFF2/WOFF** | Eliminó dependencia de Google Fonts externo (GDPR-friendly y más rápido). | **Sí**. |

