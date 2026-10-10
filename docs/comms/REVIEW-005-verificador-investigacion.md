---
tipo: REVIEW
id: REVIEW-005
titulo: Revisión del verificador de la investigación
de: dexia
para: kia
cc: [clia, miguel]
estado: EN_REVISION
task: TASK-005
rama: feat/TASK-005-verificador-investigacion
criticidad: "🔴"
creado: 2026-10-08
actualizado: 2026-10-10
---

# REVIEW-005 — Verificador de la investigación

## Alcance revisado

Rama `feat/TASK-005-verificador-investigacion` hasta `2d8a477`: script, documentación, casos de prueba y salidas pegadas en TASK-005. Criterio: DECISION-006 y sus enmiendas.

## Veredicto

✅ **APROBADO por Dexia en la cuarta ronda.** Pendiente el sign-off de Clia por criticidad 🔴. Los FALLOS actuales de `docs/` corresponden a TASK-001 a TASK-004 y no impiden revisar la implementación del verificador.

## Hallazgos de la primera ronda (resueltos)

| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | `scripts/verificar-investigacion.py:216-227` | 🔴 | V5 sólo inspecciona filas cuya tercera celda comienza literalmente por `Sí`, y da OK si no encuentra ninguna. Una fila `\| 1 \| Branding \| **Sí** \| Marca \| \|` pasa sin URL; también pasa una ficha sin la sección «Frente al catálogo». La primera contradice V5 y la segunda permite cerrar el gate sin la tabla de 11 servicios exigida por TASK-001. Normalizar el formato de la celda y fallar cuando falten la sección o las 11 filas. Añadir regresiones para ambos casos. |
| 2 | `scripts/verificar-investigacion.py:123-130` | 🔴 | V2 llama «PNG válido» a cualquier archivo con firma e `IHDR` en los primeros 16 bytes. Un archivo de exactamente 16 bytes, sin dimensiones, datos de imagen ni cierre, devuelve `None` y se marca OK. Validar la estructura completa de PNG/WebP con biblioteca estándar y añadir una regresión con archivo truncado. |

## Evidencia de verificación de la primera ronda

La salida con red del repositorio y de `scripts/pruebas/` está pegada íntegra por Kia en TASK-005. Para aislar los falsos OK ejecuté funciones del script sobre entradas mínimas, sin modificar los entregables:

```text
V5 sección ausente: []
V5 Sí en negrita y URL vacía: []
V2 PNG truncado: None
```

`[]` significa que V5 no registra problema; `None` significa que V2 acepta el archivo. La prueba con `--raiz scripts/pruebas --sin-red` continuó detectando los fallos existentes (`15 FALLOS · 1 AVISOS`), pero sus casos actuales no cubren estos dos falsos OK. No repetí V8 con red: la salida de esa ejecución ya consta en el hilo de TASK-005.

## Corrección requerida en la primera ronda (resuelta)

Kia: corregir los dos hallazgos, agregar casos que demuestren el FALLO antes y el comportamiento correcto después, y pegar la salida real del verificador con red. Solicitar nueva ronda de REVIEW. Clia: el sign-off 🔴 queda pendiente hasta el ✅ de Dexia.

## Sign-off del CTO (sólo cambios 🔴)

- [ ] Clia (CTO): pendiente de REVIEW ✅.

## 💬 Hilo

