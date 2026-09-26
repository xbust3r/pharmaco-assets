---
tipo: RFC
id: RFC-001
titulo: Alcance, stack, criticidad y verificación
de: clia
para: [miguel]
cc: [dexia, ania]
estado: EN_DEBATE
area: docs
relacionado: [AGENTS.md, protocolo.md, DECISION-001, TASK-001, linea-base-2020.md]
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
>
> **[2026-09-26 16:15] miguel:** haremos el HTML de este proyecto. Ania busca en internet y trae la información, Dexia valida, Clia es la CTO. Es una agencia de marketing y desarrollo de 2020; se quiere retomar, pero los servicios están desfasados. Compararlo con webs de agencias europeas y americanas. Pasamos a la etapa de investigación.
>
> **[2026-09-26 16:20] clia:** con esto quedan respondidas las preguntas 1 y 3:
>
> - **Qué es:** el sitio HTML de **Pharmaco**, «laboratorio digital de Marketing & Software» con sede en Perú, fundado en 2020. El sitio de entonces es un WordPress en `~/servers/pharmaco.pe` que nunca se terminó: lo documento en [`linea-base-2020.md`](../linea-base-2020.md).
> - **Qué se publica:** el nuevo HTML del sitio de la agencia.
>
> Siguen abiertas la 2 (stack del HTML nuevo), la 4 (contenido regulado: por el nombre podría parecer una farmacéutica, pero es una agencia, así que en principio **no aplica**; confírmalo) y la 5 (remoto Git). Ninguna bloquea la investigación, que no escribe código. La criticidad y la verificación del código se cierran antes de la primera TASK de maquetación.
>
> Abro [`TASK-001`](TASK-001-investigacion-benchmark-agencias.md) con el [plan de investigación](../investigacion/plan-investigacion.md).
