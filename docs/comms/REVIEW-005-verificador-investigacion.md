---
tipo: REVIEW
id: REVIEW-005
titulo: Revisión del verificador de la investigación
de: dexia
para: kia
cc: [clia, miguel]
estado: RECHAZADO
task: TASK-005
rama: feat/TASK-005-verificador-investigacion
criticidad: "🔴"
creado: 2026-10-08
actualizado: 2026-10-10
---

# REVIEW-005 — Verificador de la investigación

## Alcance revisado

Rama `feat/TASK-005-verificador-investigacion` hasta `06f2e25`: script, documentación, casos de prueba y salidas pegadas en TASK-005. Criterio: DECISION-006 y sus aclaraciones.

## Veredicto

❌ **RECHAZADO.** Dos comprobaciones pueden dar OK ante datos que deben producir FALLO. El gate 🔴 no está listo para integrarse.

## Hallazgos

| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | `scripts/verificar-investigacion.py:216-227` | 🔴 | V5 sólo inspecciona filas cuya tercera celda comienza literalmente por `Sí`, y da OK si no encuentra ninguna. Una fila `\| 1 \| Branding \| **Sí** \| Marca \| \|` pasa sin URL; también pasa una ficha sin la sección «Frente al catálogo». La primera contradice V5 y la segunda permite cerrar el gate sin la tabla de 11 servicios exigida por TASK-001. Normalizar el formato de la celda y fallar cuando falten la sección o las 11 filas. Añadir regresiones para ambos casos. |
| 2 | `scripts/verificar-investigacion.py:123-130` | 🔴 | V2 llama «PNG válido» a cualquier archivo con firma e `IHDR` en los primeros 16 bytes. Un archivo de exactamente 16 bytes, sin dimensiones, datos de imagen ni cierre, devuelve `None` y se marca OK. Validar la estructura completa de PNG/WebP con biblioteca estándar y añadir una regresión con archivo truncado. |

## Evidencia de verificación

La salida con red del repositorio y de `scripts/pruebas/` está pegada íntegra por Kia en TASK-005. Para aislar los falsos OK ejecuté funciones del script sobre entradas mínimas, sin modificar los entregables:

```text
V5 sección ausente: []
V5 Sí en negrita y URL vacía: []
V2 PNG truncado: None
```

`[]` significa que V5 no registra problema; `None` significa que V2 acepta el archivo. La prueba con `--raiz scripts/pruebas --sin-red` continuó detectando los fallos existentes (`15 FALLOS · 1 AVISOS`), pero sus casos actuales no cubren estos dos falsos OK. No repetí V8 con red: la salida de esa ejecución ya consta en el hilo de TASK-005.

## Corrección requerida

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
