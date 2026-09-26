---
tipo: DECISION
id: DECISION-001
titulo: Adopción del flujo multiagente Clia · Dexia · Ania
de: clia
para: [miguel]
cc: [dexia, ania]
estado: PROPUESTA
estrategica: true
relacionado: [AGENTS.md, protocolo.md, equipo.md]
creado: 2026-09-26
actualizado: 2026-09-26
---

# DECISION-001 — Adopción del flujo multiagente Clia · Dexia · Ania

## Contexto

Pharmaco Assets arranca vacío. Miguel pide implantar el método multiagente del equipo (paquete `flujo-multiagente`, copia en `docs/metodo/`).

## Decisión

Se adopta el método tal como viene en el paquete, con tres puntos a confirmar por Miguel, los mismos que se aprobaron donde se estrenó:

1. **El CTO absorbe las funciones de PM y Arquitecto** —crear TASKs, priorizar y aprobar RFCs— mientras el equipo sea de tres.
2. **El gate 🔴 con doble aprobación**: REVIEW de Dexia + sign-off de Clia.
3. **Cierre de DECISION por silencio de 48h** en decisiones no estratégicas; las estratégicas necesitan el ✅ explícito de Miguel.

Además se incorporan como reglas de Git en `AGENTS.md` las lecciones que el paquete documenta como fallos:

- Si un commit toca lo crítico, lo dice su primera línea.
- Las ramas no se apilan.
- Una firma vale para un estado concreto del código.

## Motivo

Es el método del equipo; lo único que se adapta es lo que el propio paquete manda adaptar: los nombres (se mantienen), la criticidad y los comandos del gate.

## Consecuencias

- `AGENTS.md`, `docs/equipo.md` y `docs/comms/protocolo.md` quedan como norma.
- **La criticidad y la verificación son provisionales** hasta cerrar `RFC-001`. Sin comandos reales el gate es decorativo, así que no se abren TASKs 🔴 ni 🟡 antes.
- Con el ✅ de Miguel, el protocolo pasa a ACTIVO.

## Vigencia

Estratégica: requiere el ✅ explícito de Miguel en el hilo.

## 💬 Hilo

> **[2026-09-26 15:40] clia:** emito la decisión. Miguel, faltan tu ✅ a los tres puntos y tus respuestas en `RFC-001`.
>
> **[2026-09-26 16:15] miguel:** «ok», y asigna los roles: Ania investiga, Dexia valida, Clia es la CTO.
>
> **[2026-09-26 16:20] clia:** tomo el reparto como confirmado en la práctica. La decisión es estratégica y necesita tu ✅ explícito a los tres puntos, así que la dejo en PROPUESTA hasta que lo escribas aquí. No bloquea TASK-001.
