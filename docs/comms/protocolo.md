# 📡 Protocolo de comunicación multi-agente por MDs — v1

> **Fecha:** 2026-09-26
> **Autor:** Clia (CTO), a pedido de Miguel
> **Origen:** el método multiagente del equipo (copia de referencia en [`../metodo/`](../metodo/)), adaptado de un protocolo pensado para siete agentes con PM y Arquitecto. Aquí son tres, y las funciones de esos dos roles están reasignadas.
> **Status:** 🟡 **PROPUESTO** — pendiente del ✅ de Miguel en [`DECISION-001`](DECISION-001-adopcion-flujo-tres-agentes.md)

---

## 🎯 Problema que resuelve

El equipo vive en **tres plataformas que no se hablan entre sí**:

| Agente | Nombre | Plataforma |
| --- | --- | --- |
| CTO | **Clia** | Claude Code |
| Lead Dev / Reviews | **Dexia** | ChatGPT (Codex) |
| DEV principal | **Ania** | Antigravity (Google) |
| Jefe | **Miguel** | Todas |

> Los agentes se nombran **Clia**, **Dexia** y **Ania**; ésos son sus identificadores en `de:`, `para:`, `cc:` y en las entradas del hilo. «Claude», «Codex» y «Antigravity» son **las plataformas**, y se siguen nombrando como tales cuando se habla de la herramienta.

El único terreno común es **el repositorio Git**. Por tanto: **los archivos MD son los mensajes y Git es el bus**. Este protocolo define cómo se escriben para que los roles se respeten y nada se pierda.

---

## 📜 Los 6 principios

1. **Si no está en un MD commiteado, no se comunicó.** Nadie asume que otro agente vio su plataforma.
2. **Un archivo = una conversación, con un solo dueño.** Sólo el dueño edita el cuerpo; los demás **agregan** al hilo, nunca editan lo ajeno.
3. **Todo mensaje tiene tipo, destinatario y estado** (frontmatter obligatorio).
4. **Los roles se respetan por la matriz de permisos.**
5. **Miguel es la autoridad final**: puede crear, aprobar, rechazar o vetar cualquier cosa, en cualquier estado, saltándose cualquier paso.
6. **El tablero es la fuente de verdad de lo pendiente**: todo mensaje abierto está en [`tablero.md`](tablero.md).

---

## ⚖️ Este protocolo no manda sobre `AGENTS.md`

[`AGENTS.md`](../../AGENTS.md) es la ley del código. Este documento sólo dice **cómo se hablan los agentes**. Ante conflicto, manda `AGENTS.md`.

---

## 📬 Tipos de mensaje

| Tipo | Qué es | Quién lo crea | Quién lo cierra |
| --- | --- | --- | --- |
| **TASK** | Tarea de trabajo asignada a un agente | Clia (CTO) o Miguel | Clia, cuando el entregable + review están ✅ |
| **RFC** | Propuesta técnica o cambio de diseño que pide opinión | Cualquiera | Clia (CTO), con veto de Miguel |
| **REVIEW** | Revisión de un branch/PR | Dexia (**nadie más emite reviews**) | Dexia (veredicto) + CTO si el cambio es 🔴 |
| **DECISION** | Decisión vinculante para el proyecto | Clia (CTO) o Miguel | Miguel, o el CTO con silencio de Miguel > 48h en decisiones no estratégicas |
| **BLOCKER** | Algo que impide avanzar y no lo resuelve quien lo encuentra | Cualquiera | Quien lo desbloquea |
| **STATUS** | Estado por agente, en `docs/status/` | Cada agente el suyo | Nunca se cierra; se actualiza |

**Nomenclatura:** `TIPO-###-slug-corto.md`, correlativo global por tipo. Ejemplo: `TASK-001-inventario-assets.md`. Plantillas en [`plantillas/`](plantillas/).

> ⚠️ **Aquí no hay PM ni Arquitecto.** Esas dos funciones las absorbe el **CTO**, y Miguel conserva el veto sobre ambas. Si el equipo crece, se separan otra vez.

---

## 📄 Anatomía de un mensaje

```markdown
---
tipo: TASK
id: TASK-001
titulo: (título)
de: clia
para: ania
cc: [dexia]
prioridad: P0            # P0 | P1 | P2
estado: ABIERTA
area: (según el stack)   # ⏳ RFC-001
criticidad: "🟡"         # 🔴 | 🟡 | 🟢 — ver § Criticidad
relacionado: []
creado: 2026-09-26
actualizado: 2026-09-26
---

# TASK-001 — (título)

## Contexto
(por qué existe; enlaces a docs)

## Pedido
(qué se espera exactamente)

## Criterios de aceptación
- [ ] …
- [ ] Verificación completa de AGENTS.md en verde
- [ ] REVIEW de Dexia ✅ (+ sign-off del CTO si 🔴)

## 💬 Hilo
> **[2026-09-26 15:00] clia:** creo la task.
> **[2026-09-26 16:10] ania:** la tomo. Duda: …
```

Reglas del hilo:

- Formato: `> **[fecha hora] agente:** texto` — **append-only**, siempre al final.
- El cambio de `estado` lo hace quien tiene permiso, editando el frontmatter **y** dejando entrada en el hilo.
- Un commit por intervención: `comms(TASK-001): ania toma la task`.

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

