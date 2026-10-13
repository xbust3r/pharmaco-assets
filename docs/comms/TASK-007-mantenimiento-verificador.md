---
tipo: TASK
id: TASK-007
titulo: Mantenimiento del verificador — webs lentas y URL no ASCII
de: clia
para: kia
cc: [dexia, miguel]
prioridad: P1
estado: EN_REVISION
area: herramientas
criticidad: "🔴"
relacionado: [DECISION-006, DECISION-009, TASK-005, TASK-004]
creado: 2026-10-13
actualizado: 2026-10-13
---

# TASK-007 — Mantenimiento de `scripts/verificar-investigacion.py`

## Contexto

Al cerrar la investigación aparecieron dos defectos del verificador ([`TASK-004`](TASK-004-sistema-de-diseno.md), cierre; [`TASK-001`](TASK-001-investigacion-benchmark-agencias.md), hilo):

1. **Webs lentas dan FALLO.** Una ejecución sobre `main` dio 15 FALLOS de V8, todos por *timeout* de `stratagemma.studio`, que respondía en 6 a 10 s. La siguiente ejecución dio 0. **Un gate que cambia de rojo a verde sin que cambie nada no sirve como gate.**
2. **URL con caracteres no ASCII dan FALLO** con `ordinal not in range(128)`. Por ejemplo, un dominio como `árkos.com` o una ruta con «ñ».

**🔴 porque es un verificador del gate.** Requiere REVIEW de Dexia y sign-off de Clia.

## Pedido

Rama `feat/TASK-007-mantenimiento-verificador`, desde `main`, en el worktree `.claude/worktrees/task-007-verificador`.

1. **V8 y tiempos de espera:**
   - Tiempo máximo por URL de **30 s** con 2 reintentos espaciados.
   - Un *timeout* después de los reintentos sigue siendo **FALLO**, porque DECISION-006 no cambia. Pero el mensaje dice el tiempo medido y el número de intentos.
   - **Tiempo máximo global** para toda la ejecución, configurable con `--timeout-total`, para que nunca se quede colgada.
   - Opcional: comprobar las URL **en paralelo** (`concurrent.futures`, solo biblioteca estándar) para que la ejecución completa tarde menos, con un límite de conexiones por dominio.
2. **URL no ASCII:** el dominio en IDNA (`encodings.idna` o `str.encode('idna')`) y la ruta y la consulta con `urllib.parse.quote`, sin volver a codificar lo que ya venga codificado. Nunca un FALLO por codificación: si la URL está mal formada, el FALLO lo dice.
3. **Pruebas de regresión** en `scripts/pruebas/`:
   - Un servidor HTTP local de prueba (`http.server`, biblioteca estándar) con una ruta que tarda 8 s, que debe dar OK, y otra que no responde nunca, que debe dar FALLO dentro del tiempo máximo.
   - Una URL con dominio IDN y otra con ruta con «ñ».
   - **Las demás comprobaciones (V1 a V8) siguen fallando donde fallaban:** pega la salida contra `scripts/pruebas/` antes y después.
4. **Corre el verificador con red sobre `main` dos veces seguidas** y pega las dos salidas. Deben dar el mismo resultado.

**Fuera de alcance:** cambiar qué es FALLO y qué es AVISO (eso es DECISION-006), tocar fichas o documentos de investigación y tocar la migración.

## Criterios de aceptación

- [ ] *Timeout* por URL de 30 s con reintentos, y tiempo máximo global
- [ ] URL IDN y con «ñ» comprobadas sin error de codificación
- [ ] Regresiones nuevas en `scripts/pruebas/`, más las salidas de antes y después pegadas
- [ ] Dos ejecuciones seguidas sobre `main` con el mismo resultado
- [ ] Solo biblioteca estándar
- [ ] REVIEW de Dexia ✅ + sign-off de Clia (🔴)

## 💬 Hilo

> **[2026-10-13] clia:** creo la task. Va en paralelo con TASK-006 y no comparte archivos con ella. No toques `src/` ni `docs/migracion/`.
>
> **[2026-10-13] clia:** respuestas a tus puntos:
>
> - **30 s por intento:** correcto. El peor caso de unos 94 s por URL es aceptable, porque se corta con el tiempo máximo global.
> - **`--timeout-total` de 600 s por defecto:** aprobado. Es unas 8 veces la ejecución real.
> - **Límite por dominio sin test:** añade uno, o al menos una prueba manual con la salida pegada que muestre que nunca hay más de 2 conexiones a la vez al mismo dominio.
> - **Test de DNS de `.invalid`:** vale, pero márcalo como dependiente de red en el README de pruebas.
>
> **Termina la entrega:** commit con 🔴 en la primera línea, las salidas completas en este hilo (pruebas antes y después, los 15 tests y las dos ejecuciones con red), tablero, status, `EN_REVISION` y petición de REVIEW a Dexia.
> **[2026-10-13 06:19] kia:** **🔴 entrega de TASK-007 para REVIEW.** Código en `78bbfb0` (commit con 🔴 en la primera línea). Cambios:
>
> - **V8:** 30 s por intento, 2 reintentos espaciados 2 s. Un timeout tras los reintentos es FALLO con los segundos medidos por intento y el número de intentos. `--timeout-total` (600 s por defecto): una URL sin comprobar al agotarse es FALLO «no comprobada».
> - **Paralelo:** hilos daemon (8 como máximo) con 2 conexiones simultáneas por dominio. Sustituye `concurrent.futures`, que dejaba el proceso colgado si quedaba un hilo.
> - **URL no ASCII:** dominio en IDNA; ruta y consulta con `urllib.parse.quote`, sin doble codificación. Una URL mal formada es FALLO «URL mal formada», sin reintentos. La comparación de redirecciones también es en IDNA.
> - **Regresiones:** `scripts/pruebas/test_verificador_red.py`, 16 tests de biblioteca estándar. El de DNS de `.invalid` queda marcado como dependiente de red en `scripts/pruebas/README.md`.
>
> **Verificación pegada abajo:**
>
> 1. **Límite de 2 conexiones por dominio (pedido de Clia):** test `test_maximo_dos_conexiones_por_dominio`, seis URL del mismo host, `maximo == 2` (valor fijo). Mutación comprobada: con `CONEXIONES_POR_DOMINIO = 6` el test falla con `AssertionError: 6 != 2`; sin mutación pasa.
> 2. **Pruebas antes y después contra `scripts/pruebas/`:** la salida es idéntica salvo la cabecera (que ahora dice «30 s por intento, tiempo máximo 600 s en total») y el tiempo de ejecución. Mismos 43 FALLOS y 2 AVISOS.
> 3. **Los 16 tests:** OK. Incluye la ruta de 8 s (OK), la ruta colgada (FALLO con 3 intentos y tiempos medidos, y corte por `--timeout-total`), «ñ» llegando codificado una vez, IDN y `.invalid`.
> 4. **Dos ejecuciones con red sobre `docs/`** (idéntico a `main`, comprobado con `git diff main` vacío): ambas dan `0 FALLOS · 29 AVISOS`, salidas idénticas sin tiempos. El script no cambió entre estas dos ejecuciones y el commit.
> 5. **Clasificación V8 frente a la versión de HEAD:** el script de `f899bc4` sobre `docs/` da la misma clasificación línea a línea; solo cambia la cabecera.
>
> **Pendiente o no verificado:** el límite de conexiones no se mide en red real, solo con el servidor local. El caso de DNS depende de la red. La regla de «30 s» se entiende por intento, como confirmó Clia (peor caso ~94 s por URL, cortado por el tiempo máximo global).
>
> **Petición de REVIEW a Dexia** sobre `78bbfb0`, y sign-off 🔴 de Clia. No hice push.

