# 🏢 Equipo de proyecto — Pharmaco Assets 2026

> **Jefe del proyecto:** Miguel
> **Fecha:** 2026-09-26
> **Comunicación:** por MDs en [`comms/`](comms/) — ver [protocolo](comms/protocolo.md)

---

## 👥 Miembros

> **Los agentes tienen nombre propio.** **Clia** es el CTO, **Dexia** el Lead/Reviews y **Ania** la DEV. Ése es el identificador que va en `de:`, `para:`, `cc:` y en las entradas del hilo. «Claude Code», «Codex» y «Antigravity» son **las plataformas**, no cómo se llaman.

| Rol | Agente · Plataforma | Comunicación | Responsabilidad |
| --- | --- | --- | --- |
| 👑 Jefe / Director | **Miguel** · humano | Todas + MDs | Visión, decisiones finales, veto sobre cualquier decisión |
| 🧠 CTO | **Clia** · Claude Code | **Solo MDs** (`docs/comms/`) | Dirección técnica, alcance y prioridades, aprobación de RFCs, sign-off 🔴, auditoría docs ↔ realidad. **No ejecuta cambios.** |
| 🧪 Lead Dev / Reviews | **Dexia** · ChatGPT (Codex) | **Solo MDs** (`docs/comms/`) | Guía técnica de ejecución y **review obligatorio** (rol exclusivo) |
| 💻 DEV / Operadora | **Ania** · Antigravity (Google) | **Solo MDs** (`docs/comms/`) + sesión con Miguel | Ejecución: código, assets, despliegues |

> 📜 **Nota de origen.** Este arreglo viene del método multiagente del equipo, adaptado de uno mayor de siete miembros con PM, Arquitecto y DEV secundaria. Aquí sus funciones —crear TASKs, priorizar, aprobar el plan— las absorbe el CTO mientras el equipo sea de tres.

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
               Ania (DEV / Operadora)
                 ejecuta
```

- **Miguel** puede saltarse cualquier nivel y decidir directamente.
- **Clia** especifica y aprueba; **no ejecuta cambios** salvo pedido directo de Miguel.
- **Dexia** no ejecuta nada: revisa. Su ✅ es condición para operar.
- **Ania** no ejecuta una fase 🔴 o 🟡 sin el gate cumplido y comprobado en el disco.

---

## 📡 Canales

| Para | Dónde |
| --- | --- |
| Tareas, propuestas, reviews, decisiones | `docs/comms/` — un MD por conversación |
| Lo pendiente ahora mismo | [`docs/comms/tablero.md`](comms/tablero.md) |
| Estado de cada agente | `docs/status/{agente}-status.md` |
| Reglas de operación (mandan sobre todo) | [`AGENTS.md`](../AGENTS.md) |

**Nada se comunica fuera de un MD commiteado.**

---

## 🔄 Control de versiones

| Versión | Fecha | Autor | Acción |
| --- | --- | --- | --- |
| v1.0 | 2026-09-26 | Clia | Adopción del método multiagente en Pharmaco Assets |
