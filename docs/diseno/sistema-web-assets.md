# Sistema de diseño: web de assets (Parte A)

> **Documento:** `docs/diseno/sistema-web-assets.md` · **Tarea:** [TASK-004](../comms/TASK-004-sistema-de-diseno.md), Parte A
> **Autora:** Kia (DEV) · **Fecha de medición:** 2026-10-12 · **Rama:** `feat/TASK-004-sistema-diseno`
> **Fuente única:** las maquetas de `assets/` de este repositorio (estado de `da78418`): diez HTML, `css/main.css`, `css/main.css.map` y `js/main.js`. El tema WordPress de `pharmaco.pe` no está en el repositorio y no se ha analizado.
> **Solo lectura:** no se ha modificado nada fuera de `docs/diseno/`.

Este documento describe lo que hay. No elige dirección visual: eso corresponde a `RFC-002`.

---

## 0. Cómo se midió

- **Tokens:** se leyeron los valores de `css/main.css` con un analizador propio (3.160 declaraciones, con su `@media`). Cada valor se cita con el selector donde aparece. No se ha estimado ninguno a ojo.
- **Componentes y páginas:** las maquetas se sirvieron por HTTP desde `assets/` en un servidor local (puerto 8787) y se capturaron con Chrome headless por CDP. Cada componente se recorta por la caja medida con `getBoundingClientRect` del elemento, tras desplazar la página para que las animaciones de AOS terminen.
- **Estados:** las medidas de visibilidad y de `display` se leyeron con `getComputedStyle`. Donde un componente no se ve, se anota el valor medido y no se fabrica una captura.
- **Lo que no se hace:** no se modifica ninguna maqueta ni el tema. No se usan redes externas: los vídeos de YouTube de las campañas pueden no cargar en la captura, y se anota en su fila si ocurre.

---

## 1. Tokens (extraídos de `css/main.css`)

El CSS compilado **no tiene propiedades personalizadas** (0 declaraciones `--*` y 0 usos de `var(`). Los valores están repetidos en cada selector. El mapa de fuentes incluye los parciales SCSS (46 con variables), pero **no incluye el archivo de ajustes**: aparecen nombres como `$color-purple` o `$color-white`, pero nadie define su valor en el mapa. Por eso los tokens de abajo son **los valores del CSS**, no un nombre de variable confirmado.

### 1.1 Colores

Colores de marca y de texto, con el selector donde se aplican (propiedad entre paréntesis):

| Valor | Uso medido (selector · propiedad) |
| --- | --- |
| `#5956e9` | `.c-button--purple` (fondo) · `.c-section--purple` (fondo) · `.c-section__subtitle--purple` (texto) · `.c-button-view-all` (texto) · `.c-services-teaser__img` (fondo) |
| `#433fe6` | `.c-button--purple:hover` y `:focus` (fondo) |
| `#4c40f7` | `.c-button--blue` (fondo) · `.c-hero--blue` (fondo) · `.c-section__title--blue` (texto) |
| `#473bf7` | `.c-button--blue:hover` y `:focus` (fondo) |
| `#4d30a0` | `.c-button--dark-purple` (fondo) · `.c-hero--dark-purple` (fondo) |
| `#442a8c` | `.c-button--dark-purple:hover` y `:focus` (fondo) |
| `#3a30a0` | `.c-button--dark-blue` (fondo) · `.c-hero--purple` (fondo) · texto de `.c-button--sky-blue` |
| `#392f9c` | `.c-button--dark-blue:hover` y `:focus` (fondo) |
| `#b8defa` | `.c-button--sky-blue` (fondo); hover `#b3dcfa` |
| `#7c56e9` | `.c-hero--purple-original` (fondo; es el héroe de la portada) |
| `#00113b` | `.c-site-footer` (fondo) · sombra interior de `.c-section--contact` (desde 980 px) |
| `#111029` | `html` (color base del texto) · `.c-site-header-nav__link` (texto en móvil) · `.c-services-teaser__button` (texto) |
| `#ffffff` | `.c-section`, `.c-section--white`, `.c-section--contact` (fondo) · texto sobre fondos oscuros |
| `#f0f5f8` | `.c-section--gray` (fondo) |
| `#edf0f3` | `.c-section--contact` (fondo, desde 980 px) |
| `#eaeaeb` | `.c-section__tag` (fondo) · `#929292` su texto |
| `#d6dade` | `.c-button--grey` (fondo) · `.c-clients__slider-control` (fondo) |
| `#f4f4f4` | `.c-contact-form__input` y `.c-contact-form__textarea` (fondo) |
| `#6b6b6b` · `#666` | marcador de posición de los campos (`::placeholder`) |
| `#6e7177` | `.c-section__intro--gray` (texto) |
| `#787878` | `.c-section__subtitle--gray` (texto) |
| `#a7a7a7` | `.c-page-breadcrumb__link` y separador (texto) |
| `#9da4ac` | iconos de `.c-button--circle` y de `.c-clients__slider-control` |
| `#999fae` | `.c-services-teaser__text` (texto) |
| `#be0000` | estado de error de `.c-contact-form` (borde y fondo de `.js-form-error`) |
| `#ffd027` | foco visible: `outline: 2px solid #ffd027` con `.is-keyboard-pressed :focus`; anillo `0 0 0 2px #ffd027` en radios y casillas |