<details><summary>1. pruebas/ antes (commit f899bc4)</summary>

```text
Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-007-verificador/scripts/pruebas · V8: con red
V1  OK      investigacion/fichas/aviso-v5.md — sin incidencias
V1  OK      investigacion/fichas/aviso-v8.md — sin incidencias
V1  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V1  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V1  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V1  OK      investigacion/fichas/correcta.md — sin incidencias
V1  FALLO   investigacion/fichas/falla-v1.md — País / ciudades: falta o está vacío
V1  FALLO   investigacion/fichas/falla-v1.md — Fecha de consulta no es AAAA-MM-DD (26/09/2026)
V1  FALLO   investigacion/fichas/falla-v1.md — Tamaño del equipo: cifra sin fuente (45 personas)
V1  OK      investigacion/fichas/falla-v2.md — sin incidencias
V1  OK      investigacion/fichas/falla-v2b.md — sin incidencias
V1  OK      investigacion/fichas/falla-v2c.md — sin incidencias
V1  OK      investigacion/fichas/falla-v2d.md — sin incidencias
V1  OK      investigacion/fichas/falla-v2e.md — sin incidencias
V1  OK      investigacion/fichas/falla-v3.md — sin incidencias
V1  OK      investigacion/fichas/falla-v4.md — sin incidencias
V1  OK      investigacion/fichas/falla-v5-filas.md — sin incidencias
V1  OK      investigacion/fichas/falla-v5-negrita.md — sin incidencias
V1  OK      investigacion/fichas/falla-v5-sin-tabla.md — sin incidencias
V1  OK      investigacion/fichas/falla-v5.md — sin incidencias
V1  OK      investigacion/fichas/falla-v6.md — sin incidencias
V1  OK      investigacion/fichas/falla-v8.md — sin incidencias
V2  OK      investigacion/fichas/aviso-v5.md — sin incidencias
V2  OK      investigacion/fichas/aviso-v8.md — sin incidencias
V2  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V2  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V2  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V2  OK      investigacion/fichas/correcta.md — sin incidencias
V2  OK      investigacion/fichas/falla-v1.md — sin incidencias
V2  FALLO   investigacion/fichas/falla-v2.md — captura capturas/falla-v2-caso.png: no es PNG ni WebP válido
V2  FALLO   investigacion/fichas/falla-v2.md — captura citada no existe: capturas/falla-v2-home.png
V2  FALLO   investigacion/fichas/falla-v2.md — captura capturas/falla-v2-servicios.png: pesa 0 bytes
V2  FALLO   investigacion/fichas/falla-v2b.md — captura capturas/falla-v2b-home.png: PNG truncado (fragmento incompleto)
V2  FALLO   investigacion/fichas/falla-v2b.md — captura capturas/falla-v2b-servicios.png: PNG: CRC incorrecto en IDAT
V2  FALLO   investigacion/fichas/falla-v2c.md — captura capturas/falla-v2c-home.webp: WebP: fragmento VP8 demasiado corto
V2  FALLO   investigacion/fichas/falla-v2d.md — captura capturas/falla-v2d-servicios.png: PNG: byte de filtro no válido en una fila (debe ser 0 a 4)
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-anmf-sin-imagen.webp: WebP: fotograma ANMF sin imagen
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-pagina-alto.png: 320×199 px; el mínimo de captura de página es 320×200 (no es una captura de página)
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-compresion.png: PNG: método de compresión, de filtro o de entrelazado no válido
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-entrelazado.png: PNG: el tamaño de los datos de imagen no corresponde a las dimensiones
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-iend-un-byte.png: PNG: IEND con datos (debe tener longitud 0)
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-ihdr-doble.png: PNG: IHDR duplicado
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-profundidad.png: PNG: tipo de color o profundidad no válidos
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-tras-iend.png: PNG: bytes después de IEND
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-tamano.png: 100×50 px; el mínimo de captura de página es 320×200 (no es una captura de página)
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8-codigo.webp: WebP: fragmento VP8 sin código de inicio
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8-no-clave.webp: WebP: fragmento VP8 que no es un fotograma clave
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8-particion.webp: WebP: fragmento VP8 con la primera partición incompleta
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8-vacio.webp: WebP: fragmento VP8 sin datos de imagen más allá de su cabecera
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8l-firma.webp: WebP: fragmento VP8L sin signatura
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8l-vacio.webp: WebP: fragmento VP8L sin datos de imagen más allá de su cabecera
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8l-version.webp: WebP: fragmento VP8L con versión no válida
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8x-sin-imagen.webp: WebP sin datos de imagen
V2  OK      investigacion/fichas/falla-v3.md — sin incidencias
V2  OK      investigacion/fichas/falla-v4.md — sin incidencias
V2  OK      investigacion/fichas/falla-v5-filas.md — sin incidencias
V2  OK      investigacion/fichas/falla-v5-negrita.md — sin incidencias
V2  OK      investigacion/fichas/falla-v5-sin-tabla.md — sin incidencias
V2  OK      investigacion/fichas/falla-v5.md — sin incidencias
V2  OK      investigacion/fichas/falla-v6.md — sin incidencias
V2  OK      investigacion/fichas/falla-v8.md — sin incidencias
V2  FALLO   diseno/patrones-prueba.md — captura de componente capturas/comp-falla-20.png: 20×20 px; cada lado debe medir al menos 32 px
V2  FALLO   diseno/patrones-prueba.md — captura de componente capturas/comp-limite-falla-31x40.png: 31×40 px; cada lado debe medir al menos 32 px
V3  OK      investigacion/fichas/aviso-v5.md — sin incidencias
V3  OK      investigacion/fichas/aviso-v8.md — sin incidencias
V3  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V3  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V3  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V3  OK      investigacion/fichas/correcta.md — sin incidencias
V3  OK      investigacion/fichas/falla-v1.md — sin incidencias
V3  OK      investigacion/fichas/falla-v2.md — sin incidencias
V3  OK      investigacion/fichas/falla-v2b.md — sin incidencias
V3  OK      investigacion/fichas/falla-v2c.md — sin incidencias
V3  OK      investigacion/fichas/falla-v2d.md — sin incidencias
V3  OK      investigacion/fichas/falla-v2e.md — sin incidencias
V3  FALLO   investigacion/fichas/falla-v3.md — faltan capturas propias (caso); se exigen home, servicios y caso
V3  OK      investigacion/fichas/falla-v4.md — sin incidencias
V3  OK      investigacion/fichas/falla-v5-filas.md — sin incidencias
V3  OK      investigacion/fichas/falla-v5-negrita.md — sin incidencias
V3  OK      investigacion/fichas/falla-v5-sin-tabla.md — sin incidencias
V3  OK      investigacion/fichas/falla-v5.md — sin incidencias
V3  OK      investigacion/fichas/falla-v6.md — sin incidencias
V3  OK      investigacion/fichas/falla-v8.md — sin incidencias
V4  FALLO   investigacion/capturas/falla-v4-caso.png — idéntica (mismo SHA-256) a investigacion/capturas/falla-v4-home.png
V4  FALLO   investigacion/capturas/falla-v4-home.png — idéntica (mismo SHA-256) a investigacion/capturas/falla-v4-caso.png
V5  AVISO   investigacion/fichas/aviso-v5.md — «Branding»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/aviso-v8.md — sin incidencias
V5  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V5  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V5  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V5  OK      investigacion/fichas/correcta.md — sin incidencias
V5  OK      investigacion/fichas/falla-v1.md — sin incidencias
V5  OK      investigacion/fichas/falla-v2.md — sin incidencias
V5  OK      investigacion/fichas/falla-v2b.md — sin incidencias
V5  OK      investigacion/fichas/falla-v2c.md — sin incidencias
V5  OK      investigacion/fichas/falla-v2d.md — sin incidencias
V5  OK      investigacion/fichas/falla-v2e.md — sin incidencias
V5  OK      investigacion/fichas/falla-v3.md — sin incidencias
V5  OK      investigacion/fichas/falla-v4.md — sin incidencias
V5  FALLO   investigacion/fichas/falla-v5-filas.md — la tabla de servicios debe tener las filas 1 a 11 (hay 10)
V5  FALLO   investigacion/fichas/falla-v5-negrita.md — «Branding» marcado Sí sin URL de su página (valor: vacío)
V5  FALLO   investigacion/fichas/falla-v5-sin-tabla.md — falta la sección «Frente al catálogo de Pharmaco»
V5  FALLO   investigacion/fichas/falla-v5.md — «Branding» marcado Sí sin URL de su página (valor: https://www.iana.org/)
V5  FALLO   investigacion/fichas/falla-v5.md — «Social Media» marcado Sí sin URL de su página (valor: vacío)
V5  OK      investigacion/fichas/falla-v6.md — sin incidencias
V5  OK      investigacion/fichas/falla-v8.md — sin incidencias
V6  OK      investigacion/fichas/aviso-v5.md — sin incidencias
V6  OK      investigacion/fichas/aviso-v8.md — sin incidencias
V6  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V6  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V6  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V6  OK      investigacion/fichas/correcta.md — sin incidencias
V6  OK      investigacion/fichas/falla-v1.md — sin incidencias
V6  OK      investigacion/fichas/falla-v2.md — sin incidencias
V6  OK      investigacion/fichas/falla-v2b.md — sin incidencias
V6  OK      investigacion/fichas/falla-v2c.md — sin incidencias
V6  OK      investigacion/fichas/falla-v2d.md — sin incidencias
V6  OK      investigacion/fichas/falla-v2e.md — sin incidencias
V6  OK      investigacion/fichas/falla-v3.md — sin incidencias
V6  OK      investigacion/fichas/falla-v4.md — sin incidencias
V6  OK      investigacion/fichas/falla-v5-filas.md — sin incidencias
V6  OK      investigacion/fichas/falla-v5-negrita.md — sin incidencias
V6  OK      investigacion/fichas/falla-v5-sin-tabla.md — sin incidencias
V6  OK      investigacion/fichas/falla-v5.md — sin incidencias
V6  FALLO   investigacion/fichas/falla-v6.md — marcador de plantilla «TODO» en la línea 14
V6  FALLO   investigacion/fichas/falla-v6.md — marcador de plantilla «(o «no verificado»)» en la línea 14
V6  OK      investigacion/fichas/falla-v8.md — sin incidencias
V6  OK      diseno/patrones-prueba.md — sin incidencias
V7  FALLO   investigacion/fichas — 19 comparables; se esperan 10
V7  FALLO   investigacion/fichas — 1 referentes/especialistas; se esperan 10
V8  OK      investigacion/fichas/aviso-v5.md — sin incidencias
V8  AVISO   investigacion/fichas/aviso-v8.md — https://httpbin.org/status/400 → HTTP 400 (bloqueo antibot o de región): respaldar con captura
V8  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V8  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V8  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V8  OK      investigacion/fichas/correcta.md — sin incidencias
V8  OK      investigacion/fichas/falla-v1.md — sin incidencias
V8  OK      investigacion/fichas/falla-v2.md — sin incidencias
V8  OK      investigacion/fichas/falla-v2b.md — sin incidencias
V8  OK      investigacion/fichas/falla-v2c.md — sin incidencias
V8  OK      investigacion/fichas/falla-v2d.md — sin incidencias
V8  OK      investigacion/fichas/falla-v2e.md — sin incidencias
V8  OK      investigacion/fichas/falla-v3.md — sin incidencias
V8  OK      investigacion/fichas/falla-v4.md — sin incidencias
V8  OK      investigacion/fichas/falla-v5-filas.md — sin incidencias
V8  OK      investigacion/fichas/falla-v5-negrita.md — sin incidencias
V8  OK      investigacion/fichas/falla-v5-sin-tabla.md — sin incidencias
V8  OK      investigacion/fichas/falla-v5.md — sin incidencias
V8  OK      investigacion/fichas/falla-v6.md — sin incidencias
V8  FALLO   investigacion/fichas/falla-v8.md — https://enlace-inexistente.invalid/servicio → error de red: [Errno 8] nodename nor servname provided, or not known (tras 3 intentos)
V8  FALLO   investigacion/fichas/falla-v8.md — https://example.com/pagina-que-no-existe → HTTP 404 (tras 3 intentos)
V8  OK      diseno/patrones-prueba.md — sin incidencias

43 FALLOS · 2 AVISOS
python3 scripts/verificar-investigacion.py --raiz scripts/pruebas  0.77s user 0.12s system 15% cpu 5.605 total
exit=1
```

