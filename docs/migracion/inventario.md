# Inventario de origen — web de assets

> **Documento:** `docs/migracion/inventario.md` · **Tarea:** [TASK-006](../comms/TASK-006-migracion-blackgrow.md), fase 0
> **Autora:** Kia (DEV) · **Fecha:** 2026-10-12
> **Origen:** `assets/` tal como está en `main` (último commit que lo toca: `c968e58`). No se ha modificado nada en `assets/`.
> **Parte de:** [`docs/diseno/sistema-web-assets.md`](../diseno/sistema-web-assets.md) (TASK-004, parte A). Lo que ese documento dice y no se sostiene al leer `assets/` está en la sección 9.

---

## 1. Qué se ha leído

| Fuente | Qué aporta |
| --- | --- |
| `assets/*.html` (10 archivos) | Páginas, componentes, textos, enlaces, formularios, hooks de JS |
| `assets/css/main.css` (104 KB) | Valores exactos: colores, tipografía, medias queries, radios, sombras |
| `assets/css/main.css.map` | 61 fuentes SCSS. Contienen `objects/_objects.wrapper.scss` y los parciales de componentes, pero **no** el archivo de settings con las variables de color y de breakpoint |
| `assets/js/main.js` (187 KB) | JavaScript compilado y final. El código de aplicación está **al final del archivo**, desde `let openMenuButton`. Lo que hay antes son las librerías empaquetadas |
| `assets/js/main.js.map` | Fuentes del propio JS (tools, input-filters) y de jQuery, AOS y tiny-slider. **No** trae `components.site-header`, `components.hero`, `components.clients`, `components.forms`, `components.modals` ni `jquery-validation`: su código se lee del JS compilado |
| `assets/js/components.js` | Bundle aparte. **Ninguna maqueta lo carga** (sección 6.2) |
| `assets/images/`, `assets/fonts/` | Inventario de archivos y comprobación de referencias |

Las comprobaciones de referencias (487 rutas locales) se hicieron con scripts sobre el árbol del worktree. Los conteos de este documento salen de esas ejecuciones.

---

## 2. Discrepancias que hay que decidir

Estas son las diferencias entre el encargo (TASK-006, DECISION-010) y el origen, o entre `sistema-web-assets.md` y el origen. Se han llevado al hilo de la TASK.

1. **Son 10 maquetas, no 9.** TASK-006 y DECISION-010 dicen «9». `assets/` tiene 10 `.html`. Se inventarían las 10. Pregunta abierta en el hilo; hasta respuesta, se migran las 10 (la fase 5 pide «fieles a `assets/*.html`»).
2. **Hay medias queries fuera de los 7 breakpoints.** DECISION-010 y la TASK piden «los 7 breakpoints de origen». El CSS compilado tiene 19 `@media`: 7 `min-width` de sass-mq, y 12 más (sección 5.3): 6 `max-width` (600, 700, 900, 980, 1140 px), 4 `max-height` (820, 900, 1000 y 1100 px), un `min-width:1400px` que duplica `ultrawide` y un `@media screen` sin condición. Los 7 valores sí existen. Hay que decidir si los otros 12 se mantienen como breakpoints propios de `@theme` o se resuelven como excepciones.
3. **Sólo hay 3 pesos de Poppins, no 5.** `assets/fonts/` contiene Regular, Medium y SemiBold, cada uno en `.woff2` y `.woff`. El CSS pide también 300, 700 y «bolder» (sección 5.2). `sistema-web-assets.md` nombra Bold y ExtraBold: **no existen**.
4. **El ancho del contenedor es 1302 px, no 1200 px.** `.o-wrapper` tiene `max-width: 1302px` y `padding: 30px` (CSS compilado y `objects/_objects.wrapper.scss`). `sistema-web-assets.md` dice 1200 px.
5. **Dos referencias de imagen rotas en el origen.** Se migran rotas y se listan en el informe (sección 7.3).
6. **Enlaces internos a páginas que no existen.** `test.html`, `blog.html`, `buscar.html` y `portafolio-detalle.html` (sección 8). Se migran tal cual.
7. **El botón de contacto de la cabecera lo cambia el JS al cargar.** El código de `main.js` deja la clase `c-button--sky-blue` salvo que el héroe sea `c-hero--blue`, `c-hero--dark-purple` o `c-hero--purple`. Así que el resultado visible depende de ese orden (sección 6.1, punto 9). **Pregunta:** ¿es intención o está invertido?
8. **Un `c-hero--blue` que el JS busca no existe en ninguna maqueta.** Sólo está en el selector del JS.
9. **`components.js` no se carga en ninguna página** (sección 6.2). Es código muerto del origen.
10. **Sin versiones de librería.** `sistema-web-assets.md` dice que jQuery, Modaal, AOS y tiny-slider no tienen versión explícita. En el bundle no he encontrado la cadena de versión (`jQuery v…`); no lo puedo afirmar más allá de eso.

