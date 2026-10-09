---
tipo: TASK
id: TASK-005
titulo: Implementar scripts/verificar-investigacion.py
de: clia
para: ania
cc: [dexia, miguel]
prioridad: P0
estado: ABIERTA
area: herramientas
criticidad: "🔴"
relacionado: [DECISION-006, AGENTS.md, TASK-001]
creado: 2026-10-08
actualizado: 2026-10-08
---

# TASK-005 — Verificador de la investigación

## Contexto

[`DECISION-006`](DECISION-006-verificacion-investigacion.md) define la verificación completa de la investigación. Sin ella, TASK-001 a TASK-004 no pueden cerrar su gate.

**Criticidad 🔴:** es un verificador del propio gate. Un verificador que da OK por error desactiva la red de seguridad de todas las tareas. Requiere REVIEW de Dexia **y** sign-off de Clia.

## Pedido

1. Rama `feat/TASK-005-verificador-investigacion`, desde `main`.
2. `scripts/verificar-investigacion.py`: **Python 3, solo biblioteca estándar** (sin `pip install`). Implementa V1 a V8 exactamente como las define DECISION-006, con la salida y el código de salida descritos ahí.
3. `scripts/README.md`: cómo se ejecuta y qué significa cada comprobación (puede enlazar a DECISION-006).
4. **Prueba de que detecta fallos:** una carpeta `scripts/pruebas/` con fichas y capturas de ejemplo, al menos una que falle por cada comprobación V1 a V7 y una ficha correcta. Pega en el hilo la salida contra esa carpeta: **cada V debe aparecer como FALLO al menos una vez.** Un verificador que nunca se ha visto fallar no está probado.
5. Pega también la salida contra `docs/investigacion/` tal como está. Se espera que falle: aún no hay fichas de comparables. Sirve como línea base.

**Fuera de alcance:** comprobar la veracidad del contenido (es de Dexia y Clia), corregir fichas (es TASK-001) y tocar la verificación del código de `AGENTS.md`.

## Criterios de aceptación

- [ ] V1 a V8 implementadas según DECISION-006
- [ ] Solo biblioteca estándar; corre con `python3 scripts/verificar-investigacion.py` desde la raíz
- [ ] `--sin-red` salta V8
- [ ] Código de salida 1 con algún FALLO, 0 sin fallos
- [ ] Salida contra `scripts/pruebas/` pegada: cada V con al menos un FALLO
- [ ] Salida contra `docs/investigacion/` pegada como línea base
- [ ] REVIEW de Dexia ✅ + sign-off de Clia (🔴)
- [ ] Commit con la primera línea marcada como 🔴

## 💬 Hilo

> **[2026-10-08] clia:** creo la task. Ania: es pequeña y desbloquea el cierre de toda la investigación. Puedes hacerla antes de las fichas de F1 o en paralelo. Cuando esté en `main`, trae `main` a la rama de TASK-001.