Colores de las tarjetas de servicio (`.c-services-teaser--*`, fondo): amarillo `#ffeddc`, morado `#bddeff`, azul `#bdf8ff`, rosa `#f3d1ff`, violeta `#d9c7ff`, rojo `#ffe2e2`.

Colores del héroe por variante (`.c-hero--*`, fondo): `#4c40f7` (blue), `#4d30a0` (dark-purple), `#5956e9` (light-purple), `#2565b8` (medium-blue), `#fa832b` (orange), `#afe7e9` (paleturquoise), `#3a30a0` (purple), `#0030ff` (strong-blue), `#7ad5f2` (turquoise-service), `#7c56e9` (purple-original), y ocho variantes de servicio con colores propios (`#6490ff`, `#7d7afa`, `#888`, `#bb85e5`, `#b27afa`, `#b896ff`, `#ff99fb`, `#8082c0`).

El mapa de colores completo que sale del CSS tiene 67 valores distintos. Los de Modaal (`.modaal-*`) vienen de la librería embebida y no son del diseño de Pharmaco; se excluyen de la tabla.

### 1.2 Tipografía

- **Familia:** `html` declara `Poppins,Arial,Helvetica,sans-serif`. Otras reglas usan `sans-serif`, `monospace` (en `pre`, `code`, `kbd`) y `Helvetica` (en `.c-views__text`).
- **Archivos declarados** (`@font-face`, en `fonts/`): Poppins 400 (`Poppins-Regular`), 500 (`Poppins-Medium`) y 600 (`Poppins-SemiBold`), en WOFF2 y WOFF, con `font-display: swap`. **No hay `@font-face` para 700** (ni hay archivo de Bold o ExtraBold en `fonts/`; solo están los tres pesos citados), aunque `.s-cms-content h2`, `h3` y `strong` piden `font-weight: 700`. Qué pinta el navegador en ese caso no se ha medido.
- **Pesos usados:** 600 (11 reglas), 500 (9), 400 (4), 700 (4), 300 (1, en `.c-views__text`).

Escala por selector (`base` es sin media query; los puntos de corte son los de la sección 1.5):

| Selector | Base | 700 px | 980 px | 1200 px | Interlineado y peso |
| --- | --- | --- | --- | --- | --- |
| `html` | 16 px | | | | interlineado 1,15; `.c-section__intro` 1,4 |
| `.c-section__title` | 16 px | 17 px | 18 px | 20 px | peso 600; interlineado 1,6 |
| `.c-section__subtitle` | 35 px | 49 px | 63 px | 77 px | peso 600; interlineado 1,16 (1,03 desde 980 px) |
| `.c-section__subtitle--small` | 35 px | 37 px | 39 px | 40 px | |
| `.c-section__subtitle--big` | 24 px | 44 px | 64 px | 84 px | |
| `.c-section__subtitle--small-light` | 22 px | 22 px | 22 px | 22 px | peso 500 |
| `.c-section__intro` | 16 px | | 18 px | | interlineado 1,4 |
| `.c-section__tag` | 9 px | | 14 px | | peso 400 |
| `.c-button` | 14 px | | | 18 px | peso 500; interlineado 1,2 |
| `.c-button--large` | 14 px | | 20 px | | |
| `.c-services-teaser__title` | 24 px | | 28 px | | peso 500; interlineado 1 |
| `.c-services-teaser__text` | 16 px | | | | interlineado 1,3 (1,8 desde 980 px) |
| `.c-project-teaser__title` | 24 px | | | | peso 600; interlineado 1 |
| `.c-content-block__subtitle` | 24 px | | 28 px | | peso 600 |
| `.c-team-member__name` | 30 px | | 42 px | | peso 600 |
| `.c-team-member__job` | 14 px | | 20 px | | peso 500 |
| `.c-site-header-nav__link` | 18 px | | 16 px | | |
| `.c-site-footer__text` | 16 px | | | | peso 500; interlineado 1,46 |
| `.c-page-breadcrumb__link` | 14 px | | | 18 px | |
| `.s-cms-content h2` | 24 px | 27 px | 30 px | 32 px | peso 700 |
| `.s-cms-content h3` | 18 px | 20 px | 22 px | 24 px | peso 700 |
| `.c-note__title` | 35 px | 37 px | 39 px | 40 px | peso 600 |

### 1.3 Espaciado, anchuras y dimensiones