---

## 3. Páginas

Diez maquetas. Métricas tomadas del HTML de cada una.

| Maqueta | `<title>` | Héroe (`c-hero--…`) | `data-aos` | «Lorem» | Formulario (`action`) | Modal | Slider |
| --- | --- | --- | --: | --: | --- | --- | --- |
| `index.html` | Laboratorio digital de Marketing & Software 👋 \| Pharmaco | purple-original | 9 | 3 | — | — | clientes |
| `nosotros.html` | Conoce Nuestro Laboratorio \| Pharmaco | light-purple | 5 | 0 | — | — | clientes |
| `servicios.html` | Hacemos que las cosas pasen \| Pharmaco | dark-purple | 12 | 0 | — | — | — |
| `servicio-detalle.html` | Hacemos que las cosas pasen \| Pharmaco | dark-purple | 7 | 2 | sí (`#`) | — | — |
| `portafolio.html` | Conoce nuestras soluciones \| Pharmaco | light-purple | 10 | 9 | — | — | — |
| `contactanos.html` | Contáctanos desde el medio que prefieras \| Pharmaco | purple | 1 | 0 | sí (`#`) | — | — |
| `campana-cyberwow.html` | Conoce nuestras soluciones \| Pharmaco | strong-blue | 1 | 9 | — | vídeo ×1 | — |
| `campana-iveco.html` | Conoce nuestras soluciones \| Pharmaco | medium-blue | 1 | 9 | — | — | — |
| `campana-stralis.html` | Conoce nuestras soluciones \| Pharmaco | orange | 1 | 9 | — | vídeo ×4 | — |
| `diseño-de-personajes.html` | Conoce nuestras soluciones \| Pharmaco | paleturquoise | 6 | 9 | — | imagen ×1 | — |

Todas las páginas comparten: cabecera (`c-site-header`, con el menú móvil y el overlay), héroe, sección, pie (`c-site-footer`), `main.js` y `css/main.css`, la precarga de los tres `.woff2` de Poppins, y el `<h1>` único. El `<title>` del menú «Abri navegación» tiene una errata en todas las páginas (sección 8).

**Conteos totales:** 53 atributos `data-aos` (fade-left 26, fade-right 16, fade-in 10, zoom-in 1; `data-aos-delay` 50, 100 o 150 y `data-aos-once`).

---

## 4. Componentes

Bloques BEM del HTML y en qué páginas aparecen. «todas» son las 10.