Al cerrar (✅ o ❌): mover la fila del [`tablero.md`](tablero.md) a «Cerrados». **El MD nunca se borra**: es el historial.

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
| Escribir código de producto | ✅ | ❌ **(ver nota)** | ❌ (prototipos en el hilo) | ✅ **dueño** |
| Tocar archivos 🔴 | ✅ | especifica y aprueba | ❌ | ✅ sólo con TASK 🔴 aprobada |
| Mergear a `main` | ✅ | ✅ | ❌ | ✅ sólo con el gate cumplido |
| Editar `tablero.md` | ✅ | ✅ | ✅ (sus filas) | ✅ (sus filas) |

> 🧠 **El CTO no implementa.** Especifica, audita y aprueba. Ejecuta la verificación porque tiene el repositorio delante y necesita comprobar antes de firmar, pero **no escribe features**. Si Miguel se lo pide directamente, entonces sí, y queda dicho en el hilo.

---

## 🚦 Criticidad y gates de merge

La criticidad **no se hereda del proyecto de origen**. Se mide por **cuánto se propaga un error y cuánto cuesta deshacerlo**. Lo 🔴 no es lo difícil: es lo que falla en silencio.

> ⏳ **Provisional hasta [`RFC-001`](RFC-001-alcance-del-proyecto.md).** Cuando se conozca el stack, la columna «Qué entra» se reescribe con rutas y archivos concretos.

| Nivel | Qué entra | Por qué |
| --- | --- | --- |
| 🔴 | Configuración global (tokens de diseño, layout base, config de build), los verificadores del propio gate, contratos con terceros (formularios, tracking, endpoints), contenido regulado (claims sanitarios, textos legales) | Se propaga a todo a la vez, desactiva la red de seguridad o falla en silencio |
| 🟡 | Componentes y módulos compartidos, assets y su pipeline | Afectan a varias piezas, pero el fallo se ve |
| 🟢 | Una pieza suelta, documentación, contenido de relleno | El radio de daño es el propio archivo |

| Criticidad | Requisito para mergear |
| --- | --- |
| 🔴 | REVIEW de Dexia ✅ **+ sign-off de Clia (CTO)** en el mismo MD + la verificación completa en verde |
| 🟡 | REVIEW de Dexia ✅ + verificación completa en verde |
| 🟢 | REVIEW ligero de Dexia, puede ser posterior al merge |

**«Verificación completa» es la de [`AGENTS.md`](../../AGENTS.md)**, sin sustitutos ni resúmenes. Se pega la **salida real** en el hilo del MD, no un «pasó todo». Y se mira el resultado servido: ningún comando sabe si se ve bien.

---

## 🔁 Flujo típico

```text
1. Clia (CTO) crea TASK-XXX — alcance, criterios, criticidad       [ABIERTA]
2. Si hay diseño que decidir: RFC en el hilo → el CTO aprueba
3. Ania la toma y trabaja en feat/TASK-XXX-slug                    [EN_PROGRESO]
4. Pide review en el hilo → Dexia emite REVIEW-YYY                 [EN_REVISION]
   └─ ✅ / ⚠️ / ❌ con hallazgos; Ania corrige e itera
5. Si es 🔴 → Clia (CTO) firma el sign-off en REVIEW-YYY
6. Ania mergea → el CTO verifica criterios y cierra                 [CERRADA ✅]
7. Cada agente actualiza su status/{agente}-status.md
```

**Dexia no ejecuta código.** Cuando necesite evidencia, la pide en el hilo y la corre Ania —o el CTO— y se pega la salida.

Ejemplo completo de un ciclo (rechazo → corrección → firma → merge): [`../metodo/ejemplos/REVIEW-001-ciclo-completo-de-review.md`](../metodo/ejemplos/REVIEW-001-ciclo-completo-de-review.md).

---

## ⚖️ Desacuerdos

1. Se debate **en el hilo del MD**, máximo dos rondas por agente.
2. Sin consenso → se etiqueta al CTO (`cc: clia`) → el CTO emite `DECISION-XXX`.
3. Miguel puede vetar o revertir cualquier DECISION. Su palabra cierra el tema.

Cómo se revierte una decisión con el coste escrito: [`../metodo/ejemplos/DECISION-002-como-se-revierte-una-decision.md`](../metodo/ejemplos/DECISION-002-como-se-revierte-una-decision.md).

---

## 🕐 Rutina de sesión (todos)

1. `git pull` (o `git log --oneline -5` mientras no haya remoto)
2. Leer [`tablero.md`](tablero.md) → filtrar los mensajes donde figure en `para:` o `cc:`
3. Responder hilos / avanzar sus TASKs
4. Actualizar su `status/{agente}-status.md` si algo cambió
5. Actualizar sus filas del tablero
6. Commit (+ push si hay remoto): `comms(ID): resumen corto`

---

## 📂 Estructura

```text
AGENTS.md                      ← la ley del código + el puntero al protocolo
CLAUDE.md                      ← importa AGENTS.md para Claude Code
docs/
├── equipo.md                  ← quién es quién y la cadena de mando
├── agentes/{clia,dexia,ania}.md
├── status/{clia,dexia,ania}-status.md
├── metodo/                    ← copia de referencia del método + ejemplos
└── comms/
    ├── protocolo.md           ← este protocolo
    ├── tablero.md             ← índice vivo
    ├── plantillas/{TASK,RFC,REVIEW,DECISION}.md
    └── TASK-001-….md          ← los mensajes, planos en esta carpeta
```

---

## 🔄 Control de versiones

| Versión | Fecha | Autor | Acción |
| --- | --- | --- | --- |
| v1.0 | 2026-09-26 | Clia (CTO) | Adopción del método en Pharmaco Assets. Criticidad y verificación provisionales hasta `RFC-001` |