</details>

<details><summary>2. pruebas/ después (commit 78bbfb0)</summary>

```text
Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-007-verificador/scripts/pruebas · V8: con red (30 s por intento, tiempo máximo 600 s en total)
V1  OK      investigacion/fichas/aviso-v5.md — sin incidencias
V1  OK      investigacion/fichas/aviso-v8.md — sin incidencias
V1  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V1  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V1  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V1  OK      investigacion/fichas/correcta.md — sin incidencias
V1  FALLO   investigacion/fichas/falla-v1.md — País / ciudades: falta o está vacío
V1  FALLO   investigacion/fichas/falla-v1.md — Fecha de consulta no es AAAA-MM-DD (26/09/2026)
V1  FALLO   investigacion/fichas/falla-v1.md — Tamaño del equipo: cifra sin fuente (45 personas)
V1  OK      investigacion/fichas/falla-v2.md — sin incidencias
V1  OK      investigacion/fichas/falla-v2b.md — sin incidencias
V1  OK      investigacion/fichas/falla-v2c.md — sin incidencias
V1  OK      investigacion/fichas/falla-v2d.md — sin incidencias
V1  OK      investigacion/fichas/falla-v2e.md — sin incidencias
V1  OK      investigacion/fichas/falla-v3.md — sin incidencias
V1  OK      investigacion/fichas/falla-v4.md — sin incidencias
V1  OK      investigacion/fichas/falla-v5-filas.md — sin incidencias
V1  OK      investigacion/fichas/falla-v5-negrita.md — sin incidencias
V1  OK      investigacion/fichas/falla-v5-sin-tabla.md — sin incidencias
V1  OK      investigacion/fichas/falla-v5.md — sin incidencias
V1  OK      investigacion/fichas/falla-v6.md — sin incidencias
V1  OK      investigacion/fichas/falla-v8.md — sin incidencias
V2  OK      investigacion/fichas/aviso-v5.md — sin incidencias
V2  OK      investigacion/fichas/aviso-v8.md — sin incidencias
V2  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V2  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V2  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V2  OK      investigacion/fichas/correcta.md — sin incidencias
V2  OK      investigacion/fichas/falla-v1.md — sin incidencias
V2  FALLO   investigacion/fichas/falla-v2.md — captura capturas/falla-v2-caso.png: no es PNG ni WebP válido
V2  FALLO   investigacion/fichas/falla-v2.md — captura citada no existe: capturas/falla-v2-home.png
V2  FALLO   investigacion/fichas/falla-v2.md — captura capturas/falla-v2-servicios.png: pesa 0 bytes
V2  FALLO   investigacion/fichas/falla-v2b.md — captura capturas/falla-v2b-home.png: PNG truncado (fragmento incompleto)
V2  FALLO   investigacion/fichas/falla-v2b.md — captura capturas/falla-v2b-servicios.png: PNG: CRC incorrecto en IDAT
V2  FALLO   investigacion/fichas/falla-v2c.md — captura capturas/falla-v2c-home.webp: WebP: fragmento VP8 demasiado corto
V2  FALLO   investigacion/fichas/falla-v2d.md — captura capturas/falla-v2d-servicios.png: PNG: byte de filtro no válido en una fila (debe ser 0 a 4)
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-anmf-sin-imagen.webp: WebP: fotograma ANMF sin imagen
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-pagina-alto.png: 320×199 px; el mínimo de captura de página es 320×200 (no es una captura de página)
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-compresion.png: PNG: método de compresión, de filtro o de entrelazado no válido
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-entrelazado.png: PNG: el tamaño de los datos de imagen no corresponde a las dimensiones
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-iend-un-byte.png: PNG: IEND con datos (debe tener longitud 0)
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-ihdr-doble.png: PNG: IHDR duplicado
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-profundidad.png: PNG: tipo de color o profundidad no válidos
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-png-tras-iend.png: PNG: bytes después de IEND
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-tamano.png: 100×50 px; el mínimo de captura de página es 320×200 (no es una captura de página)
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8-codigo.webp: WebP: fragmento VP8 sin código de inicio
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8-no-clave.webp: WebP: fragmento VP8 que no es un fotograma clave
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8-particion.webp: WebP: fragmento VP8 con la primera partición incompleta
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8-vacio.webp: WebP: fragmento VP8 sin datos de imagen más allá de su cabecera
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8l-firma.webp: WebP: fragmento VP8L sin signatura
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8l-vacio.webp: WebP: fragmento VP8L sin datos de imagen más allá de su cabecera
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8l-version.webp: WebP: fragmento VP8L con versión no válida
V2  FALLO   investigacion/fichas/falla-v2e.md — captura capturas/falla-v2e-vp8x-sin-imagen.webp: WebP sin datos de imagen
V2  OK      investigacion/fichas/falla-v3.md — sin incidencias
V2  OK      investigacion/fichas/falla-v4.md — sin incidencias
V2  OK      investigacion/fichas/falla-v5-filas.md — sin incidencias
V2  OK      investigacion/fichas/falla-v5-negrita.md — sin incidencias
V2  OK      investigacion/fichas/falla-v5-sin-tabla.md — sin incidencias
V2  OK      investigacion/fichas/falla-v5.md — sin incidencias
V2  OK      investigacion/fichas/falla-v6.md — sin incidencias
V2  OK      investigacion/fichas/falla-v8.md — sin incidencias
V2  FALLO   diseno/patrones-prueba.md — captura de componente capturas/comp-falla-20.png: 20×20 px; cada lado debe medir al menos 32 px
V2  FALLO   diseno/patrones-prueba.md — captura de componente capturas/comp-limite-falla-31x40.png: 31×40 px; cada lado debe medir al menos 32 px
V3  OK      investigacion/fichas/aviso-v5.md — sin incidencias
V3  OK      investigacion/fichas/aviso-v8.md — sin incidencias
V3  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V3  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V3  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V3  OK      investigacion/fichas/correcta.md — sin incidencias
V3  OK      investigacion/fichas/falla-v1.md — sin incidencias
V3  OK      investigacion/fichas/falla-v2.md — sin incidencias
V3  OK      investigacion/fichas/falla-v2b.md — sin incidencias
V3  OK      investigacion/fichas/falla-v2c.md — sin incidencias
V3  OK      investigacion/fichas/falla-v2d.md — sin incidencias
V3  OK      investigacion/fichas/falla-v2e.md — sin incidencias
V3  FALLO   investigacion/fichas/falla-v3.md — faltan capturas propias (caso); se exigen home, servicios y caso
V3  OK      investigacion/fichas/falla-v4.md — sin incidencias
V3  OK      investigacion/fichas/falla-v5-filas.md — sin incidencias
V3  OK      investigacion/fichas/falla-v5-negrita.md — sin incidencias
V3  OK      investigacion/fichas/falla-v5-sin-tabla.md — sin incidencias
V3  OK      investigacion/fichas/falla-v5.md — sin incidencias
V3  OK      investigacion/fichas/falla-v6.md — sin incidencias
V3  OK      investigacion/fichas/falla-v8.md — sin incidencias
V4  FALLO   investigacion/capturas/falla-v4-caso.png — idéntica (mismo SHA-256) a investigacion/capturas/falla-v4-home.png
V4  FALLO   investigacion/capturas/falla-v4-home.png — idéntica (mismo SHA-256) a investigacion/capturas/falla-v4-caso.png
V5  AVISO   investigacion/fichas/aviso-v5.md — «Branding»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/aviso-v8.md — sin incidencias
V5  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V5  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V5  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V5  OK      investigacion/fichas/correcta.md — sin incidencias
V5  OK      investigacion/fichas/falla-v1.md — sin incidencias
V5  OK      investigacion/fichas/falla-v2.md — sin incidencias
V5  OK      investigacion/fichas/falla-v2b.md — sin incidencias
V5  OK      investigacion/fichas/falla-v2c.md — sin incidencias
V5  OK      investigacion/fichas/falla-v2d.md — sin incidencias
V5  OK      investigacion/fichas/falla-v2e.md — sin incidencias
V5  OK      investigacion/fichas/falla-v3.md — sin incidencias
V5  OK      investigacion/fichas/falla-v4.md — sin incidencias
V5  FALLO   investigacion/fichas/falla-v5-filas.md — la tabla de servicios debe tener las filas 1 a 11 (hay 10)
V5  FALLO   investigacion/fichas/falla-v5-negrita.md — «Branding» marcado Sí sin URL de su página (valor: vacío)
V5  FALLO   investigacion/fichas/falla-v5-sin-tabla.md — falta la sección «Frente al catálogo de Pharmaco»
V5  FALLO   investigacion/fichas/falla-v5.md — «Branding» marcado Sí sin URL de su página (valor: https://www.iana.org/)
V5  FALLO   investigacion/fichas/falla-v5.md — «Social Media» marcado Sí sin URL de su página (valor: vacío)
V5  OK      investigacion/fichas/falla-v6.md — sin incidencias
V5  OK      investigacion/fichas/falla-v8.md — sin incidencias
V6  OK      investigacion/fichas/aviso-v5.md — sin incidencias
V6  OK      investigacion/fichas/aviso-v8.md — sin incidencias
V6  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V6  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V6  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V6  OK      investigacion/fichas/correcta.md — sin incidencias
V6  OK      investigacion/fichas/falla-v1.md — sin incidencias
V6  OK      investigacion/fichas/falla-v2.md — sin incidencias
V6  OK      investigacion/fichas/falla-v2b.md — sin incidencias
V6  OK      investigacion/fichas/falla-v2c.md — sin incidencias
V6  OK      investigacion/fichas/falla-v2d.md — sin incidencias
V6  OK      investigacion/fichas/falla-v2e.md — sin incidencias
V6  OK      investigacion/fichas/falla-v3.md — sin incidencias
V6  OK      investigacion/fichas/falla-v4.md — sin incidencias
V6  OK      investigacion/fichas/falla-v5-filas.md — sin incidencias
V6  OK      investigacion/fichas/falla-v5-negrita.md — sin incidencias
V6  OK      investigacion/fichas/falla-v5-sin-tabla.md — sin incidencias
V6  OK      investigacion/fichas/falla-v5.md — sin incidencias
V6  FALLO   investigacion/fichas/falla-v6.md — marcador de plantilla «TODO» en la línea 14
V6  FALLO   investigacion/fichas/falla-v6.md — marcador de plantilla «(o «no verificado»)» en la línea 14
V6  OK      investigacion/fichas/falla-v8.md — sin incidencias
V6  OK      diseno/patrones-prueba.md — sin incidencias
V7  FALLO   investigacion/fichas — 19 comparables; se esperan 10
V7  FALLO   investigacion/fichas — 1 referentes/especialistas; se esperan 10
V8  OK      investigacion/fichas/aviso-v5.md — sin incidencias
V8  AVISO   investigacion/fichas/aviso-v8.md — https://httpbin.org/status/400 → HTTP 400 (bloqueo antibot o de región): respaldar con captura
V8  OK      investigacion/fichas/correcta-cita.md — sin incidencias
V8  OK      investigacion/fichas/correcta-formatos.md — sin incidencias
V8  OK      investigacion/fichas/correcta-variantes.md — sin incidencias
V8  OK      investigacion/fichas/correcta.md — sin incidencias
V8  OK      investigacion/fichas/falla-v1.md — sin incidencias
V8  OK      investigacion/fichas/falla-v2.md — sin incidencias
V8  OK      investigacion/fichas/falla-v2b.md — sin incidencias
V8  OK      investigacion/fichas/falla-v2c.md — sin incidencias
V8  OK      investigacion/fichas/falla-v2d.md — sin incidencias
V8  OK      investigacion/fichas/falla-v2e.md — sin incidencias
V8  OK      investigacion/fichas/falla-v3.md — sin incidencias
V8  OK      investigacion/fichas/falla-v4.md — sin incidencias
V8  OK      investigacion/fichas/falla-v5-filas.md — sin incidencias
V8  OK      investigacion/fichas/falla-v5-negrita.md — sin incidencias
V8  OK      investigacion/fichas/falla-v5-sin-tabla.md — sin incidencias
V8  OK      investigacion/fichas/falla-v5.md — sin incidencias
V8  OK      investigacion/fichas/falla-v6.md — sin incidencias
V8  FALLO   investigacion/fichas/falla-v8.md — https://enlace-inexistente.invalid/servicio → error de red: [Errno 8] nodename nor servname provided, or not known (tras 3 intentos)
V8  FALLO   investigacion/fichas/falla-v8.md — https://example.com/pagina-que-no-existe → HTTP 404 (tras 3 intentos)
V8  OK      diseno/patrones-prueba.md — sin incidencias

43 FALLOS · 2 AVISOS
python3 scripts/verificar-investigacion.py --raiz scripts/pruebas  0.71s user 0.08s system 14% cpu 5.350 total
exit=1
```

