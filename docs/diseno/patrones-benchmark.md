# Patrones del benchmark (Parte B)

> **Documento:** `docs/diseno/patrones-benchmark.md` · **Tarea:** [TASK-004](../comms/TASK-004-sistema-de-diseno.md), Parte B
> **Autora:** Kia (DEV) · **Fecha:** 2026-10-12 · **Rama:** `feat/TASK-004-sistema-diseno`
> **Fuente única:** las 20 fichas de [`docs/investigacion/fichas/`](../investigacion/fichas/) (10 comparables y 10 referentes o especialistas), con la sección «Estructura de la web y diseño». El anexo `anexo-medianas/` no cuenta. Las fichas son las aceptadas en la undécima ronda de REVIEW-001 de TASK-001.
> **Estado:** documento de investigación. Describe patrones y su frecuencia; no elige dirección visual ni propone textos para la web. Eso es de `RFC-002`.

---

## 0. Qué se cuenta y cómo

- **No se han vuelto a abrir las webs.** Cada celda sale de una viñeta de una ficha, citada por su número de línea (`L`). Si TASK-001 cambia antes de cerrar, esta matriz se recalcula.
- **Tres valores por celda:**
  - **Sí**: la ficha lo atribuye a la portada o a la web.
  - **No**: la ficha lo contradice (por ejemplo, «fondo blanco»), o, en menús, la ficha enumera el menú y la categoría no aparece en la lista.
  - **NC** (no consta): la ficha no lo menciona. **NC no es No.** Que una ficha no revisara una sección no prueba que el patrón falte.
- **Denominador:** 20 en todas las frecuencias. Los «Sí» son mínimos: en 9 de los 11 patrones hay 6 o más NC.
- **Dos casos a tener en cuenta:** Dogstudio clasifica su portada como oscura porque la ficha describe una captura con un showreel oscuro, pero esa captura muestra sobre todo un cargador animado. Monopo tiene una portada con «captura sin contenido legible», y su patrón de vídeo o animación viene de la descripción de la ficha, no de la captura.

---

## 1. Arquitectura

### 1.1 Menús, páginas y secciones

| Elemento | Fichas que lo describen | Lectura |
| --- | --- | --- |
| Menú principal | 20 de 20 | Todas listan su menú. Es lo más homogéneo de la muestra. |
| Lista de secciones de la home | 3 sin advertencia (`artefact`, `devibi`, `tescanet`); 16 con advertencia de que no está revisada o no es completa; 1 sin viñeta (`monopo`) | Tres fichas listan las secciones «en orden» sin advertir que la lista sea parcial; las otras 16 advierten que no está revisada o no es completa. **No hay un orden común verificable.** |
| Anatomía de página de servicio | 17 de 20 | Tres no la describen: `devibi` dice que no está revisada en detalle; `dogstudio` y `monopo` no tienen viñeta. |
| Anatomía de página de caso | 12 de 20 | Ocho no tienen viñeta de caso. |
| Casos o trabajos en el menú (A2) | Sí 10 · No 7 · NC 3 | Diez menús incluyen «Work», «Trabajos», «Portafolio», «Our Cases» o equivalente. |
| Blog, noticias o contenido editorial en el menú (A3) | Sí 13 · No 7 · NC 0 | Trece incluyen blog, noticias, «Insights», «Resources», «Learn», «Press» o «Latest». |
| Selector de idioma (A4) | Sí 4 · NC 16 | Solo cuatro fichas describen un selector: `agencia-buffalo`, `artefact`, `media-monks` y `studiodigital`. |

### 1.2 Anatomía repetida

Las fichas describen páginas de servicio y de caso con elementos recurrentes: titular grande, bloque de texto, un CTA y, en casos, una ficha lateral o una cifra. Los conteos de cada elemento no se han hecho porque las viñetas no siguen un formato común. Se usan las frecuencias de la sección 2 cuando una descripción es comparable.

---

## 2. Matriz de observaciones (20 agencias × 11 patrones)

Leyenda de los patrones:

- **A1**: Botón de acción (CTA) en el encabezado.
- **A2**: Casos o trabajos en el menú principal.
- **A3**: Blog, noticias o contenido editorial en el menú.
- **A4**: Selector de idioma visible.
- **V1**: Serif en titulares o en el texto principal.
- **V2**: Sans en titulares o en el texto principal.
- **V3**: Fondo oscuro como fondo principal.
- **V4**: Vídeo o animación en la portada.
- **V5**: Logotipos o sección de clientes en la portada.
- **V6**: Cifras o métricas en la portada.
- **V7**: Testimonios, valoraciones o citas de terceros en la portada.