| Bloque | Páginas | Nº |
|---|---|---|
| `.c-button` | todas | 10 |
| `.c-button-line` | todas | 10 |
| `.c-button-next` | servicios | 1 |
| `.c-button-view-all` | index | 1 |
| `.c-carrousel-format` | campana-cyberwow, campana-stralis | 2 |
| `.c-clients` | index, nosotros | 2 |
| `.c-contact-form` | contactanos, servicio-detalle | 2 |
| `.c-contact-form-checkboxes` | contactanos | 1 |
| `.c-contact-form-radios` | contactanos | 1 |
| `.c-contact-options` | contactanos | 1 |
| `.c-content-block` | servicio-detalle, servicios | 2 |
| `.c-featured-ads` | campana-cyberwow | 1 |
| `.c-featured-stories` | campana-cyberwow, campana-stralis | 2 |
| `.c-format-album` | campana-cyberwow | 1 |
| `.c-format-canvas` | campana-stralis | 1 |
| `.c-format-magazine` | campana-iveco | 1 |
| `.c-format-web` | campana-iveco | 1 |
| `.c-gallery` | campana-cyberwow, campana-stralis, diseño-de-personajes | 3 |
| `.c-gallery-grid` | campana-cyberwow, campana-stralis | 2 |
| `.c-gallery-teaser` | diseño-de-personajes | 1 |
| `.c-header-controls` | todas | 10 |
| `.c-hero` | todas | 10 |
| `.c-main-content` | todas | 10 |
| `.c-media-block` | index, nosotros, servicios | 3 |
| `.c-media-block-reasons` | servicio-detalle | 1 |
| `.c-media-block-services` | servicio-detalle | 1 |
| `.c-note` | servicio-detalle | 1 |
| `.c-overlay` | todas | 10 |
| `.c-page-breadcrumb` | campana-cyberwow, campana-iveco, campana-stralis, diseño-de-personajes, servicio-detalle | 5 |
| `.c-process-teaser` | diseño-de-personajes | 1 |
| `.c-project-teaser` | index, portafolio | 2 |
| `.c-projects-teasers` | index, portafolio | 2 |
| `.c-publication` | campana-iveco | 1 |
| `.c-section` | todas | 10 |
| `.c-services-teaser` | index, servicios | 2 |
| `.c-services-teasers` | index, servicios | 2 |
| `.c-simple-banner` | campana-cyberwow, campana-stralis | 2 |
| `.c-site-footer` | todas | 10 |
| `.c-site-footer-nav` | todas | 10 |
| `.c-site-footer-social` | todas | 10 |
| `.c-site-header` | todas | 10 |
| `.c-site-header-nav` | todas | 10 |
| `.c-team-member` | nosotros, servicio-detalle | 2 |
| `.c-team-members` | nosotros, servicio-detalle | 2 |
| `.c-videos` | campana-cyberwow, campana-stralis | 2 |
| `.c-videos-banner` | campana-cyberwow, campana-stralis | 2 |
| `.c-videos-grid` | campana-stralis | 1 |
| `.c-views` | diseño-de-personajes | 1 |
| `.c-web-content` | campana-cyberwow | 1 |
| `.o-crop` | index, portafolio | 2 |
| `.o-icon` | todas | 10 |
| `.o-list-bare` | todas | 10 |
| `.o-wrapper` | todas | 10 |
| `.s-cms-content` | campana-cyberwow, campana-iveco, campana-stralis, diseño-de-personajes, index, nosotros, servicio-detalle, servicios | 8 |
| `.u-hidden-visually` | todas | 10 |

**Nota:** el `.c-hero` tiene 10 modificadores en total, uno por página (sección 3). Los `.c-site-header-nav__*` de la sublista del menú (`js-menu-link-dropdown`, `js-site-header-nav-sublist`) **no aparecen en ninguna maqueta**; sólo existen en el JS.

---

## 5. Tokens

Valores del CSS compilado (`css/main.css`). **Los nombres de token no se pueden sacar del origen:** el archivo de settings no está en el mapa. Los nombres `$color-*` de `sistema-web-assets.md` no aparecen en ninguna fuente disponible; sólo se conservan los valores. En fase 2 se les pone nombre por rol observado en el CSS, y el nombre se declara en el hilo.

### 5.1 Colores

Los 57 hex se tokenizan en `src/styles/styles.css` (fase 2). Comprobación: los 57 hex del CSS origen son los 57 de `@theme`, sin sobrantes ni faltantes.

