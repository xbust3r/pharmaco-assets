---
tipo: RFC
id: RFC-002
titulo: Catálogo de servicios, posicionamiento y estructura del sitio de Pharmaco
de: clia
para: [miguel]
cc: [dexia, kia]
estado: ABIERTA
area: producto
relacionado: [DECISION-002, DECISION-003, DECISION-004, TASK-002, TASK-003, TASK-004, TASK-006, resumen.md, prueba-social.md, patrones-benchmark.md]
creado: 2026-10-13
actualizado: 2026-10-13
---

# RFC-002 — Catálogo, posicionamiento y estructura del sitio

## Problema

La etapa de investigación está cerrada (TASK-001 a TASK-005; verificador con 0 FALLOS globales sobre `main`, `42a9e87`). El catálogo de **11 servicios** y el modelo operativo (**senior + agentes de IA + capacidad limitada**) los fijó Miguel en [`DECISION-002`](DECISION-002-catalogo-base-servicios.md) y [`DECISION-004`](DECISION-004-modelo-operativo-senior-ia.md). Falta decidir **cómo se nombran, cómo se agrupan, qué páginas tiene el sitio y cómo se cuenta todo eso**. De aquí salen las TASKs de contenido y rediseño, que se aplicarán sobre la web migrada a Blackgrow ([`TASK-006`](TASK-006-migracion-blackgrow.md)).

**Cómo se lee este RFC:** cada punto lleva una **propuesta de Clia**, la **evidencia** que la sostiene, las **alternativas** y lo que **decide Miguel**. Miguel aprueba, cambia o veta punto por punto en el hilo.

**Lo que este RFC no hace:** no escribe textos para la web, no fija precios y no diseña pantallas. Eso viene después, en TASKs.

**Límite de la evidencia:** 20 agencias no son estadística. Las frecuencias dicen qué aparece en la muestra, no qué hace el mercado ([`patrones-benchmark.md`](../diseno/patrones-benchmark.md), § 4).

---

## 1. Agrupación: cuatro pilares

**Propuesta.** Los 11 servicios se presentan en **4 pilares**, agrupados por los servicios que las agencias de la muestra venden juntos:

| Pilar (nombre provisional) | Servicios | Evidencia de que van juntos ([`resumen.md`](../investigacion/servicios/resumen.md), § 2) |
| --- | --- | --- |
| **Marca y contenido** | 1 Branding · 2 Social media · 7 Foto y video | Social y Foto/video coinciden en 5 de 6 agencias |
| **Producto digital** | 3 Desarrollo web · 6 Apps y software | Las 9 agencias de Apps hacen también Web (9 de 9) |
| **Crecimiento** | 4 Campañas · 5 Performance · 9 SEO y GEO | Las 7 de Performance hacen Campañas (7 de 7); SEO/GEO y Campañas, 9 de 13 |
| **Datos e IA** | 8 IA · 10 CRO · 11 Datos y automatización | IA y Datos, 9 de 11; las 6 de CRO hacen Datos (6 de 6) |

**Alternativas.**

- **Lista plana de 11.** Es lo que hacen Devibi y otras comparables pequeñas, que presentan una lista única. Más simple, pero con 11 entradas el menú y la página de servicios se hacen largos.
- **Tres pilares**, uniendo Crecimiento con Datos e IA. Pierde la separación entre adquirir tráfico y medirlo o automatizarlo, que es justo donde Pharmaco suma servicios nuevos.

**Decide Miguel:** ¿4 pilares? ¿Con estos nombres o con otros?

---

## 2. Nombres de los servicios

**Propuesta.** El nombre que más se repite en la muestra, en español, para un sitio dirigido a Perú y Latinoamérica:

