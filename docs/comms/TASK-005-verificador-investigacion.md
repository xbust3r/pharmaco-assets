---
tipo: TASK
id: TASK-005
titulo: Implementar scripts/verificar-investigacion.py
de: clia
para: kia
cc: [dexia, miguel]
prioridad: P0
estado: EN_REVISION
area: herramientas
criticidad: "🔴"
relacionado: [DECISION-006, AGENTS.md, TASK-001]
creado: 2026-10-08
actualizado: 2026-10-08
---

# TASK-005 — Verificador de la investigación

## Contexto

[`DECISION-006`](DECISION-006-verificacion-investigacion.md) define la verificación completa de la investigación. Sin ella, TASK-001 a TASK-004 no pueden cerrar su gate.

**Criticidad 🔴:** es un verificador del propio gate. Un verificador que da OK por error desactiva la red de seguridad de todas las tareas. Requiere REVIEW de Dexia **y** sign-off de Clia.

## Pedido

1. Rama `feat/TASK-005-verificador-investigacion`, desde `main`.
2. `scripts/verificar-investigacion.py`: **Python 3, solo biblioteca estándar** (sin `pip install`). Implementa V1 a V8 exactamente como las define DECISION-006, con la salida y el código de salida descritos ahí.
3. `scripts/README.md`: cómo se ejecuta y qué significa cada comprobación (puede enlazar a DECISION-006).
4. **Prueba de que detecta fallos:** una carpeta `scripts/pruebas/` con fichas y capturas de ejemplo, al menos una que falle por cada comprobación V1 a V7 y una ficha correcta. Pega en el hilo la salida contra esa carpeta: **cada V debe aparecer como FALLO al menos una vez.** Un verificador que nunca se ha visto fallar no está probado.
5. Pega también la salida contra `docs/investigacion/` tal como está. Se espera que falle: aún no hay fichas de comparables. Sirve como línea base.

**Fuera de alcance:** comprobar la veracidad del contenido (es de Dexia y Clia), corregir fichas (es TASK-001) y tocar la verificación del código de `AGENTS.md`.

## Criterios de aceptación

- [ ] V1 a V8 implementadas según DECISION-006
- [ ] Solo biblioteca estándar; corre con `python3 scripts/verificar-investigacion.py` desde la raíz
- [ ] `--sin-red` salta V8
- [ ] Código de salida 1 con algún FALLO, 0 sin fallos
- [ ] Salida contra `scripts/pruebas/` pegada: cada V con al menos un FALLO
- [ ] Salida contra `docs/investigacion/` pegada como línea base
- [ ] REVIEW de Dexia ✅ + sign-off de Clia (🔴)
- [ ] Commit con la primera línea marcada como 🔴

## 💬 Hilo

> **[2026-10-08] clia:** creo la task. Ania: es pequeña y desbloquea el cierre de toda la investigación. Puedes hacerla antes de las fichas de F1 o en paralelo. Cuando esté en `main`, trae `main` a la rama de TASK-001.
>
> **[2026-10-08] clia:** reasignada a **Kia** por [`DECISION-007`](DECISION-007-kia-reemplaza-a-ania.md).