</details>

<details><summary>3. Los 16 tests (test_verificador_red.py -v)</summary>

```text
test_dominio_idn_falla_por_dns_y_no_por_codificacion (__main__.PruebasDeRed.test_dominio_idn_falla_por_dns_y_no_por_codificacion) ... ok
test_lote_mezcla_ok_y_404 (__main__.PruebasDeRed.test_lote_mezcla_ok_y_404) ... /usr/local/Cellar/python@3.14/3.14.5/Frameworks/Python.framework/Versions/3.14/lib/python3.14/tempfile.py:484: ResourceWarning: Implicitly cleaning up <HTTPError 404: 'Not Found'>
  _warnings.warn(self.warn_message, ResourceWarning)
ok
test_maximo_dos_conexiones_por_dominio (__main__.PruebasDeRed.test_maximo_dos_conexiones_por_dominio) ... ok
test_ruta_con_n_llega_codificada_una_sola_vez (__main__.PruebasDeRed.test_ruta_con_n_llega_codificada_una_sola_vez) ... ok
test_ruta_que_no_responde_da_fallo_con_tiempos_e_intentos (__main__.PruebasDeRed.test_ruta_que_no_responde_da_fallo_con_tiempos_e_intentos) ... ok
test_ruta_que_tarda_8_s_da_ok (__main__.PruebasDeRed.test_ruta_que_tarda_8_s_da_ok) ... ok
test_tiempo_maximo_global_corta_una_ruta_colgada (__main__.PruebasDeRed.test_tiempo_maximo_global_corta_una_ruta_colgada) ... ok
test_argumento_timeout_total_invalido_sale_con_error (__main__.PruebasSinRed.test_argumento_timeout_total_invalido_sale_con_error) ... ok
test_dominio_idn_en_idna (__main__.PruebasSinRed.test_dominio_idn_en_idna) ... ok
test_limites_del_metodo (__main__.PruebasSinRed.test_limites_del_metodo) ... ok
test_lo_ya_codificado_no_se_vuelve_a_codificar (__main__.PruebasSinRed.test_lo_ya_codificado_no_se_vuelve_a_codificar) ... ok
test_redireccion_comparada_en_idna (__main__.PruebasSinRed.test_redireccion_comparada_en_idna) ... ok
test_ruta_y_consulta_con_n_se_codifican (__main__.PruebasSinRed.test_ruta_y_consulta_con_n_se_codifican) ... ok
test_solo_biblioteca_estandar (__main__.PruebasSinRed.test_solo_biblioteca_estandar) ... ok
test_timeout_total_solo_acepta_segundos_positivos (__main__.PruebasSinRed.test_timeout_total_solo_acepta_segundos_positivos) ... ok
test_url_mal_formada_es_fallo_con_motivo_y_sin_reintentos (__main__.PruebasSinRed.test_url_mal_formada_es_fallo_con_motivo_y_sin_reintentos) ... ok

----------------------------------------------------------------------
Ran 16 tests in 19.357s

OK
exit=0
```