| # | Hoy (DECISION-002) | Propuesta | Evidencia (nombres más repetidos, nº de agencias) |
| --- | --- | --- | --- |
| 1 | Branding | **Branding e identidad** | «brand» (7), «identi» (4) |
| 2 | Social Media | **Social media** | «social» (5), «social media» (3) |
| 3 | Desarrollo Web | **Desarrollo web** | «web» (14), «desarrollo/development» (9) |
| 4 | Campañas publicitarias | **Campañas publicitarias** | «campaña/campaign» (6), «Ads» (4) |
| 5 | Performance | **Paid media y performance** | La palabra «performance» **no aparece** como nombre de servicio en la muestra; sí «paid media» (3) y «ROI/ROAS» (3) |
| 6 | Desarrollo de apps y software | **Apps y software a medida** | «platform/product/software» (7), «app» (4) |
| 7 | Fotografía y video | **Producción de foto y video** | «video» (4), «producción/production» (4) |
| 8 | Inteligencia artificial | **IA aplicada y agentes** | «AI/IA» (11), «agent/agentic» (3) |
| 9 | SEO y GEO | **SEO y GEO** | «SEO» (8), «GEO/AEO/AIO» (6); dos agencias los nombran juntos (Digiberries, Pallax) |
| 10 | CRO | **Optimización de conversión (CRO)** | «conversion» (6), «CRO» (2) |
| 11 | Datos y automatización | **Datos, analítica y automatización** | «data/datos» (6), «analytics/analítica» (4), «automation» (3) |

**Una tensión que decide Miguel: Campañas (4) frente a Performance (5).** En la muestra coinciden siempre (7 de 7) y nadie usa «performance» como nombre de servicio.

- **Opción A (propuesta):** dos servicios distintos. **Campañas** es la idea creativa y la pieza; **Paid media y performance** es la compra de medios y su optimización.
- **Opción B:** fusionarlos en uno solo, «Campañas y paid media». El catálogo pasaría a 10 servicios y cambiaría DECISION-002.

**Decide Miguel:** ¿nombres? ¿A o B?

---

## 3. Alcance de cada servicio

**Propuesta.** Cada página de servicio dice **qué incluye** con los subservicios que la muestra repite, sin prometer resultados. Los subservicios por servicio están en las 11 fichas de [`servicios/`](../investigacion/servicios/).

**Límite declarado:** las fichas **no recogen entregables con frecuencia** ([`resumen.md`](../investigacion/servicios/resumen.md), § 5). El alcance concreto de cada servicio (qué entrega Pharmaco, en cuánto tiempo y con qué herramientas) **solo lo puede definir Miguel**. Se pide en una TASK de contenido, servicio por servicio, con un formulario corto: qué se entrega, qué no, qué hacen las personas y qué hacen los agentes.

**Decide Miguel:** ¿de acuerdo en levantar el alcance con él, servicio por servicio, antes de redactar?

---

## 4. Posicionamiento: senior + IA + capacidad limitada

**Propuesta.** El modelo operativo de DECISION-004 es **el mensaje central del sitio**, contado con tres afirmaciones comprobables. La muestra tiene ejemplos de las tres:

| Afirmación | Cómo la cuentan otros (literal, de las fichas) | Condición para Pharmaco |
| --- | --- | --- |
| **Equipo senior** | Devibi: «We're a deliberately small senior team — no account-manager telephone games, no juniors learning on your budget.» · Trajectory: «A small, senior team. No junior handoffs, no learning on your budget, no unnecessary layers.» | Cierta solo si todo el equipo es senior. Se muestra con personas con nombre y trayectoria |
| **IA como herramienta, con control humano** | Stratagemma: «L'AI è una delle tecnologie utilizzate, non il prodotto.» y «AI con controllo umano» · Single Grain: «We Don't Advise on AI. We Run It.» | Encaja con DECISION-004: las personas deciden y revisan, los agentes producen. Se cuenta como **cómo trabajamos**, no como «IA mágica» |
| **Capacidad limitada** | Upraw Media: «Fewer clients» (declaración de cupo, sin cifra) | Exige un número real (proyectos simultáneos o por trimestre) que solo Miguel conoce |

**Lo que no se hace** (regla de `AGENTS.md` y de DECISION-004): no se promete un resultado, no se llama «AI-native» a algo que no lo sea y no se publica una cifra de capacidad que no se cumpla.

**Alternativa:** contar solo «senior» y dejar la IA y la capacidad como detalle interno. Es más prudente, pero pierde lo que distingue a Pharmaco de las agencias de 2020.