**57 colores hexadecimales distintos** en `main.css`, más 10 `rgba()`. Número de apariciones entre paréntesis.

| Color | Apariciones | | Color | Apariciones |
|---|--:|---|---|--:|
| `#fff` | 52 | | `#afb7bc` | 2 |
| `#5956e9` | 16 | | `#2f2f2f` | 2 |
| `#111029` | 8 | | `#433fe6` | 2 |
| `#6b6b6b` | 8 | | `#4d30a0` | 2 |
| `#4c40f7` | 6 | | `#9da4ac` | 2 |
| `#a7a7a7` | 6 | | `#d6dade` | 2 |
| `#666` | 4 | | `#6e7177` | 2 |
| `#be0000` | 4 | | `#f4f4f4` | 2 |
| `#000` | 3 | | `#ff0`, `#b93d0c`, `#555`, `#442a8c`, `#473bf7`, `#b8defa`, `#b3dcfa`, `#392f9c`, `#2d29e3`, `#f0f5f8`, `#787878`, `#73dcde`, `#eaeaeb`, `#929292`, `#afe7e9`, `#fa832b`, `#2565b8`, `#0030ff`, `#7c56e9`, `#7ad5f2`, `#6490ff`, `#8082c0`, `#ff99fb`, `#b896ff`, `#888`, `#7d7afa`, `#b27afa`, `#bb85e5`, `#ffeddc`, `#bddeff`, `#bdf8ff`, `#f3d1ff`, `#d9c7ff`, `#ffe2e2`, `#999fae`, `#cfcfcf`, `#edf0f3` | 1 cada uno |
| `#ffd027` | 3 | | `#3a30a0` | 3 |
| `#00113b` | 3 | | | |

Rgba: `rgba(0,0,0,.08)` ×4, `rgba(0,0,0,0)` ×2, `rgba(0,0,0,.15)` ×2, `rgba(0,0,0,.2)`, `rgba(0,0,0,.3)`, `rgba(89,86,233,.2)`, `rgba(0,0,0,.4)`, `rgba(0,0,0,.16)`, `rgba(0,0,0,.1)`, `rgba(0,0,0,.7)`.

**Fuera de `main.css`:**
- `#3a30a0` en `<meta name="theme-color">`, `msapplication-TileColor` y `mask-icon` de todas las páginas.
- `style="color: #5956E9"` en `servicios.html` y en `servicio-detalle.html`: el único estilo inline de las maquetas. Es el mismo valor que `#5956e9` con otra capitalización; según la fase 2 se extrae a token.

### 5.2 Tipografía

- **Familia:** `Poppins` en `@font-face` (3 pesos, `.woff2` y `.woff`). Pilas de respaldo: `Poppins,Arial,Helvetica,sans-serif` (1 vez), `Helvetica` (1), `monospace,monospace` (2), `sans-serif` (1), `inherit` (2).
- **Pesos pedidos por el CSS:** 600 (12 veces), 500 (10), 400 (5), 700 (4), 300 (1), `bolder` (1), `inherit` (1). **Sólo hay archivos de 400, 500 y 600.** Lo que pidan 300 y 700 lo decidirá el navegador entre los archivos existentes; no está verificado en navegador.
- **Tamaños en píxeles** (27 valores distintos): 9, 10, 12, 14, 16, 17, 18, 19, 20, 21, 22, 24, 27, 28, 30, 32, 35, 37, 39, 40, 42, 44, 49, 63, 64, 77 y 84. Los más usados: 16 px (30 apariciones), 18 px (11), 14 px (10) y 20 px (10). Además hay `em`, `%` y `0`. Varios tamaños de titular cambian entre breakpoints. Los 27 son tokens en `src/styles/styles.css` (`--text-*`), desde la fase 2.
- **Espaciados e interlineados:** no se han listado todos en esta fase. La extracción completa es parte de la fase 2.