- **Contenedor `.o-wrapper`:** `max-width` 1302 px con `padding` 0 30 px. Variantes: `.o-wrapper--small` 1120 px, `.o-wrapper--large` 1440 px, `.o-wrapper--flush` sin padding lateral. `.o-wrapper-body` y `.c-hero__content` llegan a 1440 px.
- **Secciones `.c-section`:** `padding` 62 px 0 en base y 152 px 0 desde 980 px. `.c-section__content` tiene `margin-top` 50 px.
- **Botones:** `.c-button` mide 48 px de alto en base, 64 px desde 1200 px, con `padding` 0 30 px. `.c-button--large` mide 72 px desde 980 px. `.c-button--circle` mide 38 px.
- **Tarjetas de servicio `.c-services-teaser`:** `padding` 24 px 22 px 18 px en base y 36 px 20 px 20 px desde 980 px.
- **Listados de tarjetas:** `.c-services-teasers__list` y `.c-projects-teasers__list` tienen `margin-top` -25 px en base y -40 px desde 980 px, con `width` calc(100% + 46 px) desde 700 px.
- **Anchos fijos que aparecen en más de una regla:** 248 px (`.c-media-block__media` en base), 350 px (mismo selector desde 700 px), 360 px (`.c-hero__pic`, `.c-process-teaser__image`) y un `max-width` de 320 px en `.c-views__image-big` y `.c-format-canvas`.

### 1.4 Radios y sombras

| Elemento | Radio (base → desde punto de corte) | Sombra |
| --- | --- | --- |
| `.c-button` | 15 px → 20 px desde 1200 px | `none`; al foco y al hover `4px 5px 13px rgba(0,0,0,.08)` |
| `.c-button--circle` | 50 % | ninguna |
| `.c-services-teaser` | 20 px → 28 px desde 980 px | ninguna |
| `.c-project-teaser` | 12 px → 18 px desde 980 px | `4px 5px 13px rgba(0,0,0,.08)` |
| `.c-contact-options__option` | 9 px → 14 px desde 980 px | ninguna |
| `.c-contact-form__input` y `textarea` | 8 px | ninguna; `0 3px 6px 0 rgba(0,0,0,.16)` en `label.js-form-error` |
| `.c-section__tag` | 5 px → 8 px desde 980 px | ninguna |
| `.c-views__image-big_pic` | 14 px | ninguna |
| `.c-format-canvas__item` | ninguna | `6px 10px 24px rgba(0,0,0,.1)` |
| `.c-section--contact` | ninguno | `0 -48px 0 0 #00113b inset` desde 980 px |

### 1.5 Puntos de corte (`@media`)

Los puntos de corte están en `em` (base 16 px). Los valores en píxeles se calculan así: 22,5 em = 360 px; 26,5625 em = 425 px; 31,25 em = 500 px; 43,75 em = 700 px; 61,25 em = 980 px; 75 em = 1200 px; 87,5 em = 1400 px. Se leen en `main.css` como `min-width`, con esta frecuencia: 980 px (358 reglas), 1200 px (71), 700 px (44), 360 px (3), 500 px (2), 425 px (1), 1400 px (1).

En sentido descendente aparecen `max-width` de 600 px (37,5 em), 699,84 px (43,74 em), 979,84 px (61,24 em), 900 px, 1140 px y 600 px, además de consultas por altura (`max-height` 820, 900, 1000 y 1100 px). Los puntos de corte del `sass-mq` de la librería (320, 740, 980, 1300) están en el mapa, pero el CSS compilado usa los de arriba: la configuración del proyecto no está en el mapa.

### 1.6 Movimiento

- **Transiciones:** `all .2s ease, outline 0s` es la más repetida (33 declaraciones); luego `.2s` en `background`, y `.3s` en `color`, `opacity`, `visibility` y `transform`.
- **Animaciones de entrada:** AOS. Las maquetas usan `data-aos` (9 veces en `index.html`) con efectos como `fade-up`, `fade-right`.
- **Otros:** `transform` con `translateY(-50%)`, `scale(1.2)`, `rotate(45deg)`, y el giro del spinner de Modaal.

---

## 2. Componentes

Hay **48 bloques raíz** en las maquetas: cada clase `c-*` sin `__` ni `--`, contada en su primera aparición en el orden de las maquetas. Los modificadores (`c-hero--*`, `c-section--*`, `c-services-teaser--*`, etc.) no cuentan como componentes aparte; se citan en la sección 1.

Cada fila tiene una captura de escritorio (1280 px) y otra de 375 px del **primer elemento visible** de esa raíz, salvo que el estado medido diga otra cosa. Cuando dos componentes tienen la misma caja (contenedor e hijo), la captura es idéntica byte a byte y se referencia la misma imagen; eso se indica en la fila.