**Decide Miguel:** ¿las tres afirmaciones? ¿Cuál es la capacidad real?

---

## 5. Estructura del sitio

### 5.1 Páginas

**Propuesta:**

| Página | Qué lleva | Evidencia |
| --- | --- | --- |
| **Inicio** | Ver 5.2 | — |
| **Servicios** | Índice por los 4 pilares | Punto 1 |
| **11 páginas de servicio** | Qué es, qué incluye, cómo lo hacemos (personas + agentes), caso relacionado si existe, llamada a la acción | 17 de 20 fichas describen página de servicio. Además, **Pharmaco vende SEO y GEO**: su propia web tiene que poder posicionar cada servicio |
| **Portafolio / Casos** | Solo con material autorizado (punto 6) | 10 de 20 menús nombran casos o trabajos |
| **Nosotros** | Equipo senior con nombre y cargo, y el modelo operativo | Hoy solo 1 comparable lo muestra: es un diferencial barato |
| **Contacto** | Formulario y disponibilidad (punto 8) | — |
| **Blog** | **Solo si va a haber contenido** (punto 6, opción A) | 13 de 20 menús tienen sección editorial. Hoy `blog.html` no existe en la web de assets |

**Alternativa a las 11 páginas:** 4 páginas, una por pilar. Es menos contenido que escribir, pero 4 URLs para 11 servicios posicionan peor, y eso contradice la oferta de SEO y GEO.

### 5.2 Portada

**Propuesta de orden.** Parte de la portada actual de la web de assets y le añade el modelo operativo. La muestra **no tiene un orden común verificable**: solo 3 de 20 fichas listan las secciones sin advertir que la lista es parcial ([`patrones-benchmark.md`](../diseno/patrones-benchmark.md), § 1.1).

1. Héroe con la propuesta de valor y la llamada a la acción.
2. Los 4 pilares.
3. **Cómo trabajamos:** senior + IA + capacidad (punto 4).
4. Casos o clientes, si hay material autorizado.
5. Proceso (ya existe en la web de assets: Descubrimiento → Plan → Ejecución → Entrega).
6. Contacto con disponibilidad.

### 5.3 Menú

Nosotros · Servicios · Portafolio · (Blog, si se decide) · botón **«Contáctanos»** como llamada a la acción (14 de 20 lo llevan en la cabecera).

**Decide Miguel:** ¿11 páginas de servicio o 4? ¿Habrá blog?

---

## 6. Prueba social

**Propuesta.** Por fases, empezando por lo que no depende de nadie. Las opciones son las de [`prueba-social.md`](../investigacion/prueba-social.md), parte 5:

| Fase | Opciones | Por qué ahora |
| --- | --- | --- |
| **1 · Sin terceros, ya** | **C** Google Business Profile (verificación en hasta 5 días hábiles) · **B** certificación de Google Analytics de cada persona (cursos gratuitos) · **A** contenido propio, si se decide hacer blog | Dependen solo de Pharmaco |
| **2 · Con plataformas** | **D** Meta Blueprint (99–150 USD por examen) · **E** HubSpot Solutions Partner, solo si Pharmaco trabaja con HubSpot · **F** perfil de Clutch con reseñas | Reseñas y certificaciones de terceros |
| **3 · Con clientes** | **H** casos con página propia y cifra de resultado · **I** portafolio de 2020 | Requieren permiso y datos de clientes |

**Descartada por ahora: G, Google Partner** como empresa. Exige 10 000 USD de gasto gestionado en 90 días y 50 % de estrategas certificados. No encaja con un estudio que arranca.

**Lo que bloquea la fase 3 son las 7 preguntas de [`prueba-social.md`](../investigacion/prueba-social.md), § 4.3**, sobre los clientes de 2020, los logos, las métricas y los clientes recientes. Sin respuesta, el sitio sale **sin portafolio**, como hacen 3 de las 10 comparables (Devibi, Digiberries y TESCANET no tienen casos con página propia).

**Decide Miguel:** ¿las fases? ¿Las 7 preguntas?

---

## 7. Dirección visual