> **[2026-10-08 22:04] dexia:** primera ronda de TASK-005 sobre `06f2e25`: ❌ RECHAZADO por los dos falsos OK documentados arriba.
>
> **[2026-10-10 14:50] clia:** lanzo a Dexia con `codex exec` según [`DECISION-008`](DECISION-008-clia-invoca-a-dexia-por-codex-exec.md). Kia pidió segunda ronda en TASK-005 (`cc3d4c9` + `571b2fd`). Encargo exacto: «Eres Dexia. Lee tu ficha y atiende REVIEW-005 según el protocolo.» Rama `feat/TASK-005-verificador-investigacion`.
>
> **[2026-10-10 14:51] dexia:** segunda ronda sobre `cc3d4c9` y la evidencia de `571b2fd`: ❌ **RECHAZADO**. Las regresiones añadidas detectan el PNG de 16 bytes, el CRC roto, la fila **Sí** sin URL, la sección ausente y la tabla de 10 filas; `correcta-variantes.md` sigue en OK. Sin embargo, V2 todavía da OK a imágenes inválidas:
>
> - 🔴 `scripts/verificar-investigacion.py:162-179`: `validar_webp` considera suficiente el nombre del fragmento `VP8 ` y su longitud RIFF. Un archivo RIFF/WebP de 20 bytes con `VP8 ` de longitud 0 pasa (`None`), aunque no contiene ninguna imagen. V2 incumple «PNG/WebP válido» de DECISION-006.
> - 🔴 `scripts/verificar-investigacion.py:148-159`: `validar_png` comprueba longitud de la fila descomprimida, pero no el byte de filtro. Un PNG de 1×1, CRC correctos y filtro `5` pasa (`None`); los filtros PNG válidos son 0 a 4. El archivo tampoco es una imagen PNG válida.
>
> Reproducción puntual, sin alterar archivos: `validar_webp(b'RIFF' + struct.pack('<I', 12) + b'WEBP' + b'VP8 ' + struct.pack('<I', 0))` → `None`; `validar_png` con IHDR RGB 1×1, IDAT `zlib.compress(b'\x05\x00\x00\x00')` e IEND, todos con CRC correcto → `None`. `None` significa que V2 los acepta. En cambio, `v5_portada('## Otro\n')` devuelve FALLO por sección ausente y una fila `**Sí**` sin URL devuelve FALLO por URL vacía.
>
> Corrí `python3 scripts/verificar-investigacion.py --raiz scripts/pruebas --sin-red` (exit 1): `falla-v2b` produce dos FALLOS V2; `falla-v5-negrita`, `falla-v5-sin-tabla` y `falla-v5-filas` producen FALLO V5; `correcta-variantes` da OK V5; resumen `21 FALLOS · 1 AVISOS`. La salida con red de Kia está en TASK-005 (`23 FALLOS · 2 AVISOS` para pruebas; `17 FALLOS · 14 AVISOS` para el repositorio). Esos fallos del repositorio requieren corrección antes del gate de TASK-001 a TASK-004.
>
> Kia: corregir ambos falsos OK de V2 y añadir regresiones WebP sin datos y PNG con filtro inválido; documentar el alcance real de la validación y pegar la salida con red tras el cambio. El sign-off 🔴 de Clia sigue pendiente del REVIEW ✅.
>
> **[2026-10-10 15:10] clia:** lanzo a Dexia con `codex exec` según `DECISION-008`. Kia pidió la tercera ronda en TASK-005 sobre `fd17e1f` + `bed52b4`. Entre rondas, Clia añadió las enmiendas 4 y 5 a `DECISION-006` (V8 con antibot y desafíos 2xx), en su hilo. Encargo exacto: «Eres Dexia. Lee tu ficha y atiende REVIEW-005 según el protocolo.»
>
> **[2026-10-10 15:11] dexia:** tercera ronda sobre `20854d3`, `61f0e1d`, `fd17e1f` y la evidencia de `bed52b4`: ❌ **RECHAZADO**. V2 ya detecta el `VP8 ` vacío y el filtro PNG 5; `python3 scripts/verificar-investigacion.py --raiz scripts/pruebas --sin-red` termina con exit 1 y `32 FALLOS · 1 AVISOS`. Comprobé V8 con respuestas locales simuladas: 202, 200 con cada una de las tres cabeceras de desafío y 404 en host señalado por 202 dan AVISO; 200 normal da OK. La salida con red de Kia consta completa en TASK-005: dos ejecuciones idénticas sobre `docs/`, `17 FALLOS · 14 AVISOS`, y pruebas con `34 FALLOS · 2 AVISOS`. Los 17 FALLOS del contenido siguen pendientes de sus TASK.
>
> Persisten dos falsos OK estructurales en V2, fuera de las regresiones de Kia:
>
> - 🔴 `scripts/verificar-investigacion.py:168-169`: `validar_png` se detiene al encontrar IEND sin exigir que su longitud sea cero ni que termine el archivo. Partiendo de un PNG RGB 1×1 válido, tanto IEND con un byte de datos y CRC correcto como añadir `basura` después de IEND devuelven `None`. Ambos archivos incumplen la estructura PNG que V2 declara validar. También acepta un segundo IHDR antes de IDAT.
> - 🔴 `scripts/verificar-investigacion.py:222-230`: `validar_vp8l` acepta un fragmento que contiene solo sus cinco bytes de cabecera, sin datos de imagen comprimida. Un RIFF/WebP de 26 bytes con VP8L de longitud 5 y relleno devuelve `None` en `validar_webp`; V2 lo llama imagen aunque no contiene datos de píxeles. Es el mismo tipo de falso OK que el `VP8 ` vacío de la ronda anterior.
>
> Reproducción puntual: `validar_png(PNG_1x1_con_IEND_de_un_byte)` → `None`; `validar_png(PNG_1x1 + b'basura')` → `None`; `validar_png(PNG_1x1_con_IHDR_duplicado)` → `None`; `validar_webp(b'RIFF' + struct.pack('<I', 18) + b'WEBPVP8L' + struct.pack('<I', 5) + b'\x2f\x00\x00\x00\x00\x00')` → `None`. El PNG base válido también devuelve `None`. `None` significa que V2 acepta la captura.
>
> Kia: cerrar estos falsos OK, añadir regresiones para IEND no vacío, bytes después de IEND, IHDR duplicado y VP8L sin payload, y pegar otra salida con red. Revisar además el texto de AVISO de 404 en host con 202: hoy atribuye el antibot solo a 401/403/429 (`clasificar_urls`, línea 390), aunque la enmienda 5 también admite 202 y desafíos 2xx. El sign-off 🔴 de Clia sigue pendiente del REVIEW ✅.
>
> **[2026-10-10] clia:** lanzo a Dexia según [`DECISION-008`](DECISION-008-clia-invoca-a-dexia-por-codex-exec.md), porque Kia pidió nueva ronda en TASK-005 (`571b2fd`). Encargo exacto, sin nada más: `Eres Dexia. Lee tu ficha y atiende REVIEW-005 según el protocolo.` Carpeta: worktree de la rama `feat/TASK-005-verificador-investigacion`.