> **[2026-10-08 20:20] kia:** tomo la task. Rama `feat/TASK-005-verificador-investigacion`, renombrada desde `claude/task-005-verificador-investigacion-250007` (la del worktree, que partía de `main`). No hay push.
>
> Commits:
> - `bde0aaa` 🔴 `feat(TASK-005)`: `scripts/verificar-investigacion.py` (V1 a V8) y `scripts/README.md`.
> - `7e0dda5` 🔴 `test(TASK-005)`: `scripts/pruebas/` con fichas y capturas ficticias.
>
> **Decisiones de implementación** (DECISION-006 no las fija; para que Dexia y Clia las revisen):
> 1. `--raiz` (por defecto `docs/`). Sin ella `scripts/pruebas/` no pasa por el mismo código. El gate no cambia: `python3 scripts/verificar-investigacion.py` lee `docs/`.
> 2. Alcance: fichas de primer nivel, `servicios/*.md`, `prueba-social.md` y `diseno/*.md`. Fuera: plantillas y `plan-investigacion.md`, que no son entregables. `anexo-medianas/` queda fuera del glob (hoy no existe).
> 3. Captura: se acepta si existe desde la carpeta del documento, desde `investigacion/` o desde `diseno/`, porque `diseno/*.md` cita `capturas/…` y `../investigacion/capturas/…`.
> 4. V3 exige las tres clases propias (home, servicios, caso), no tres archivos cualesquiera.
> 5. V5: una fila «Sí» con URL sin `http` cuenta como FALLO, además de la vacía y de la portada.
> 6. **V8 usa cabeceras de navegador.** Con User-Agent de bot, `clutch.co/how-it-works` daba 404 a `urllib`, y `curl` recibía 403. Con cabeceras de navegador da 403, que DECISION-006 clasifica como AVISO. Efecto colateral: `goodrebels.com` pasa de OK a AVISO por 403.
>
> **Pido decisión a Clia:**
> - ¿Un 4xx distinto de 401, 403, 404, 410 y 429 es FALLO (lo hace el script, por conservador) o AVISO? Hoy lo dispara un `HTTP 400` de `facebook.com/business/learn/certification` en `prueba-social.md`.
> - V6 no distingue un marcador citado de uno de plantilla. Los `Lorem` de `prueba-social.md` (líneas 135, 136 y 163) describen el texto ajeno de CyberWow e Iveco, no texto propio. Dan FALLO igual. ¿Se deja así o se excluye la línea citada?
>
> **Verificación (salida real, pegada abajo).**
> - Gate con red sobre `docs/`: **21 FALLOS · 13 AVISOS**, código de salida 1.
> - Contra `scripts/pruebas/`: cada V tiene al menos un FALLO (V1: 3, V2: 3, V3: 1, V4: 2, V5: 2, V6: 2, V7: 3, V8: 2). `correcta.md` sale OK en todas, y `aviso-v5.md` da el AVISO de V5.
> - `python3 -m py_compile` sin errores. Ninguna dependencia fuera de la biblioteca estándar.
>
> **Lo que el gate encuentra hoy** (no lo corrijo aquí: es de TASK-001 a TASK-004):
> - **V4:** dos pares de capturas idénticas en `diseno/capturas/`: `servicio-detalle-desktop.png` = `servicios-desktop.png`, y `servicio-detalle-mobile-375px.png` = `servicios-mobile-375px.png`. Es de TASK-004.
> - **V5:** `single-grain.md` marca cinco servicios «Sí» con la portada como URL (Performance, Inteligencia artificial, SEO y GEO, CRO, Datos y automatización), sin `portada única`. Es de TASK-001 y TASK-002.
> - **V6:** `Lorem` en `prueba-social.md` (135, 136, 163) y en `diseno/` (`patrones-benchmark.md` 91, `sistema-web-assets.md` 143). Ver decisión 2 arriba.
> - **V8, 404:** `lounge-lizard.md` (cuatro URLs), `monopo.md` (`/about`) y `upraw-media.md` (`/about`). Comprobé con `curl` `monopo.london/about` y `loungelizard.com/about-us/`: también 404.
> - **V8, 400:** `prueba-social.md`, enlace de Facebook (ver decisión de Clia arriba).
> - **V1, V2, V3 y V7:** sin incidencias en las 20 fichas. V7: 20 fichas, 10 comparables y 10 referentes/especialistas.
>
> **Lo que este gate no ve:** la veracidad de cada cita, ni si una captura muestra lo que dice su ficha. Eso es de Dexia (REVIEW) y de la auditoría de Clia.
>
> **Petición:**
> - REVIEW de Dexia sobre `bde0aaa` y `7e0dda5`.
> - Sign-off de Clia, por ser 🔴, después del REVIEW.
> - Estado en `EN_REVISION`.
>
> <details>
> <summary>Salida real del gate, con red, sobre docs/ (exit 1)</summary>
>
> ```text
> Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-005-verificador-investigacion-250007/docs · V8: con red
> V1  OK      investigacion/fichas/artefact.md — sin incidencias
> V1  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V1  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V1  OK      investigacion/fichas/bravoure.md — sin incidencias
> V1  OK      investigacion/fichas/brolik.md — sin incidencias
> V1  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V1  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V1  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V1  OK      investigacion/fichas/flightpath.md — sin incidencias
> V1  OK      investigacion/fichas/good-rebels.md — sin incidencias
> V1  OK      investigacion/fichas/instrument.md — sin incidencias
> V1  OK      investigacion/fichas/lounge-lizard.md — sin incidencias
> V1  OK      investigacion/fichas/major-tom.md — sin incidencias
> V1  OK      investigacion/fichas/media-monks.md — sin incidencias
> V1  OK      investigacion/fichas/monopo.md — sin incidencias
> V1  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V1  OK      investigacion/fichas/redbility.md — sin incidencias
> V1  OK      investigacion/fichas/single-grain.md — sin incidencias
> V1  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V1  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V2  OK      investigacion/fichas/artefact.md — sin incidencias
> V2  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V2  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V2  OK      investigacion/fichas/bravoure.md — sin incidencias
> V2  OK      investigacion/fichas/brolik.md — sin incidencias
> V2  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V2  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V2  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V2  OK      investigacion/fichas/flightpath.md — sin incidencias
> V2  OK      investigacion/fichas/good-rebels.md — sin incidencias
> V2  OK      investigacion/fichas/instrument.md — sin incidencias
> V2  OK      investigacion/fichas/lounge-lizard.md — sin incidencias
> V2  OK      investigacion/fichas/major-tom.md — sin incidencias
> V2  OK      investigacion/fichas/media-monks.md — sin incidencias
> V2  OK      investigacion/fichas/monopo.md — sin incidencias
> V2  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V2  OK      investigacion/fichas/redbility.md — sin incidencias
> V2  OK      investigacion/fichas/single-grain.md — sin incidencias
> V2  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V2  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V2  OK      investigacion/servicios/01-branding.md — sin incidencias
> V2  OK      investigacion/servicios/02-social-media.md — sin incidencias
> V2  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
> V2  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
> V2  OK      investigacion/servicios/05-performance.md — sin incidencias
> V2  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
> V2  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
> V2  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
> V2  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
> V2  OK      investigacion/servicios/10-cro.md — sin incidencias
> V2  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
> V2  OK      investigacion/servicios/resumen.md — sin incidencias
> V2  OK      investigacion/prueba-social.md — sin incidencias
> V2  OK      diseno/patrones-benchmark.md — sin incidencias
> V2  OK      diseno/sistema-web-assets.md — sin incidencias
> V3  OK      investigacion/fichas/artefact.md — sin incidencias
> V3  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V3  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V3  OK      investigacion/fichas/bravoure.md — sin incidencias
> V3  OK      investigacion/fichas/brolik.md — sin incidencias
> V3  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V3  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V3  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V3  OK      investigacion/fichas/flightpath.md — sin incidencias
> V3  OK      investigacion/fichas/good-rebels.md — sin incidencias
> V3  OK      investigacion/fichas/instrument.md — sin incidencias
> V3  OK      investigacion/fichas/lounge-lizard.md — sin incidencias
> V3  OK      investigacion/fichas/major-tom.md — sin incidencias
> V3  OK      investigacion/fichas/media-monks.md — sin incidencias
> V3  OK      investigacion/fichas/monopo.md — sin incidencias
> V3  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V3  OK      investigacion/fichas/redbility.md — sin incidencias
> V3  OK      investigacion/fichas/single-grain.md — sin incidencias
> V3  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V3  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V4  FALLO   diseno/capturas/servicio-detalle-desktop.png — idéntica (mismo SHA-256) a diseno/capturas/servicios-desktop.png
> V4  FALLO   diseno/capturas/servicios-desktop.png — idéntica (mismo SHA-256) a diseno/capturas/servicio-detalle-desktop.png
> V4  FALLO   diseno/capturas/servicio-detalle-mobile-375px.png — idéntica (mismo SHA-256) a diseno/capturas/servicios-mobile-375px.png
> V4  FALLO   diseno/capturas/servicios-mobile-375px.png — idéntica (mismo SHA-256) a diseno/capturas/servicio-detalle-mobile-375px.png
> V5  OK      investigacion/fichas/artefact.md — sin incidencias
> V5  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V5  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V5  OK      investigacion/fichas/bravoure.md — sin incidencias
> V5  OK      investigacion/fichas/brolik.md — sin incidencias
> V5  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V5  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V5  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V5  OK      investigacion/fichas/flightpath.md — sin incidencias
> V5  OK      investigacion/fichas/good-rebels.md — sin incidencias
> V5  OK      investigacion/fichas/instrument.md — sin incidencias
> V5  OK      investigacion/fichas/lounge-lizard.md — sin incidencias
> V5  OK      investigacion/fichas/major-tom.md — sin incidencias
> V5  OK      investigacion/fichas/media-monks.md — sin incidencias
> V5  OK      investigacion/fichas/monopo.md — sin incidencias
> V5  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V5  OK      investigacion/fichas/redbility.md — sin incidencias
> V5  FALLO   investigacion/fichas/single-grain.md — «Performance» marcado Sí sin URL de su página (valor: https://singlegrain.com/)
> V5  FALLO   investigacion/fichas/single-grain.md — «Inteligencia artificial» marcado Sí sin URL de su página (valor: https://singlegrain.com/)
> V5  FALLO   investigacion/fichas/single-grain.md — «SEO y GEO» marcado Sí sin URL de su página (valor: https://singlegrain.com/)
> V5  FALLO   investigacion/fichas/single-grain.md — «CRO» marcado Sí sin URL de su página (valor: https://singlegrain.com/)
> V5  FALLO   investigacion/fichas/single-grain.md — «Datos y automatización» marcado Sí sin URL de su página (valor: https://singlegrain.com/)
> V5  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V5  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V6  OK      investigacion/fichas/artefact.md — sin incidencias
> V6  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V6  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V6  OK      investigacion/fichas/bravoure.md — sin incidencias
> V6  OK      investigacion/fichas/brolik.md — sin incidencias
> V6  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V6  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V6  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V6  OK      investigacion/fichas/flightpath.md — sin incidencias
> V6  OK      investigacion/fichas/good-rebels.md — sin incidencias
> V6  OK      investigacion/fichas/instrument.md — sin incidencias
> V6  OK      investigacion/fichas/lounge-lizard.md — sin incidencias
> V6  OK      investigacion/fichas/major-tom.md — sin incidencias
> V6  OK      investigacion/fichas/media-monks.md — sin incidencias
> V6  OK      investigacion/fichas/monopo.md — sin incidencias
> V6  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V6  OK      investigacion/fichas/redbility.md — sin incidencias
> V6  OK      investigacion/fichas/single-grain.md — sin incidencias
> V6  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V6  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V6  OK      investigacion/servicios/01-branding.md — sin incidencias
> V6  OK      investigacion/servicios/02-social-media.md — sin incidencias
> V6  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
> V6  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
> V6  OK      investigacion/servicios/05-performance.md — sin incidencias
> V6  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
> V6  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
> V6  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
> V6  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
> V6  OK      investigacion/servicios/10-cro.md — sin incidencias
> V6  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
> V6  OK      investigacion/servicios/resumen.md — sin incidencias
> V6  FALLO   investigacion/prueba-social.md — marcador de plantilla «Lorem» en la línea 135
> V6  FALLO   investigacion/prueba-social.md — marcador de plantilla «Lorem» en la línea 136
> V6  FALLO   investigacion/prueba-social.md — marcador de plantilla «Lorem» en la línea 163
> V6  FALLO   diseno/patrones-benchmark.md — marcador de plantilla «Lorem» en la línea 91
> V6  FALLO   diseno/sistema-web-assets.md — marcador de plantilla «Lorem» en la línea 143
> V7  OK      investigacion/fichas — 20 fichas: 10 comparables, 10 referentes/especialistas
> V8  OK      investigacion/fichas/artefact.md — sin incidencias
> V8  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V8  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V8  OK      investigacion/fichas/bravoure.md — sin incidencias
> V8  OK      investigacion/fichas/brolik.md — sin incidencias
> V8  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V8  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V8  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V8  OK      investigacion/fichas/flightpath.md — sin incidencias
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/contacto/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/servicios/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/servicios/data-analytics/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/servicios/experience-design/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/servicios/performance-media/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/servicios/pr-reputation-strategic-influence/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/somos/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/fichas/instrument.md — sin incidencias
> V8  FALLO   investigacion/fichas/lounge-lizard.md — https://www.loungelizard.com/about-us/ → HTTP 404
> V8  FALLO   investigacion/fichas/lounge-lizard.md — https://www.loungelizard.com/contact-us/ → HTTP 404
> V8  FALLO   investigacion/fichas/lounge-lizard.md — https://www.loungelizard.com/services/branding/ → HTTP 404
> V8  FALLO   investigacion/fichas/lounge-lizard.md — https://www.loungelizard.com/services/mobile-apps/ → HTTP 404
> V8  OK      investigacion/fichas/major-tom.md — sin incidencias
> V8  OK      investigacion/fichas/media-monks.md — sin incidencias
> V8  FALLO   investigacion/fichas/monopo.md — https://monopo.london/about → HTTP 404
> V8  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V8  OK      investigacion/fichas/redbility.md — sin incidencias
> V8  OK      investigacion/fichas/single-grain.md — sin incidencias
> V8  FALLO   investigacion/fichas/upraw-media.md — https://www.uprawmedia.com/about → HTTP 404
> V8  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V8  AVISO   investigacion/servicios/01-branding.md — https://www.goodrebels.com/es/servicios/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/servicios/02-social-media.md — https://www.goodrebels.com/es/servicios/pr-reputation-strategic-influence/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/servicios/03-desarrollo-web.md — https://www.goodrebels.com/es/servicios/experience-design/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
> V8  OK      investigacion/servicios/05-performance.md — sin incidencias
> V8  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
> V8  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
> V8  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
> V8  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
> V8  OK      investigacion/servicios/10-cro.md — sin incidencias
> V8  AVISO   investigacion/servicios/11-datos-automatizacion.md — https://www.goodrebels.com/es/servicios/data-analytics/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/servicios/resumen.md — sin incidencias
> V8  FALLO   investigacion/prueba-social.md — https://clutch.co/how-it-works → HTTP 404
> V8  FALLO   investigacion/prueba-social.md — https://www.facebook.com/business/learn/certification → HTTP 400
> V8  OK      diseno/patrones-benchmark.md — sin incidencias
> V8  OK      diseno/sistema-web-assets.md — sin incidencias
>
> 22 FALLOS · 12 AVISOS
> ```
>
> </details>
>
> <details>
> <summary>Salida real contra scripts/pruebas/ (exit 1)</summary>
>
> ```text
> Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-005-verificador-investigacion-250007/scripts/pruebas · V8: con red
> V1  OK      investigacion/fichas/aviso-v5.md — sin incidencias
> V1  OK      investigacion/fichas/correcta.md — sin incidencias
> V1  FALLO   investigacion/fichas/falla-v1.md — País / ciudades: falta o está vacío
> V1  FALLO   investigacion/fichas/falla-v1.md — Fecha de consulta no es AAAA-MM-DD (26/09/2026)
> V1  FALLO   investigacion/fichas/falla-v1.md — Tamaño del equipo: cifra sin fuente (45 personas)
> V1  OK      investigacion/fichas/falla-v2.md — sin incidencias
> V1  OK      investigacion/fichas/falla-v3.md — sin incidencias
> V1  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V1  OK      investigacion/fichas/falla-v5.md — sin incidencias
> V1  OK      investigacion/fichas/falla-v6.md — sin incidencias
> V1  OK      investigacion/fichas/falla-v8.md — sin incidencias
> V2  OK      investigacion/fichas/aviso-v5.md — sin incidencias
> V2  OK      investigacion/fichas/correcta.md — sin incidencias
> V2  OK      investigacion/fichas/falla-v1.md — sin incidencias
> V2  FALLO   investigacion/fichas/falla-v2.md — captura capturas/falla-v2-caso.png: no es PNG ni WebP válido
> V2  FALLO   investigacion/fichas/falla-v2.md — captura citada no existe: capturas/falla-v2-home.png
> V2  FALLO   investigacion/fichas/falla-v2.md — captura capturas/falla-v2-servicios.png: pesa 0 bytes
> V2  OK      investigacion/fichas/falla-v3.md — sin incidencias
> V2  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V2  OK      investigacion/fichas/falla-v5.md — sin incidencias
> V2  OK      investigacion/fichas/falla-v6.md — sin incidencias
> V2  OK      investigacion/fichas/falla-v8.md — sin incidencias
> V3  OK      investigacion/fichas/aviso-v5.md — sin incidencias
> V3  OK      investigacion/fichas/correcta.md — sin incidencias
> V3  OK      investigacion/fichas/falla-v1.md — sin incidencias
> V3  OK      investigacion/fichas/falla-v2.md — sin incidencias
> V3  FALLO   investigacion/fichas/falla-v3.md — faltan capturas propias (caso); se exigen home, servicios y caso
> V3  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V3  OK      investigacion/fichas/falla-v5.md — sin incidencias
> V3  OK      investigacion/fichas/falla-v6.md — sin incidencias
> V3  OK      investigacion/fichas/falla-v8.md — sin incidencias
> V4  FALLO   investigacion/capturas/falla-v4-caso.png — idéntica (mismo SHA-256) a investigacion/capturas/falla-v4-home.png
> V4  FALLO   investigacion/capturas/falla-v4-home.png — idéntica (mismo SHA-256) a investigacion/capturas/falla-v4-caso.png
> V5  AVISO   investigacion/fichas/aviso-v5.md — «Branding»: portada única declarada; respaldar con la captura de la home
> V5  OK      investigacion/fichas/correcta.md — sin incidencias
> V5  OK      investigacion/fichas/falla-v1.md — sin incidencias
> V5  OK      investigacion/fichas/falla-v2.md — sin incidencias
> V5  OK      investigacion/fichas/falla-v3.md — sin incidencias
> V5  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V5  FALLO   investigacion/fichas/falla-v5.md — «Branding» marcado Sí sin URL de su página (valor: https://www.iana.org/)
> V5  FALLO   investigacion/fichas/falla-v5.md — «Social Media» marcado Sí sin URL de su página (valor: vacío)
> V5  OK      investigacion/fichas/falla-v6.md — sin incidencias
> V5  OK      investigacion/fichas/falla-v8.md — sin incidencias
> V6  OK      investigacion/fichas/aviso-v5.md — sin incidencias
> V6  OK      investigacion/fichas/correcta.md — sin incidencias
> V6  OK      investigacion/fichas/falla-v1.md — sin incidencias
> V6  OK      investigacion/fichas/falla-v2.md — sin incidencias
> V6  OK      investigacion/fichas/falla-v3.md — sin incidencias
> V6  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V6  OK      investigacion/fichas/falla-v5.md — sin incidencias
> V6  FALLO   investigacion/fichas/falla-v6.md — marcador de plantilla «TODO» en la línea 14
> V6  FALLO   investigacion/fichas/falla-v6.md — marcador de plantilla «(o «no verificado»)» en la línea 14
> V6  OK      investigacion/fichas/falla-v8.md — sin incidencias
> V7  FALLO   investigacion/fichas — hay 9 fichas principales; se esperan 20
> V7  FALLO   investigacion/fichas — 8 comparables; se esperan 10
> V7  FALLO   investigacion/fichas — 1 referentes/especialistas; se esperan 10
> V8  OK      investigacion/fichas/aviso-v5.md — sin incidencias
> V8  OK      investigacion/fichas/correcta.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v1.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v2.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v3.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v5.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v6.md — sin incidencias
> V8  FALLO   investigacion/fichas/falla-v8.md — https://enlace-inexistente.invalid/servicio → error de red: [Errno 8] nodename nor servname provided, or not known
> V8  FALLO   investigacion/fichas/falla-v8.md — https://example.com/pagina-que-no-existe → HTTP 404
>
> 18 FALLOS · 1 AVISOS
> ```
>
> </details>
>
>
> **[2026-10-08] clia:** buena entrega, y gracias por documentar las decisiones y preguntar en lugar de suponer. Antes de responder lo comprobé por mi cuenta: contra `scripts/pruebas/ --sin-red`, V1 a V7 dan FALLO (16 FALLOS · 1 AVISO, exit 1). Contra los datos reales de la rama de TASK-001 detecta lo que de verdad falta: V7, 0 de 10 comparables; V5, Single Grain; V4, las capturas de diseño duplicadas.
>
> **Respuestas** (añadidas como aclaraciones en [`DECISION-006`](DECISION-006-verificacion-investigacion.md)):
>
> 1. **4xx distintos de 404 y 410 → AVISO**, no FALLO. El 400 de Facebook es un bloqueo antibot, no una página inexistente.
> 2. **V6: un marcador entre comillas invertidas (`` `Lorem` ``) es una cita deliberada y no cuenta.** Uno sin comillas invertidas sigue siendo FALLO. Corregir las líneas de `prueba-social.md` y `diseno/` toca a TASK-003 y TASK-004, no a esta TASK.
> 3. **Tus decisiones de implementación las acepto** (`--raiz`, alcance, rutas, V3, V5, cabeceras de navegador). Dexia tiene la última palabra en su REVIEW.
>
> **Un apunte sobre la línea base:** la corriste sobre `docs/` de `main`, que todavía tiene las fichas antiguas de Ania (con las 10 medianas como comparables). Por eso V7 te dio 10+10 en verde. **El gate de cada TASK se corre en su propia rama.** No es un fallo tuyo, pero dilo en la entrega para que Dexia no lea ese V7 como bueno.
>
> **Para ti, Kia:** implementa las aclaraciones 1 y 2, añade una prueba de cada una en `scripts/pruebas/` (un 400 como AVISO y un `` `Lorem` `` que no falle), vuelve a pegar las salidas y pide el REVIEW a Dexia.

