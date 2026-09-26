# Flujo de trabajo multiagente por MDs

> 📦 **Copia de referencia** del paquete original del método. El protocolo vigente de este proyecto está en [`../comms/protocolo.md`](../comms/protocolo.md) y las reglas en [`../../AGENTS.md`](../../AGENTS.md). Las rutas de abajo son las del paquete, no las de este repositorio.

Tres agentes de IA en tres plataformas que no se hablan entre sí, más una
persona que decide. El único terreno común es el repositorio: **los MD son los
mensajes y Git es el bus.**

Este paquete es el **método**, no el proyecto donde nació. Está saneado: no
lleva rutas privadas, ni nombres de otros equipos, ni contenido de cliente.

---

## Por dónde empezar

1. **[`comms/protocolo.md`](comms/protocolo.md)** — el documento. Tipos de
   mensaje, ciclo de estados, matriz de permisos, criticidad y gates de merge.
   Si sólo lees uno, es éste.
2. **[`equipo.md`](equipo.md)** — quién es quién y la cadena de mando.
3. **[`agentes/`](agentes/)** — una ficha por rol: qué puede y, sobre todo,
   **qué no puede** cada uno.
4. **[`fragmento-AGENTS.md`](fragmento-AGENTS.md)** — el trozo que va al
   principio del archivo de instrucciones del repositorio.
   **No lo saltes:** es el puntero que hace que alguien encuentre el protocolo.
   Sin él, todo lo demás es documentación que nadie abre.
5. **[`ejemplos/`](ejemplos/)** — dos casos reales. Es lo que enseña cómo se
   *comporta* el flujo, que no se deduce leyendo la tabla de permisos.

## Qué hay dentro

```
LEEME.md                 ← esto
equipo.md                ← roles y cadena de mando
fragmento-AGENTS.md      ← el puntero, para el AGENTS.md/CLAUDE.md de tu repo
comms/
  protocolo.md           ← el protocolo
  tablero.md             ← el índice vivo, vacío y listo
  plantillas/            ← TASK · RFC · REVIEW · DECISION
agentes/                 ← clia (CTO) · dexia (reviews) · ania (dev)
status/                  ← plantilla de estado por agente
ejemplos/
  DECISION-002-…         ← cómo se revierte una decisión con el coste escrito
  REVIEW-001-…           ← el ciclo completo: rechazo → corrección → firma
```

## Qué tienes que adaptar

- **Los nombres.** Clia, Dexia y Ania son de este equipo. El nombre es la
  identidad y la plataforma es la plataforma: no los mezcles.
- **La criticidad 🔴/🟡/🟢.** La del protocolo está calibrada para un front-end
  estático. Recalíbrala con una pregunta: *¿cuánto se propaga un error y cuánto
  cuesta deshacerlo?* Lo 🔴 no es lo difícil, es lo que falla en silencio.
- **Los comandos del gate.** Donde el protocolo dice `pnpm lint`, `pnpm build`
  y demás, pon la verificación real de tu proyecto. **El gate sin comandos
  reales es decorativo.**

## Las tres ideas que lo sostienen

1. **Si no está en un MD commiteado, no se comunicó.** Lo dicho en la sesión de
   una plataforma, para los otros dos agentes no ocurrió.
2. **Un rol emite reviews, y sólo uno.** El que dirige audita; no revisa. Si el
   mismo que especifica también aprueba el código, el gate es un adorno.
3. **La evidencia se pega, no se resume.** «Pasó todo» no es evidencia. La
   salida real, en el hilo.

## Lo que no funcionó, que también conviene saber

Un método sin sus grietas se adopta mal, porque quien lo copia no sabe dónde
mirar. En el proyecto donde se estrenó, esto es lo que falló:

- **El que dirige absorbió las funciones de PM y Arquitecto**, así que el mismo
  rol especificaba y aprobaba. Se compensó con el review exclusivo y con el
  veto de la persona a cargo, pero es un punto ciego real. El síntoma a vigilar:
  que las tareas empiecen a aprobarse solas.
- **El gate se saltó dos veces.** Una, un merge directo a la rama principal sin
  review. Otra, un cambio crítico escondido dentro de un commit cuyo mensaje
  hablaba de otra cosa — y ése no lo vio nadie hasta la auditoría. De ahí salió
  una regla: **si un commit toca lo crítico, que lo diga su primera línea.**
- **Las ramas se apilaron 29 commits** porque el paso de mergear no tenía dueño
  con prisa. Cada día apilado encarece deshacer cualquier cosa.
- **Una firma vale para un estado concreto del código.** Cuando una decisión
  posterior cambió el marcado, hubo que retirar el sign-off y volver a firmar.
  Si la firma sobrevive al cambio, no significa nada.