### 5.3 Breakpoints

**Los 7 de sass-mq** (`min-width`, en `em` con base de 16 px, y su equivalente en px):

| Nombre (`sistema-web-assets.md`) | Valor en el CSS | px |
|---|---|--:|
| mobile-small | `min-width: 22.5em` | 360 |
| mobile-mid | `min-width: 26.5625em` | 425 |
| mobile-wide | `min-width: 31.25em` | 500 |
| tablet | `min-width: 43.75em` | 700 |
| desktop | `min-width: 61.25em` | 980 |
| wide | `min-width: 75em` | 1200 |
| ultrawide | `min-width: 87.5em` | 1400 |

El nombre viene de `sistema-web-assets.md`: no aparece en el CSS, que sólo tiene los valores.

**Los 12 `@media` restantes** (no son breakpoints del sistema, son reglas concretas):

- `max-width`: `61.24em` (≈980 px), `43.74em` (≈700 px), `37.5em` (600 px), `only screen and (max-width:600px)`, `screen and (max-width:900px)`, `only screen and (max-width:1140px)`.
- `max-height`: `820px`, `900px`, `1000px`, `1100px`.
- `only screen and (min-width:1400px)`: el mismo corte que `ultrawide`, escrito en px.
- `@media screen` sin condición (1).

Y: `prefers-reduced-motion` aparece **0 veces** en el CSS. El origen no contempla movimiento reducido.

### 5.4 Contenedor

Del SCSS (`objects/_objects.wrapper.scss`), compilado a `main.css`:
- `.o-wrapper`: `max-width: 1302px`; `padding: 0 30px`; márgenes automáticos.
- `.o-wrapper--small`: 1120 px. `--large`: 1440 px. `--full`: 100%. `--flush`: sin padding lateral.

### 5.5 Radios, sombras y otros

Los colores de Modaal (plugin de modales) están en `main.css` y se tokenizan igual que el resto. Dejan de tener uso cuando Modaal se sustituye, en la fase 6.

- **Radios** (19 valores distintos en `border-radius`: 15 en px, `50%`, `100%`, `0` y `0 !important`): 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 28 y 40 px; 50% (9 apariciones) y 100%. Los de px son tokens `--radius-*` en `styles.css`, y `50%` y `100%` son `--radius-circle` y `--radius-round`.
- **Sombras:** `4px 5px 13px rgba(0,0,0,.08)` (3), `0 0 0 2px #ffd027` (2, foco), `1.58463px 1.58463px 6.33854px rgba(0,0,0,.15)` (2), `0 4px 15px rgba(0,0,0,.2)`, `0 0 10px rgba(0,0,0,.3)`, `0 4px 8px rgba(0,0,0,.08)`, `0 3px 6px 0 rgba(0,0,0,.16)`, `6px 10px 24px rgba(0,0,0,.1)` (1 cada una). Además `none` (6 entre `none` y `none!important`).
- **Animación:** `@keyframes instaReveal` y `modaal-loading-spinner`.

---

## 6. JavaScript

`assets/js/main.js` es el único script que cargan las 10 maquetas (`<script src="js/main.js">`). Contiene jQuery, jquery-validation, Modaal, tiny-slider y AOS empaquetados, y al final el código de aplicación. La lista siguiente es el **código de aplicación**: lo que hay que reproducir sin jQuery.

### 6.1 Comportamientos

