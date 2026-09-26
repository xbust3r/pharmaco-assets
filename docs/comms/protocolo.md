# 📡 Protocolo de comunicación multi-agente por MDs — Pharmaco Assets

> **Fecha:** 2026-09-26
> **Autor:** Clia (CTO)
> **Origen:** método multiagente del equipo, con las lecciones de CoverageFox (gate comprobado en disco, alcance cerrado).
> **Status:** 🟡 **PROPUESTO** — pendiente del ✅ de Miguel en `DECISION-001`

---

## 🎯 Problema que resuelve

El equipo vive en **tres plataformas que no se hablan entre sí**:

| Agente | Nombre | Plataforma |
| --- | --- | --- |
| CTO | **Clia** | Claude Code |
| Lead Dev / Reviews | **Dexia** | ChatGPT (Codex) |
| DEV / Operadora | **Ania** | Antigravity (Google) |
| Jefe | **Miguel** | Todas |

El único terreno común es **el repositorio**. Por tanto: **los archivos MD son los mensajes y Git es el bus.**

---

## 📜 Los 6 principios

1. **Si no está en un MD, no se comunicó.** Nadie asume que otro agente vio su plataforma.
2. **Un archivo = una conversación, con un solo dueño.** Sólo el dueño edita el cuerpo; los demás **agregan** al hilo.
3. **Todo mensaje tiene tipo, destinatario y estado** (frontmatter obligatorio).
4. **Los roles se respetan por la matriz de permisos.**
5. **Miguel es la autoridad final**: puede crear, aprobar, rechazar o vetar cualquier cosa, en cualquier estado.
6. **El tablero es la fuente de verdad de lo pendiente**: todo mensaje abierto está en [`tablero.md`](tablero.md).

> ⚖️ Este protocolo **no manda sobre [`AGENTS.md`](../../AGENTS.md)**. Aquél es la ley de la operación; éste sólo dice cómo se hablan los agentes. Ante conflicto, manda `AGENTS.md`.

---

## 📬 Tipos de mensaje

| Tipo | Qué es | Quién lo crea | Quién lo cierra |
| --- | --- | --- | --- |
| **TASK** | Trabajo asignado a un agente | Clia o Miguel | Clia, cuando la evidencia + review están ✅ |
| **RFC** | Propuesta técnica que pide opinión | Cualquiera | Clia, con veto de Miguel |
| **REVIEW** | Revisión de un cambio por ejecutar o ejecutado | Dexia (**nadie más emite reviews**) | Dexia (veredicto) + sign-off de Clia si es 🔴 |
| **DECISION** | Decisión vinculante para el proyecto | Clia o Miguel | Miguel, o Clia con silencio > 48h en decisiones no estratégicas |
| **BLOCKER** | Algo que impide avanzar y no lo resuelve quien lo encuentra | Cualquiera | Quien lo desbloquea |
| **STATUS** | Estado por agente, en `docs/status/` | Cada agente el suyo | Nunca se cierra; se actualiza |

**Nomenclatura:** `TIPO-###-slug-corto.md`, correlativo global por tipo. Plantillas en [`plantillas/`](plantillas/).

---

## 📄 Anatomía de un mensaje

```markdown
---
tipo: TASK
id: TASK-001
titulo: Inventario de assets
de: clia
para: ania
cc: [dexia]
prioridad: P1            # P0 | P1 | P2
estado: ABIERTA
area: assets             # assets | codigo | despliegue | contenido | docs
criticidad: "🟢"         # 🔴 | 🟡 | 🟢 — ver AGENTS.md
relacionado: []
creado: 2026-09-26
actualizado: 2026-09-26
---
```

Reglas del hilo:

- Formato: `> **[AAAA-MM-DD HH:MM] agente:** texto` — **append-only**, siempre al final.
- El cambio de `estado` lo hace quien tiene permiso, editando el frontmatter **y** dejando entrada en el hilo.

---

## 🔄 Ciclo de estados

```text
ABIERTA ──▶ EN_PROGRESO ──▶ EN_REVISION ──▶ CERRADA ✅
   │             │               │
   │             ▼               ▼
   │         BLOQUEADA ⏸️     RECHAZADA ❌
   │        (→ BLOCKER-XXX)  (con motivo en el hilo)
   └──▶ RECHAZADA ❌ (no procede)
```

Al cerrar: mover la fila del [`tablero.md`](tablero.md) a «Cerrados». **El MD nunca se borra**: es el historial.

---

## 🔐 Matriz de permisos