> **[2026-10-08 20:30] kia:** recibo la respuesta de Clia y aplico las aclaraciones. Commit `96bd697` 🔴 (`fix(TASK-005)`).
>
> **Cambios:**
> - **V8:** solo 404 y 410 son FALLO; cualquier otro 4xx es AVISO; 5xx y errores de red siguen siendo FALLO.
> - **V6:** un marcador entre comillas invertidas se trata como cita deliberada y no cuenta; sin comillas, sigue siendo FALLO.
> - **Pruebas nuevas:** `fichas/correcta-cita.md` (`Lorem` y `TODO` entre comillas invertidas: OK en V6) y `fichas/aviso-v8.md` (un 400 de `httpbin.org/status/400`: AVISO en V8). `scripts/README.md` y `scripts/pruebas/README.md` actualizados.
>
> **Sobre la línea base (corrección):** la corrida de la entrega sobre `docs/` era la de mi rama, que parte de `main` y tiene las fichas antiguas de Ania. Mis fichas son idénticas a las de `main` (`git diff main -- docs/investigacion` vacío). Por eso el V7 de 10+10 no mide el corpus nuevo, como dice Clia. El gate de esta TASK no debe leerse sobre `docs/` de esta rama.
>
> **Inestabilidad de V8 (no resuelta, para Clia):** `clutch.co/how-it-works` responde 403 en cinco de seis peticiones con las mismas cabeceras y 404 en la sexta. Con el 404 el gate falla por azar. Propuesta: reintentar una vez antes de dar FALLO en 404; no lo he implementado porque cambia una regla que Clia acaba de fijar.
>
> **Salidas reales, con red, tras el fix:**
> - Gate sobre `docs/`: **18 FALLOS · 13 AVISOS**, código 1. Cambian respecto a la entrega: V6 ya no marca los `Lorem` de `diseno/` (son citas entre comillas); V8 pasa el 400 de Facebook a AVISO.
> - `scripts/pruebas/`: **17 FALLOS · 2 AVISOS**, código 1. Cada V (V1 a V8) tiene al menos un FALLO. `correcta.md` y `correcta-cita.md` pasan en V6, y `aviso-v8.md` da AVISO en V8.
>
> **Petición:** REVIEW de Dexia sobre `bde0aaa`, `7e0dda5` y `96bd697`. Sign-off de Clia después. Estado sigue en `EN_REVISION`.
>
> <details>
> <summary>Salida real del gate, con red, sobre docs/ (exit 1)</summary>
>
> ```text
> Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-005-verificador-investigacion-250007/docs · V8: con red
> V1  OK      investigacion/fichas/artefact.md — sin incidencias
> V1  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V1  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V1  OK      investigacion/fichas/bravoure.md — sin incidencias
> V1  OK      investigacion/fichas/brolik.md — sin incidencias
> V1  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V1  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V1  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V1  OK      investigacion/fichas/flightpath.md — sin incidencias
> V1  OK      investigacion/fichas/good-rebels.md — sin incidencias
> V1  OK      investigacion/fichas/instrument.md — sin incidencias
> V1  OK      investigacion/fichas/lounge-lizard.md — sin incidencias
> V1  OK      investigacion/fichas/major-tom.md — sin incidencias
> V1  OK      investigacion/fichas/media-monks.md — sin incidencias
> V1  OK      investigacion/fichas/monopo.md — sin incidencias
> V1  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V1  OK      investigacion/fichas/redbility.md — sin incidencias
> V1  OK      investigacion/fichas/single-grain.md — sin incidencias
> V1  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V1  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V2  OK      investigacion/fichas/artefact.md — sin incidencias
> V2  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V2  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V2  OK      investigacion/fichas/bravoure.md — sin incidencias
> V2  OK      investigacion/fichas/brolik.md — sin incidencias
> V2  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V2  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V2  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V2  OK      investigacion/fichas/flightpath.md — sin incidencias
> V2  OK      investigacion/fichas/good-rebels.md — sin incidencias
> V2  OK      investigacion/fichas/instrument.md — sin incidencias
> V2  OK      investigacion/fichas/lounge-lizard.md — sin incidencias
> V2  OK      investigacion/fichas/major-tom.md — sin incidencias
> V2  OK      investigacion/fichas/media-monks.md — sin incidencias
> V2  OK      investigacion/fichas/monopo.md — sin incidencias
> V2  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V2  OK      investigacion/fichas/redbility.md — sin incidencias
> V2  OK      investigacion/fichas/single-grain.md — sin incidencias
> V2  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V2  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V2  OK      investigacion/servicios/01-branding.md — sin incidencias
> V2  OK      investigacion/servicios/02-social-media.md — sin incidencias
> V2  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
> V2  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
> V2  OK      investigacion/servicios/05-performance.md — sin incidencias
> V2  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
> V2  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
> V2  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
> V2  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
> V2  OK      investigacion/servicios/10-cro.md — sin incidencias
> V2  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
> V2  OK      investigacion/servicios/resumen.md — sin incidencias
> V2  OK      investigacion/prueba-social.md — sin incidencias
> V2  OK      diseno/patrones-benchmark.md — sin incidencias
> V2  OK      diseno/sistema-web-assets.md — sin incidencias
> V3  OK      investigacion/fichas/artefact.md — sin incidencias
> V3  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V3  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V3  OK      investigacion/fichas/bravoure.md — sin incidencias
> V3  OK      investigacion/fichas/brolik.md — sin incidencias
> V3  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V3  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V3  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V3  OK      investigacion/fichas/flightpath.md — sin incidencias
> V3  OK      investigacion/fichas/good-rebels.md — sin incidencias
> V3  OK      investigacion/fichas/instrument.md — sin incidencias
> V3  OK      investigacion/fichas/lounge-lizard.md — sin incidencias
> V3  OK      investigacion/fichas/major-tom.md — sin incidencias
> V3  OK      investigacion/fichas/media-monks.md — sin incidencias
> V3  OK      investigacion/fichas/monopo.md — sin incidencias
> V3  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V3  OK      investigacion/fichas/redbility.md — sin incidencias
> V3  OK      investigacion/fichas/single-grain.md — sin incidencias
> V3  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V3  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V4  FALLO   diseno/capturas/servicio-detalle-desktop.png — idéntica (mismo SHA-256) a diseno/capturas/servicios-desktop.png
> V4  FALLO   diseno/capturas/servicios-desktop.png — idéntica (mismo SHA-256) a diseno/capturas/servicio-detalle-desktop.png
> V4  FALLO   diseno/capturas/servicio-detalle-mobile-375px.png — idéntica (mismo SHA-256) a diseno/capturas/servicios-mobile-375px.png
> V4  FALLO   diseno/capturas/servicios-mobile-375px.png — idéntica (mismo SHA-256) a diseno/capturas/servicio-detalle-mobile-375px.png
> V5  OK      investigacion/fichas/artefact.md — sin incidencias
> V5  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V5  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V5  OK      investigacion/fichas/bravoure.md — sin incidencias
> V5  OK      investigacion/fichas/brolik.md — sin incidencias
> V5  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V5  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V5  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V5  OK      investigacion/fichas/flightpath.md — sin incidencias
> V5  OK      investigacion/fichas/good-rebels.md — sin incidencias
> V5  OK      investigacion/fichas/instrument.md — sin incidencias
> V5  OK      investigacion/fichas/lounge-lizard.md — sin incidencias
> V5  OK      investigacion/fichas/major-tom.md — sin incidencias
> V5  OK      investigacion/fichas/media-monks.md — sin incidencias
> V5  OK      investigacion/fichas/monopo.md — sin incidencias
> V5  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V5  OK      investigacion/fichas/redbility.md — sin incidencias
> V5  FALLO   investigacion/fichas/single-grain.md — «Performance» marcado Sí sin URL de su página (valor: https://singlegrain.com/)
> V5  FALLO   investigacion/fichas/single-grain.md — «Inteligencia artificial» marcado Sí sin URL de su página (valor: https://singlegrain.com/)
> V5  FALLO   investigacion/fichas/single-grain.md — «SEO y GEO» marcado Sí sin URL de su página (valor: https://singlegrain.com/)
> V5  FALLO   investigacion/fichas/single-grain.md — «CRO» marcado Sí sin URL de su página (valor: https://singlegrain.com/)
> V5  FALLO   investigacion/fichas/single-grain.md — «Datos y automatización» marcado Sí sin URL de su página (valor: https://singlegrain.com/)
> V5  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V5  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V6  OK      investigacion/fichas/artefact.md — sin incidencias
> V6  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V6  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V6  OK      investigacion/fichas/bravoure.md — sin incidencias
> V6  OK      investigacion/fichas/brolik.md — sin incidencias
> V6  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V6  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V6  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V6  OK      investigacion/fichas/flightpath.md — sin incidencias
> V6  OK      investigacion/fichas/good-rebels.md — sin incidencias
> V6  OK      investigacion/fichas/instrument.md — sin incidencias
> V6  OK      investigacion/fichas/lounge-lizard.md — sin incidencias
> V6  OK      investigacion/fichas/major-tom.md — sin incidencias
> V6  OK      investigacion/fichas/media-monks.md — sin incidencias
> V6  OK      investigacion/fichas/monopo.md — sin incidencias
> V6  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V6  OK      investigacion/fichas/redbility.md — sin incidencias
> V6  OK      investigacion/fichas/single-grain.md — sin incidencias
> V6  OK      investigacion/fichas/upraw-media.md — sin incidencias
> V6  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V6  OK      investigacion/servicios/01-branding.md — sin incidencias
> V6  OK      investigacion/servicios/02-social-media.md — sin incidencias
> V6  OK      investigacion/servicios/03-desarrollo-web.md — sin incidencias
> V6  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
> V6  OK      investigacion/servicios/05-performance.md — sin incidencias
> V6  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
> V6  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
> V6  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
> V6  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
> V6  OK      investigacion/servicios/10-cro.md — sin incidencias
> V6  OK      investigacion/servicios/11-datos-automatizacion.md — sin incidencias
> V6  OK      investigacion/servicios/resumen.md — sin incidencias
> V6  FALLO   investigacion/prueba-social.md — marcador de plantilla «Lorem» en la línea 135
> V6  FALLO   investigacion/prueba-social.md — marcador de plantilla «Lorem» en la línea 136
> V6  OK      diseno/patrones-benchmark.md — sin incidencias
> V6  OK      diseno/sistema-web-assets.md — sin incidencias
> V7  OK      investigacion/fichas — 20 fichas: 10 comparables, 10 referentes/especialistas
> V8  OK      investigacion/fichas/artefact.md — sin incidencias
> V8  OK      investigacion/fichas/atomic-digital-marketing.md — sin incidencias
> V8  OK      investigacion/fichas/blueorange-digital.md — sin incidencias
> V8  OK      investigacion/fichas/bravoure.md — sin incidencias
> V8  OK      investigacion/fichas/brolik.md — sin incidencias
> V8  OK      investigacion/fichas/code-and-theory.md — sin incidencias
> V8  OK      investigacion/fichas/dogstudio.md — sin incidencias
> V8  OK      investigacion/fichas/edenspiekermann.md — sin incidencias
> V8  OK      investigacion/fichas/flightpath.md — sin incidencias
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/contacto/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/servicios/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/servicios/data-analytics/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/servicios/experience-design/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/servicios/performance-media/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/servicios/pr-reputation-strategic-influence/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/fichas/good-rebels.md — https://www.goodrebels.com/es/somos/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/fichas/instrument.md — sin incidencias
> V8  FALLO   investigacion/fichas/lounge-lizard.md — https://www.loungelizard.com/about-us/ → HTTP 404
> V8  FALLO   investigacion/fichas/lounge-lizard.md — https://www.loungelizard.com/contact-us/ → HTTP 404
> V8  FALLO   investigacion/fichas/lounge-lizard.md — https://www.loungelizard.com/services/branding/ → HTTP 404
> V8  FALLO   investigacion/fichas/lounge-lizard.md — https://www.loungelizard.com/services/mobile-apps/ → HTTP 404
> V8  OK      investigacion/fichas/major-tom.md — sin incidencias
> V8  OK      investigacion/fichas/media-monks.md — sin incidencias
> V8  FALLO   investigacion/fichas/monopo.md — https://monopo.london/about → HTTP 404
> V8  OK      investigacion/fichas/neo-consulting.md — sin incidencias
> V8  OK      investigacion/fichas/redbility.md — sin incidencias
> V8  OK      investigacion/fichas/single-grain.md — sin incidencias
> V8  FALLO   investigacion/fichas/upraw-media.md — https://www.uprawmedia.com/about → HTTP 404
> V8  OK      investigacion/fichas/work-and-co.md — sin incidencias
> V8  AVISO   investigacion/servicios/01-branding.md — https://www.goodrebels.com/es/servicios/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/servicios/02-social-media.md — https://www.goodrebels.com/es/servicios/pr-reputation-strategic-influence/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  AVISO   investigacion/servicios/03-desarrollo-web.md — https://www.goodrebels.com/es/servicios/experience-design/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/servicios/04-campanas-publicitarias.md — sin incidencias
> V8  OK      investigacion/servicios/05-performance.md — sin incidencias
> V8  OK      investigacion/servicios/06-desarrollo-apps-software.md — sin incidencias
> V8  OK      investigacion/servicios/07-fotografia-video.md — sin incidencias
> V8  OK      investigacion/servicios/08-inteligencia-artificial.md — sin incidencias
> V8  OK      investigacion/servicios/09-seo-geo.md — sin incidencias
> V8  OK      investigacion/servicios/10-cro.md — sin incidencias
> V8  AVISO   investigacion/servicios/11-datos-automatizacion.md — https://www.goodrebels.com/es/servicios/data-analytics/ → HTTP 403 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/servicios/resumen.md — sin incidencias
> V8  FALLO   investigacion/prueba-social.md — https://clutch.co/how-it-works → HTTP 404
> V8  AVISO   investigacion/prueba-social.md — https://www.facebook.com/business/learn/certification → HTTP 400 (bloqueo antibot o de región): respaldar con captura
> V8  OK      diseno/patrones-benchmark.md — sin incidencias
> V8  OK      diseno/sistema-web-assets.md — sin incidencias
>
> 18 FALLOS · 13 AVISOS
> ```
>
> </details>
>
> <details>
> <summary>Salida real contra scripts/pruebas/ (exit 1)</summary>
>
> ```text
> Verificación de la investigación · raíz: /Users/miguel/servers/pharmaco-assets/.claude/worktrees/task-005-verificador-investigacion-250007/scripts/pruebas · V8: con red
> V1  OK      investigacion/fichas/aviso-v5.md — sin incidencias
> V1  OK      investigacion/fichas/aviso-v8.md — sin incidencias
> V1  OK      investigacion/fichas/correcta-cita.md — sin incidencias
> V1  OK      investigacion/fichas/correcta.md — sin incidencias
> V1  FALLO   investigacion/fichas/falla-v1.md — País / ciudades: falta o está vacío
> V1  FALLO   investigacion/fichas/falla-v1.md — Fecha de consulta no es AAAA-MM-DD (26/09/2026)
> V1  FALLO   investigacion/fichas/falla-v1.md — Tamaño del equipo: cifra sin fuente (45 personas)
> V1  OK      investigacion/fichas/falla-v2.md — sin incidencias
> V1  OK      investigacion/fichas/falla-v3.md — sin incidencias
> V1  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V1  OK      investigacion/fichas/falla-v5.md — sin incidencias
> V1  OK      investigacion/fichas/falla-v6.md — sin incidencias
> V1  OK      investigacion/fichas/falla-v8.md — sin incidencias
> V2  OK      investigacion/fichas/aviso-v5.md — sin incidencias
> V2  OK      investigacion/fichas/aviso-v8.md — sin incidencias
> V2  OK      investigacion/fichas/correcta-cita.md — sin incidencias
> V2  OK      investigacion/fichas/correcta.md — sin incidencias
> V2  OK      investigacion/fichas/falla-v1.md — sin incidencias
> V2  FALLO   investigacion/fichas/falla-v2.md — captura capturas/falla-v2-caso.png: no es PNG ni WebP válido
> V2  FALLO   investigacion/fichas/falla-v2.md — captura citada no existe: capturas/falla-v2-home.png
> V2  FALLO   investigacion/fichas/falla-v2.md — captura capturas/falla-v2-servicios.png: pesa 0 bytes
> V2  OK      investigacion/fichas/falla-v3.md — sin incidencias
> V2  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V2  OK      investigacion/fichas/falla-v5.md — sin incidencias
> V2  OK      investigacion/fichas/falla-v6.md — sin incidencias
> V2  OK      investigacion/fichas/falla-v8.md — sin incidencias
> V3  OK      investigacion/fichas/aviso-v5.md — sin incidencias
> V3  OK      investigacion/fichas/aviso-v8.md — sin incidencias
> V3  OK      investigacion/fichas/correcta-cita.md — sin incidencias
> V3  OK      investigacion/fichas/correcta.md — sin incidencias
> V3  OK      investigacion/fichas/falla-v1.md — sin incidencias
> V3  OK      investigacion/fichas/falla-v2.md — sin incidencias
> V3  FALLO   investigacion/fichas/falla-v3.md — faltan capturas propias (caso); se exigen home, servicios y caso
> V3  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V3  OK      investigacion/fichas/falla-v5.md — sin incidencias
> V3  OK      investigacion/fichas/falla-v6.md — sin incidencias
> V3  OK      investigacion/fichas/falla-v8.md — sin incidencias
> V4  FALLO   investigacion/capturas/falla-v4-caso.png — idéntica (mismo SHA-256) a investigacion/capturas/falla-v4-home.png
> V4  FALLO   investigacion/capturas/falla-v4-home.png — idéntica (mismo SHA-256) a investigacion/capturas/falla-v4-caso.png
> V5  AVISO   investigacion/fichas/aviso-v5.md — «Branding»: portada única declarada; respaldar con la captura de la home
> V5  OK      investigacion/fichas/aviso-v8.md — sin incidencias
> V5  OK      investigacion/fichas/correcta-cita.md — sin incidencias
> V5  OK      investigacion/fichas/correcta.md — sin incidencias
> V5  OK      investigacion/fichas/falla-v1.md — sin incidencias
> V5  OK      investigacion/fichas/falla-v2.md — sin incidencias
> V5  OK      investigacion/fichas/falla-v3.md — sin incidencias
> V5  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V5  FALLO   investigacion/fichas/falla-v5.md — «Branding» marcado Sí sin URL de su página (valor: https://www.iana.org/)
> V5  FALLO   investigacion/fichas/falla-v5.md — «Social Media» marcado Sí sin URL de su página (valor: vacío)
> V5  OK      investigacion/fichas/falla-v6.md — sin incidencias
> V5  OK      investigacion/fichas/falla-v8.md — sin incidencias
> V6  OK      investigacion/fichas/aviso-v5.md — sin incidencias
> V6  OK      investigacion/fichas/aviso-v8.md — sin incidencias
> V6  OK      investigacion/fichas/correcta-cita.md — sin incidencias
> V6  OK      investigacion/fichas/correcta.md — sin incidencias
> V6  OK      investigacion/fichas/falla-v1.md — sin incidencias
> V6  OK      investigacion/fichas/falla-v2.md — sin incidencias
> V6  OK      investigacion/fichas/falla-v3.md — sin incidencias
> V6  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V6  OK      investigacion/fichas/falla-v5.md — sin incidencias
> V6  FALLO   investigacion/fichas/falla-v6.md — marcador de plantilla «TODO» en la línea 14
> V6  FALLO   investigacion/fichas/falla-v6.md — marcador de plantilla «(o «no verificado»)» en la línea 14
> V6  OK      investigacion/fichas/falla-v8.md — sin incidencias
> V7  FALLO   investigacion/fichas — hay 11 fichas principales; se esperan 20
> V7  FALLO   investigacion/fichas — 1 referentes/especialistas; se esperan 10
> V8  OK      investigacion/fichas/aviso-v5.md — sin incidencias
> V8  AVISO   investigacion/fichas/aviso-v8.md — https://httpbin.org/status/400 → HTTP 400 (bloqueo antibot o de región): respaldar con captura
> V8  OK      investigacion/fichas/correcta-cita.md — sin incidencias
> V8  OK      investigacion/fichas/correcta.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v1.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v2.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v3.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v4.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v5.md — sin incidencias
> V8  OK      investigacion/fichas/falla-v6.md — sin incidencias
> V8  FALLO   investigacion/fichas/falla-v8.md — https://enlace-inexistente.invalid/servicio → error de red: [Errno 8] nodename nor servname provided, or not known
> V8  FALLO   investigacion/fichas/falla-v8.md — https://example.com/pagina-que-no-existe → HTTP 404
>
> 17 FALLOS · 2 AVISOS
> ```
>
> </details>
>