1. **AOS.** `AOS.init()` sin opciones. Anima los 53 `data-aos` (sección 3).
2. **Desplazamiento a ancla.** Clic en `a[href^="#"]` (sin `.has-dropdown`) desplaza la página al destino con `$('html, body').animate`. Si la URL trae `#ancla` al cargar, desplaza a ella tras `load`. Fuente: `tools/tools.go-to-element.js` (en el mapa) y el bundle.
3. **Foco visible por teclado.** `Tab` añade `is-keyboard-pressed` al `<body>`. Un clic o `mousedown` lo quita salvo en radios, checkboxes, botones y `a[href="#"]`. Fuente: `tools/tools.focus-on-keydown.js`.
4. **Animación parada al redimensionar.** Cada `resize` añade `u-resize-animation-stopper` al `<body>` y lo quita 400 ms después. Fuente: `tools/tools.stop-transition-on-resize.js`.
5. **Menú móvil.** Botón `.js-site-header-menu-button` (abre) y `.js-site-header-close-menu-button` (cierra). Al abrir: `aria-expanded="true"` en ambos, `is-active` en `.js-site-header-nav-wrapper` y en `.js-overlay`, y foco atrapado dentro del panel. Al cerrar: `aria-expanded="false"` y foco devuelto al botón que abrió. Cierran el menú: `Escape`, el clic fuera del header y el clic en el overlay.
6. **Sublista del menú.** `toggleSublist` y `closeAllSublits` existen en el JS, pero sus hooks (`.js-menu-link-dropdown`, `.js-site-header-nav-sublist`) **no están en ninguna maqueta**. Código muerto.
7. **Botón de contacto de la cabecera.** Si `.c-hero` tiene `c-hero--blue`, `c-hero--dark-purple` o `c-hero--purple`, no hace nada. En cualquier otro caso cambia `c-button--purple` por `c-button--sky-blue` en `.c-header-controls__contact`. Ver sección 2, punto 7.
8. **Carrusel de clientes.** tiny-slider sobre `.js-clients-slider`: `items: 1`, `gutter: 20`, `nav: false`, `controlsContainer: .js-clients-slider-controls`, `responsive: {700: {items: 3}, 980: {items: 5}}`. Lo usan `index` y `nosotros`. Los botones `.js-clients-slider-prev` y `-next` están en el HTML con `aria-label` («Anterior slide», «Siguiente slide»). Si tiny-slider los usa o crea los suyos **no está verificado en navegador**.
9. **Filtros de entrada.** `.js-only-numbers` (sólo dígitos), `.js-only-letters` (letras con acentos, apóstrofo, espacio y guion), `.js-only-alpha-numeric` y `.js-only-phone` (dígitos y guion). Se aplican sobre `input`, `keydown`, `keyup`, `mousedown`, `mouseup`, `select`, `contextmenu` y `drop`. **`.js-only-email` tiene hook en el HTML pero ningún filtro en el JS.**
10. **Validación de formularios (jquery-validation).** Sobre `.js-form` (contactanos, servicio-detalle): `errorClass: js-form-error`, `validClass: js-form-valid`. El error del grupo de checkboxes va a `.js-contact-form-checboxes-error`, el de los demás campos se inserta tras el campo. Al enviar: añade `js-form--loading` al formulario, deshabilita el botón `[type=submit]` y llama a `form.submit()`. Los mensajes de validación en español están en el bundle (`$.extend($.validator.messages, …)`); se copian tal cual. Regla de correo: `^\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b$`, insensible a mayúsculas.
11. **Campo de empresa.** En contactanos, el radio `.js-contact-form-radio-business` (valor «Empresa») muestra `.c-contact-form__item--business` y habilita `.js-contact-form-business-name`. El radio «Persona Natural» (`.js-contact-form-radio-person`, marcado por defecto) hace lo contrario. El campo empresa empieza deshabilitado.
12. **Campo de mensaje.** En contactanos, el checkbox `.js-contact-form-checkbox-message` («Deseo contar un poco sobre mi idea») muestra `.c-contact-form__item--textarea` y habilita el textarea `.js-contact-form-textarea-message`. Empieza deshabilitado.
13. **Modales (Modaal).** `.video-modal-js` abre modal de tipo `video` (enlaces a YouTube embed). `.image-modal-js` abre modal de tipo `image`. Lo usan campana-cyberwow, campana-stralis (vídeo) y diseño-de-personajes (imagen).

### 6.2 `components.js`

