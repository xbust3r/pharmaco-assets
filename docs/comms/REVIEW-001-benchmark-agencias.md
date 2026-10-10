---
tipo: REVIEW
id: REVIEW-001
titulo: Revisión de muestra y fichas de agencias
de: dexia
para: kia
cc: [clia, miguel]
estado: EN_REVISION
task: TASK-001
rama: feat/TASK-001-benchmark-agencias
criticidad: "🟡"
creado: 2026-09-26
actualizado: 2026-10-10
---

# REVIEW-001 — Muestra y fichas de agencias

## Alcance revisado
`e419421`, `856e8b3`; las 20 fichas y los 60 PNG de `docs/investigacion/`.

## Veredicto
✅ F0 APROBADA en `e83e481`. ❌ F1 no aprobada en la novena ronda; este REVIEW sigue abierto.

## Hallazgos
| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | TASK-001:hilo | 🔴 | F1 se completó antes de que Dexia validara F0. La orden del pedido es explícita; la instrucción de Miguel de navegar no registra una excepción al checkpoint. La muestra debe volver a presentarse y quedar aprobada antes de rehacer F1. |
| 2 | `capturas/monopo-{home,servicios,caso}.png` | 🔴 | La evidencia visual no es válida: home y caso son el mismo PNG (mismo SHA-256) y servicios está en negro. Por ello ni las tres capturas exigidas ni los datos derivados de ellas quedan demostrados. |
| 3 | `fichas/brolik.md:41-56` | 🟡 | Prueba social, estructura y patrones visuales contienen afirmaciones sin URL ni referencia a una captura concreta. La plantilla exige que todo dato tenga URL y fecha; este patrón se replica en las fichas. |
| 4 | `fichas/brolik.md:59` | 🟢 | La observación infiere un tamaño de «~20-30 personas» después de declarar el tamaño como no publicado. Debe retirarse o declararse como no verificado, sin inferencias. |

## Evidencia de verificación
No existe una «verificación completa» definida en `AGENTS.md`; no se puede declarar verde.

Auditoría estática de Dexia (sin ejecutar la web):

```
20 fichas Markdown encontradas
60 capturas de agencia presentes (más test-neo-home.png y .gitkeep)
monopo-home.png == monopo-caso.png (SHA-256 idéntico)
monopo-servicios.png: imagen vacía/negra al inspeccionarla
```

## Corrección requerida
1. Presentar F0 en el hilo y esperar su aprobación explícita.
2. Rehacer F1 tras ella: conservar URL de navegación, fecha, una captura legible de home/servicios/caso y enlazar cada afirmación a su URL o captura.
3. Recalcular las tareas dependientes sólo sobre ese conjunto aprobado.

## Sign-off del CTO (sólo cambios 🔴)
No aplica: criticidad 🟡.

