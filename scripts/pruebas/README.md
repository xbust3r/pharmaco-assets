# Pruebas del verificador

Fichas y capturas **ficticias** para comprobar que `verificar-investigacion.py` detecta cada fallo. No describen a ninguna agencia real: los textos son de prueba, las capturas son PNG sintéticos de 4×4 píxeles y los enlaces apuntan a `example.com` y a IANA (siempre vivos), o a dominios que no existen (`.invalid`, que siempre falla el DNS).

Un verificador que nunca se ha visto fallar no está probado. Por eso cada caso falla por **una sola causa**, salvo la ficha correcta.

```bash
python3 scripts/verificar-investigacion.py --raiz scripts/pruebas
```

## Casos

| Archivo | Qué hace | Resultado esperado |
| --- | --- | --- |
| `fichas/correcta.md` | Ficha completa, capturas propias, enlaces vivos | OK en V1, V2, V3, V5, V6 y V8 |
| `fichas/falla-v1.md` | País vacío, fecha `26/09/2026`, tamaño `45 personas` sin fuente | FALLO V1 (3 líneas) |
| `fichas/falla-v2.md` | Captura `home` inexistente, `servicios` de 0 bytes, `caso` con texto plano | FALLO V2 (3 líneas) |
| `fichas/falla-v3.md` | Solo cita `home` y `servicios`, falta `caso` | FALLO V3 |
| `fichas/falla-v4.md` | `caso` es byte a byte igual que `home` | FALLO V4 (en ambos archivos) |
| `fichas/falla-v5.md` | Dos filas «Sí»: una con la portada como URL, otra sin URL | FALLO V5 (2 líneas) |
| `fichas/aviso-v5.md` | Fila «Sí» que declara `portada única` | AVISO V5 |
| `fichas/falla-v6.md` | Contiene `TODO` y `(o «no verificado»)` sin comillas invertidas | FALLO V6 (2 líneas) |
| `fichas/correcta-cita.md` | `Lorem` y `TODO` entre comillas invertidas, como cita deliberada | OK en V6 |
| `fichas/falla-v8.md` | Una URL da 404 y otra no resuelve el DNS | FALLO V8 (2 líneas) |
| `fichas/aviso-v8.md` | Una URL da 400 (`httpbin.org/status/400`, endpoint de pruebas) | AVISO V8 |
| — | 11 fichas en total y 1 referente o especialista | FALLO V7 (composición) |

Con `--sin-red` la V8 aparece como `OMITIDA` y no cuenta como FALLO: por eso el gate se pega **con red**.

Las capturas de `capturas/` se han generado con un script de biblioteca estándar; son bytes válidos de PNG, de color fijo por nombre.
