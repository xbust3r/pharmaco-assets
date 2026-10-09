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