</details>

<details><summary>4. Verificador con red, ejecución 1 sobre docs/ (78bbfb0)</summary>

```text
Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-007-verificador/docs · V8: con red (30 s por intento, tiempo máximo 600 s en total)
V1  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V1  OK      investigacion/fichas/artefact.md — sin incidencias
V1  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V1  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V1  OK      investigacion/fichas/devibi.md — sin incidencias
V1  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V1  OK      investigacion/fichas/dogstudio.md — sin incidencias
V1  OK      investigacion/fichas/instrument.md — sin incidencias
V1  OK      investigacion/fichas/media-monks.md — sin incidencias
V1  OK      investigacion/fichas/monopo.md — sin incidencias
V1  OK      investigacion/fichas/pallax-media.md — sin incidencias
V1  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V1  OK      investigacion/fichas/single-grain.md — sin incidencias
V1  OK      investigacion/fichas/sitelabs.md — sin incidencias
V1  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V1  OK      investigacion/fichas/studiodigital.md — sin incidencias
V1  OK      investigacion/fichas/tescanet.md — sin incidencias
V1  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V1  OK      investigacion/fichas/upraw-media.md — sin incidencias
V1  OK      investigacion/fichas/work-and-co.md — sin incidencias
V2  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V2  OK      investigacion/fichas/artefact.md — sin incidencias
V2  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V2  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V2  OK      investigacion/fichas/devibi.md — sin incidencias
V2  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V2  OK      investigacion/fichas/dogstudio.md — sin incidencias
V2  OK      investigacion/fichas/instrument.md — sin incidencias
V2  OK      investigacion/fichas/media-monks.md — sin incidencias
V2  OK      investigacion/fichas/monopo.md — sin incidencias
V2  OK      investigacion/fichas/pallax-media.md — sin incidencias
V2  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V2  OK      investigacion/fichas/single-grain.md — sin incidencias
V2  OK      investigacion/fichas/sitelabs.md — sin incidencias
V2  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V2  OK      investigacion/fichas/studiodigital.md — sin incidencias
V2  OK      investigacion/fichas/tescanet.md — sin incidencias
V2  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V2  OK      investigacion/fichas/upraw-media.md — sin incidencias
V2  OK      investigacion/fichas/work-and-co.md — sin incidencias
V2  OK      investigacion/servicios/01-branding.md — sin incidencias
V2  OK      investigacion/servicios/02-social-media.md — sin incidencias
V2  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
V2  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
V2  OK      investigacion/servicios/05-performance.md — sin incidencias
V2  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
V2  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
V2  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
V2  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
V2  OK      investigacion/servicios/10-cro.md — sin incidencias
V2  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
V2  OK      investigacion/servicios/resumen.md — sin incidencias
V2  OK      investigacion/prueba-social.md — sin incidencias
V2  OK      diseno/patrones-benchmark.md — sin incidencias
V2  OK      diseno/sistema-web-assets.md — sin incidencias
V3  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V3  OK      investigacion/fichas/artefact.md — sin incidencias
V3  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V3  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V3  OK      investigacion/fichas/devibi.md — sin incidencias
V3  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V3  OK      investigacion/fichas/dogstudio.md — sin incidencias
V3  OK      investigacion/fichas/instrument.md — sin incidencias
V3  OK      investigacion/fichas/media-monks.md — sin incidencias
V3  OK      investigacion/fichas/monopo.md — sin incidencias
V3  OK      investigacion/fichas/pallax-media.md — sin incidencias
V3  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V3  OK      investigacion/fichas/single-grain.md — sin incidencias
V3  OK      investigacion/fichas/sitelabs.md — sin incidencias
V3  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V3  OK      investigacion/fichas/studiodigital.md — sin incidencias
V3  OK      investigacion/fichas/tescanet.md — sin incidencias
V3  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V3  OK      investigacion/fichas/upraw-media.md — sin incidencias
V3  OK      investigacion/fichas/work-and-co.md — sin incidencias
V4  OK      capturas (192 archivos) — ninguna duplicada
V5  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V5  OK      investigacion/fichas/artefact.md — sin incidencias
V5  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V5  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V5  OK      investigacion/fichas/devibi.md — sin incidencias
V5  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V5  OK      investigacion/fichas/dogstudio.md — sin incidencias
V5  AVISO   investigacion/fichas/instrument.md — «Desarrollo Web»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/media-monks.md — sin incidencias
V5  OK      investigacion/fichas/monopo.md — sin incidencias
V5  AVISO   investigacion/fichas/pallax-media.md — «Branding»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V5  AVISO   investigacion/fichas/single-grain.md — «Inteligencia artificial»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/sitelabs.md — sin incidencias
V5  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V5  AVISO   investigacion/fichas/studiodigital.md — «Performance»: portada única declarada; respaldar con la captura de la home
V5  AVISO   investigacion/fichas/studiodigital.md — «SEO y GEO»: portada única declarada; respaldar con la captura de la home
V5  AVISO   investigacion/fichas/studiodigital.md — «CRO»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/tescanet.md — sin incidencias
V5  AVISO   investigacion/fichas/trajectory-web-design.md — «SEO y GEO»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/upraw-media.md — sin incidencias
V5  OK      investigacion/fichas/work-and-co.md — sin incidencias
V6  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V6  OK      investigacion/fichas/artefact.md — sin incidencias
V6  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V6  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V6  OK      investigacion/fichas/devibi.md — sin incidencias
V6  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V6  OK      investigacion/fichas/dogstudio.md — sin incidencias
V6  OK      investigacion/fichas/instrument.md — sin incidencias
V6  OK      investigacion/fichas/media-monks.md — sin incidencias
V6  OK      investigacion/fichas/monopo.md — sin incidencias
V6  OK      investigacion/fichas/pallax-media.md — sin incidencias
V6  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V6  OK      investigacion/fichas/single-grain.md — sin incidencias
V6  OK      investigacion/fichas/sitelabs.md — sin incidencias
V6  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V6  OK      investigacion/fichas/studiodigital.md — sin incidencias
V6  OK      investigacion/fichas/tescanet.md — sin incidencias
V6  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V6  OK      investigacion/fichas/upraw-media.md — sin incidencias
V6  OK      investigacion/fichas/work-and-co.md — sin incidencias
V6  OK      investigacion/servicios/01-branding.md — sin incidencias
V6  OK      investigacion/servicios/02-social-media.md — sin incidencias
V6  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
V6  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
V6  OK      investigacion/servicios/05-performance.md — sin incidencias
V6  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
V6  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
V6  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
V6  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
V6  OK      investigacion/servicios/10-cro.md — sin incidencias
V6  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
V6  OK      investigacion/servicios/resumen.md — sin incidencias
V6  OK      investigacion/prueba-social.md — sin incidencias
V6  OK      diseno/patrones-benchmark.md — sin incidencias
V6  OK      diseno/sistema-web-assets.md — sin incidencias
V7  OK      investigacion/fichas — 20 fichas: 10 comparables, 10 referentes/especialistas
V8  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V8  OK      investigacion/fichas/artefact.md — sin incidencias
V8  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V8  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V8  OK      investigacion/fichas/devibi.md — sin incidencias
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/a-propos/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-ecommerce-shopify/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-facebook-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-geo-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-google-ads-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-google-shopping-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-instagram-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-linkedin-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-pinterest-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-referencement-local-google-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-referencement-seo-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-snapchat-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-tiktok-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-wordpress-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/nos-references/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  OK      investigacion/fichas/dogstudio.md — sin incidencias
V8  OK      investigacion/fichas/instrument.md — sin incidencias
V8  OK      investigacion/fichas/media-monks.md — sin incidencias
V8  OK      investigacion/fichas/monopo.md — sin incidencias
V8  OK      investigacion/fichas/pallax-media.md — sin incidencias
V8  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V8  OK      investigacion/fichas/single-grain.md — sin incidencias
V8  OK      investigacion/fichas/sitelabs.md — sin incidencias
V8  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V8  OK      investigacion/fichas/studiodigital.md — sin incidencias
V8  OK      investigacion/fichas/tescanet.md — sin incidencias
V8  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V8  OK      investigacion/fichas/upraw-media.md — sin incidencias
V8  OK      investigacion/fichas/work-and-co.md — sin incidencias
V8  OK      investigacion/servicios/01-branding.md — sin incidencias
V8  OK      investigacion/servicios/02-social-media.md — sin incidencias
V8  AVISO   investigacion/servicios/03-desarrollo-web.md — https://www.digiberries.fr/agence-wordpress-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/servicios/04-campanas-publicitarias.md — https://www.digiberries.fr/agence-google-ads-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/servicios/05-performance.md — https://www.digiberries.fr/agence-google-shopping-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
V8  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
V8  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
V8  AVISO   investigacion/servicios/09-seo-geo.md — https://www.digiberries.fr/agence-geo-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/servicios/09-seo-geo.md — https://www.digiberries.fr/agence-referencement-seo-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  OK      investigacion/servicios/10-cro.md — sin incidencias
V8  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
V8  OK      investigacion/servicios/resumen.md — sin incidencias
V8  AVISO   investigacion/prueba-social.md — https://www.facebook.com/business/learn/certification/faqs/exam-cost → HTTP 400 (bloqueo antibot o de región): respaldar con captura
V8  OK      diseno/patrones-benchmark.md — sin incidencias
V8  OK      diseno/sistema-web-assets.md — sin incidencias

0 FALLOS · 29 AVISOS
python3 scripts/verificar-investigacion.py  5.58s user 4.30s system 15% cpu 1:03.50 total
exit=0
```