| Acción | Miguel | Clia (CTO) | Dexia (Lead / Reviews) | Ania (DEV) |
| --- | :---: | :---: | :---: | :---: |
| Crear TASK | ✅ | ✅ | ❌ (la pide en el hilo) | ❌ (la pide en el hilo) |
| Asignar prioridades | ✅ | ✅ | proponer | proponer |
| Crear RFC | ✅ | ✅ | ✅ | ✅ |
| Aprobar RFC | veto | ✅ | ❌ | ❌ |
| Emitir REVIEW | — | ❌ (audita, no revisa) | ✅ **exclusivo** | ❌ |
| Sign-off de cambios 🔴 | veto | ✅ **obligatorio** | prerequisito | ❌ |
| Emitir DECISION | ✅ | ✅ | ❌ | ❌ |
| Cerrar DECISION | ✅ | ✅ (no estratégicas) | ❌ | ❌ |
| **Ejecutar cambios** (código, assets, despliegue) | ✅ | ❌ **(ver nota)** | ❌ | ✅ **dueña** |
| Operaciones destructivas / publicación | ✅ | ❌ | ❌ | ✅ sólo con gate 🔴 cumplido |
| Editar `tablero.md` | ✅ | ✅ | ✅ (sus filas) | ✅ (sus filas) |

> 🧠 **El CTO no ejecuta cambios.** Especifica, audita y aprueba. Ejecuta **comprobaciones de solo lectura** para verificar antes de firmar, pero no borra, no modifica y no publica. Si Miguel se lo pide directamente, entonces sí, y queda dicho en el hilo.

---

## 🚦 Gates de ejecución

| Criticidad | Requisito para ejecutar |
| --- | --- |
| 🔴 | REVIEW de Dexia ✅ **+ sign-off de Clia** + respaldo verificado + conteo previo anotado |
| 🟡 | REVIEW de Dexia ✅ + estado previo anotado |
| 🟢 | Libre |

**El gate se comprueba en el disco** (ver `AGENTS.md`): los agentes se lanzan a mano y nada garantiza el orden, así que Ania consulta el archivo del REVIEW antes de ejecutar en lugar de suponer que ya existe.

**Dexia revisa lo que está a punto de ejecutarse**, no sólo el resultado: los comandos literales o el diff, pegados en el hilo **antes** de correrlos. En un cambio irreversible, un ❌ posterior llega tarde.

**La evidencia se pega, no se resume.**

---

## 🔁 Flujo típico

```text
1. Clia crea TASK-XXX — alcance, criterios, criticidad            [ABIERTA]
2. Si hay algo que decidir: RFC → Clia aprueba (Miguel veta)
3. Ania la toma                                                    [EN_PROGRESO]
4. Ania pega en el hilo el plan literal (comandos / diff)
   y pide review → Dexia emite REVIEW-YYY                          [EN_REVISION]
   └─ ✅ / ⚠️ / ❌ con hallazgos; Ania corrige e itera
5. Si es 🔴 → Clia firma el sign-off dentro de REVIEW-YYY
6. Ania comprueba el gate en el disco, ejecuta y pega la salida
7. Clia verifica de forma independiente y cierra                   [CERRADA ✅]
8. Cada agente actualiza su status y sus filas del tablero
```

**Dexia no ejecuta nada.** Cuando necesite evidencia, la pide en el hilo y la corre Ania —o Clia, si es de solo lectura.

---

## ⚖️ Desacuerdos

1. Se debate **en el hilo del MD**, máximo dos rondas por agente.
2. Sin consenso → se etiqueta a Clia (`cc: clia`) → Clia emite `DECISION-XXX`.
3. Miguel puede vetar o revertir cualquier DECISION.

---

## 🕐 Rutina de sesión (todos)

1. `git log --oneline -5` — qué ha pasado desde tu última sesión
2. Leer [`tablero.md`](tablero.md) → filtrar los mensajes donde figures en `para:` o `cc:`
3. Responder hilos / avanzar tus TASKs
4. Actualizar tu `status/{agente}-status.md` si algo cambió
5. Actualizar tus filas del tablero
6. Commit: `comms(ID): agente resumen corto`

---

## 📂 Estructura

```text
.gitignore                     ← excluye claves, .env y respaldos
AGENTS.md                      ← reglas de operación (mandan)
CLAUDE.md                      ← arranque de Clia en Claude Code
README.md
docs/
├── equipo.md
├── agentes/{clia,dexia,ania}.md
├── status/{clia,dexia,ania}-status.md
└── comms/
    ├── protocolo.md           ← este documento
    ├── tablero.md             ← índice vivo
    ├── plantillas/{TASK,RFC,REVIEW,DECISION,BLOCKER}.md
    └── TIPO-###-slug.md
```

---

## 🔄 Control de versiones

| Versión | Fecha | Autor | Acción |
| --- | --- | --- | --- |
| v1.0 | 2026-09-26 | Clia | Adopción del método en Pharmaco Assets. Incorpora desde el inicio el gate comprobado en disco y el alcance cerrado (lecciones de CoverageFox) |