Bundle aparte con el índice de componentes (`.c-components-index`), que construye la lista a partir de las secciones con `id`. **Ninguna de las 10 maquetas lo carga.** No se migra. Se anota aquí para que nadie lo busque después.

### 6.3 Dependencias que se sustituyen

| Hoy | Sustituto (DECISION-010) | Dónde se usa |
| --- | --- | --- |
| jQuery | JavaScript nativo | Todo el `main.js` |
| jquery-validation | Validación nativa del formulario y una función propia | contactanos, servicio-detalle |
| Modaal | `<dialog>` + `showModal()` + `inert` | cyberwow, stralis, diseño-de-personajes |
| AOS | `IntersectionObserver` + CSS, con `prefers-reduced-motion` | 10 páginas |
| tiny-slider | `scroll-snap` + botones propios, con fallback | index, nosotros |

---

## 7. Assets

### 7.1 Archivos

- **`assets/images/`:** 485 archivos, 136 MB. Por extensión: 233 `.webp`, 123 `.png`, 110 `.jpg`, 16 `.svg`, 1 `.xml`, 1 `.webmanifest`, 1 `.ico`.
- **`assets/fonts/`:** 6 archivos (Poppins Regular, Medium y SemiBold, en `.woff2` y `.woff`). 372 KB.
- **Sprite de iconos:** `images/icons/icons.svg` con 12 símbolos usados: `icon-arrow-left`, `icon-arrow-right`, `icon-chevron-right`, `icon-close`, `icon-facebook`, `icon-instagram`, `icon-linkedin`, `icon-menu`, `icon-search`, `icon-to-top`, `icon-web`, `icon-youtube`.
- **Favicons:** `images/favicon/` (apple-touch-icon, favicon 16 y 32, `.ico`, `safari-pinned-tab.svg`, `site.webmanifest`, `browserconfig.xml` referenciado en un `<meta>`).

### 7.2 Referencias

Se comprobaron **487 referencias locales** (por página, sin deduplicar entre páginas). Sólo 2 apuntan a un archivo que no existe. La comparación se hizo con Unicode normalizado (NFC), porque los nombres con tilde (`diseño`, `campaña`) pueden estar escritos de dos formas en el HTML y en disco.

### 7.3 Referencias rotas

| Página | Referencia | Lo que hay en disco |
| --- | --- | --- |
| `campana-cyberwow.html` | `images/components/portafolio/campaña-cyberwow/video1-l.webp` | No existe. Hay `video-lg.webp` y `video-sm.webp` |
| `campana-iveco.html` | `images/components/portafolio/campaña-iveco/publicacion-revista-revista1-lg.webp` | No existe. Hay `publicacion-revista1-lg.webp` |

Se migran rotas. En fase 6 se anota en el informe; **no se cambia el nombre** sin decisión de Clia.

### 7.4 Recursos externos

- `https://www.youtube.com/embed/pa-A2g0wxPs`: 5 enlaces de vídeo (cyberwow ×1, stralis ×4), en modales.
- `https://wa.me/999999999/?text=Pharmaco+…` y `tel:999999999` (contactanos): **número de marcador**, no un número real. Se migra como está y se anota como pendiente de dato.
- `http://humaan.com` aparece como texto suelto en `main.css`, sin `url()` que lo cargue. No es un recurso del sitio.

---

## 8. Contenido

### 8.1 Texto de relleno, tal cual

- **«Lorem»:** 9 apariciones en cada una de cyberwow, iveco, stralis, diseño-de-personajes y portafolio; 3 en index y 2 en servicio-detalle. Ninguna en nosotros, servicios ni contactanos.
  - Campañas (cyberwow, iveco, stralis, diseño-de-personajes): un bloque de texto en inglés de relleno que empieza por «Lorem Ipsum is simply dummy text…».
  - Portafolio: **9 tarjetas**, cada una con `<p class="c-project-teaser__text">Lorem ipsum</p>`, y las 9 usan la misma imagen `images/components/projects/project-1.webp`.
