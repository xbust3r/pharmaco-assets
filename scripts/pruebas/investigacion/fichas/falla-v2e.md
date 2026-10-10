# Agencia de prueba: falla-v2e (ficticia)

| Campo | Valor | Fuente |
| --- | --- | --- |
| URL | https://example.com/ | https://example.com/ |
| País / ciudades | Ficticio (prueba) | https://example.com/ |
| Bloque · perfil | Europa · comparable | — |
| Tamaño del equipo | «no publicado» | https://example.com/ |
| Año de fundación | no publicado | https://example.com/ |
| Fecha de consulta | 2026-10-08 | — |
| Capturas | `capturas/falla-v2e-home.png`, `capturas/falla-v2e-servicios.png`, `capturas/falla-v2e-caso.png` | — |

## Propuesta de valor
Ficha de prueba ficticia. Matriz de REVIEW-005 (segunda ronda): cada captura adicional tiene un único defecto, y cada uno debe dar un FALLO V2 con su motivo. Las tres capturas propias son válidas.

## Capturas adicionales con un defecto cada una
- WebP VP8 sin fotograma clave: `capturas/falla-v2e-vp8-no-clave.webp`
- WebP VP8 sin código de inicio: `capturas/falla-v2e-vp8-codigo.webp`
- WebP VP8 con la primera partición fuera del archivo: `capturas/falla-v2e-vp8-particion.webp`
- WebP VP8L sin signatura: `capturas/falla-v2e-vp8l-firma.webp`
- WebP VP8L con versión distinta de 0: `capturas/falla-v2e-vp8l-version.webp`
- WebP con VP8X y sin imagen: `capturas/falla-v2e-vp8x-sin-imagen.webp`
- WebP animado con un fotograma ANMF sin imagen: `capturas/falla-v2e-anmf-sin-imagen.webp`
- PNG con profundidad 3 en RGB: `capturas/falla-v2e-png-profundidad.png`
- PNG con método de compresión 1: `capturas/falla-v2e-png-compresion.png`
- PNG entrelazado con datos de imagen de tamaño incorrecto: `capturas/falla-v2e-png-entrelazado.png`

## Frente al catálogo de Pharmaco (alimenta TASK-002)
| # | Servicio Pharmaco | ¿Lo ofrecen? | Nombre literal que usan | URL de su página |
| --- | --- | --- | --- | --- |
| 1 | Branding | Sí | Marca de prueba | https://www.iana.org/domains/reserved |
| 2 | Social Media | Sí | Redes de prueba | https://www.iana.org/domains/reserved |
| 3 | Desarrollo Web | Sí | Web de prueba | https://www.iana.org/domains/reserved |
| 4 | Campañas publicitarias | No |  |  |
| 5 | Performance | No |  |  |
| 6 | Desarrollo de apps y software | No |  |  |
| 7 | Fotografía y video | No |  |  |
| 8 | Inteligencia artificial | No |  |  |
| 9 | SEO y GEO | No |  |  |
| 10 | CRO | No |  |  |
| 11 | Datos y automatización | No |  |  |

**Servicios suyos que no están en la tabla:** ninguno (dato de prueba).
