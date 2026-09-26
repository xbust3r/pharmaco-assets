---
tipo: TASK
id: TASK-001
titulo: Investigación — benchmark de 20 agencias de marketing y desarrollo (Europa y América)
de: clia
para: ania
cc: [dexia, miguel]
prioridad: P0
estado: ABIERTA
area: investigacion
criticidad: "🟡"
relacionado: [plan-investigacion.md, linea-base-2020.md, RFC-001]
creado: 2026-09-26
actualizado: 2026-09-26
---

# TASK-001 — Investigación: benchmark de agencias

## Contexto

Pharmaco es un laboratorio digital de marketing y software fundado en Perú en 2020. Se retoma el proyecto, y el catálogo de 2020 está desfasado (ver [línea base](../linea-base-2020.md)). Vamos a rehacer el HTML del sitio, pero primero hay que saber qué ofrecen y cómo se presentan hoy las agencias de referencia.

**Criticidad 🟡, no 🟢.** No toca código, pero de este informe sale el catálogo de servicios que se publicará. Un dato mal traído se convierte en un servicio mal definido, así que el REVIEW de Dexia es obligatorio antes de cerrar.

## Pedido

Ejecutar el [plan de investigación](../investigacion/plan-investigacion.md) completo, fases F0 a F2. **Léelo entero antes de empezar**: define la muestra, las preguntas, las reglas de evidencia y los entregables.

Resumen:

1. **F0:** proponer en este hilo 20 agencias (10 de Europa y 10 de América, con cuotas por perfil) más 5 suplentes, con su URL y el criterio por el que entran. **Esperar el ✅ de Dexia a la muestra antes de fichar.**
2. **F1:** una ficha por agencia en `docs/investigacion/fichas/`, con la [plantilla](../investigacion/plantilla-ficha.md), más sus capturas.
3. **F2:** `matriz-servicios.md` e `informe-hallazgos.md`, que responden P1–P7.
4. Pedir el REVIEW a Dexia.

**Fuera de alcance:** redactar servicios o textos para Pharmaco, proponer precios, diseñar, enviar formularios o registrarse en ningún sitio.

## Criterios de aceptación

- [ ] Muestra de 20 validada por Dexia en este hilo, antes de F1
- [ ] 20 fichas completas; todo dato con URL y fecha de consulta
- [ ] Capturas de la home y de la página de servicios de cada agencia
- [ ] Nombres de servicios literales, en el idioma original
- [ ] La matriz cuadra con las fichas (Dexia lo comprueba)
- [ ] El informe responde P1–P7 y cada conclusión enlaza a sus fichas
- [ ] Cada hipótesis de P3, confirmada, refutada o marcada «sin evidencia suficiente»
- [ ] Lo no encontrado, declarado como tal
- [ ] REVIEW de Dexia ✅

## 💬 Hilo

> **[2026-09-26 16:20] clia:** creo la task. Ania: empieza por F0 y para ahí hasta que Dexia valide la muestra. Los comparables (independientes de 10 a 80 personas que hacen marketing y desarrollo) son lo que más pesa: una agencia de 2.000 personas no es referencia de catálogo para Pharmaco, sólo de tendencia. Un commit por fase: `comms(TASK-001): ania …`.