Cada fila enlaza a la ficha. Las letras `L` de la lista de evidencia indican la línea de la viñeta que sostiene el valor.

| Agencia (ficha) | A1 | A2 | A3 | A4 | V1 | V2 | V3 | V4 | V5 | V6 | V7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [agencia-buffalo](../investigacion/fichas/agencia-buffalo.md) | Sí | Sí | Sí | Sí | NC | Sí | No | NC | NC | NC | NC |
| [artefact](../investigacion/fichas/artefact.md) | Sí | NC | Sí | Sí | Sí | NC | NC | Sí | Sí | Sí | Sí |
| [blueorange-digital](../investigacion/fichas/blueorange-digital.md) | Sí | No | Sí | NC | Sí | NC | Sí | Sí | NC | Sí | NC |
| [code-and-theory](../investigacion/fichas/code-and-theory.md) | Sí | Sí | Sí | NC | Sí | Sí | Sí | NC | NC | NC | Sí |
| [devibi](../investigacion/fichas/devibi.md) | Sí | Sí | Sí | NC | NC | NC | No | Sí | NC | NC | NC |
| [digiberries-paris](../investigacion/fichas/digiberries-paris.md) | Sí | NC | No | NC | NC | Sí | No | NC | Sí | NC | Sí |
| [dogstudio](../investigacion/fichas/dogstudio.md) | NC | Sí | No | NC | NC | NC | Sí | Sí | NC | NC | NC |
| [instrument](../investigacion/fichas/instrument.md) | Sí | Sí | Sí | NC | Sí | NC | No | Sí | Sí | NC | NC |
| [media-monks](../investigacion/fichas/media-monks.md) | NC | Sí | No | Sí | Sí | NC | NC | NC | NC | NC | NC |
| [monopo](../investigacion/fichas/monopo.md) | NC | Sí | Sí | NC | NC | NC | NC | Sí | NC | NC | NC |
| [pallax-media](../investigacion/fichas/pallax-media.md) | Sí | No | No | NC | NC | NC | No | NC | NC | NC | Sí |
| [screenfire-media](../investigacion/fichas/screenfire-media.md) | NC | No | Sí | NC | NC | NC | NC | NC | Sí | NC | NC |
| [single-grain](../investigacion/fichas/single-grain.md) | Sí | No | Sí | NC | Sí | NC | Sí | Sí | Sí | Sí | NC |
| [sitelabs](../investigacion/fichas/sitelabs.md) | Sí | Sí | No | NC | NC | Sí | No | NC | NC | Sí | NC |
| [stratagemma-studio](../investigacion/fichas/stratagemma-studio.md) | NC | No | No | NC | NC | Sí | Sí | NC | NC | NC | NC |
| [studiodigital](../investigacion/fichas/studiodigital.md) | Sí | No | No | Sí | NC | NC | Sí | NC | NC | Sí | NC |
| [tescanet](../investigacion/fichas/tescanet.md) | Sí | Sí | Sí | NC | Sí | NC | NC | Sí | NC | NC | NC |
| [trajectory-web-design](../investigacion/fichas/trajectory-web-design.md) | Sí | Sí | Sí | NC | NC | NC | NC | NC | Sí | NC | NC |
| [upraw-media](../investigacion/fichas/upraw-media.md) | Sí | No | Sí | NC | NC | NC | Sí | Sí | Sí | NC | Sí |
| [work-and-co](../investigacion/fichas/work-and-co.md) | NC | NC | Sí | NC | Sí | Sí | No | NC | NC | NC | Sí |

### 2.1 Frecuencias

Las frecuencias salen de la matriz de arriba (20 observaciones por patrón):

| Patrón | Sí | No | NC | Total |
| --- | --- | --- | --- | --- |
| **A1** Botón de acción (CTA) en el encabezado | 14 | 0 | 6 | 20 |
| **A2** Casos o trabajos en el menú principal | 10 | 7 | 3 | 20 |
| **A3** Blog, noticias o contenido editorial en el menú | 13 | 7 | 0 | 20 |
| **A4** Selector de idioma visible | 4 | 0 | 16 | 20 |
| **V1** Serif en titulares o en el texto principal | 8 | 0 | 12 | 20 |
| **V2** Sans en titulares o en el texto principal | 6 | 0 | 14 | 20 |
| **V3** Fondo oscuro como fondo principal | 7 | 7 | 6 | 20 |
| **V4** Vídeo o animación en la portada | 9 | 0 | 11 | 20 |
| **V5** Logotipos o sección de clientes en la portada | 7 | 0 | 13 | 20 |
| **V6** Cifras o métricas en la portada | 5 | 0 | 15 | 20 |
| **V7** Testimonios, valoraciones o citas de terceros en la portada | 6 | 0 | 14 | 20 |

