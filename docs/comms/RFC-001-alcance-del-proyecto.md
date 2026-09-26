---
tipo: RFC
id: RFC-001
titulo: Alcance, stack y calibración de la criticidad
de: clia
para: [miguel]
cc: [dexia, ania]
estado: ABIERTA
area: docs
relacionado: [AGENTS.md, DECISION-001]
creado: 2026-09-26
actualizado: 2026-09-26
---

# RFC-001 — Alcance, stack y calibración de la criticidad

## Problema

El repositorio está vacío. La tabla de criticidad y la «verificación completa del proyecto» de `AGENTS.md` son genéricas: sin saber qué es Pharmaco Assets no se puede decidir qué es 🔴 ni qué comando demuestra que el proyecto está sano.

## Preguntas para Miguel

1. **¿Qué es el proyecto?** ¿Biblioteca de assets de marca, assets de un sitio web, material promocional, otra cosa? ¿Para qué cliente o marca?
2. **¿Dónde viven los originales?** ¿Aquí, en un DAM, en un bucket/CDN? ¿Hay algo que se publique directamente desde este repositorio?
3. **¿Stack?** ¿Hay código (build, optimización de imágenes, un sitio) o sólo archivos?
4. **¿Hay contenido regulado?** Claims sanitarios, prospectos, etiquetado: si lo hay, cualquier cambio de texto es 🔴 y quizá pida una validación externa.
5. **¿Quién despliega?** En CoverageFox lo hacía Miguel por merge a `production`.

## Propuesta

Con las respuestas, Clia reescribe la sección de criticidad y la de verificación de `AGENTS.md`, Dexia opina sobre si el gate está bien calibrado y Ania aporta el comando real de verificación. Luego se abre la primera TASK.

## Impacto

- **¿Es 🔴?** No: es documentación.

## 💬 Hilo

> **[2026-09-26 15:10] clia:** abro el RFC. Dejo la criticidad provisional en vez de inventar una: prefiero un vacío declarado a un gate mal calibrado.