**Propuesta.** Conservar la base de la web de assets, porque ya coincide con buena parte de la muestra, y añadir solo lo que la evidencia sostiene ([`patrones-benchmark.md`](../diseno/patrones-benchmark.md), § 3):

| Patrón | Propuesta | Por qué |
| --- | --- | --- |
| Tipografía | **Poppins**, solo sans (V2). Sin serif | Añadir una familia tiene coste de carga, y la muestra no decide (8 serif, 6 sans, 12 sin dato) |
| Fondo | **Claro, con héroe de color** (como hoy) | La muestra se reparte 7 y 7 |
| Animación | **Ligera**, ya en JS nativo (TASK-006) | 9 portadas con animación o vídeo; el vídeo de fondo exige material que no hay |
| Clientes en portada | **Sí, si hay logos autorizados** (pregunta 4) | 7 de 20 |
| Cifras en portada | **Solo con fuente propia** (por ejemplo, proyectos entregados) | 5 de 20; una cifra sin fuente rompe la regla de no inventar |
| Testimonios | **Solo con nombre y permiso** | 6 de 20 |
| Paleta | **La actual** (57 colores ya en `@theme`) | Se migró tal cual; un cambio de paleta sería un RFC propio |

**Alternativa:** rediseño visual completo. No hay evidencia que lo justifique, y duplicaría el trabajo de la migración.

**Decide Miguel:** ¿se conserva la base visual?

---

## 8. Contacto y capacidad

**Propuesta.** La página de contacto muestra la **disponibilidad real**: por ejemplo, «aceptamos N proyectos nuevos este trimestre» o una lista de espera cuando no hay cupo. El formulario pide solo lo mínimo para valorar el encaje.

**Evidencia:** solo Upraw Media declara algo parecido («Fewer clients»), sin cifra. Es poco frecuente y por eso es diferencial, pero solo funciona si el número es cierto y se actualiza.

**Decide Miguel:** ¿cupo con número, lista de espera o solo «trabajamos con pocos clientes»? ¿Quién lo actualiza?

---

## 9. Fuera del catálogo: comercio electrónico

**Información, no propuesta.** **8 de 20 agencias** venden comercio electrónico como servicio propio ([`resumen.md`](../investigacion/servicios/resumen.md), § 4). Es el servicio fuera de catálogo más repetido. La investigación no dice si Pharmaco hizo trabajos de e-commerce: el portafolio de 2020 solo tiene campañas, branding y diseño de personajes.

**Decide Miguel:** ¿se queda fuera, entra como servicio 12 o va dentro de Desarrollo web?

---

## Impacto

- **Qué sale de aquí:** las TASKs de contenido (alcance por servicio, textos) y de rediseño sobre la web migrada. Empiezan cuando TASK-006 esté en `main` y este RFC aprobado.
- **¿Es 🔴?** El RFC no: es documentación. Las TASKs que salgan sí lo serán cuando toquen layout, tokens, formularios o contenido que sale hacia el cliente.
- **Cambia DECISION-002** solo si Miguel elige la opción B del punto 2 o el comercio electrónico como servicio 12.

## Resumen de lo que decide Miguel

| # | Pregunta | Propuesta de Clia |
| --- | --- | --- |
| 1 | Agrupación | 4 pilares |
| 2 | Nombres; Campañas y Performance | Nombres de la tabla; dos servicios separados (A) |
| 3 | Alcance | Levantarlo con Miguel, servicio por servicio |
| 4 | Posicionamiento y capacidad real | Senior + IA con control humano + cupo real |
| 5 | Páginas y blog | 11 páginas de servicio; blog solo si hay contenido |
| 6 | Prueba social | Fases 1 → 2 → 3; las 7 preguntas |
| 7 | Dirección visual | Conservar la base actual |
| 8 | Contacto | Disponibilidad real visible |
| 9 | Comercio electrónico | Decisión abierta |

## 💬 Hilo

> **[2026-10-13] clia:** abro el RFC con la investigación cerrada. Cada propuesta cita su evidencia. Donde la muestra no da para decidir (orden de la portada, tipografía, fondo), lo digo y propongo conservar lo que ya hay. Miguel: puedes responder punto por punto, aunque sea con «sí», «no» o «cambia X».
