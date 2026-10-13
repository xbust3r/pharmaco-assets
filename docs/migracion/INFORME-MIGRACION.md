# Informe de migración — web de assets a Blackgrow 2026, sin jQuery

> **Documento:** `docs/migracion/INFORME-MIGRACION.md` · **Tarea:** [TASK-006](../comms/TASK-006-migracion-blackgrow.md), fase 8
> **Autora:** Kia (DEV) · **Fecha:** 2026-10-13 · **Estado:** para REVIEW final de Dexia y sign-off 🔴 de Clia
> **Rama:** `feat/TASK-006-migracion-blackgrow`. Origen: `assets/` sin modificar (`git diff main -- assets/` vacío).

---

## 1. Qué se migró

- **10 maquetas** (`assets/*.html`) a `src/pages/*.pug`, sobre el layout `src/layouts/main-template.pug`. Textos copiados tal cual, con sus erratas (comprobado: el texto visible de `main`, cabecera y pie coincide carácter a carácter en las 10).
- **Cabecera y pie** como mixins (`src/components/site-header.pug`, `site-footer.pug`), con los `aria-label` del origen.
- **53 mixins de componentes repetidos** (177 llamadas) en `src/components/repetidos.pug` (tarjetas de servicios, proceso, equipo, logos, portafolio, héroes, bloques de contacto y de medios). Textos y atributos de contenido son parámetros; cada llamada lleva el nombre BEM de origen en un comentario `//- origen:`.
- **JavaScript nativo** en `src/scripts/main.js`, un único archivo (ver §3.4).
- **Iconos** del sprite del origen, extraídos a `src/assets/icons/` (13 símbolos). **Imágenes** referenciadas por las 10 páginas, copiadas a `src/assets/images/` (218 archivos, 31 MB).
- **Tokens** en `src/styles/styles.css` (`@theme`): 57 colores hex de `main.css`, 27 tamaños, 7 breakpoints en em, radios, sombras, Poppins 400/500/600.

## 2. Decisiones tomadas

| Decisión | Motivo | Quién |
| --- | --- | --- |
| Utilidades de Tailwind en el marcado; sin CSS de componente con nombres BEM | DECISION-010 y decisión A de Clia | Clia |
| Los 7 breakpoints de sass-mq como tokens; el resto de medias, como variantes | Decisión B de Clia | Clia |
| Sin preflight de Tailwind; reset del origen en `@layer base` | Mantener el render del origen | Kia, firmada |
| Orden de capas `theme, base, components, utilities` | Sin él, el reset ganaba a las utilidades (botón de contacto sin fondo) | Kia |
| Mixins `rep*` para lo que se repite en 2 o más sitios; resto, en la página | Decisión de Clia (fase 4) | Clia |
| Un solo `main.js` por la partición de Vite (ver §3.4) | `htmlAutonomo` exige un script por página | Kia |

## 3. Desviaciones del origen, con su motivo

### 3.1 Marcado y accesibilidad

- **Atributos `focusable="false"`** (de IE) quitados de los `svg`.
- **`rel="shortcut icon"`** pasa a `rel="icon"`: mismo efecto en navegador.
- **Iconos `svg` decorativos sin `<title>`** llevan `aria-hidden="true"` y no `role="img"`. Están dentro de enlaces con texto visible.
- **Enlaces de icono sin texto** reciben como nombre el `<title>` de su icono (servicios, «Ir a nuestro proceso»).
- **Botones del slider de clientes de nosotros** no tenían nombre accesible en el origen: se les pone `aria-label` («Anterior slide», «Siguiente slide»), copiado de ese mismo componente en la portada.
- **`source media="(min-width: 700px)"`** pasa a `43.75rem`: misma base de 16 px, y es lo que exige la regla de markuplint de Blackgrow.

### 3.2 Imágenes

