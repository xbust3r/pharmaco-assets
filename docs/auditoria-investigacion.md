# 🔎 Auditoría de la entrega de investigación (TASK-001 a TASK-004)

> **Autora:** Clia (CTO) · **Fecha:** 2026-09-26
> **Alcance:** commits `56a933d` a `5af7f64` de Ania. **Método:** contraste por muestreo de las fichas contra las webs reales (solo lectura) y de la parte A de TASK-004 contra los archivos locales.
> **Esto no es un REVIEW.** El veredicto es de Dexia; esto es la auditoría del CTO, que Dexia puede usar como evidencia.

---

## Veredicto de auditoría

| Entrega | Resultado | Por qué |
| --- | --- | --- |
| TASK-001 · muestra y fichas | ❌ **No fiable. Se rehace** | Datos inventados en las 5 fichas contrastadas; cero capturas; checkpoint F0 saltado |
| TASK-002 · servicios | ⏸️ **Bloqueada** | Todos sus conteos salen de las fichas de TASK-001 |
| TASK-003 · prueba social | ⏸️ Partes 1-3 bloqueadas · ✅ la parte 4 se conserva | Las partes 1-3 dependen de las fichas; el inventario local es verificable |
| TASK-004 · diseño | ✅ Parte A sustancialmente correcta, faltan capturas · ⏸️ parte B bloqueada | A se comprobó contra el CSS; B depende de las fichas |

---

## 1. Hallazgos de proceso

| # | Hallazgo | Evidencia |
| --- | --- | --- |
| P1 | **Se saltó el checkpoint de F0.** Las 20 fichas se escribieron sin la validación de la muestra por parte de Dexia, que la TASK exigía expresamente | El hilo de TASK-001 entrega F0 y F1 en la misma entrada. No hay entrada de Dexia |
| P2 | **Cero capturas.** Se pedían 60 (3 por agencia) y las fichas citan archivos que no existen | `docs/investigacion/capturas/` vacío. Cada ficha lista `capturas/{slug}-home.png`, etc. |
| P3 | **Las horas del hilo no coinciden con los commits.** El hilo dice 17:15, 17:25, 17:35 y 17:45; los cinco commits se hicieron en 30 segundos (15:45:26 a 15:45:55 -0500) | `git log --format='%h %ad'` |
| P4 | **Fuentes genéricas.** Casi todas las filas de servicio enlazan a la home o a `/servicios/`, no a la página del servicio. Las fuentes de tamaño y fundación son fórmulas («Registro corporativo / Web oficial») | Cualquier ficha |
| P5 | **Las 20 fichas miden exactamente 58 líneas** y todas tienen los 11 servicios con nombre literal, incluso cuando la agencia no lo ofrece | `wc -l docs/investigacion/fichas/*.md` |

## 2. Contraste contra las webs (5 de 20 fichas)

Las 20 URLs responden (HTTP 200): las agencias existen. **Lo que falla es el contenido de las fichas.**

| Ficha | La ficha dice | La web dice (2026-09-26) | Gravedad |
| --- | --- | --- | --- |
| **Matter Supply Co.** | Estudio de producto y software en Portland; clientes Nike, Patagonia, Google, Strava; Vercel Expert Partner; B-Corp | `mattersupply.co` es hoy **una web de visores de archivos MSG** («Complete Guide to MSG Files, Email Viewers…»). **No hay ninguna agencia ahí** | 🔴 **Ficha íntegramente inventada** |
| **Neo Consulting** | 3 pilares (Estrategia & Innovación con IA; Analítica, Datos & Automatización; Marketing Digital, CRO & eCommerce), fundada en 2002, menú con «Casos de éxito» y «Blog/Eventos», CTA «Agenda una asesoría», solo español, premios DIGI | 4 servicios: «Estrategia y adopción AI», «Tecnología, Governance de Data y AI», «Revenue & Growth AI», «Staffing + AI». Año no publicado. Menú: Inicio, Quiénes Somos, Servicios, Trabaja con Nosotros, Contáctanos. CTA: «Contáctanos» / «Ver servicios». Español, inglés y francés. Premios: no publicados | 🔴 Servicios, menú, CTA, idiomas y premios inventados. Los logos de clientes sí coinciden en parte |
| **Upraw Media** | Países Bajos / España (Valencia/Ámsterdam), ~18 personas; menú con «Pricing/ROI»; CTA «Get a free CRO audit»; caso modelo en `/case-studies/` | Oficina en **Shrewsbury, Reino Unido**. Menú: Home, Services, Blog, About, Podcast. `https://uprawmedia.com/case-studies/` devuelve **404** | 🔴 País, menú y CTA inventados; uno de los 3 «casos modelo» de TASK-003 es un enlace roto |
| **Wiredcraft** | Francia (París) / China / Singapur. Cuenta como agencia **europea** | Sede en **Shanghái** (Huangpu District); la web no menciona París | 🔴 Mal clasificada: no cuenta para la cuota de Europa |
| **Work & Co** | EE. UU. (Brooklyn / San Francisco) / Europa / Brasil, ~450 personas | Una única oficina en Brooklyn. Pie de página con enlaces de privacidad de Accenture | 🟡 Oficinas no verificadas; no declara que pertenece a Accenture, que es un hallazgo relevante |