| Componente (raíz BEM) | Maqueta de la captura | Escritorio 1280 px | Móvil 375 px |
| --- | --- | --- | --- |
| `c-site-header` | index.html | [comp-site-header-desktop.png](capturas/comp-site-header-desktop.png) | [comp-site-header-mobile.png](capturas/comp-site-header-mobile.png) |
| `c-site-header-nav` | index.html | [comp-site-header-nav-desktop.png](capturas/comp-site-header-nav-desktop.png) | cerrado: `visibility: hidden` y desplazado fuera de pantalla; el estado abierto está en [menú abierto](capturas/comp-site-header-nav-mobile-open.png) |
| `c-button` | index.html | [comp-button-desktop.png](capturas/comp-button-desktop.png) | [comp-button-mobile.png](capturas/comp-button-mobile.png) |
| `c-header-controls` | index.html | [comp-header-controls-desktop.png](capturas/comp-header-controls-desktop.png) | [comp-header-controls-mobile.png](capturas/comp-header-controls-mobile.png) |
| `c-overlay` | index.html | no visible: `display: none` a 1280 px (medido) | cerrado: opacidad 0 y `visibility: hidden`; el estado abierto está en [overlay abierto](capturas/comp-overlay-mobile-open.png) |
| `c-hero` | index.html | [comp-hero-desktop.png](capturas/comp-hero-desktop.png) | [comp-hero-mobile.png](capturas/comp-hero-mobile.png) |
| `c-section` | index.html | [comp-section-desktop.png](capturas/comp-section-desktop.png) | [comp-section-mobile.png](capturas/comp-section-mobile.png) |
| `c-media-block` | index.html | [comp-media-block-desktop.png](capturas/comp-media-block-desktop.png) | [comp-media-block-mobile.png](capturas/comp-media-block-mobile.png) |
| `c-services-teasers` | index.html | [comp-services-teasers-desktop.png](capturas/comp-services-teasers-desktop.png) | [comp-services-teasers-mobile.png](capturas/comp-services-teasers-mobile.png) |
| `c-services-teaser` | index.html | [comp-services-teaser-desktop.png](capturas/comp-services-teaser-desktop.png) | [comp-services-teaser-mobile.png](capturas/comp-services-teaser-mobile.png) |
| `c-button-view-all` | index.html | [comp-button-view-all-desktop.png](capturas/comp-button-view-all-desktop.png) | [comp-button-view-all-mobile.png](capturas/comp-button-view-all-mobile.png) |
| `c-projects-teasers` | index.html | [comp-projects-teasers-desktop.png](capturas/comp-projects-teasers-desktop.png) | [comp-projects-teasers-mobile.png](capturas/comp-projects-teasers-mobile.png) |
| `c-project-teaser` | index.html | [comp-project-teaser-desktop.png](capturas/comp-project-teaser-desktop.png) | [comp-project-teaser-mobile.png](capturas/comp-project-teaser-mobile.png) |
| `c-clients` | index.html | [comp-clients-desktop.png](capturas/comp-clients-desktop.png) | [comp-clients-mobile.png](capturas/comp-clients-mobile.png) |
| `c-site-footer` | index.html | [comp-site-footer-desktop.png](capturas/comp-site-footer-desktop.png) | [comp-site-footer-mobile.png](capturas/comp-site-footer-mobile.png) |
| `c-site-footer-social` | index.html | [comp-site-footer-social-desktop.png](capturas/comp-site-footer-social-desktop.png) | [comp-site-footer-social-mobile.png](capturas/comp-site-footer-social-mobile.png) |
| `c-site-footer-nav` | index.html | [comp-site-footer-nav-desktop.png](capturas/comp-site-footer-nav-desktop.png) | [comp-site-footer-nav-mobile.png](capturas/comp-site-footer-nav-mobile.png) |
| `c-button-line` | index.html | [comp-button-line-desktop.png](capturas/comp-button-line-desktop.png) | [comp-button-line-mobile.png](capturas/comp-button-line-mobile.png) |
| `c-team-members` | nosotros.html | [comp-team-members-desktop.png](capturas/comp-team-members-desktop.png) | [comp-team-members-mobile.png](capturas/comp-team-members-mobile.png) |
| `c-team-member` | nosotros.html | [comp-team-member-desktop.png](capturas/comp-team-member-desktop.png) | [comp-team-member-mobile.png](capturas/comp-team-member-mobile.png) |
| `c-content-block` | servicios.html | [comp-content-block-desktop.png](capturas/comp-content-block-desktop.png) | [comp-content-block-mobile.png](capturas/comp-content-block-mobile.png) |
| `c-button-next` | servicios.html | [comp-button-next-desktop.png](capturas/comp-button-next-desktop.png) | [comp-button-next-mobile.png](capturas/comp-button-next-mobile.png) |
| `c-page-breadcrumb` | servicio-detalle.html | [comp-page-breadcrumb-desktop.png](capturas/comp-page-breadcrumb-desktop.png) | no visible a 375 px en `servicio-detalle.html`: la primera instancia tiene `display: none` |
| `c-note` | servicio-detalle.html | [comp-note-desktop.png](capturas/comp-note-desktop.png) | [comp-note-mobile.png](capturas/comp-note-mobile.png) |
| `c-media-block-reasons` | servicio-detalle.html | [comp-media-block-reasons-desktop.png](capturas/comp-media-block-reasons-desktop.png) | [comp-media-block-reasons-mobile.png](capturas/comp-media-block-reasons-mobile.png) |
| `c-media-block-services` | servicio-detalle.html | [comp-media-block-services-desktop.png](capturas/comp-media-block-services-desktop.png) | [comp-media-block-services-mobile.png](capturas/comp-media-block-services-mobile.png) |
| `c-contact-form` | servicio-detalle.html | [comp-contact-form-desktop.png](capturas/comp-contact-form-desktop.png) | [comp-contact-form-mobile.png](capturas/comp-contact-form-mobile.png) |
| `c-contact-options` | contactanos.html | [comp-contact-options-desktop.png](capturas/comp-contact-options-desktop.png) | [comp-contact-options-mobile.png](capturas/comp-contact-options-mobile.png) |
| `c-contact-form-radios` | contactanos.html | [comp-contact-form-radios-desktop.png](capturas/comp-contact-form-radios-desktop.png) | [comp-contact-form-radios-mobile.png](capturas/comp-contact-form-radios-mobile.png) |
| `c-contact-form-checkboxes` | contactanos.html | [comp-contact-form-checkboxes-desktop.png](capturas/comp-contact-form-checkboxes-desktop.png) | [comp-contact-form-checkboxes-mobile.png](capturas/comp-contact-form-checkboxes-mobile.png) |
| `c-simple-banner` | campana-cyberwow.html | [comp-simple-banner-desktop.png](capturas/comp-simple-banner-desktop.png) | [comp-simple-banner-mobile.png](capturas/comp-simple-banner-mobile.png) |
| `c-web-content` | campana-cyberwow.html | [comp-web-content-desktop.png](capturas/comp-web-content-desktop.png) | [comp-web-content-mobile.png](capturas/comp-web-content-mobile.png) |
| `c-format-album` | campana-cyberwow.html | [comp-format-album-desktop.png](capturas/comp-format-album-desktop.png) | [comp-format-album-mobile.png](capturas/comp-format-album-mobile.png) |
| `c-featured-ads` | campana-cyberwow.html | [comp-featured-ads-desktop.png](capturas/comp-featured-ads-desktop.png) | [comp-featured-ads-mobile.png](capturas/comp-featured-ads-mobile.png) |
| `c-carrousel-format` | campana-cyberwow.html | [comp-carrousel-format-desktop.png](capturas/comp-carrousel-format-desktop.png) | [comp-carrousel-format-mobile.png](capturas/comp-carrousel-format-mobile.png) |
| `c-featured-stories` | campana-cyberwow.html | [comp-featured-stories-desktop.png](capturas/comp-featured-stories-desktop.png) | [comp-featured-stories-mobile.png](capturas/comp-featured-stories-mobile.png) |
| `c-videos` | campana-cyberwow.html | misma caja que `c-videos-banner`: se usa [la captura del banner](capturas/comp-videos-banner-desktop.png) | misma caja que `c-videos-banner`: se usa [la captura del banner](capturas/comp-videos-banner-mobile.png) |
| `c-videos-banner` | campana-cyberwow.html | [comp-videos-banner-desktop.png](capturas/comp-videos-banner-desktop.png) | [comp-videos-banner-mobile.png](capturas/comp-videos-banner-mobile.png) |
| `c-gallery` | campana-cyberwow.html | misma caja que `c-gallery-grid`: el contenedor no añade contenido propio; se usa [la captura de la cuadrícula](capturas/comp-gallery-grid-desktop.png) | misma caja que `c-gallery-grid`: se usa [la captura de la cuadrícula](capturas/comp-gallery-grid-mobile.png) |
| `c-gallery-grid` | campana-cyberwow.html | [comp-gallery-grid-desktop.png](capturas/comp-gallery-grid-desktop.png) | [comp-gallery-grid-mobile.png](capturas/comp-gallery-grid-mobile.png) |
| `c-format-magazine` | campana-iveco.html | [comp-format-magazine-desktop.png](capturas/comp-format-magazine-desktop.png) | [comp-format-magazine-mobile.png](capturas/comp-format-magazine-mobile.png) |
| `c-publication` | campana-iveco.html | [comp-publication-desktop.png](capturas/comp-publication-desktop.png) | [comp-publication-mobile.png](capturas/comp-publication-mobile.png) |
| `c-format-web` | campana-iveco.html | [comp-format-web-desktop.png](capturas/comp-format-web-desktop.png) | [comp-format-web-mobile.png](capturas/comp-format-web-mobile.png) |
| `c-format-canvas` | campana-stralis.html | [comp-format-canvas-desktop.png](capturas/comp-format-canvas-desktop.png) | [comp-format-canvas-mobile.png](capturas/comp-format-canvas-mobile.png) |
| `c-videos-grid` | campana-stralis.html | [comp-videos-grid-desktop.png](capturas/comp-videos-grid-desktop.png) | [comp-videos-grid-mobile.png](capturas/comp-videos-grid-mobile.png) |
| `c-gallery-teaser` | diseño-de-personajes.html | [comp-gallery-teaser-desktop.png](capturas/comp-gallery-teaser-desktop.png) | [comp-gallery-teaser-mobile.png](capturas/comp-gallery-teaser-mobile.png) |
| `c-process-teaser` | diseño-de-personajes.html | [comp-process-teaser-desktop.png](capturas/comp-process-teaser-desktop.png) | [comp-process-teaser-mobile.png](capturas/comp-process-teaser-mobile.png) |
| `c-views` | diseño-de-personajes.html | [comp-views-desktop.png](capturas/comp-views-desktop.png) | [comp-views-mobile.png](capturas/comp-views-mobile.png) |