- **«Desinf anything from simple clean style to fully featured websites…»:** aparece **una vez en las 10 páginas**. Es resto de plantilla con errata («Desinf»).
- **«Agency is a full-service agency, busy designing…»**: servicios.html, línea 243. Resto de plantilla en inglés.
- **Atributos `alt="alt"`:** 37 en los logos de clientes.
- **Etiquetas en inglés dentro de un sitio en español:** `aria-label="Anterior slide"` y `"Siguiente slide"`.

### 8.2 Erratas y datos a conservar

- **«Abri navegación»** en el `<title>` del botón de menú de las 10 páginas (debería ser «Abrir»). Se conserva.
- **Formulario de contacto (contactanos.html):** dos checkboxes con el mismo valor «Campañas publicitarias», uno con `id="campanasPublicitarias"` y otro con `id="campañasPublicitarias"`. Se conservan ambos; el `id` duplicado se anota.
- **Contrato del formulario**, que no se renombra: `tipo` (radio: «Persona Natural» / «Empresa»), `nombreApellido`, `telefono`, `correo`, `nombreEmpresa`, `servicios` (checkboxes), `mensaje`. Los valores de `servicios` son «Branding», «Social media», «Desarrollo de apps», «Otro servicio», «Campañas publicitarias» (×2), «Producción de videos» y «Deseo contar un poco sobre mi idea».
- **`action="#"`** en los dos formularios. No hay destino de envío.
- **Enlaces `href="#"`:** 11 en total, en cyberwow (2), iveco (2), stralis (2), diseño-de-personajes (2), portafolio (1) y servicio-detalle (2).

### 8.3 Catálogo de servicios

La lista de servicios de `servicios.html` y los 11 servicios de DECISION-002 **no son esta TASK**: el catálogo se trata en RFC-002. Aquí se migran los textos que hay en `assets/`, tal cual.

---

## 9. Correcciones a `sistema-web-assets.md`

Lo que el documento de TASK-004 dice y que al leer `assets/` no se sostiene. No se corrige el documento (es de Ania y no se edita); se deja aquí para la migración.

| `sistema-web-assets.md` | Lo que hay en `assets/` |
| --- | --- |
| Fuentes Poppins Bold (700) y ExtraBold (800) en `assets/fonts/` | No existen. Hay Regular, Medium y SemiBold |
| Tokens `$color-purple`, `$color-dark-blue`… | Los nombres no están en el mapa. Los valores hex sí (sección 5.1) |
| Contenedor `.o-wrapper` de 1200 px | 1302 px |
| Portafolio: «Grid de 8 proyectos» | 9 tarjetas |
| «Breakpoints: los 7» | Los 7 de sass-mq, más 12 `@media` propios (sección 5.3) |
| Jquery, Modaal, AOS y tiny-slider sin versión | Confirmado: sin versión en el bundle |
| «Textos simulados» en `portafolio.html` | Confirmado: 9 de 9 tarjetas con «Lorem ipsum» |
| Archivos `conf-server.bk.php`, `wp-config.bk.php`, `wp.txt` en la raíz del repositorio de WordPress | **No verificado**: no están en `assets/` ni en este repositorio. No se migran |

---

## 10. Pendientes para fases siguientes

- **Decisión de Clia:** 9 o 10 maquetas (sección 2.1).
- **Decisión de Clia:** los 12 `@media` propios: ¿se mantienen como breakpoints del sistema o como excepciones por componente? (sección 2.2)
- **Decisión de Clia:** el orden de la condición del botón de contacto (sección 2.7).
- **Fase 2:** nombres de los tokens de color y tamaño; escala de espaciados e interlineados completa.
- **Fase 6:** comportamiento de tiny-slider con `controlsContainer` en el navegador.
- **Fase 7:** capturas de cada página a 375 px y en escritorio, origen contra migración.
