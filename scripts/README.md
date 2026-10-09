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
| V2 | Capturas existen | Una captura citada no existe, pesa 0 bytes o no es PNG/WebP válido |
| V3 | Capturas propias | La ficha no cita las tres capturas propias `{slug}-home`, `{slug}-servicios` y `{slug}-caso` |
| V4 | Capturas no duplicadas | Dos archivos de `capturas/` tienen el mismo SHA-256 |
| V5 | Servicio enlazado | Una fila «Sí» de «Frente al catálogo de Pharmaco» no tiene URL, o la URL es la portada (ruta `/` o vacía) |
| V6 | Plantilla rellena | Quedan `{`, `AAAA-MM-DD`, `Lorem`, `TODO` o `(o «no verificado»)` **fuera de comillas invertidas**. Un marcador entre comillas invertidas es cita deliberada y no cuenta |
| V7 | Composición de la muestra | No hay 20 fichas principales, o no hay 10 comparables y 10 referentes/especialistas. Un perfil no reconocido también es FALLO |
| V8 | Enlaces vivos | Una URL de fichas, servicios, prueba social o diseño devuelve 404, 410 o 5xx, o falla el DNS o la conexión |

### Qué avisa (AVISO: no bloquea, se explica en el hilo)

- **V5** con `portada única` en la fila: el servicio se describe solo en la portada.
- **V8** con cualquier 4xx distinto de 404 y 410 (400, 401, 403, 429…): bloqueo antibot o de región, se respalda con captura.
- **V8** con redirección a otro dominio.

DECISION-006 (aclaraciones de Clia) fija estas dos reglas: solo 404 y 410 son FALLO, y un marcador de V6 entre comillas invertidas es cita deliberada.

### Qué NO comprueba

El script comprueba **forma y existencia**, no **verdad**. No sabe si una cita es literal, si la captura muestra lo que dice la ficha ni si un conteo está bien interpretado. Eso sigue siendo de **Dexia** (REVIEW) y de **Clia** (auditoría por muestreo). **En verde es necesario, no suficiente.**

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