- **`width`/`height` del `img`** se convierten en `aspect-[W/H]`. El origen los usa como proporción cuando el CSS deja el alto en automático, y algunos no coinciden con el archivo real. Quitarlos sin más dejaba el alto a 0 (detectado y corregido con la comprobación de geometría).
- **`height="auto"`** (valor inválido) se quita; el CSS fija el alto.
- **Dos imágenes rotas en el origen** (ver §4.2). Se migran sin archivo: en `campana-cyberwow` y `campana-iveco` el `img` de respaldo de un `picture` apunta al primer `source`, que es el que el navegador ya usaba. El `src` roto queda en un comentario `//-` de la página, para que el dato no se pierda.

### 3.3 Medias queries y estilos de origen

- **Breakpoints del origen:** los cortes de 700 y 980 px son `tablet` y `desktop`. Los de 360, 425, 500, 1200 y 1400 px son los demás breakpoints del sistema. Las reglas de 600, 900 y 1140 px del origen no producen ninguna variante en el marcado final; sólo queda **una** variante arbitraria, `min-[601px]:`, que es el complemento de un `max-width:600px` del origen. Pendiente de tokenizar.
- **Medias de altura** (820 a 1100 px): **no se migran**. El compilador las omite, así que no hay variantes ni tokens para ellas. No se ha comprobado si alguna regla afecta a un elemento de estas 10 páginas; queda como pendiente (inventario, sección 5.3).
- **`min-width:1400px` duplicado y `@media screen` sin condición**: no se migran (ruido del origen).
- **Pesos 300 y 700** de Poppins: el origen los pide y no hay archivos. Se migran igual; el navegador sintetiza el peso.

### 3.4 JavaScript (fase 6)

Sustituciones, sin dependencias nuevas, con `prefers-reduced-motion` respetado:

| Hoy (origen) | Migrado |
| --- | --- |
| jQuery | JavaScript nativo |
| Modaal | `<dialog>` único en el layout, `showModal()`, cierre con botón, Escape y clic fuera |
| AOS | `IntersectionObserver` (margen de 120 px, como el `offset` de AOS) y CSS; `data-reveal` y `data-reveal-delay` |
| tiny-slider | `scroll-snap` y botones propios; 1, 3 o 5 ítems según el ancho (700 y 980 px); separación de 20 px |
| jquery-validation | Validación nativa con los mensajes del origen; campos condicionales de empresa y mensaje; filtros de entrada |

Comportamientos del origen reproducidos: menú móvil con `is-active` y `aria-expanded`, foco atrapado, Escape y clic fuera, cambio de color del botón de contacto según el héroe, anclas con desplazamiento suave, foco por teclado (`is-keyboard-pressed`), y parada de transiciones al redimensionar.

Un único `main.js`: las 10 páginas son entradas separadas, y con formato `iife` Vite no admite varias entradas. Sin partir en trozos compartidos, Vite genera un solo script por página, que es lo que exige `htmlAutonomo` para abrir `dist/` con `file://`.

## 4. Pendientes y defectos del origen

### 4.1 Pendientes de fidelidad

- **Slider de clientes (`index`, `nosotros`).** La geometría no coincide con tiny-slider: el origen cambia el DOM al iniciar (clones y envoltorios). A 1280 px la altura coincide, pero hay 38 y 19 cajas desalineadas. Pendiente de ajuste fino.
- **`servicios` a 375 px**: la migración mide 289 px menos (8253 frente a 8542). A 1280 px coincide. Diferencias de 1 px en el bloque de contenido que se acumulan; el origen es el de referencia, y la causa no está identificada.
- **`servicio-detalle` a 375 px**: 13 px menos y 78 cajas desalineadas.
- **Tokens para valores arbitrarios repetidos.** `verify:render` avisa de 20 valores repetidos en las 10 páginas (por ejemplo, el ancho del logo de cabecera). Son valores del origen; ponerles nombre queda para una segunda pasada.
- **654 clases de propiedad arbitraria** (`[prop:valor]`), frente a utilidades con nombre. Es la forma menos idiomática del resultado: funciona y es fiel, pero es el primer candidato a limpiar.

### 4.2 Defectos del origen migrados tal cual