**Notas sobre las filas:**

- `c-overlay` no es un texto: es la capa que el menú móvil activa (`is-active`). Su `background-color` es rgba(0,0,0,.4) según el CSS (selector `.c-overlay`). Con el menú cerrado tiene `opacity` 0 y `visibility: hidden`; con el menú abierto, medido en la misma sesión, tiene `opacity` 1, `visibility: visible` y mide 375 × 812 px. La captura [overlay abierto](capturas/comp-overlay-mobile-open.png) muestra el panel del menú sobre el héroe oscurecido. En escritorio tiene `display: none`.
- `c-site-header-nav` tiene `visibility: hidden` con el menú cerrado, y su contenedor lleva un `transform` de 320 px en horizontal (medido). Con el menú abierto, medido en la misma sesión, mide 280 × 330 px en la posición 75, 20, `visibility: visible` y el `transform` del contenedor vuelve a 0. La captura [menú abierto](capturas/comp-site-header-nav-mobile-open.png) muestra los cinco enlaces del menú y el botón «Cerrar».
- Las capturas de estado abierto de la versión anterior de esta rama mostraban el héroe y no el menú, porque no se comprobaba el estado antes de capturar. Se han rehecho con comprobación del estado (`is-active`, `visibility`, `transform`) antes de cada captura.
- `c-page-breadcrumb` no tiene instancia visible a 375 px en `servicio-detalle.html` (su primera instancia tiene `display: none`). Ni la primera instancia ni ninguna otra de esa maqueta se muestra a ese ancho. Se anota en lugar de fabricar una captura.
- `c-button` es el CTA visible del héroe de la portada («Empecemos»), no el botón de la cabecera: la primera instancia del DOM, dentro del menú, está oculta a 1280 px y en blanco a 375 px.
- Las capturas de `c-format-magazine` (escritorio) se hicieron a escala 0,5 porque a escala 1 Chrome no terminó la captura. La imagen tiene la mitad de resolución.
- Todas las capturas pasan un comprobador de color plano (ninguna queda en un solo color). A ojo se han mirado las capturas de estado (menú abierto, overlay), el botón del héroe y el botón siguiente; el resto no se ha revisado visualmente uno a uno. Un recorte sigue pudiendo incluir parte de un elemento vecino si se solapa (la cabecera, por ejemplo, está en posición absoluta sobre el héroe).

