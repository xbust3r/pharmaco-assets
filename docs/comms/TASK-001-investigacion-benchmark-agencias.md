---
tipo: TASK
id: TASK-001
titulo: Investigación — muestra y fichas de 20 agencias de marketing y desarrollo (Europa y América)
de: clia
para: ania
cc: [dexia, miguel]
prioridad: P0
estado: ABIERTA
area: investigacion
criticidad: "🟡"
relacionado: [plan-investigacion.md, plantilla-ficha.md, linea-base-2020.md, DECISION-002]
creado: 2026-09-26
actualizado: 2026-09-26
---

# TASK-001 — Muestra y fichas de 20 agencias

## Contexto

Pharmaco es un laboratorio digital de marketing y software fundado en Perú en 2020. Se retoma con un catálogo de **11 servicios** ya decidido por Miguel ([`DECISION-002`](DECISION-002-catalogo-base-servicios.md)). Antes de rehacer el HTML hay que ver cómo trabajan y se presentan hoy las agencias de referencia.

Esta TASK es **la base común** de la investigación: de sus fichas salen `TASK-002` (servicios), `TASK-003` (prueba social) y la parte B de `TASK-004` (diseño).

**Criticidad 🟡.** No toca código, pero de aquí sale lo que se publicará. El REVIEW de Dexia es obligatorio.

## Pedido

Lee entero el [plan de investigación v2](../investigacion/plan-investigacion.md): define la muestra, las cuotas y las reglas de evidencia.

1. **F0 · Muestra.** Proponer en este hilo **20 agencias + 5 suplentes**: nombre, URL, país, bloque, perfil y en una línea por qué entra. Marcar cuáles ofrecen foto y video (se buscan al menos 4). **Esperar el ✅ de Dexia antes de fichar.** Mientras tanto, puedes avanzar la parte A de [`TASK-004`](TASK-004-sistema-de-diseno.md).
2. **F1 · Fichas.** Una ficha por agencia en `docs/investigacion/fichas/{slug}.md`, con la [plantilla](../investigacion/plantilla-ficha.md). Capturas en `docs/investigacion/capturas/` de la home, la página de servicios y una página de caso.
3. Pedir el REVIEW a Dexia.

**Fuera de alcance:** redactar textos para Pharmaco, investigar precios o modelos comerciales, enviar formularios o registrarse en ningún sitio.

## Criterios de aceptación

- [ ] Muestra de 20 validada por Dexia en este hilo, antes de F1
- [ ] Cuotas cumplidas: 10 de Europa (≥ 4 países, con España) y 10 de América (≥ 6 de EE. UU.); 5 comparables, 3 referentes y 2 especialistas por bloque
- [ ] 20 fichas completas; todo dato con URL y fecha de consulta
- [ ] Tabla «Frente al catálogo de Pharmaco» rellena para los 11 servicios en cada ficha
- [ ] Nombres de servicios literales, en el idioma original
- [ ] 3 capturas por agencia (home, servicios, caso)
- [ ] Lo no encontrado, declarado como tal
- [ ] REVIEW de Dexia ✅

## 💬 Hilo

> **[2026-09-26 16:20] clia:** creo la task. Ania: empieza por F0 y para ahí hasta que Dexia valide la muestra. Los comparables (independientes de 10 a 80 personas que hacen marketing y desarrollo) son lo que más pesa: una agencia de 2.000 personas no es referencia de catálogo para Pharmaco, sólo de tendencia. Un commit por fase: `comms(TASK-001): ania …`.
>
> **[2026-09-26 16:50] clia:** reajusto la task tras `DECISION-002`. El catálogo ya está decidido (11 servicios), así que la ficha ya no pregunta qué servicios hay, sino cómo trata cada agencia **nuestros** 11. Sale el modelo comercial. Entra una captura más: una página de caso, para `TASK-003`. El análisis pasa a `TASK-002`, `003` y `004`. Aún no la habías tomado, así que no hay trabajo perdido.
