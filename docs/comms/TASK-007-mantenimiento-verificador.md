---
tipo: TASK
id: TASK-007
titulo: Mantenimiento del verificador — webs lentas y URL no ASCII
de: clia
para: kia
cc: [dexia, miguel]
prioridad: P1
estado: ABIERTA
area: herramientas
criticidad: "🔴"
relacionado: [DECISION-006, DECISION-009, TASK-005, TASK-004]
creado: 2026-10-13
actualizado: 2026-10-13
---

# TASK-007 — Mantenimiento de `scripts/verificar-investigacion.py`

## Contexto

Al cerrar la investigación aparecieron dos defectos del verificador ([`TASK-004`](TASK-004-sistema-de-diseno.md), cierre; [`TASK-001`](TASK-001-investigacion-benchmark-agencias.md), hilo):

1. **Webs lentas dan FALLO.** Una ejecución sobre `main` dio 15 FALLOS de V8, todos por *timeout* de `stratagemma.studio`, que respondía en 6 a 10 s. La siguiente ejecución dio 0. **Un gate que cambia de rojo a verde sin que cambie nada no sirve como gate.**
2. **URL con caracteres no ASCII dan FALLO** con `ordinal not in range(128)`. Por ejemplo, un dominio como `árkos.com` o una ruta con «ñ».

**🔴 porque es un verificador del gate.** Requiere REVIEW de Dexia y sign-off de Clia.

## Pedido

Rama `feat/TASK-007-mantenimiento-verificador`, desde `main`, en el worktree `.claude/worktrees/task-007-verificador`.

1. **V8 y tiempos de espera:**
   - Tiempo máximo por URL de **30 s** con 2 reintentos espaciados.
   - Un *timeout* después de los reintentos sigue siendo **FALLO**, porque DECISION-006 no cambia. Pero el mensaje dice el tiempo medido y el número de intentos.
   - **Tiempo máximo global** para toda la ejecución, configurable con `--timeout-total`, para que nunca se quede colgada.
   - Opcional: comprobar las URL **en paralelo** (`concurrent.futures`, solo biblioteca estándar) para que la ejecución completa tarde menos, con un límite de conexiones por dominio.
2. **URL no ASCII:** el dominio en IDNA (`encodings.idna` o `str.encode('idna')`) y la ruta y la consulta con `urllib.parse.quote`, sin volver a codificar lo que ya venga codificado. Nunca un FALLO por codificación: si la URL está mal formada, el FALLO lo dice.
3. **Pruebas de regresión** en `scripts/pruebas/`:
   - Un servidor HTTP local de prueba (`http.server`, biblioteca estándar) con una ruta que tarda 8 s, que debe dar OK, y otra que no responde nunca, que debe dar FALLO dentro del tiempo máximo.
   - Una URL con dominio IDN y otra con ruta con «ñ».
   - **Las demás comprobaciones (V1 a V8) siguen fallando donde fallaban:** pega la salida contra `scripts/pruebas/` antes y después.
4. **Corre el verificador con red sobre `main` dos veces seguidas** y pega las dos salidas. Deben dar el mismo resultado.

**Fuera de alcance:** cambiar qué es FALLO y qué es AVISO (eso es DECISION-006), tocar fichas o documentos de investigación y tocar la migración.

## Criterios de aceptación

- [ ] *Timeout* por URL de 30 s con reintentos, y tiempo máximo global
- [ ] URL IDN y con «ñ» comprobadas sin error de codificación
- [ ] Regresiones nuevas en `scripts/pruebas/`, más las salidas de antes y después pegadas
- [ ] Dos ejecuciones seguidas sobre `main` con el mismo resultado
- [ ] Solo biblioteca estándar
- [ ] REVIEW de Dexia ✅ + sign-off de Clia (🔴)

## 💬 Hilo

> **[2026-10-13] clia:** creo la task. Va en paralelo con TASK-006 y no comparte archivos con ella. No toques `src/` ni `docs/migracion/`.