### 2.2 Evidencia por patrón (líneas de cada ficha)

Cada línea lista la agencia y la línea de la ficha. Las agencias marcadas NC no aparecen.

- **A1** Sí: agencia-buffalo (L65), artefact (L72), blueorange-digital (L67), code-and-theory (L68), devibi (L64), digiberries-paris (L70), instrument (L66), pallax-media (L70), single-grain (L65), sitelabs (L68), studiodigital (L73), tescanet (L71), trajectory-web-design (L70), upraw-media (L67). No: —.
- **A2** Sí: agencia-buffalo (L65), code-and-theory (L64), devibi (L61), dogstudio (L64), instrument (L62), media-monks (L65), monopo (L62), sitelabs (L65), tescanet (L68), trajectory-web-design (L66). No: blueorange-digital (L63), pallax-media (L67), screenfire-media (L65), single-grain (L61), stratagemma-studio (L66), studiodigital (L70), upraw-media (L63).
- **A3** Sí: agencia-buffalo (L65), artefact (L68), blueorange-digital (L63), code-and-theory (L64), devibi (L61), instrument (L62), monopo (L62), screenfire-media (L65), single-grain (L61), tescanet (L68), trajectory-web-design (L66), upraw-media (L63), work-and-co (L66). No: digiberries-paris (L70), dogstudio (L64), media-monks (L65), pallax-media (L67), sitelabs (L65), stratagemma-studio (L66), studiodigital (L70).
- **A4** Sí: agencia-buffalo (L65), artefact (L68), media-monks (L70), studiodigital (L70). No: —.
- **V1** Sí: artefact (L74), blueorange-digital (L69), code-and-theory (L70), instrument (L68), media-monks (L68), single-grain (L67), tescanet (L73), work-and-co (L72). No: —.
- **V2** Sí: agencia-buffalo (L70), code-and-theory (L70), digiberries-paris (L75), sitelabs (L70), stratagemma-studio (L71), work-and-co (L72). No: —.
- **V3** Sí: blueorange-digital (L69), code-and-theory (L70), dogstudio (L65), single-grain (L67), stratagemma-studio (L71), studiodigital (L75), upraw-media (L69). No: agencia-buffalo (L70), devibi (L66), digiberries-paris (L75), instrument (L68), pallax-media (L72), sitelabs (L70), work-and-co (L72).
- **V4** Sí: artefact (L75), blueorange-digital (L64), devibi (L62), dogstudio (L66), instrument (L69), monopo (L63), single-grain (L68), tescanet (L74), upraw-media (L64). No: —.
- **V5** Sí: artefact (L69), digiberries-paris (L71), instrument (L63), screenfire-media (L66), single-grain (L62), trajectory-web-design (L67), upraw-media (L64). No: —.
- **V6** Sí: artefact (L69), blueorange-digital (L64), single-grain (L62), sitelabs (L66), studiodigital (L71). No: —.
- **V7** Sí: artefact (L69), code-and-theory (L65), digiberries-paris (L71), pallax-media (L68), upraw-media (L64), work-and-co (L67). No: —.

### 2.3 Capturas de ejemplo

Estas dos capturas son de TASK-001 y se han mirado para este documento:

- **Fondo oscuro (V3, Sí):** [blueorange-digital-home.png](../investigacion/capturas/blueorange-digital-home.png). La portada tiene fondo azul marino oscuro y un panel de métricas en el bloque superior. La ficha dice que las métricas se animan (líneas 64 y 69); una captura fija no muestra la animación, así que ese punto no se confirma aquí.
- **Vídeo en la portada (V4, Sí):** [instrument-home.png](../investigacion/capturas/instrument-home.png). Se ve un vídeo enmarcado sobre fondo crema, con el botón de pausa abajo a la izquierda, como dice la ficha en las líneas 68 y 69. La captura tiene el banner de cookies sin aceptar. No se ha aceptado nada.

---

## 3. Contraste con la web de assets

Esta tabla pone juntos lo que hay en la web de assets (medido en `sistema-web-assets.md`) y lo que muestra el benchmark. Es un contraste de evidencia. Cada fila termina en opciones; ninguna es una recomendación.

