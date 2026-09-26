---
tipo: DECISION
id: DECISION-002
titulo: Se revierte «no se quieren carruseles» para el carrusel de categorías
de: clia
para: [dexia, ania]
cc: [miguel]
estado: EFECTIVA
estrategica: true
relacionado: [origen-comportamientos.json, TASK-003]
creado: 2026-09-07
actualizado: 2026-09-07
---

> ℹ️ **Ejemplo real**, tomado del proyecto donde se estrenó este flujo. Los enlaces internos se han
> convertido en texto porque los documentos que citan no viajan en este paquete. Lo que importa no es
> el contenido técnico, sino **la forma**: cómo se argumenta, qué se declara como coste y quién firma.

# DECISION-002 — Carrusel de categorías

## Contexto

El catálogo de comportamientos tiene dos entradas en `descartado`, y no por falta de tiempo:

> `product-carousel` — *«Decisión del proyecto: no se quieren carruseles. El mismo contenido se resuelve como rejilla.»*
> `hero-slider` — *«Decisión del proyecto: no se quieren sliders. Por eso existen ocho variantes de hero.»*

Esa decisión **ya está implementada**: `categories.pug` es ese contenido resuelto como rejilla de seis, y las ocho variantes de hero existen porque son la alternativa estática al carrusel.

Miguel pide el carrusel de categorías del origen: un Swiper de **8 categorías** —Cribs, Beds, Toys, Other, Specials, Carriage, New, Bottles— con anillo punteado, imagen de 92×92 y título.

## Decisión

**Se revierte «no se quieren carruseles», y sólo para el carrusel de categorías.**

1. `product-carousel` pasa de `descartado` a `pendiente` en el catálogo.
2. **`hero-slider` sigue `descartado`.** La reversión es de alcance mínimo: Miguel pidió este carrusel, no todos. Las ocho variantes de hero se quedan como están.
3. **No entra Swiper ni ninguna otra dependencia.** Se implementa con `scroll-snap` nativo y botones propios.

## Motivo

**Sobre revertir sólo esto.** Una decisión de proyecto se revierte donde se pidió, no en general. Cambiar «no se quieren carruseles» por «sí se quieren» dejaría la puerta abierta a que el hero vuelva a ser un slider, y eso Miguel no lo ha pedido. Si más adelante lo quiere, es otra DECISION de una línea.

**Sobre no meter Swiper.** Es el mismo criterio que ya se aplicó tres veces en este proyecto y que está escrito en `playgrow-origen.md`: GSAP + ScrollTrigger se descartó porque `IntersectionObserver` resuelve lo mismo sin dependencias; Magnific Popup y select2, porque arrastran jQuery; perfect-scrollbar, porque reemplaza el scroll del sistema. Swiper cae en el mismo sitio: pesa más que el problema.

`scroll-snap` da gratis lo que Swiper implementa a mano —arrastre táctil, rueda del ratón, trackpad, teclado, y la posición del scroll como estado— y **degrada a una fila desplazable si el JavaScript no carga**, que es exactamente lo que este proyecto pide de cada pieza. El JavaScript sólo añade los botones de anterior y siguiente.

**Lo que esta decisión cuesta, y hay que decirlo.** Un carrusel esconde contenido: de las 8 categorías se ven 3 o 4, y las demás dependen de que alguien las busque. La rejilla las enseñaba todas. Se acepta el coste porque es lo que el origen hace y lo que Miguel quiere, pero **la rejilla no se borra**: se conserva como variante, por si en móvil resulta mejor.

## Consecuencias

- `categories.pug` gana una variante en carrusel. **La rejilla sigue existiendo** y sigue siendo la que se usa donde no se pida lo otro.
- Aparece `src/scripts/components/carousel.js` con el hook `js-carousel` que el catálogo ya tenía reservado.
- El anillo punteado del origen (`stroke #EAE3DE`, ancho 4, `dasharray 10`) se resuelve con el token `--color-line`, que ya es ese color exacto.
- Los `alt="s"` y `alt="f"` del origen **no se copian**: son texto alternativo basura y `AGENTS.md` no los admite.
- Sale TASK-003.

## Vigencia

Efectiva desde **2026-09-07**, a petición explícita de Miguel.

## 💬 Hilo

> **[2026-09-07 00:00] clia:** señalo el conflicto con la decisión previa antes de escribir nada, porque revertirla no es una TASK.
> **[2026-09-07 00:00] miguel:** sí lo quiero — emite la DECISION.
> **[2026-09-07 00:00] clia:** emitida con alcance mínimo: sólo el carrusel de categorías, `hero-slider` sigue descartado, y sin dependencia nueva. Si alguna de las tres acotaciones no es lo que querías, dilo y se corrige aquí.
