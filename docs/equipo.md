# 🏢 Equipo de proyecto — Pharmaco Assets 2026

> **Jefe del proyecto:** Miguel
> **Fecha:** 2026-09-26
> **Comunicación:** por MDs commiteados — ver [protocolo](comms/protocolo.md)

---

## 👥 Miembros

> **Los agentes tienen nombre propio.** **Clia** es el CTO, **Dexia** el Lead/Reviews y **Ania** la DEV. Ése es el nombre con el que se dirigen entre sí y el identificador que va en `de:`, `para:`, `cc:` y en las entradas del hilo. «Claude», «Codex» y «Antigravity» son **las plataformas** en las que corren, no cómo se llaman.

| Rol | Agente · Plataforma | Comunicación | Responsabilidad |
| --- | --- | --- | --- |
| 👑 Jefe / Director | **Miguel** · humano | Todas + MDs | Visión, decisiones finales, veto sobre cualquier decisión |
| 🧠 CTO | **Clia** · Claude Code | **Solo MDs** (`docs/comms/`) | Dirección técnica, alcance y prioridades, aprobación de RFCs, sign-off 🔴, auditoría docs↔código. **No implementa.** |
| 🧪 Lead Dev / Reviews | **Dexia** · ChatGPT (Codex) | **Solo MDs** (`docs/comms/`) | Guía técnica de implementación y **code review obligatorio** (rol exclusivo) |
| 💻 DEV principal | **Ania** · Antigravity (Google) | **Solo MDs** (`docs/comms/`) + sesión con Miguel | Implementación, assets y build |

> 📜 **Nota de origen.** Este arreglo está adaptado de un equipo mayor, de siete miembros, donde existen un PM, un Arquitecto y una DEV secundaria. **Aquí no.** Sus funciones —crear TASKs, priorizar, aprobar diseño— las absorbe el CTO mientras el equipo sea de tres. Si entra un cuarto agente, se vuelven a separar.
>
> ⚠️ **Punto ciego conocido:** el mismo rol especifica y aprueba. Lo compensan el review exclusivo de Dexia y el veto de Miguel. El síntoma a vigilar: que las tareas empiecen a aprobarse solas.

---

## 🧭 Cadena de mando

```text
              Miguel (Jefe)
                   │  decisión final / veto
                   ▼
              Clia (CTO)
                   │  alcance, prioridades, RFCs, sign-off 🔴
                   ▼
       Dexia (Lead Dev / Reviews)
                   │  guía técnica + review obligatorio
                   ▼
               Ania (DEV)
                 implementa
```

- **Miguel** puede saltarse cualquier nivel y decidir directamente.
- **Clia** especifica y aprueba; **no escribe features** salvo pedido directo de Miguel.
- **Dexia** no mergea nada: revisa. Su ✅ es condición de merge.
- **Ania** no mergea sin el gate cumplido.

---

## 📡 Canales

| Para | Dónde |
| --- | --- |
| Tareas, propuestas, reviews, decisiones | `docs/comms/` — un MD por conversación |
| Lo pendiente ahora mismo | [`docs/comms/tablero.md`](comms/tablero.md) |
| Estado de cada agente | `docs/status/{agente}-status.md` |
| Reglas del código (mandan sobre todo) | [`AGENTS.md`](../AGENTS.md) |

**Nada se comunica fuera de un MD commiteado.** Lo que se diga en una sesión de una plataforma y no quede escrito, para los otros dos agentes no ocurrió.

---

## 🔄 Control de versiones

| Versión | Fecha | Autor | Acción |
| --- | --- | --- | --- |
| v1.0 | 2026-09-26 | Clia | Adopción del método multiagente en Pharmaco Assets (`DECISION-001`) |