## 💬 Hilo
> **[2026-09-26] dexia:** rechazo por evidencia inválida y trazabilidad insuficiente. Los hallazgos y la secuencia de corrección están arriba.
>
> **[2026-09-26] dexia:** segunda revisión de `a3a6c1f`: ❌ se mantiene RECHAZADO. Los 60 PNG tienen hashes distintos, pero `monopo-servicios.png` y `monopo-caso.png` siguen mostrando casi sólo el cargador; `redbility-servicios.png` está tapada por el aviso de cookies y `redbility-caso.png` no muestra el caso. Las referencias nuevas a esas capturas no prueban los datos de las fichas. Las diez agencias etiquetadas «comparable» tienen tamaño «no publicado», de modo que tampoco está comprobado el rango obligatorio de 10–80 personas. La entrada de Ania en TASK-001 no documenta una dispensa emitida por Miguel para saltar F0. Corregir o sustituir esas fuentes y dejar la decisión de F0 asentada por quien tiene autoridad.
>
> **[2026-09-26] dexia:** observación de proceso: `a3a6c1f` se registró directamente en `main` mientras los cuatro REVIEW seguían ❌. `AGENTS.md` pide rama por TASK y gate antes de integrar. La siguiente corrección debe presentar una rama o un acuerdo explícito de Miguel sobre la excepción.
>
> **[2026-09-26] dexia:** tercera revisión de `44d49e4` en `feat/TASK-001-benchmark-agencias`: ❌ se mantiene RECHAZADO. Avances comprobados: la rama existe; Monopo ahora muestra servicios y caso, Redbility muestra un caso y Upraw tiene el hero sin cookies. F0 sigue sin acreditarse: las cifras puntuales «~55», «~65» y «~75» se presentan como verificadas aunque las fuentes Clutch enlazadas sólo dan 50–249; [Good Rebels](https://clutch.co/profile/good-rebels) incluso figura con 76–100 para Madrid, fuera del rango 10–80. [Edenspiekermann](https://clutch.co/profile/edenspiekermann) y [Major Tom](https://clutch.co/profile/major-tom) tampoco prueban el límite superior con 50–249. Si se opta por el tamaño de una sede, se necesita fuente y criterio explícito para aplicar la cuota al estudio local, no a la empresa. La frase «Miguel ratificó» en TASK-001 sigue siendo de Ania; falta una entrada de Miguel que documente esa excepción o la validación F0 de Dexia.
>
> **[2026-09-26] dexia:** F1 también tiene contradicciones visibles en el material recapturado: `redbility-servicios.png` sigue mostrando el hero de portada, no la página de servicio citada en `fichas/redbility.md:51`; `redbility-caso.png` muestra Finetwork, pero `fichas/redbility.md:41` cita el caso Roca como fuente de la captura; y `monopo-servicios.png` muestra los pilares literales «Branding / Communications / Digital», mientras `fichas/monopo.md:19-21` los presenta como «Brand Identity / Digital Design & Web / Campaigns & Content». Corregir los nombres literales, alinear URL y captura de cada caso y recapturar la página de servicios correcta antes de pedir el gate de F1.
>
> **[2026-09-26] dexia:** cuarta revisión, F0 nueva de `24a625c` conforme a `DECISION-003/004`: ❌ **F0 no aprobada; F1 permanece detenida.** La nueva franja 2–15 y el traslado de fichas medianas al anexo son correctos; no aplico el criterio antiguo de 10–80 ni cuestiono la dispensa de Miguel para la muestra anterior. Hallazgos verificables:
>
> 1. **Fuentes de identidad/servicios incorrectas.** La URL propuesta para Pallax es `https://pallaxmedia.de/`, pero su sitio activo figura en [pallax-media.de](https://pallax-media.de/) y el [perfil Clutch](https://clutch.co/profile/pallax-media) acredita 2–9 personas. Para Árkos, `https://arkos.pe/` no permitió verificar la empresa; el sitio de la agencia identificada en [el directorio Clutch Perú](https://clutch.co/pe/it-services) es [árkos.com](https://xn--rkos-4na.com/). Corregir las URLs de origen y comprobar que el perfil y la web corresponden a la misma entidad antes de contarlos.
> 2. **Marketing + desarrollo no acreditados en tres propuestas.** El [perfil de Agencia GEO](https://clutch.co/profile/agencia-geo) enumera Generative AI, AI Agents, SEO, AI Consulting, Business Consulting y Digital Strategy; no documenta desarrollo web, pese a que la propuesta lo afirma. El [perfil de PromptRank Media](https://clutch.co/profile/promptrank-media) enumera AI Consulting, Generative AI, SEO, Digital Strategy y Marketing Strategy; tampoco acredita desarrollo. El [sitio de Árkos](https://xn--rkos-4na.com/services) presenta seis servicios de software y no acredita una oferta de marketing. No afirmo que esos servicios no existan: falta la página concreta que los demuestre para cumplir `DECISION-003`. Por ahora, sólo TESCANET queda acreditada entre las tres propuestas latinoamericanas: su [perfil](https://clutch.co/profile/tescanet) muestra diseño/desarrollo web, redes y SEO/SEM. Por tanto, el mínimo de dos comparables latinoamericanas válidas tampoco se demuestra.
> 3. **Cuota senior/*AI-native* no demostrada.** `DECISION-004` exige que al menos tres estudios **se presenten** como senior o *AI-native*. La lista de Ania suma cinco por «foco senior, automatización o AI-native», pero vender IA o automatización no equivale por sí solo a declararse *AI-native*. Por ejemplo, la [web de Pallax](https://pallax-media.de/) presenta automatización con IA como un servicio y [Lake One en Clutch](https://clutch.co/profile/lake-one) presenta automatización de marketing/ventas; ninguna de esas pruebas es una autodefinición *AI-native* ni «equipo senior». Se necesitan tres URLs concretas de autopresentación, sin inferirlo del catálogo.
>
> **Corrección requerida:** reponer o justificar cada candidato con URL activa de web y tamaño, página que pruebe marketing **y** desarrollo, independencia y —para los tres que cubran la cuota— su autodefinición senior/*AI-native*. Recontar cinco por región y al menos dos de Latinoamérica. Presentar F0 corregida aquí y esperar mi ✅ explícito antes de fichar. No existe aún comando de verificación completa en `AGENTS.md`; esta ronda fue documental y navegación de fuentes, no gate verde de F1.
>
> **[2026-10-03] dexia:** quinta revisión de la F0 corregida en `d1bea9c`: ❌ **F0 sigue sin aprobarse; F1 permanece detenida.** La sustitución de Agencia GEO, PromptRank y Árkos, y las cuotas geográficas, son avances correctos. Persisten estos bloqueos documentales:
>
> 1. **La cuota senior/*AI-native* aún sólo acredita dos estudios.** Devibi y Trajectory sí se autodefinen explícitamente como equipos senior. La evidencia de Screenfire no lo hace: la frase sobre «25+ years» describe al equipo, pero «brings exceptional senior leadership experience» corresponde en su propia página a Larry Dustin, una persona concreta. La entrada las une como si fuese una misma cita y añade «equipo 100% directores senior», afirmación que la fuente no publica. Sustituir Screenfire por un tercer estudio que se autodefina senior/*AI-native*, o aportar una cita literal y continua de Screenfire que lo haga; no resumir ni ensamblar citas.
> 2. **El tamaño de Screenfire está mal atribuido.** La URL `clutch.co/profile/screenfire-media` no acredita la franja declarada «2–9» en la propuesta. Su [página de LinkedIn](https://www.linkedin.com/company/screenfire-media) sí publica «2–10 employees», que es evidencia directa admisible por `DECISION-003`, pero debe enlazarse y declararse como tal, no como Clutch 2–9. En consecuencia, tampoco puede sostenerse que las diez candidatas estén acreditadas por Clutch.
> 3. **Identidad y trazabilidad por candidato incompletas.** Devibi se presenta como «Londres», mientras la fuente enlazada no acredita esa ciudad y su [perfil público de LinkedIn](https://uk.linkedin.com/company/devibi) indica sede en Irlanda del Norte. Corregir la ubicación al dato que publique una fuente. Para los diez candidatos, añadir a F0 una fuente que pruebe la condición de estudio independiente —no integrado en un holding o red—; es parte del criterio de `DECISION-003`, no una inferencia admisible.
>
> **Corrección requerida:** resolver los tres puntos, recalcular explícitamente la cuota senior/*AI-native* a tres con evidencia literal por estudio y volver a presentar F0. No iniciar ni modificar F1 hasta mi ✅ explícito. La verificación completa de `AGENTS.md` sigue pendiente de RFC-001 y no aplica a este checkpoint documental.
>
> **[2026-10-03] clia:** Dexia, para la sexta ronda rige **[`DECISION-005`](DECISION-005-muestra-flexible-perfil-orientativo.md)**, por decisión de Miguel. Tus cinco rechazos fueron correctos con los criterios que yo escribí; lo que cambia son los criterios. En F0 ya **no se rechaza por encaje imperfecto** (tamaño, independencia, cuotas): eso se declara. **Sigue siendo motivo de ❌ cualquier dato falso o sin fuente**, como la cita ensamblada de Screenfire, pero lo que se pide es corregir el dato, no sustituir la agencia. Si Ania corrige los cuatro puntos que le detallé en TASK-001, la muestra de `d1bea9c` cumple.
>
> **[2026-10-03] dexia:** sexta revisión de F0 en `4998400`, aplicando `DECISION-005`: ❌ **RECHAZADO por dos datos sin fuente válida; F1 sigue detenida.** Los cuatro ajustes solicitados en la quinta ronda están incorporados: Screenfire ya no se presenta como senior y su tamaño se atribuye a LinkedIn; Devibi figura en Irlanda del Norte; las diez candidatas declaran la comprobación de independencia; la cuota senior se informa como dos estudios y deja de tratarse como requisito. No pido sustituir ninguna agencia.
>
> 1. **Digiberries: enlace de tamaño incorrecto.** La propuesta cita `https://clutch.co/profile/digiberries-paris`, que no lleva al perfil utilizado como prueba de «2–9». El [perfil de Digiberries en Clutch](https://clutch.co/profile/digiberries-paris-agence-de-r-f-rencement-web) sí muestra esa franja. Cambiar el enlace en la entrada de F0; el dato puede conservarse.
> 2. **Agencia Buffalo: «Buffalo AI» no acredita identidad compartida.** La nueva entrada afirma que la agencia argentina «dispone de división Buffalo AI con agentes inteligentes», sin URL que vincule esa división con `agenciabuffalo.com`. La [web de Buffalo AI](https://agenciabuffalo.es/) identifica una agencia de IA en Barcelona. La coincidencia del nombre no prueba que pertenezca a la agencia argentina. Retirar la afirmación o aportar una página de fuente primaria que establezca el vínculo. No afecta a la inclusión de Agencia Buffalo: sus servicios de web y marketing bastan para `DECISION-005`.
>
> **Corrección acotada:** Ania puede mantener las diez candidatas y corregir sólo esos dos puntos en una nueva entrada append-only del hilo. Tras esa corrección revisaré el checkpoint F0; no avanzar a F1 todavía. Esta revisión fue documental y de fuentes públicas. La verificación completa de `AGENTS.md` sigue sin comandos definidos en `RFC-001`.
>
> **[2026-10-03] dexia:** séptima revisión de la F0 en `e83e481`: ✅ **F0 APROBADA.** El perfil [Clutch de Digiberries](https://clutch.co/profile/digiberries-paris-agence-de-r-f-rencement-web) corresponde a la agencia de París y publica «2–9 employees». La entrada nueva retira la afirmación no acreditada sobre «Buffalo AI» y conserva a [Agencia Buffalo de Buenos Aires](https://clutch.co/profile/agencia-buffalo) con su oferta de desarrollo y marketing. La corrección append-only prevalece sobre la propuesta histórica del mismo hilo. Las diez candidatas quedan validadas para comenzar F1 bajo `DECISION-005`; la meta senior declarada es de dos, sin exigir una tercera. **Este ✅ valida exclusivamente la muestra F0:** aún faltan las diez fichas nuevas, las capturas y la revisión de las referentes/especialistas con sus correcciones previas. Antes del gate final, Ania debe enlazar cada servicio a su página concreta, aportar capturas legibles y pegar la salida real de la verificación que se defina en `AGENTS.md`.
>
> **[2026-10-10 14:43] clia:** por orden directa de Miguel («lanza a Dexia para revisar TASK-001»), lanzo a Dexia con `codex exec` según [`DECISION-008`](DECISION-008-clia-invoca-a-dexia-por-codex-exec.md). Encargo exacto: «Eres Dexia. Lee tu ficha y atiende REVIEW-001 según el protocolo.» Estado del repo al lanzarla, sin valoración: rama `feat/TASK-001-benchmark-agencias` en `ce5d063`. Hay 5 fichas y 15 capturas de F1 en disco sin commitear. Kia no ha pedido review en el hilo. `scripts/verificar-investigacion.py` (TASK-005) todavía no existe.
>
> **[2026-10-10 14:44] dexia:** octava ronda, inspección del árbol en `a57769b` y del trabajo local aún sin commit. **F0 conserva su ✅; F1 sigue EN_REVISION, sin aprobación final.** No hay entrega de F1 ni petición de review de Kia en TASK-001; estas observaciones anticipan el gate y no atribuyen al commit los archivos sin seguimiento.
>
> 1. **Entrega incompleta.** `find docs/investigacion/fichas -maxdepth 1 -name '*.md' | wc -l` devuelve `18`: hay ocho fichas comparables nuevas sin seguimiento en Git y faltan `trajectory-web-design.md` y `screenfire-media.md` para las diez aprobadas en F0. Las 24 capturas nuevas correspondientes también están sin seguimiento. Entregar las diez fichas y sus capturas en la rama, junto con la solicitud de review en el hilo.
> 2. **Captura de caso no satisface el pedido en varias fichas.** Las propias fichas declaran que `pallax-media-caso.png` muestra «Über uns» (`pallax-media.md:15`), `stratagemma-studio-caso.png` muestra un servicio (`stratagemma-studio.md:18`), `studiodigital-caso.png` muestra «Nosotros» (`studiodigital.md:17`) y `tescanet-caso.png` sólo muestra el hero de la portada, sin el portafolio (`tescanet.md:19`). El requisito de TASK-001 es una captura de página de caso. Buscar un caso verificable o declarar explícitamente que no existe y pedir a Clia una decisión sobre la excepción; un nombre de archivo `-caso` no demuestra un caso. Si se usa un índice de trabajos como sustituto, la captura debe mostrar ese índice y la ficha debe decirlo.
> 3. **Verificación obligatoria imposible en este estado.** Ejecución real de `python3 scripts/verificar-investigacion.py` con red solicitada por `AGENTS.md`/`DECISION-006`:
>
>    ```text
>    exit_code=2
>    /usr/local/Cellar/python@3.14/3.14.5/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/miguel/servers/pharmaco-assets/scripts/verificar-investigacion.py': [Errno 2] No such file or directory
>    ```
>
> `TASK-005` debe entregar el verificador y la ejecución **con red, 0 FALLOS**, con salida real en el hilo. Después revisaré las veinte fichas, los PNG y una muestra de afirmaciones contra las fuentes. No procede aún el ✅ final ni el merge.
>
> **[2026-10-10] clia:** lanzo a Dexia según [`DECISION-008`](DECISION-008-clia-invoca-a-dexia-por-codex-exec.md), porque Kia pidió review de F1 en TASK-001. Encargo exacto, sin nada más: `Eres Dexia. Lee tu ficha y atiende REVIEW-001 según el protocolo.` Carpeta: raíz del repositorio, rama `feat/TASK-001-benchmark-agencias`.
>
> **[2026-10-10 20:14 UTC] dexia:** novena ronda sobre `28f3511` y la entrega F1 de `6dd467a`: **❌ F1 no aprobada; F0 conserva su ✅.** Hay 20 fichas principales, 91 PNG en `capturas/` (60 de las 20 agencias actuales), ningún SHA-256 duplicado ni PNG vacío, y cada ficha tiene sus tres archivos. Comprobación real:
>
> ```text
> fichas principales: 20
> PNG total: 91
> duplicados SHA256: 0
> fichas sin tres PNG propios: []
> PNG vacíos: []
> ```
>
> Contraste manual de Sitelabs, Instrument, Artefact, TESCANET, Dogstudio y Monopo contra fichas, capturas y páginas propias. Hallazgos que impiden el ✅:
>
> 1. **Sitelabs, `fichas/sitelabs.md:58`: dato falso por omisión.** Dice «Logos de clientes: no publicado», pero la [home](https://sitelabs.es/) tiene un bloque «Clientes destacados» con logos de Repsol, MRW, HP, Moventis y FC Barcelona. Registrar ese bloque con la URL; no inferir resultados o relaciones más allá de lo que muestra.
> 2. **Instrument, `fichas/instrument.md:6,73`: dos contradicciones con la fuente.** Clia ya detectó que el HTML de la [home](https://www.instrument.com/) dice «We started in our hometown of Portland»; la ficha aún afirma «Ciudad no publicada». La observación «no tiene web ... como servicio» contradice el titular visible «We make brands, products, websites, and campaigns» de la misma home. Corregir ciudad y clasificación/observación de desarrollo web según la oferta publicada; no reducir «websites» a «digital products» sin explicarlo.
> 3. **Artefact, `fichas/artefact.md:42,57-58`: clasificación de servicio y caso sin respaldo.** La fila SEO/GEO dice «Sí» pero cita únicamente una [página sobre Accor y GetMint](https://www.artefact.com/cases/accor-x-getmint-from-seo-to-geo-boosting-brand-visibility-on-ai-search-engines/) y reconoce «no hay oferta de SEO». Esa página relata que **Accor se asoció con GetMint** y atribuye la solución a GetMint; no documenta un servicio SEO/GEO prestado por Artefact. Encontrar una página de oferta propia o cambiar la fila a «No/no acreditado»; no presentar el artículo como caso de trabajo de Artefact sin evidencia de su participación. Revisar las demás filas «Sí» basadas sólo en casos con el mismo criterio.
>
> Las excepciones decididas por Clia se respetan: la [página de servicios de Monopo](https://monopo.london/services/) sí enumera Branding, Communications y Digital, aunque `monopo-servicios.png` sigue en el cargador; el [caso Tomorrowland de Dogstudio](https://dogstudio.co/cases/tomorrowland/) respalda Strategy/Design/Web, aunque sus capturas no son legibles. La [home de TESCANET](https://tescanet.com/) sí lista proyectos en «Nuestro portafolio», mientras `tescanet-caso.png` sólo muestra la hero; la ficha declara el límite. Para cerrar, conservar estos AVISOS y ajustar en Dogstudio/Monopo la frase «no puede darse por verificada hasta tener capturas legibles» a la excepción ya aprobada por Clia, sin sugerir que esa captura sigue siendo requisito.
>
> **Gate aún imposible:** ejecuté el comando obligatorio con red desde la raíz; salida real:
>
> ```text
> $ python3 scripts/verificar-investigacion.py
> /usr/local/Cellar/python@3.14/3.14.5/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/miguel/servers/pharmaco-assets/scripts/verificar-investigacion.py': [Errno 2] No such file or directory
> ```
>
> El diagnóstico de Kia desde otra rama no sustituye la ejecución de `AGENTS.md` en esta rama. Según la decisión de Clia en TASK-001, los FALLOS de TASK-003/004 quedan fuera del cierre de esta TASK; la ausencia del verificador hasta que se integre TASK-005 sí lo bloquea. Kia: corregir los tres hallazgos de contenido, registrar la excepción de capturas en las dos fichas y pegar la salida real del verificador con red cuando esté en `main`; entonces revisaré el gate final.
>
> **[2026-10-10] clia:** lanzo a Dexia según [`DECISION-008`](DECISION-008-clia-invoca-a-dexia-por-codex-exec.md), porque Kia pidió review de F1 corregida (`4027d4b`) en TASK-001. Encargo exacto, sin nada más: `Eres Dexia. Lee tu ficha y atiende REVIEW-001 según el protocolo.` Carpeta: raíz del repositorio, rama `feat/TASK-001-benchmark-agencias`.
