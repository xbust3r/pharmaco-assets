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

Pharmaco Assets arranca vacío. Miguel pide implantar el mismo método de tres agentes que se usó en CoverageFox.

## Decisión

Se adopta el método tal como quedó en CoverageFox **tras sus correcciones**, no en su versión inicial:

1. **Tres roles y un jefe**: Clia (CTO, especifica y audita), Dexia (review exclusivo), Ania (ejecuta), Miguel (veto).
2. **Los MD son los mensajes y Git es el bus**, desde el primer commit. Repositorio local, sin remoto.
3. **El gate se comprueba en el disco** (lección de `DECISION-002` de CoverageFox): antes de ejecutar un cambio 🔴 o 🟡, Ania consulta con un `grep` que el REVIEW existe y está aprobado.
4. **El alcance de una TASK no se amplía sobre la marcha** (misma lección).
5. **Dexia revisa antes de ejecutar**: el comando literal o el diff, no una descripción.

## Motivo

En CoverageFox el gate se saltó dos veces porque el orden de lanzamiento manual de los agentes no garantizaba que el REVIEW existiera cuando Ania empezaba. Incorporar esas dos correcciones desde el día uno evita repetir la lección.

## Consecuencias

- `AGENTS.md`, `CLAUDE.md`, `docs/equipo.md` y `docs/comms/protocolo.md` quedan como la norma del proyecto.
- La **criticidad es provisional** hasta cerrar `RFC-001`.
- Hasta el ✅ de Miguel, el protocolo figura como PROPUESTO.

## Vigencia

Estratégica: requiere el ✅ explícito de Miguel en el hilo.

## 💬 Hilo

> **[2026-09-26 15:10] clia:** emito la decisión y dejo montada la estructura. Miguel, falta tu ✅ aquí y tus respuestas en `RFC-001` para calibrar la criticidad al proyecto real.
