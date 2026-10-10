# Pruebas del verificador

Fichas y capturas **ficticias** para comprobar que `verificar-investigacion.py` detecta cada fallo. No describen a ninguna agencia real: los textos son de prueba, las capturas son PNG y WebP sintéticos (ver al final) y los enlaces apuntan a `example.com` y a IANA (siempre vivos), o a dominios que no existen (`.invalid`, que siempre falla el DNS).

Un verificador que nunca se ha visto fallar no está probado. Por eso cada caso falla por **una sola causa**, salvo la ficha correcta.

```bash
python3 scripts/verificar-investigacion.py --raiz scripts/pruebas
```

## Casos

| Archivo | Qué hace | Resultado esperado |
| --- | --- | --- |
| `fichas/correcta.md` | Ficha completa, capturas propias, enlaces vivos | OK en V1, V2, V3, V5, V6 y V8 |
| `fichas/falla-v1.md` | País vacío, fecha `26/09/2026`, tamaño `45 personas` sin fuente | FALLO V1 (3 líneas) |
| `fichas/falla-v2.md` | Captura `home` inexistente, `servicios` de 0 bytes, `caso` con texto plano | FALLO V2 (3 líneas) |
| `fichas/falla-v2b.md` | `home` truncado a 16 bytes (sin IEND), `servicios` con CRC roto, `caso` válido | FALLO V2 (2 líneas) |
| `fichas/falla-v3.md` | Solo cita `home` y `servicios`, falta `caso` | FALLO V3 |
| `fichas/falla-v4.md` | `caso` es byte a byte igual que `home` | FALLO V4 (en ambos archivos) |
| `fichas/falla-v5.md` | Dos filas «Sí»: una con la portada como URL, otra sin URL | FALLO V5 (2 líneas) |
| `fichas/aviso-v5.md` | Fila «Sí» que declara `portada única` | AVISO V5 |
| `fichas/falla-v5-negrita.md` | «**Sí**» en negrita sin URL | FALLO V5 |
| `fichas/falla-v5-sin-tabla.md` | Falta la sección «Frente al catálogo de Pharmaco» | FALLO V5 |
| `fichas/falla-v5-filas.md` | Tabla con 10 filas en vez de 11 | FALLO V5 |
| `fichas/correcta-variantes.md` | «**Sí**», «si» y «Sí.» con URL válida | OK en V5 |
| `fichas/falla-v6.md` | Contiene `TODO` y `(o «no verificado»)` sin comillas invertidas | FALLO V6 (2 líneas) |
| `fichas/correcta-cita.md` | `Lorem` y `TODO` entre comillas invertidas, como cita deliberada | OK en V6 |
| `fichas/falla-v8.md` | Una URL da 404 y otra no resuelve el DNS | FALLO V8 (2 líneas) |
| `fichas/aviso-v8.md` | Una URL da 400 (`httpbin.org/status/400`, endpoint de pruebas) | AVISO V8 |
| `fichas/falla-v2c.md` | `home` es un WebP de 20 bytes con un `VP8 ` de longitud 0 (caso de REVIEW-005, segunda ronda) | FALLO V2 (1 línea) |
| `fichas/falla-v2d.md` | `servicios` es un PNG de 320×200 con byte de filtro 5 en la primera fila (caso de REVIEW-005, segunda ronda) | FALLO V2 (1 línea) |
| `fichas/falla-v2e.md` | Matriz: 16 capturas adicionales con un único defecto cada una (cabeceras WebP y PNG, IEND, IHDR, datos vacíos y tamaño mínimo; lista en la ficha) | FALLO V2 (16 líneas) |
| `fichas/correcta-formatos.md` | WebP con pérdida, sin pérdida y animado (ANMF) válidos, y un PNG entrelazado válido | OK en V2 |
| — | 20 fichas, pero 19 comparables y 1 referente o especialista | FALLO V7 (composición, 2 líneas) |

Con `--sin-red` la V8 aparece como `OMITIDA` y no cuenta como FALLO: por eso el gate se pega **con red**.

Las capturas de `capturas/` no son fotos de ninguna web.

- **Positivos PNG:** 320×200 píxeles RGB de 8 bits (el mínimo de captura, DECISION-006 enmienda 6), color fijo por nombre, para que cada una sea distinta (V4). Los PNG entrelazados son de Adam7 de 320×200.
- **Positivos WebP:** `cwebp` 1.6.0 (con pérdida `-q 80` y sin pérdida) e `img2webp` (animado, dos fotogramas), a partir de PNG de 320×200.
- **Negativos:** bytes válidos con un único cambio:
  - `falla-v2c-home.webp`: RIFF de 20 bytes con `VP8 ` de longitud 0.
  - `falla-v2d-servicios.png`: PNG de 320×200 RGB con filtro 5 en la primera fila.
  - `falla-v2e-vp8-no-clave.webp`: bit 0 de la etiqueta VP8 a 1. `falla-v2e-vp8-codigo.webp`: byte 3 del VP8 a 0. `falla-v2e-vp8-particion.webp`: tamaño de la primera partición al máximo.
  - `falla-v2e-vp8l-firma.webp`: primer byte del VP8L a 0. `falla-v2e-vp8l-version.webp`: versión del VP8L a 1.
  - `falla-v2e-vp8x-sin-imagen.webp`: solo un fragmento VP8X. `falla-v2e-anmf-sin-imagen.webp`: VP8X y un ANMF de 16 bytes sin subfragmentos.
  - `falla-v2e-png-profundidad.png`: profundidad 3 con RGB. `falla-v2e-png-compresion.png`: método de compresión 1. `falla-v2e-png-entrelazado.png`: PNG entrelazado de 320×200 con 3 bytes de datos en lugar de los necesarios. `falla-v2e-png-iend-un-byte.png`: IEND con un byte de datos y CRC correcto. `falla-v2e-png-tras-iend.png`: bytes después de IEND. `falla-v2e-png-ihdr-doble.png`: IHDR repetido.
  - `falla-v2e-vp8l-vacio.webp`: VP8L de solo su cabecera de 5 bytes (RIFF de 26 bytes, caso de REVIEW-005, tercera ronda). `falla-v2e-vp8-vacio.webp`: VP8 de solo su cabecera de 10 bytes, con partición de tamaño 0. `falla-v2e-tamano.png`: 100×50 px, por debajo del mínimo de 320×200.

Comprobación fuera del verificador: `dwebp` acepta los WebP positivos y rechaza los negativos. `webpmux -info` acepta el animado y rechaza los dos negativos sin imagen (`ffmpeg` no decodifica el animado, limitación de su decodificador nativo). `ffmpeg` rechaza los PNG negativos de profundidad, compresión y entrelazado, pero **acepta** el de filtro 5: ese caso se decide por la especificación.

Las capturas de 320×200 px y los defectos son los descritos arriba. Son bytes sintéticos; el generador no está en el repositorio. Las dos de origen estructural (`falla-v2-caso.png` con texto plano, `falla-v2-servicios.png` de 0 bytes) y `falla-v2b-home.png` (16 bytes truncados) se conservan tal cual.