- **Enlaces a páginas inexistentes:** `test.html` (50 apariciones; también en el pie, en las redes), `blog.html` (20), `buscar.html` (10) y `portafolio-detalle.html` (16). Se migran tal cual.
- **Imágenes rotas:** `campana-cyberwow` (`video1-l.webp`) y `campana-iveco` (`publicacion-revista-revista1-lg.webp`). Ver §3.2.
- **Botón de contacto de la cabecera:** el JS lo deja en `sky-blue` salvo en héroes `blue`, `dark-purple` o `purple`. Parece invertido. Se reproduce tal cual hasta decisión.
- **Placeholders de teléfono:** `tel:999999999` y `wa.me/999999999`. Número de marcador, no dato real.
- **Textos de plantilla en inglés:** «Desinf anything from simple clean style…» (aparece en las 10 páginas) y «Agency is a full-service agency…» (`servicios`). `aria-label` del pie «Go to Southern Harvest's…». Se conservan por ser contenido del origen.
- **Erratas:** «Abri navegación» en el título del botón de menú; `aria-label` en inglés («Anterior slide», «Siguiente slide»).
- **Formulario:** dos `checkbox` con el mismo valor «Campañas publicitarias» (ids `campanasPublicitarias` y `campañasPublicitarias`); `action="#"` en los dos formularios.
- **`alt="alt"`** en los logos de clientes (37 apariciones) y `alt="#"` en las imágenes de campaña.
- **Lorem ipsum** en `portafolio` (9 tarjetas con la misma imagen `project-1.webp`) y en las campañas.
- **`components.js`** no lo carga ninguna maqueta: código muerto, no migrado.
- **`sistema-web-assets.md`** tiene errores: Poppins Bold y ExtraBold no existen; el contenedor es de 1302 px, no 1200; hay 9 tarjetas de portafolio, no 8. Ver inventario, sección 9.

### 4.3 Peso

- **Imágenes:** 218 archivos, 31 MB, copiados a `src/assets/images/` para que el build los sirva. Es mucho para un repositorio. Pregunta para Clia: ¿se versionan así, se usa LFS, o se sirven desde `assets/` como estáticos?

## 5. Verificación

Salida completa, con código de salida por comando, en `docs/migracion/logs/`.

| Comprobación | Resultado | Registro |
| --- | --- | --- |
| `pnpm optimize`, `lint`, `validate`, `build` | código 0 | `fase-7-verificacion.txt` |
| `pnpm verify:render` | código 0, 0 FALLOS, 116 AVISOS (ver §4.1) | `fase-7-verificacion.txt` |
| `pnpm validate:origen` (texto y hooks frente a `assets/`) | código 0, 0 FALLOS en las 10 páginas | `fase-7-verificacion.txt` |
| Geometría frente al origen, 1280 y 375 px | 8 de 10 páginas con la misma altura; desalineados en las 4 restantes (§4.1) | `fase-7-geometria.txt` |
| Capturas origen y migrada, 375 y 1280 px (viewport) | 40 PNG | `docs/migracion/capturas/fase7-*.png` |
| Errores de consola en el navegador | ninguno en `index`, `contactanos`, `servicio-detalle` y `campana-stralis` | verificación manual |
| Ausencia de jQuery, Modaal, AOS y tiny-slider en fuentes | 0 referencias (grep) | verificación manual |
| `git diff main -- assets/` | vacío | verificación manual |

`validate:origen` compara texto y hooks, no geometría; la geometría se mide con `docs/migracion/herramientas/geometria.mjs`, que necesita un navegador.

## 6. Cosas no verificadas

- **Visual a 375 y 1280 px** más allá del viewport inicial: sólo la altura total y las cajas (§5). Las capturas de página completa no se han revisado una a una.
- **Modales**: el aspecto del diálogo es una aproximación del de Modaal (fondo, sombra, anchura); no está comparado.
- **Formularios**: validación y campos condicionales probados por lectura de código; no se han enviado.
- **Navegadores**: sólo Chrome.
- **Revelado**: el momento de aparición se aproxima con `IntersectionObserver`; no es idéntico al de AOS.

## 7. Herramientas

`docs/migracion/herramientas/`: el generador de páginas (`generador/`) y el comparador de geometría (`geometria.mjs`), con su README. No forman parte del build.
