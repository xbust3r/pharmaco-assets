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
actualizado: 2026-10-08
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
