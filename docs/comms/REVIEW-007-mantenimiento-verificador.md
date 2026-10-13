---
tipo: REVIEW
id: REVIEW-007
titulo: Mantenimiento del verificador — webs lentas y URL no ASCII
de: dexia
para: kia
cc: [clia, miguel]
estado: RECHAZADO
task: TASK-007
rama: feat/TASK-007-mantenimiento-verificador
criticidad: "🔴"
creado: 2026-10-13
actualizado: 2026-10-13
---

# REVIEW-007 — Mantenimiento del verificador

## Alcance revisado

Rama `feat/TASK-007-mantenimiento-verificador` hasta `8c95400`; implementación de Kia en `78bbfb0`. Revisé el cambio del script, las 16 regresiones, la documentación y las salidas completas pegadas en TASK-007. Criterios: TASK-007, DECISION-006 y AGENTS.md.

## Veredicto

❌ **RECHAZADO.** Los dos hallazgos siguientes afectan al gate 🔴 y requieren nueva entrega y REVIEW antes del sign-off de Clia.

## Hallazgos

| # | Archivo:línea | Severidad | Hallazgo |
| --- | --- | --- | --- |
| 1 | `scripts/verificar-investigacion.py:479` | 🔴 | `comprobar_todas` llama `host_de` antes de que `comprobar_url` pueda convertir una URL mal formada en FALLO. Una URL con `[` sin cerrar hace que `urlsplit` lance `ValueError` y aborta toda la V8, sin salida de gate. Reproducción: `comprobar_todas(['https://[malo/ruta'], 1)` → `ValueError: Invalid IPv6 URL`. Validar/registrar cada URL antes de agrupar por dominio; una inválida debe figurar como FALLO con su motivo y no impedir comprobar las demás. Añadir regresión del lote mixto. |
| 2 | `scripts/verificar-investigacion.py:402` | 🔴 | `urlopen(..., timeout=30)` fija el tiempo de operaciones de socket, no un límite de 30 s para el intento completo. Una cadena de redirecciones puede tardar más y acabar en OK. Con un servidor local que retrasa 0,7 s cada respuesta y redirige dos veces, `TIMEOUT_SEGUNDOS=1` dio `('OK', 'responde', False)` en 2,14 s. Por tanto no se cumple el máximo por intento pedido. Aplicar un plazo real al intento completo, incluyendo redirecciones, y probarlo con respuestas locales escalonadas. |

## Evidencia de verificación

Ejecuté las regresiones existentes:

```text
$ python3 -m unittest scripts/pruebas/test_verificador_red.py
Ran 16 tests in 19.186s
OK
```

Reproducciones puntuales, sin modificar entregables:

```text
comprobar_todas(['https://[malo/ruta'], 1)
ValueError: Invalid IPv6 URL

Servidor HTTP local: /0 → /1 → /2; cada respuesta se retrasa 0,7 s.
TIMEOUT_SEGUNDOS = 1
comprobar_url('http://127.0.0.1:<puerto>/0')
('OK', 'responde', False) duration_s= 2.14
```

En TASK-007 constan las salidas íntegras de Kia: `scripts/pruebas/` antes y después, `43 FALLOS · 2 AVISOS` en ambos; dos ejecuciones con red sobre `docs/`, `0 FALLOS · 29 AVISOS` en ambas. Esas salidas no ejercitan los dos casos anteriores. No ejecuté el gate completo de `pnpm` en esta ronda: la revisión queda rechazada por los defectos reproducidos.

## Corrección requerida

Kia: corregir ambos hallazgos, añadir regresiones que fallen antes de la corrección y pasen después, ejecutar la verificación de AGENTS.md y pegar la salida real en TASK-007. Solicitar otra ronda sobre el commit corregido. Clia: sign-off 🔴 pendiente del REVIEW ✅.

## Sign-off del CTO

- [ ] Clia (CTO): pendiente.

## 💬 Hilo

> **[2026-10-13 06:22] dexia:** primera ronda sobre `78bbfb0` y evidencia de `2b81608`: ❌ RECHAZADO por los dos hallazgos 🔴 documentados arriba. Los 16 tests existentes pasan, pero una URL mal formada aborta V8 y las redirecciones pueden superar el límite por intento. Pendiente corrección, nuevas regresiones y verificación completa antes del sign-off.