| Patrón | Web de assets (medido) | Benchmark (Sí · No · NC) | Opciones con evidencia para `RFC-002` |
| --- | --- | --- | --- |
| **A1** CTA en el encabezado | Sí: «Contáctanos» como botón morado grande en la cabecera de `index.html`. | 14 · 0 · 6 | Opción A: conservar el botón de contacto tal cual. Opción B: cambiar su texto por una acción distinta, como ya hacen «Agendar una reunión» (`agencia-buffalo`, L65), «Presupuesto» (`sitelabs`, L68) o «Start a project» (`devibi`, L64). |
| **A2** Casos en el menú | Sí: «Portafolio» en el menú de `index.html`. | 10 · 7 · 3 | Las agencias que llevan casos en el menú lo nombran «Work», «Trabajos», «Portafolio» o «Our Cases». El benchmark reparte casi igual entre incluirlo y no incluirlo en el menú. |
| **A3** Blog o noticias en el menú | Sí: «Blog» en el menú, con enlace a `blog.html`, que no está en `assets/`. | 13 · 7 · 0 | Opción A: mantener la entrada de blog. Opción B: sustituirla por «Press», «Insights» o «Learn», como hacen algunas fichas. El enlace roto es un pendiente de la web de assets, no del benchmark. |
| **A4** Selector de idioma | No: la cabecera de `index.html` no tiene selector. | 4 · 0 · 16 | Solo cuatro fichas describen selector. Con tan pocas observaciones, el dato no permite decidir. |
| **V1** Serif en titulares | No: la pila declarada es Poppins con respaldo `sans-serif`; no hay serif. | 8 · 0 · 12 | Las ocho fichas con serif lo usan en titulares o en el texto principal, sobre todo en casos y en la portada. Opción A: mantener la tipografía sans. Opción B: introducir una serif en titulares de casos, con el coste de cargar otra familia. |
| **V2** Sans en titulares | Sí: Poppins es sans, y la pila la declara primero. | 6 · 0 · 14 | Las fichas que lo describen coinciden con la web de assets. Casi todo lo demás no consta. |
| **V3** Fondo oscuro principal | No como fondo general: `#ffffff` y `#f0f5f8` en las secciones; el héroe es morado (`#7c56e9`) y el pie es `#00113b`. | 7 · 7 · 6 | El benchmark se reparte por igual entre fondo oscuro y claro. Opción A: mantener fondo claro con héroe de color. Opción B: fondo oscuro en la portada, con las fichas `blueorange-digital` (L69) y `single-grain` (L67) como ejemplos. |
| **V4** Vídeo o animación en la portada | Animación: sí, con AOS (9 atributos `data-aos` en `index.html`). Vídeo incrustado: no; la portada solo tiene un icono de YouTube. | 9 · 0 · 11 | El benchmark usa vídeo o animación en 9 de 20 portadas, pero la mayoría no consta. Opción A: animaciones ligeras como las de AOS. Opción B: vídeo de fondo, como `instrument`. |
| **V5** Clientes en la portada | Sí: bloque de clientes con deslizador (`c-clients`), con imágenes de `images/components/clients/`. | 7 · 0 · 13 | Coincide en presencia. Las 13 fichas que no lo describen no permiten concluir nada. |
| **V6** Cifras en la portada | No: la portada de `index.html` no tiene bloque de cifras. | 5 · 0 · 15 | Cinco fichas tienen cifras en portada (`artefact`, `blueorange-digital`, `single-grain`, `sitelabs`, `studiodigital`). Opción A: sin cifras. Opción B: un bloque de cifras, con la fuente de cada cifra en la web de Pharmaco. |
| **V7** Testimonios o citas | No: `index.html` no tiene bloque de testimonios ni de citas. | 6 · 0 · 14 | Las seis fichas que lo describen usan testimonios, valoraciones o citas de prensa. Opción A: sin bloque. Opción B: bloque de testimonios, con la fuente de cada cita. |

---

## 4. Lo que no se puede concluir

- **NC es la mayoría en casi todos los patrones.** Las fichas describen lo que revisaron, y en muchos casos solo la portada o un menú. Los conteos son frecuencias de lo descrito, no de lo que existe en cada web.
- **Con 20 agencias no hay estadística.** Las frecuencias sirven para ver qué aparece en la muestra, no para decir qué hace el mercado.
- **Dos estudios con portada sin contenido legible** (`monopo` y `dogstudio`) aportan datos de animación y de cargador, no de diseño.
- **Las fichas no siempre distinguen portada y web.** Cuando una ficha dice «fondo negro» sin indicar página (`code-and-theory`), se cuenta como Sí en la web, y así figura en la evidencia.
- **Recalcular si cambia TASK-001.** Esta matriz depende de las fichas aceptadas; si una ficha se corrige, se corrige la celda y el conteo.