---

## 3. Páginas: qué componentes usa cada maqueta

El orden es el de aparición en el HTML. Se listan las raíces `c-*` (sin modificadores), sin repetir.

- **index.html** (18 raíces): `c-site-header`, `c-site-header-nav`, `c-button`, `c-header-controls`, `c-overlay`, `c-hero`, `c-section`, `c-media-block`, `c-services-teasers`, `c-services-teaser`, `c-button-view-all`, `c-projects-teasers`, `c-project-teaser`, `c-clients`, `c-site-footer`, `c-site-footer-social`, `c-site-footer-nav`, `c-button-line`
- **nosotros.html** (15 raíces): `c-site-header`, `c-site-header-nav`, `c-button`, `c-header-controls`, `c-overlay`, `c-hero`, `c-section`, `c-media-block`, `c-team-members`, `c-team-member`, `c-clients`, `c-site-footer`, `c-site-footer-social`, `c-site-footer-nav`, `c-button-line`
- **servicios.html** (16 raíces): `c-site-header`, `c-site-header-nav`, `c-button`, `c-header-controls`, `c-overlay`, `c-hero`, `c-section`, `c-content-block`, `c-services-teasers`, `c-services-teaser`, `c-button-next`, `c-media-block`, `c-site-footer`, `c-site-footer-social`, `c-site-footer-nav`, `c-button-line`
- **servicio-detalle.html** (19 raíces): `c-site-header`, `c-site-header-nav`, `c-button`, `c-header-controls`, `c-overlay`, `c-hero`, `c-page-breadcrumb`, `c-section`, `c-content-block`, `c-note`, `c-media-block-reasons`, `c-team-members`, `c-team-member`, `c-media-block-services`, `c-contact-form`, `c-site-footer`, `c-site-footer-social`, `c-site-footer-nav`, `c-button-line`
- **portafolio.html** (13 raíces): `c-site-header`, `c-site-header-nav`, `c-button`, `c-header-controls`, `c-overlay`, `c-hero`, `c-section`, `c-projects-teasers`, `c-project-teaser`, `c-site-footer`, `c-site-footer-social`, `c-site-footer-nav`, `c-button-line`
- **contactanos.html** (15 raíces): `c-site-header`, `c-site-header-nav`, `c-button`, `c-header-controls`, `c-overlay`, `c-hero`, `c-contact-options`, `c-section`, `c-contact-form`, `c-contact-form-radios`, `c-contact-form-checkboxes`, `c-site-footer`, `c-site-footer-social`, `c-site-footer-nav`, `c-button-line`
- **campana-cyberwow.html** (22 raíces): `c-site-header`, `c-site-header-nav`, `c-button`, `c-header-controls`, `c-overlay`, `c-hero`, `c-page-breadcrumb`, `c-section`, `c-simple-banner`, `c-web-content`, `c-format-album`, `c-featured-ads`, `c-carrousel-format`, `c-featured-stories`, `c-videos`, `c-videos-banner`, `c-gallery`, `c-gallery-grid`, `c-site-footer`, `c-site-footer-social`, `c-site-footer-nav`, `c-button-line`
- **campana-iveco.html** (15 raíces): `c-site-header`, `c-site-header-nav`, `c-button`, `c-header-controls`, `c-overlay`, `c-hero`, `c-page-breadcrumb`, `c-section`, `c-format-magazine`, `c-publication`, `c-format-web`, `c-site-footer`, `c-site-footer-social`, `c-site-footer-nav`, `c-button-line`
- **campana-stralis.html** (21 raíces): `c-site-header`, `c-site-header-nav`, `c-button`, `c-header-controls`, `c-overlay`, `c-hero`, `c-page-breadcrumb`, `c-section`, `c-simple-banner`, `c-format-canvas`, `c-carrousel-format`, `c-featured-stories`, `c-videos`, `c-videos-banner`, `c-gallery`, `c-gallery-grid`, `c-videos-grid`, `c-site-footer`, `c-site-footer-social`, `c-site-footer-nav`, `c-button-line`
- **diseño-de-personajes.html** (16 raíces): `c-site-header`, `c-site-header-nav`, `c-button`, `c-header-controls`, `c-overlay`, `c-hero`, `c-page-breadcrumb`, `c-section`, `c-gallery`, `c-gallery-teaser`, `c-process-teaser`, `c-views`, `c-site-footer`, `c-site-footer-social`, `c-site-footer-nav`, `c-button-line`

