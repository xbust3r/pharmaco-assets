---
tipo: DECISION
id: DECISION-006
titulo: La investigación tiene su propia verificación completa, mecánica y pegable
de: clia
para: [ania, dexia]
cc: [miguel]
estado: EFECTIVA
estrategica: false
relacionado: [AGENTS.md, TASK-001, TASK-002, TASK-003, TASK-004, TASK-005, REVIEW-001]
creado: 2026-10-08
actualizado: 2026-10-08
---

# DECISION-006 — Verificación completa de la investigación

## Contexto

En la séptima ronda de `REVIEW-001`, Dexia exige para el cierre de F1 «la salida real de la verificación que se defina en `AGENTS.md`». Esa verificación está vacía porque es la del **código** y depende del stack (`RFC-001`). Así, **la investigación no tenía forma de pasar su gate.** El fallo es de Clia, que no la definió al abrir la etapa.

## Decisión

La investigación tiene **su propia verificación completa**: un script que corre Ania, cuya salida real se pega en el hilo y que da paso a cerrar TASK-001 a TASK-004. Se añade a `AGENTS.md` y la implementa Ania en `TASK-005`.

```bash
python3 scripts/verificar-investigacion.py
```

### Qué comprueba (FALLO = bloquea el gate)

| # | Comprobación | FALLO si… |
| --- | --- | --- |
| V1 | **Campos de la ficha.** En cada `fichas/*.md` (excluido `anexo-medianas/`), las filas URL, País / ciudades, Bloque · perfil, Tamaño del equipo, Fecha de consulta y Capturas | Alguna falta o está vacía. La fecha no es `AAAA-MM-DD`. El tamaño es una cifra sin fuente (vale «no publicado» o un rango con fuente) |
| V2 | **Capturas existen** | Una captura citada en fichas, servicios, prueba social o diseño no existe, pesa 0 bytes o no es PNG/WebP válido |
| V3 | **Capturas mínimas por agencia** | Una ficha no cita al menos 3 capturas propias (home, servicios, caso) |
| V4 | **Capturas no duplicadas** | Dos archivos de captura tienen el mismo SHA-256 (caso Monopo de REVIEW-001) |
| V5 | **Servicio enlazado a su página** | Una fila «Sí» de «Frente al catálogo de Pharmaco» no tiene URL, o la URL es la portada (ruta `/` o vacía). **Excepción:** si la agencia solo describe sus servicios en la portada, la fila lo declara con el texto `portada única` y queda como AVISO |
| V6 | **Plantilla rellena** | Quedan marcadores de plantilla: `{`, `AAAA-MM-DD`, `Lorem`, `TODO`, `(o «no verificado»)` |
| V7 | **Composición de la muestra** | No hay 20 fichas principales, o los perfiles no suman 10 comparables + 10 referentes/especialistas |
| V8 | **Enlaces vivos** | Una URL de fichas o informes devuelve 404, 410, 5xx o error de DNS o conexión |

### Qué avisa (AVISO = no bloquea, pero se explica en el hilo)

- V5 con `portada única`.
- V8 con 401, 403 o 429 (bloqueo antibot o de región): se anota y se respalda con la captura.
- V8 con redirección a otro dominio.

### Qué NO comprueba, y por qué sigue habiendo revisión humana

El script comprueba **forma y existencia**, no **verdad**: no sabe si una cita es literal, si la captura muestra lo que dice la ficha ni si un conteo está bien interpretado. Eso sigue siendo de **Dexia** (REVIEW) y de **Clia** (auditoría por muestreo, 5 fichas al azar). **La verificación en verde es necesaria, no suficiente.**

### Aclaraciones (2026-10-08, a pregunta de Kia en TASK-005)

1. **V8 y otros 4xx.** Solo **404 y 410** son FALLO. Cualquier otro 4xx (400, 401, 403, 405, 429…) es **AVISO**: en la práctica son bloqueos antibot o de región, no páginas inexistentes. Como todo AVISO, se explica en el hilo y se respalda con la captura.
2. **V6 y marcadores citados.** Un marcador escrito entre comillas invertidas (`` `Lorem` ``) se considera **cita deliberada** y no cuenta. Un marcador sin comillas invertidas sigue siendo FALLO. Así, escribir sobre el «Lorem ipsum» de un sitio ajeno exige marcarlo a propósito, y un hueco de plantilla olvidado se sigue detectando.
3. **Implementación de Kia aceptada por Clia** en lo que DECISION-006 no fijaba: `--raiz`, el alcance de documentos, la resolución de rutas de capturas, V3 con las tres clases (home, servicios, caso), V5 con URL sin `http` como FALLO y V8 con cabeceras de navegador. Queda sujeta al REVIEW de Dexia.

### Salida

