---
tipo: DECISION
id: DECISION-008
titulo: Clia invoca a Dexia por `codex exec` desde Claude Code
de: clia
para: [dexia, kia]
cc: [miguel]
estado: PROPUESTA
estrategica: true
relacionado: [AGENTS.md, protocolo.md, agentes/dexia.md, agentes/clia.md, DECISION-007]
creado: 2026-10-10
actualizado: 2026-10-10
---

# DECISION-008 — Clia invoca a Dexia por `codex exec`

## Contexto

Hasta ahora Dexia sólo trabajaba cuando Miguel la abría a mano en ChatGPT/Codex. Cada REVIEW dependía de ese paso, y Dexia no tenía el repositorio en ejecución.

Miguel pidió que Clia pueda invocar a Dexia desde Claude Code. El 2026-10-10 se instaló Codex CLI (`codex-cli 0.162.1`, en `~/.npm-global/bin/codex`) y Miguel inició sesión con su cuenta de ChatGPT. Esa versión **ya no trae `codex mcp-server`**, así que no hay MCP. El canal es `codex exec`, que lanza a Codex sin modo interactivo.

Prueba hecha, en sólo lectura y desde la raíz del repo: Codex leyó `AGENTS.md` y respondió «Soy **Dexia**, el agente Codex de lead técnico y reviews; mi ficha es docs/agentes/dexia.md». Gastó unos 19 000 tokens de la cuenta de Miguel.

Miguel eligió este camino («A») frente a encargar a Kia un servidor MCP propio.

## Decisión

Clia puede lanzar a Dexia con `codex exec`. El veredicto sigue siendo exclusivo de Dexia, y se aplican estas reglas:

1. **Encargo fijo y mínimo.** La única instrucción es esta, con el ID cambiado:

   ```bash
   /Users/miguel/.npm-global/bin/codex exec -s workspace-write -c sandbox_workspace_write.network_access=true "Eres Dexia. Lee tu ficha y atiende REVIEW-XXX según el protocolo."
   ```

   No van resúmenes, ni opiniones de Clia, ni pistas sobre qué mirar. Todo lo demás está en los MD. Si Dexia recibe algo más, lo ignora y lo dice en el hilo.
2. **El encargo queda escrito.** Antes de lanzarla, Clia deja en el hilo del MD una entrada con la fecha y el texto exacto que le pasa a Dexia. Así cualquiera puede auditar que no hubo nada más.
3. **El review es el MD, no la respuesta.** Lo que Dexia le conteste a Clia por consola no cuenta: vale sólo lo que deje escrito en `REVIEW-XXX`, en su status y en sus filas del tablero. Clia no copia, no resume y no reinterpreta la respuesta en lugar de Dexia.
4. **Permisos de Dexia en esta vía:**
   - Escribe sólo en los archivos que su rol le permite: sus REVIEW, su status, sus filas del tablero y entradas en los hilos.
   - Puede correr comandos para comprobar cosas, incluida la verificación de `DECISION-006`. Tiene red para contrastar fuentes. La salida que pegue vale como evidencia.
   - Sigue sin escribir código de producto, sin mergear y sin hacer push.
5. **Commits.** Dexia commitea su propia intervención: `comms(REVIEW-XXX): dexia …`. Si el sandbox no le deja escribir en `.git`, Clia commitea sus archivos sin tocarlos, en un commit separado: `comms(REVIEW-XXX): dexia … (commit por clia)`.
6. **Clia no decide si hay review.** Cada vez que Kia pide review en un hilo, Clia lanza a Dexia en esa sesión. No elige cuándo ni filtra qué entra.
7. **El canal manual sigue abierto.** Miguel puede abrir a Dexia en ChatGPT/Codex cuando quiera. Ambas vías valen igual.

## Motivo

- Quita a Miguel del camino crítico de cada review sin cambiar quién da el veredicto.
- `codex exec` es lo que existe hoy. Construir un servidor MCP propio sería código nuevo, con su propia TASK y su propio review, para lograr lo mismo.
- El encargo fijo es la misma salvaguarda que ya funciona con Kia (`DECISION-007`, punto 3).

## Consecuencias

- **Qué cambia:** el principio de «tres plataformas que no se hablan entre sí» pasa a tener una excepción escrita. Git sigue siendo el bus: lo único que cambia es quién pulsa el botón para que Dexia empiece.
- **Riesgo que se acepta:** ahora Clia lanza a la DEV y a la revisora. La separación de roles depende de las reglas 1, 2 y 6. Dexia y Miguel pueden señalar cualquier lanzamiento que se salga de ellas.
- **Coste:** cada review consume cuota de la cuenta de ChatGPT de Miguel.
- **Documentos a sincronizar cuando sea EFECTIVA:**
  - `AGENTS.md`: la tabla de roles y la frase de las tres plataformas.
  - `protocolo.md`: § Problema y § Flujo típico. Además, la nota «Dexia no ejecuta código» pasa a «puede ejecutar comprobaciones».
  - `agentes/dexia.md`: § Notas de operación.
  - `agentes/clia.md`.
  - `tablero.md`.

## Vigencia

Estratégica: entra en vigor con el ✅ explícito de Miguel en este hilo, sin la regla de las 48 h. Hasta entonces, Dexia sigue entrando sólo por la vía manual.

## 💬 Hilo

> **[2026-10-10] miguel:** (transcrito por Clia) deseo instalar el MCP de GPT para que invoques a Dexia. […] A, redacta la DECISION-008.
>
> **[2026-10-10] clia:** propuesta redactada. Codex CLI instalado y con sesión iniciada. No hay MCP en esta versión, así que el canal es `codex exec`. Pendiente del ✅ de Miguel.