Capturas de página completa (`docs/diseno/paginas/capturas/`):

Cuando el documento mide más de 8.000 px, la captura es **solo la primera pantalla** (800 px en escritorio, 812 px en móvil), y así figura en la tabla. Eso es lo que pasa en las campañas, en `servicios.html` a 375 px y en la portada de CyberWow a 375 px. La captura de escritorio de CyberWow se hizo a escala 0,5 y ocupa 640 px de ancho.

| Maqueta | Escritorio 1280 px | Móvil 375 px |
| --- | --- | --- |
| index.html | [pagina-index-desktop.png](paginas/capturas/pagina-index-desktop.png) (1280×5849 px) | [pagina-index-mobile.png](paginas/capturas/pagina-index-mobile.png) (750×12532 px) |
| nosotros.html | [pagina-nosotros-desktop.png](paginas/capturas/pagina-nosotros-desktop.png) (1280×4190 px) | [pagina-nosotros-mobile.png](paginas/capturas/pagina-nosotros-mobile.png) (750×7602 px) |
| servicios.html | [pagina-servicios-desktop.png](paginas/capturas/pagina-servicios-desktop.png) (1280×7243 px) | [pagina-servicios-mobile.png](paginas/capturas/pagina-servicios-mobile.png) (750×1624 px) |
| servicio-detalle.html | [pagina-servicio-detalle-desktop.png](paginas/capturas/pagina-servicio-detalle-desktop.png) (1280×5238 px) | [pagina-servicio-detalle-mobile.png](paginas/capturas/pagina-servicio-detalle-mobile.png) (750×12756 px) |
| portafolio.html | [pagina-portafolio-desktop.png](paginas/capturas/pagina-portafolio-desktop.png) (1280×3397 px) | [pagina-portafolio-mobile.png](paginas/capturas/pagina-portafolio-mobile.png) (750×9856 px) |
| contactanos.html | [pagina-contactanos-desktop.png](paginas/capturas/pagina-contactanos-desktop.png) (1280×2576 px) | [pagina-contactanos-mobile.png](paginas/capturas/pagina-contactanos-mobile.png) (750×5240 px) |
| campana-cyberwow.html | [pagina-campana-cyberwow-desktop.png](paginas/capturas/pagina-campana-cyberwow-desktop.png) (640×7829 px) | [pagina-campana-cyberwow-mobile.png](paginas/capturas/pagina-campana-cyberwow-mobile.png) (750×1624 px) |
| campana-iveco.html | [pagina-campana-iveco-desktop.png](paginas/capturas/pagina-campana-iveco-desktop.png) (1280×800 px) | no capturada en esta pasada (Chrome no terminó la captura) |
| campana-stralis.html | [pagina-campana-stralis-desktop.png](paginas/capturas/pagina-campana-stralis-desktop.png) (1280×800 px) | no capturada en esta pasada (Chrome no terminó la captura) |
| diseño-de-personajes.html | [pagina-diseno-de-personajes-desktop.png](paginas/capturas/pagina-diseno-de-personajes-desktop.png) (1280×7631 px) | no capturada en esta pasada (Chrome no terminó la captura) |

