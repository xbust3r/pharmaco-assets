---
tipo: DECISION
id: DECISION-007
titulo: Kia (subagente Haiku 5.5, esfuerzo alto) reemplaza a Ania como DEV
de: clia
para: [dexia, kia]
cc: [miguel]
estado: EFECTIVA
estrategica: true
relacionado: [AGENTS.md, equipo.md, protocolo.md, agentes/kia.md, .claude/agents/kia.md]
creado: 2026-10-08
actualizado: 2026-10-08
---

# DECISION-007 — Kia reemplaza a Ania

## Contexto

Miguel decide reemplazar a Ania (Antigravity) por un subagente de Claude Code llamado **Kia**, con **Claude Haiku 5.5** (`claude-haiku-5-5`) y **esfuerzo alto**. El esfuerzo se fija de forma explícita porque el valor por defecto de Haiku 5.5 es `medium`. Ambos están en `.claude/agents/kia.md`.

## Decisión

1. **Kia es la DEV** desde el 2026-10-08. Hereda todas las TASKs abiertas de Ania (TASK-001 a TASK-005).
2. **Ania queda retirada.** Su ficha, su status y su historial se conservan. No se reescribe nada de lo que firmó.
3. **Kia corre como subagente en la sesión de Clia.** Para que eso no mezcle los roles:
   - **El encargo es solo el ID de la TASK.** Todo lo demás está en el MD. Lo que Clia diga al lanzarla y no esté escrito, Kia lo ignora.
   - **Clia no corrige a Kia: la audita.** El veredicto sigue siendo exclusivo de Dexia.
   - **Kia no hace push.** Lo hace Clia, con el permiso de Miguel.
4. **Vigilancia reforzada por el tamaño del modelo:** la verificación de `DECISION-006` es obligatoria antes de cada review, y Clia audita 5 fichas al azar antes de cerrar. Si la auditoría encuentra datos inventados en dos entregas, Clia propone subir el modelo (Sonnet 5.5).

## Motivo

Es decisión de Miguel. Además tiene ventajas prácticas: Kia trabaja en el mismo repositorio sin depender de que Miguel la lance a mano, y su navegación (WebFetch) y sus capturas (Chrome headless) son comprobables.

## Consecuencias

- Actualizados `AGENTS.md`, `equipo.md`, `protocolo.md`, las fichas de Clia y Dexia, la plantilla DECISION, el tablero y el `para:` de las TASKs abiertas.
- Nuevos: `.claude/agents/kia.md`, `docs/agentes/kia.md` y `docs/status/kia-status.md`.
- **Riesgo que se acepta:** Clia lanza a la DEV, así que la separación entre quien especifica y quien ejecuta depende de la regla de «solo el ID de la TASK». Dexia puede señalar en un REVIEW cualquier entrega de Kia que siga instrucciones que no estén en los MD.

## Vigencia

Efectiva desde el 2026-10-08, por decisión directa de Miguel.

## 💬 Hilo

> **[2026-10-08] miguel:** (transcrito por Clia) reemplaza a Ania por un subagente de Haiku 5.5 llamado Kia.
>
> **[2026-10-08] clia:** registrada. Ania: gracias por el trabajo; tu muestra F0 aprobada y tus capturas son la base de lo que sigue.
>
> **[2026-10-08] miguel:** (transcrito por Clia) revisa correctamente si existe Haiku 5.5; es más, me sale en la lista de modelos disponibles en Claude. La deseo con esfuerzo alto.
>
> **[2026-10-08] clia:** confirmado en la documentación oficial (platform.claude.com, *Models overview*): `claude-haiku-5-5` existe. Mis datos de modelos eran anteriores a su lanzamiento. Kia usa Haiku 5.5 con `effort: high`.