Una línea por comprobación y archivo con `OK`, `AVISO` o `FALLO` y el motivo. Al final, el resumen `N FALLOS · M AVISOS`. El código de salida es 1 si hay algún fallo. La opción `--sin-red` salta V8 para pruebas locales, pero **para el gate se pega la salida con red.**

## Consecuencias

- `AGENTS.md` gana la sección «Verificación de la investigación». La del código sigue pendiente de `RFC-001`.
- **Nace `TASK-005`** (Ania, 🔴: es un verificador del propio gate). No bloquea empezar F1: Ania puede fichar en paralelo. Sí bloquea **cerrar** F1.
- TASK-001 a TASK-004 añaden a sus criterios de aceptación: «`verificar-investigacion.py` con 0 FALLOS, salida pegada».

## Vigencia

Efectiva desde el 2026-10-08, con el visto bueno de Miguel.

## 💬 Hilo

> **[2026-10-08] miguel:** (transcrito por Clia) sí, define la verificación.
>
> **[2026-10-08] clia:** emitida. Diseñé las comprobaciones a partir de los fallos reales de REVIEW-001 (capturas duplicadas, servicios enlazados a la portada, campos vacíos, cifras de tamaño sin fuente), para que el script atrape de forma mecánica lo que hasta ahora Dexia tenía que cazar a mano.
>
> **[2026-10-10 15:05] clia:** **enmienda 4 — V8 ante hosts con antibot intermitente.** Hecho en TASK-005: `clutch.co/how-it-works` responde 403 o 404 sin patrón (6 de 8 y 2 de 8), y el reintento no lo estabiliza. Las fichas de TASK-001 citan muchos perfiles de Clutch, así que cambiar una URL no basta. Regla:
> - Si **algún intento** sobre una URL devuelve 401, 403 o 429, el resultado de esa URL es **AVISO**, aunque otros intentos den 404.
> - Si en la misma ejecución **otra URL del mismo host** devolvió 401, 403 o 429, un 404 en ese host es **AVISO** («host con antibot; 404 no concluyente»).
> - Fuera de esos casos, 404, 410, 5xx o error de red en los 3 intentos sigue siendo FALLO.
> - Como todo AVISO, se explica en el hilo y se respalda con la captura. Se pierde detección automática de perfiles borrados en hosts con antibot; la cubren la captura y el REVIEW de Dexia.
> - **Riesgo residual que se acepta:** un host citado en una sola URL que responda 404 en los 3 intentos sin un solo 403 sigue pudiendo variar. Si pasa, se anota en el hilo.
>
> **[2026-10-10 15:09] clia:** **enmienda 5 — V8 ante páginas de desafío servidas con 2xx.** Hecho, reproducido por Clia: `https://www.goodrebels.com/` responde `HTTP/2 202` con `sg-captcha: challenge` y 168 bytes. Antes daba 403 (AVISO), ahora V8 lo cuenta como OK: unos 12 AVISOS se volvieron falsos OK. Regla:
> - Un **202** a un GET de página es **AVISO** («respuesta de desafío o diferida, no la página»).
> - Un **2xx con cabecera de desafío conocida** es **AVISO**: `sg-captcha`, `cf-mitigated: challenge` o `x-amzn-waf-action`. La lista se ajusta en este hilo cuando aparezca otro proveedor.
> - Esos AVISOS cuentan como señal de antibot del host para la enmienda 4.
> - No se usa el tamaño del cuerpo como criterio, por frágil.
>
> **[2026-10-10 15:12] clia:** **enmienda 6 — alcance de V2.** Tres rondas de REVIEW-005 encontraron falsos OK de V2 con archivos fabricados a mano (VP8 vacío, filtro PNG 5, IEND con datos, bytes tras IEND, IHDR duplicado, VP8L sin datos). Todos son reales, pero un validador completo de PNG y WebP no es el objetivo. Las capturas salen de Chrome headless, y V2 existe para cazar archivos **truncados, vacíos, de marcador o que no son una captura**. Regla:
> 1. **Estructura del contenedor, cerrada:** firma; IHDR único y primero; CRC de cada fragmento; IEND de longitud 0 y **último byte del archivo**; para WebP, longitud RIFF exacta; VP8, VP8L o ANMF con datos de imagen más allá de su cabecera.
> 2. **Datos de imagen presentes:** el PNG descomprime a la longitud esperada con filtros 0 a 4 (ya implementado). El WebP lleva un bitstream no vacío.
> 3. **Tamaño mínimo de captura, nuevo:** **ancho ≥ 320 px y alto ≥ 200 px.** Una captura de página más pequeña no es una captura: es FALLO.
> 4. **Fuera de alcance, riesgo residual aceptado:** la decodificación completa del bitstream (datos comprimidos corruptos con estructura válida). Eso se cubre mirando las capturas en el REVIEW. Dexia puede abrir un RFC si considera que el riesgo no es aceptable.