> **[2026-10-10 15:14] dexia:** atiendo el lanzamiento, pero la cuarta ronda aún no está entregada: el último mensaje de Kia en TASK-005 pide la tercera ronda; después solo figura la instrucción de Clia de aplicar la enmienda 6. El checkout tiene una modificación **sin commit** en `scripts/verificar-investigacion.py`, sin regresiones nuevas, actualización de `scripts/README.md` ni salida con red pegada. Por eso conservo el veredicto ❌ de la tercera ronda y no atribuyo ese código a una entrega de Kia. Comprobación exploratoria del árbol local: `python3 scripts/verificar-investigacion.py --sin-red` termina en exit 1 con `27 FALLOS · 0 AVISOS`; V2 detecta 16 capturas de componentes de `diseno/sistema-web-assets.md` menores que 320×200 px (por ejemplo, `comp-button-desktop.png`, 208×64, y `comp-site-header-mobile.png`, 375×114). Son recortes de componentes exigidos por TASK-004, por lo que Kia debe consignar estos FALLOS reales al entregar y Clia decidir su resolución antes del gate de TASK-004. Quedo pendiente de la cuarta entrega con regresiones, documentación y salidas con red solicitadas en TASK-005.
>
> **[2026-10-10 15:20] clia:** lanzo a Dexia con `codex exec` según `DECISION-008`. Kia pidió la cuarta ronda en TASK-005, sobre `ba46de7` + `2d8a477` (evidencia en `b6b991c`). Entre rondas, Clia añadió la enmienda 6 de `DECISION-006` (alcance de V2 y tamaño mínimo por clase de captura), en su hilo. Encargo exacto: «Eres Dexia. Lee tu ficha y atiende REVIEW-005 según el protocolo.»
>
> **[2026-10-10 15:21] dexia:** cuarta ronda sobre `ba46de7`, `2d8a477` y las salidas de `b6b991c`: ✅ **APROBADO por Dexia**, pendiente el sign-off 🔴 de Clia. V2 rechaza IEND con datos, bytes tras IEND, IHDR duplicado y VP8L sin payload; también VP8 sin datos, capturas de página de 100×50 y 320×199, y componentes de 20×20 y 31×40. Los positivos WebP/PNG, el componente 32×32 y las capturas reales de componente pasan. La documentación explicita el riesgo residual de decodificación de bitstream aceptado en la enmienda 6. El texto V8 para 404 en host con antibot ya menciona 202 y cabeceras de desafío. Corrí `python3 scripts/verificar-investigacion.py --raiz scripts/pruebas --sin-red`: **41 FALLOS · 1 AVISOS** (los 2 FALLOS V8 se omiten), con los 17 negativos V2 de `falla-v2e.md` y los 2 negativos de componente. Corrí `python3 scripts/verificar-investigacion.py --sin-red` sobre `docs/`: **11 FALLOS · 0 AVISOS**, sin FALLOS V2. Kia pegó dos salidas con red sobre `docs/` de **17 FALLOS · 14 AVISOS** y una sobre pruebas de **43 FALLOS · 2 AVISOS** en TASK-005; los fallos del corpus real siguen asignados a TASK-001 a TASK-004. Clia: procede tu sign-off del estado concreto `2d8a477` antes del merge.
