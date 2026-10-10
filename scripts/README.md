# scripts/

## `verificar-investigacion.py`

Verificación completa de la investigación, definida en [`DECISION-006`](../docs/comms/DECISION-006-verificacion-investigacion.md) y exigida por [`AGENTS.md`](../AGENTS.md#verificación-de-la-investigación). Es el gate de TASK-001 a TASK-004.

Solo biblioteca estándar de Python 3. No instala nada.

```bash
python3 scripts/verificar-investigacion.py              # gate: con red
python3 scripts/verificar-investigacion.py --sin-red    # salta V8, para pruebas locales
python3 scripts/verificar-investigacion.py --raiz scripts/pruebas   # otra raíz, misma estructura
```

- Lee `docs/investigacion/` y `docs/diseno/` (o la raíz que indique `--raiz`).
- **Código de salida:** `1` si hay algún FALLO, `0` si no.
- **Salida:** una línea por comprobación y archivo (`OK`, `AVISO`, `FALLO`, o `OMITIDA`) y el resumen final `N FALLOS · M AVISOS`.
- **Para el gate** se pega la salida **con red** (sin `--sin-red`).

### Qué comprueba

| # | Comprobación | FALLO si… |
| --- | --- | --- |
| V1 | Campos de la ficha | Falta o está vacío alguno de URL, País / ciudades, Bloque · perfil, Tamaño del equipo, Fecha de consulta o Capturas. La fecha no es `AAAA-MM-DD`. El tamaño es una cifra sin fuente (vale «no publicado» o un rango con fuente) |
| V2 | Capturas existen, son válidas y miden al menos 320×200 px | Una captura citada no existe, pesa 0 bytes, no es PNG/WebP, está rota (estructura del contenedor, ver «Alcance de V2») o mide menos de 320×200 px. Una captura de página más pequeña no es una captura (DECISION-006, enmienda 6) |
| V3 | Capturas propias | La ficha no cita las tres capturas propias `{slug}-home`, `{slug}-servicios` y `{slug}-caso` |
| V4 | Capturas no duplicadas | Dos archivos de `capturas/` tienen el mismo SHA-256 |
| V5 | Servicio enlazado | Falta la sección «Frente al catálogo de Pharmaco», la tabla no tiene las filas 1 a 11, una celda «¿Lo ofrecen?» no es Sí o No (la negrita y el punto final se ignoran), o una fila Sí no tiene URL de página (ruta `/` o vacía) |
| V6 | Plantilla rellena | Quedan `{`, `AAAA-MM-DD`, `Lorem`, `TODO` o `(o «no verificado»)` **fuera de comillas invertidas**. Un marcador entre comillas invertidas es cita deliberada y no cuenta |
| V7 | Composición de la muestra | No hay 20 fichas principales, o no hay 10 comparables y 10 referentes/especialistas. Un perfil no reconocido también es FALLO |
| V8 | Enlaces vivos | Una URL de fichas, servicios, prueba social o diseño devuelve 410, o sigue dando 404, 5xx o error de DNS o conexión tras 3 intentos. Los 404, 5xx y errores de red se reintentan 2 veces, con 2 s de espera (TASK-005, regla de Clia de 2026-10-10). La línea de FALLO o AVISO indica los intentos |

### Qué avisa (AVISO: no bloquea, se explica en el hilo)

- **V5** con `portada única` en la fila: el servicio se describe solo en la portada.
- **V8** con cualquier 4xx distinto de 404 y 410 (400, 401, 403, 429…): bloqueo antibot o de región, se respalda con captura.
- **V8** con un 202 a un GET de página, o con un 2xx que trae una cabecera de desafío (`sg-captcha`, `cf-mitigated: challenge`, `x-amzn-waf-action`): respuesta de desafío, no la página (DECISION-006, enmienda 5). Esos AVISOS también marcan el host como antibot para la enmienda 4.
- **V8** con 401, 403 o 429 en algún intento, aunque otro intento dé 404. Y un 404 final en un host donde otra URL de la misma ejecución dio 401, 403 o 429 (DECISION-006, enmienda 4): 404 no concluyente.
- **V8** con redirección a otro dominio.

DECISION-006 (aclaraciones de Clia) fija estas dos reglas: solo 404 y 410 son FALLO, y un marcador de V6 entre comillas invertidas es cita deliberada.

### Qué NO comprueba

El script comprueba **forma y existencia**, no **verdad**. No sabe si una cita es literal, si la captura muestra lo que dice la ficha ni si un conteo está bien interpretado. Eso sigue siendo de **Dexia** (REVIEW) y de **Clia** (auditoría por muestreo). **En verde es necesario, no suficiente.**

### Alcance de V2 (capturas), DECISION-006 enmienda 6

V2 existe para cazar archivos **truncados, vacíos, de marcador o que no son una captura**. Las capturas salen de Chrome headless. V2 **no es un validador completo** de PNG ni de WebP.

Comprueba:

- **Contenedor PNG:** firma; IHDR único y primero; CRC de cada fragmento; IEND de longitud 0 y último byte del archivo.
- **Contenedor WebP:** tamaño RIFF exacto y fragmentos completos.
- **Datos de imagen presentes:** el PNG descomprime al tamaño que pide IHDR, con byte de filtro de 0 a 4 en cada fila (también en Adam7), y profundidad y tipo de color válidos. El WebP tiene un VP8 o VP8L con datos más allá de su cabecera. VP8X y ALPH solos no cuentan como imagen. Un fotograma ANMF cuenta si contiene una imagen así.
- **Tamaño mínimo:** 320×200 px en ancho y alto, para toda captura citada. En WebP se mide el lienzo (VP8X) o, si no hay, la imagen.

No comprueba (riesgo residual aceptado):

- **La decodificación completa del bitstream.** Un dato comprimido corrupto con estructura válida pasa V2. Se cubre mirando la captura en el REVIEW.
- **Píxeles, metadatos** (tEXt, iCCP, EXIF, XMP) **y el contenido de ALPH.** Solo se recorre su tamaño.
- **Que la captura muestre lo que dice la ficha.** Eso es de Dexia (REVIEW) y de Clia (auditoría).

Discrepancia con decodificadores: `ffmpeg` decodifica sin error un PNG con filtro 5, que V2 marca como FALLO por la especificación.

Pruebas de la validación: [`pruebas/README.md`](pruebas/README.md).

### Decisiones de implementación

Lo que DECISION-006 no fija y el script resuelve así:

- **Alcance.** Fichas de primer nivel `investigacion/fichas/*.md` (la subcarpeta `anexo-medianas/` queda fuera por el glob no recursivo), `investigacion/servicios/*.md`, `investigacion/prueba-social.md` y `diseno/*.md`. Las plantillas (`plantilla-*.md`) y `plan-investigacion.md` no son entregables y no se miran.
- **Rutas de captura.** Una captura se da por existente si está en la carpeta del documento, en `investigacion/` o en `diseno/`, porque los documentos citan rutas desde bases distintas.
- **V3.** Se exigen las tres clases de captura propia (home, servicios, caso), no solo un recuento de tres.
- **V8.** Las peticiones usan cabeceras de navegador. Con un User-Agent de bot, algunos sitios devuelven 404 donde un navegador ve 403 (antibot); así la clasificación de AVISO y FALLO sale del sitio y no del cliente.
- **Fichas `Sí` sin fila de URL.** Una fila «Sí» con URL vacía o no HTTP cuenta como FALLO en V5.

## `pruebas/`

Fichas y capturas **ficticias** que prueban el script. Cada comprobación V1 a V8 tiene al menos un caso que falla. Ver [`pruebas/README.md`](pruebas/README.md).

```bash
python3 scripts/verificar-investigacion.py --raiz scripts/pruebas
```
