---
tipo: TASK
id: TASK-XXX
titulo:
de: clia
para:
cc: []
prioridad: P1        # P0 | P1 | P2
estado: ABIERTA      # ABIERTA | EN_PROGRESO | EN_REVISION | BLOQUEADA | CERRADA | RECHAZADA
area:                # assets | codigo | despliegue | contenido | docs
criticidad: "🟡"     # 🔴 | 🟡 | 🟢 — ver AGENTS.md
relacionado: []
creado: YYYY-MM-DD
actualizado: YYYY-MM-DD
---

# TASK-XXX — (título)

## Contexto
(por qué existe esta tarea)

## Pedido
(qué se espera exactamente)

## Fuera de alcance
(lo que NO se toca; si hace falta, se para y se pide en el hilo)

## Criterios de aceptación
- [ ] (criterio verificable con un número, no con una valoración)
- [ ] Estado previo / conteo anotado en el hilo, antes de operar
- [ ] Plan literal (comandos o diff) pegado en el hilo antes de ejecutar
- [ ] Salida real de cada comando pegada en el hilo
- [ ] REVIEW de Dexia ✅ (+ sign-off de Clia si 🔴), comprobado en el disco

## 🚦 Gate 🔴 — requisitos previos (borrar si no es 🔴)
- [ ] Respaldo verificado y restaurable
- [ ] TASKs de las que depende, cerradas
- [ ] Dexia ha revisado **los comandos literales / el diff**, antes de ejecutar
- [ ] Clia ha firmado en el REVIEW

## 💬 Hilo
> **[YYYY-MM-DD HH:MM] agente:** mensaje
