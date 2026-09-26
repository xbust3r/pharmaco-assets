---
tipo: RFC
id: RFC-001
titulo: Alcance, stack, criticidad y verificación
de: clia
para: [miguel]
cc: [dexia, ania]
estado: ABIERTA
area: docs
relacionado: [AGENTS.md, protocolo.md, DECISION-001]
creado: 2026-09-26
actualizado: 2026-09-26
---

# RFC-001 — Alcance, stack, criticidad y verificación

## Problema

El paquete del método exige adaptar dos cosas al proyecto: **la criticidad 🔴/🟡/🟢** y **los comandos del gate**. El repositorio está vacío y no se sabe qué es Pharmaco Assets, así que las dos están como provisionales. Sin comandos reales, el gate es decorativo.

## Preguntas para Miguel

1. **¿Qué es el proyecto?** ¿Una biblioteca de assets, el front de un sitio, material promocional? ¿Para qué marca o cliente?
2. **¿Stack?** ¿Hay build (Vite, como en Blackgrow), optimización de imágenes, validación de assets?
3. **¿Dónde viven los originales** y qué se publica desde aquí?
4. **¿Hay contenido regulado?** Claims sanitarios, prospectos, etiquetado. Si lo hay, es 🔴.
5. **¿Habrá remoto Git?** La rutina de sesión asume `git pull`.

## Propuesta

Con las respuestas:

- Clia reescribe «Qué entra» en la tabla de criticidad del protocolo y las reglas del código de `AGENTS.md`.
- Ania aporta la línea real de verificación completa.
- Dexia opina sobre la calibración y fija qué revisa en cada review.
- Se abre la primera TASK.

## Alternativas consideradas

| Opción | A favor | En contra |
| --- | --- | --- |
| Calibrar tras conocer el proyecto (propuesta) | El gate protege lo que de verdad falla en silencio | Retrasa la primera TASK |
| Heredar la criticidad de Blackgrow | Inmediato | El paquete lo prohíbe: está calibrada para otro front-end |

## Impacto

- Qué se ve afectado: `AGENTS.md`, `protocolo.md`, fichas de Dexia y Ania.
- ¿Es 🔴? No: es documentación.

## 💬 Hilo

> **[2026-09-26 15:40] clia:** abro el RFC. Prefiero un vacío declarado a un gate mal calibrado.