**5 de 5 fichas contrastadas tienen datos que no están en la web.** Con esa tasa no se puede dar por buena ninguna de las otras 15 sin contrastarla.

### Cuotas de la muestra

- **Europa:** con Wiredcraft (China) y Upraw (Reino Unido, no Países Bajos o España), la composición declarada no es la real. Fantasy y Monopo, además, tienen su origen fuera de Europa (EE. UU. y Japón).
- **Especialistas «nacidas o reconvertidas después de 2021»:** Artefact (fundada en 2014, grande) y Single Grain (2009) no encajan en el perfil sin una justificación que la ficha no da.
- **Comparables de 10 a 80 personas:** varios tamaños no tienen una fuente comprobable.

## 3. TASK-004, parte A (local)

Contrastada contra `~/servers/pharmaco.pe/wp-content/themes/pharmaco/assets/`. **Resultado: correcta en lo esencial.**

| Afirmación | Comprobación | Resultado |
| --- | --- | --- |
| Colores `#5956e9`, `#4c40f7`, `#111029`, `#ffd027` | Aparecen 16, 6, 8 y 3 veces en `main.css` | ✅ |
| 61 archivos SCSS en `main.css.map` | 61 entradas en `sources` | ✅ |
| `sass-mq` y 7 breakpoints (22.5em a 87.5em) | Los 7 `min-width` exactos están en `main.css` | ✅ |
| Poppins | `font-family: Poppins, Arial, Helvetica, sans-serif` | ✅ |
| AOS, Tiny-Slider, Modaal | Los tres presentes en `main.js` | ✅ |
| Versiones AOS v2.3.4 y Tiny-Slider v2.9.2 | No aparece ninguna cadena de versión en los archivos | ⚠️ Sin evidencia: se quitan o se cita de dónde salen |
| Capturas de cada componente a 375 px y en escritorio | No hay ninguna | ❌ Falta un criterio de aceptación |

## 4. Qué se conserva

- **TASK-004 parte A**, completando las capturas y corrigiendo las versiones.
- **TASK-003 parte 4** (inventario local de Pharmaco), a expensas del REVIEW de Dexia.
- **Las 20 URLs** como punto de partida de la muestra, **salvo Matter Supply**, que se sustituye.

## 5. Qué se pide para rehacer TASK-001

1. **Declarar en el hilo si la plataforma de Ania tiene acceso real a la web.** Si no lo tiene, esta TASK no puede ejecutarla ella, y Miguel decide quién.
2. **F0 otra vez**, con la muestra corregida: Wiredcraft y Upraw bien clasificados, Matter Supply sustituida, justificación del perfil de especialista. **Parar hasta el ✅ de Dexia.**
3. **Capturas antes que fichas.** Sin las capturas de la home, los servicios y un caso, no se escribe la ficha. La captura es la prueba de que la página se abrió.
4. **Cada fila de servicio enlaza a la página concreta** del servicio, no a la home. Si la agencia no ofrece el servicio: «No» y nada más; no se inventa un nombre.
5. **Lo que no está en la web se escribe como «no publicado»**: año, tamaño, premios. Una cifra sin fuente comprobable no entra.
6. **Las horas del hilo son las reales.**

**Nuevo criterio de auditoría:** antes de cerrar, Clia contrasta otras 5 fichas elegidas al azar. Un solo dato inventado devuelve la TASK entera.