---

## 4. Estado de la web de assets

Lo que sigue se verificó con búsquedas en los HTML y en el CSS. No es una valoración de calidad.

### 4.1 Texto de relleno y restos de plantilla

- **Texto de relleno en latín:** `Lorem` aparece en `index.html` (3 veces), `servicio-detalle.html` (2), `portafolio.html` (9), `campana-cyberwow.html`, `campana-iveco.html`, `campana-stralis.html` y `diseño-de-personajes.html` (9 en cada una). En `index.html` y `portafolio.html` el texto de las tarjetas de proyecto es `Lorem ipsum`. `nosotros.html`, `servicios.html` y `contactanos.html` no tienen ninguno.
- **Texto en inglés residual:** la frase `Desinf anything from simple clean style to fully featured websites` aparece en `campana-cyberwow.html`, `campana-iveco.html`, `campana-stralis.html`, `nosotros.html` y `portafolio.html`. Es un fragmento de una plantilla comercial.

### 4.2 Imágenes y accesibilidad

- **`alt="alt"`** (el texto alternativo es literalmente «alt») en `index.html` (11), `portafolio.html` (9), `nosotros.html` (8), `servicios.html` (6) y `servicio-detalle.html` (3). En `index.html` incluye las imágenes de las tarjetas de servicio.
- **Imagen repetida:** `project-1.webp` aparece en las 3 tarjetas de proyecto de `index.html` y en las 9 de `portafolio.html`. Son la misma imagen para proyectos distintos.

### 4.3 Enlaces a páginas que no existen

Estos HTML no están en `assets/`:

- `blog.html` y `buscar.html` se enlazan desde la cabecera de las diez maquetas; `blog.html` es además la entrada «Blog» del menú.
- `test.html` se enlaza desde los enlaces sociales del pie de las diez maquetas.
- `portafolio-detalle.html` se enlaza desde las tarjetas de proyecto de `index.html` y `portafolio.html`.

### 4.4 Qué es reutilizable

Criterio de esta revisión, no dato medido: la base (BEM, tokens repetidos en el CSS, la escala tipográfica y los bloques de la sección 2) se puede reutilizar como referencia. Los textos, las imágenes repetidas y los enlaces rotos de la sección 4.1 a 4.3 no se reutilizan tal cual.

---

## 5. Stack observado (insumo para `RFC-001`)

Cada afirmación de esta sección sale de un archivo del repositorio, citado.

- **Compilado y mapa:** `css/main.css` con `css/main.css.map` de 61 fuentes. Esas fuentes incluyen partials de SCSS del proyecto (`components/`, `elements/`, `objects/`, `tools/`, `scope/`, `utilities/`) y archivos de `node_modules`.
- **Metodología CSS:** BEM (nombres `c-*`, `o-*`, `u-*`, `s-*`) sobre InuitCSS. Aparecen rutas de InuitCSS en el mapa (`generic`, `objects/_objects.crop`, `utilities`, `tools`).
- **Preprocesador:** SCSS con `sass-mq` (`../../node_modules/sass-mq/_mq.scss`). El mapa incluye `normalize-scss`.
- **JavaScript:** un único bundle `js/main.js` (la única etiqueta `<script>` de cada maqueta). Dentro van:
  - jQuery (código de la librería embebido; **versión no publicada** en el archivo);
  - AOS (animaciones; el archivo no declara versión);
  - tiny-slider: el bloque que expone `getInfo`, `goTo` y `play` declara `version:"2.9.3"`, y el código inicializa `.js-clients-slider`;
  - Modaal: el comentario de cabecera dice `Modaal - accessible modals - v0.4.4`. **Ninguna maqueta usa Modaal**: no hay ningún `data-modaal` en los HTML, así que la librería está incluida pero no tiene instancias.
- **CSS de terceros incluido:** `aos.css`, `tiny-slider.css` y `modaal.scss` aparecen en el mapa.
- **Fuentes:** Poppins local (WOFF2 y WOFF), precargada con `<link rel="preload">` en cada maqueta. No hay peticiones a Google Fonts en las maquetas.
- **Vídeo:** las campañas incrustan YouTube (`youtube.com/embed`). La portada no incrusta vídeo; su única mención de YouTube es un icono del pie.

---

## 6. Qué no está verificado

- **Versiones de jQuery y de AOS:** no hay cadena de versión en los archivos. Se dejan sin versión.
- **Peso 700:** el CSS lo pide y no hay `@font-face` para él. El aspecto real no se ha medido.
- **Tema WordPress:** no está en el repositorio; no se ha comparado con `blocks/` ni con el tema en producción.
- **Captura de algunos componentes:** cuando el recorte solo muestra el borde de un elemento de la página vecina, se anota en la fila; no se ha corregido.
- **Páginas de campaña en móvil:** la captura completa de `campana-iveco.html`, `campana-stralis.html` y `diseño-de-personajes.html` a 375 px no se ha conseguido en esta pasada; las tres quedan como «no capturada».