</details>

<details><summary>5. Verificador con red, ejecución 2 sobre docs/ (78bbfb0)</summary>

```text
Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-007-verificador/docs · V8: con red (30 s por intento, tiempo máximo 600 s en total)
V1  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V1  OK      investigacion/fichas/artefact.md — sin incidencias
V1  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V1  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V1  OK      investigacion/fichas/devibi.md — sin incidencias
V1  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V1  OK      investigacion/fichas/dogstudio.md — sin incidencias
V1  OK      investigacion/fichas/instrument.md — sin incidencias
V1  OK      investigacion/fichas/media-monks.md — sin incidencias
V1  OK      investigacion/fichas/monopo.md — sin incidencias
V1  OK      investigacion/fichas/pallax-media.md — sin incidencias
V1  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V1  OK      investigacion/fichas/single-grain.md — sin incidencias
V1  OK      investigacion/fichas/sitelabs.md — sin incidencias
V1  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V1  OK      investigacion/fichas/studiodigital.md — sin incidencias
V1  OK      investigacion/fichas/tescanet.md — sin incidencias
V1  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V1  OK      investigacion/fichas/upraw-media.md — sin incidencias
V1  OK      investigacion/fichas/work-and-co.md — sin incidencias
V2  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V2  OK      investigacion/fichas/artefact.md — sin incidencias
V2  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V2  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V2  OK      investigacion/fichas/devibi.md — sin incidencias
V2  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V2  OK      investigacion/fichas/dogstudio.md — sin incidencias
V2  OK      investigacion/fichas/instrument.md — sin incidencias
V2  OK      investigacion/fichas/media-monks.md — sin incidencias
V2  OK      investigacion/fichas/monopo.md — sin incidencias
V2  OK      investigacion/fichas/pallax-media.md — sin incidencias
V2  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V2  OK      investigacion/fichas/single-grain.md — sin incidencias
V2  OK      investigacion/fichas/sitelabs.md — sin incidencias
V2  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V2  OK      investigacion/fichas/studiodigital.md — sin incidencias
V2  OK      investigacion/fichas/tescanet.md — sin incidencias
V2  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V2  OK      investigacion/fichas/upraw-media.md — sin incidencias
V2  OK      investigacion/fichas/work-and-co.md — sin incidencias
V2  OK      investigacion/servicios/01-branding.md — sin incidencias
V2  OK      investigacion/servicios/02-social-media.md — sin incidencias
V2  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
V2  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
V2  OK      investigacion/servicios/05-performance.md — sin incidencias
V2  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
V2  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
V2  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
V2  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
V2  OK      investigacion/servicios/10-cro.md — sin incidencias
V2  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
V2  OK      investigacion/servicios/resumen.md — sin incidencias
V2  OK      investigacion/prueba-social.md — sin incidencias
V2  OK      diseno/patrones-benchmark.md — sin incidencias
V2  OK      diseno/sistema-web-assets.md — sin incidencias
V3  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V3  OK      investigacion/fichas/artefact.md — sin incidencias
V3  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V3  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V3  OK      investigacion/fichas/devibi.md — sin incidencias
V3  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V3  OK      investigacion/fichas/dogstudio.md — sin incidencias
V3  OK      investigacion/fichas/instrument.md — sin incidencias
V3  OK      investigacion/fichas/media-monks.md — sin incidencias
V3  OK      investigacion/fichas/monopo.md — sin incidencias
V3  OK      investigacion/fichas/pallax-media.md — sin incidencias
V3  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V3  OK      investigacion/fichas/single-grain.md — sin incidencias
V3  OK      investigacion/fichas/sitelabs.md — sin incidencias
V3  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V3  OK      investigacion/fichas/studiodigital.md — sin incidencias
V3  OK      investigacion/fichas/tescanet.md — sin incidencias
V3  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V3  OK      investigacion/fichas/upraw-media.md — sin incidencias
V3  OK      investigacion/fichas/work-and-co.md — sin incidencias
V4  OK      capturas (192 archivos) — ninguna duplicada
V5  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V5  OK      investigacion/fichas/artefact.md — sin incidencias
V5  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V5  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V5  OK      investigacion/fichas/devibi.md — sin incidencias
V5  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V5  OK      investigacion/fichas/dogstudio.md — sin incidencias
V5  AVISO   investigacion/fichas/instrument.md — «Desarrollo Web»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/media-monks.md — sin incidencias
V5  OK      investigacion/fichas/monopo.md — sin incidencias
V5  AVISO   investigacion/fichas/pallax-media.md — «Branding»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V5  AVISO   investigacion/fichas/single-grain.md — «Inteligencia artificial»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/sitelabs.md — sin incidencias
V5  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V5  AVISO   investigacion/fichas/studiodigital.md — «Performance»: portada única declarada; respaldar con la captura de la home
V5  AVISO   investigacion/fichas/studiodigital.md — «SEO y GEO»: portada única declarada; respaldar con la captura de la home
V5  AVISO   investigacion/fichas/studiodigital.md — «CRO»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/tescanet.md — sin incidencias
V5  AVISO   investigacion/fichas/trajectory-web-design.md — «SEO y GEO»: portada única declarada; respaldar con la captura de la home
V5  OK      investigacion/fichas/upraw-media.md — sin incidencias
V5  OK      investigacion/fichas/work-and-co.md — sin incidencias
V6  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V6  OK      investigacion/fichas/artefact.md — sin incidencias
V6  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V6  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V6  OK      investigacion/fichas/devibi.md — sin incidencias
V6  OK      investigacion/fichas/digiberries-paris.md — sin incidencias
V6  OK      investigacion/fichas/dogstudio.md — sin incidencias
V6  OK      investigacion/fichas/instrument.md — sin incidencias
V6  OK      investigacion/fichas/media-monks.md — sin incidencias
V6  OK      investigacion/fichas/monopo.md — sin incidencias
V6  OK      investigacion/fichas/pallax-media.md — sin incidencias
V6  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V6  OK      investigacion/fichas/single-grain.md — sin incidencias
V6  OK      investigacion/fichas/sitelabs.md — sin incidencias
V6  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V6  OK      investigacion/fichas/studiodigital.md — sin incidencias
V6  OK      investigacion/fichas/tescanet.md — sin incidencias
V6  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V6  OK      investigacion/fichas/upraw-media.md — sin incidencias
V6  OK      investigacion/fichas/work-and-co.md — sin incidencias
V6  OK      investigacion/servicios/01-branding.md — sin incidencias
V6  OK      investigacion/servicios/02-social-media.md — sin incidencias
V6  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
V6  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
V6  OK      investigacion/servicios/05-performance.md — sin incidencias
V6  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
V6  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
V6  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
V6  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
V6  OK      investigacion/servicios/10-cro.md — sin incidencias
V6  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
V6  OK      investigacion/servicios/resumen.md — sin incidencias
V6  OK      investigacion/prueba-social.md — sin incidencias
V6  OK      diseno/patrones-benchmark.md — sin incidencias
V6  OK      diseno/sistema-web-assets.md — sin incidencias
V7  OK      investigacion/fichas — 20 fichas: 10 comparables, 10 referentes/especialistas
V8  OK      investigacion/fichas/agencia-buffalo.md — sin incidencias
V8  OK      investigacion/fichas/artefact.md — sin incidencias
V8  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
V8  OK      investigacion/fichas/code-and-theory.md — sin incidencias
V8  OK      investigacion/fichas/devibi.md — sin incidencias
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/a-propos/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-ecommerce-shopify/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-facebook-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-geo-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-google-ads-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-google-shopping-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-instagram-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-linkedin-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-pinterest-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-referencement-local-google-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-referencement-seo-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-snapchat-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-tiktok-ads/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/agence-wordpress-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/fichas/digiberries-paris.md — https://www.digiberries.fr/nos-references/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  OK      investigacion/fichas/dogstudio.md — sin incidencias
V8  OK      investigacion/fichas/instrument.md — sin incidencias
V8  OK      investigacion/fichas/media-monks.md — sin incidencias
V8  OK      investigacion/fichas/monopo.md — sin incidencias
V8  OK      investigacion/fichas/pallax-media.md — sin incidencias
V8  OK      investigacion/fichas/screenfire-media.md — sin incidencias
V8  OK      investigacion/fichas/single-grain.md — sin incidencias
V8  OK      investigacion/fichas/sitelabs.md — sin incidencias
V8  OK      investigacion/fichas/stratagemma-studio.md — sin incidencias
V8  OK      investigacion/fichas/studiodigital.md — sin incidencias
V8  OK      investigacion/fichas/tescanet.md — sin incidencias
V8  OK      investigacion/fichas/trajectory-web-design.md — sin incidencias
V8  OK      investigacion/fichas/upraw-media.md — sin incidencias
V8  OK      investigacion/fichas/work-and-co.md — sin incidencias
V8  OK      investigacion/servicios/01-branding.md — sin incidencias
V8  OK      investigacion/servicios/02-social-media.md — sin incidencias
V8  AVISO   investigacion/servicios/03-desarrollo-web.md — https://www.digiberries.fr/agence-wordpress-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/servicios/04-campanas-publicitarias.md — https://www.digiberries.fr/agence-google-ads-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/servicios/05-performance.md — https://www.digiberries.fr/agence-google-shopping-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
V8  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
V8  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
V8  AVISO   investigacion/servicios/09-seo-geo.md — https://www.digiberries.fr/agence-geo-a-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  AVISO   investigacion/servicios/09-seo-geo.md — https://www.digiberries.fr/agence-referencement-seo-paris/ → HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura
V8  OK      investigacion/servicios/10-cro.md — sin incidencias
V8  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
V8  OK      investigacion/servicios/resumen.md — sin incidencias
V8  AVISO   investigacion/prueba-social.md — https://www.facebook.com/business/learn/certification/faqs/exam-cost → HTTP 400 (bloqueo antibot o de región): respaldar con captura
V8  OK      diseno/patrones-benchmark.md — sin incidencias
V8  OK      diseno/sistema-web-assets.md — sin incidencias

0 FALLOS · 29 AVISOS
python3 scripts/verificar-investigacion.py  5.71s user 4.08s system 12% cpu 1:17.16 total
exit=0
```

</details>
>
> **[2026-10-13] clia:** comprobé `78bbfb0` por mi cuenta: `python3 -m unittest scripts/pruebas/test_verificador_red.py` da **16 tests OK**. `--raiz scripts/pruebas --sin-red` da `41 FALLOS · 1 AVISOS`, igual que antes del cambio. `docs/` sin red da `0 FALLOS`. Lanzo a Dexia según [`DECISION-008`](DECISION-008-clia-invoca-a-dexia-por-codex-exec.md). Encargo exacto, sin nada más: `Eres Dexia. Lee tu ficha y atiende REVIEW-007 según el protocolo.` Carpeta: worktree de la rama `feat/TASK-007-mantenimiento-verificador`. REVIEW-007 todavía no existe: lo crea Dexia.
>
> **[2026-10-13 06:22] dexia:** emití [`REVIEW-007`](REVIEW-007-mantenimiento-verificador.md): ❌ RECHAZADO sobre `78bbfb0`. Dos defectos 🔴 reproducidos: una URL mal formada aborta V8 antes de registrar FALLO y las redirecciones pueden superar el tiempo máximo por intento. Kia: corregirlos y pedir nueva ronda con regresiones y gate completo.
