#!/usr/bin/env python3
"""Verificación de la investigación (DECISION-006).

Comprueba forma y existencia, no veracidad: la veracidad la revisan Dexia
(REVIEW) y Clia (auditoría por muestreo). Ver scripts/README.md.

    python3 scripts/verificar-investigacion.py               # gate: con red
    python3 scripts/verificar-investigacion.py --sin-red     # salta V8
    python3 scripts/verificar-investigacion.py --raiz scripts/pruebas

Solo biblioteca estándar. Código de salida: 1 si hay algún FALLO, 0 si no.
"""

import argparse
import datetime
import glob
import hashlib
import http.client
import math
import os
import queue
import re
import struct
import sys
import threading
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import zlib
from collections import Counter

RAIZ_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAMPOS_OBLIGATORIOS = ["URL", "País / ciudades", "Bloque · perfil", "Tamaño del equipo", "Fecha de consulta", "Capturas"]
CAMPOS_FICHA = CAMPOS_OBLIGATORIOS + ["Año de fundación"]
TIPOS_CAPTURA_PROPIA = ["home", "servicios", "caso"]
MARCADORES = ["{", "AAAA-MM-DD", "Lorem", "TODO", "(o «no verificado»)"]
PERFILES_VALIDOS = ["comparable", "referente", "especialista"]
FICHAS_ESPERADAS = 20
COMPARABLES_ESPERADOS = 10
REFERENTES_ESPECIALISTAS_ESPERADOS = 10
TIMEOUT_SEGUNDOS = 30  # TASK-007: tiempo máximo por intento de una URL (con 2 reintentos espaciados)
TIMEOUT_TOTAL_SEGUNDOS = 600  # TASK-007: tiempo máximo de toda la ejecución de V8 (--timeout-total)
HILOS_RED = 8
CONEXIONES_POR_DOMINIO = 2  # TASK-007: peticiones simultáneas como máximo a un mismo host
MIN_ANCHO, MIN_ALTO = 320, 200  # DECISION-006, enmienda 6 (corregida): captura de página, ancho y alto
MIN_COMPONENTE = 32  # DECISION-006, enmienda 6 (corregida): captura de componente (docs/diseno/capturas/), cada lado

RE_CAPTURA = re.compile(r"[\w./-]*capturas/[\w.-]+\.(?:png|webp|jpe?g|gif|svg)", re.IGNORECASE)
RE_URL = re.compile(r"https?://[^\s|<>()\[\]«»\"'`]+")
FRENTE = "## Frente al catálogo de Pharmaco"
SERVICIOS_CATALOGO = 11
RE_MARCA = re.compile(r"[*_`~]")  # negrita, cursiva y código alrededor de «Sí» o «No»
RE_CITA = re.compile(r"`[^`]*`")  # DECISION-006 (aclaración 2): un marcador entre comillas invertidas es cita


def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def sin_acentos(texto):
    descompuesto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in descompuesto if unicodedata.category(c) != "Mn").lower()


def vacio(valor):
    return valor.strip() in ("", "—", "-")


def filas_tabla(texto):
    """Celdas de cada fila de tabla markdown; ignora separadores."""
    filas = []
    for linea in texto.splitlines():
        s = linea.strip()
        if s.startswith("|") and not set(s) <= set("|-: "):
            filas.append([c.strip() for c in s.strip("|").split("|")])
    return filas


def seccion(texto, titulo):
    lineas, dentro = [], False
    for linea in texto.splitlines():
        if linea.startswith("## "):
            dentro = linea.startswith(titulo)
        elif dentro:
            lineas.append(linea)
    return "\n".join(lineas)


def campos_ficha(texto):
    """Primera aparición de cada campo de la tabla de cabecera: {campo: (valor, fuente)}."""
    campos = {}
    for celdas in filas_tabla(texto):
        if len(celdas) >= 3 and celdas[0] in CAMPOS_FICHA and celdas[0] not in campos:
            campos[celdas[0]] = (celdas[1], celdas[2])
    return campos


def fecha_valida(texto):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", texto):
        return False
    try:
        datetime.date.fromisoformat(texto)
    except ValueError:
        return False
    return True


def capturas_citadas(texto):
    return sorted(set(RE_CAPTURA.findall(texto)))


def buscar_captura(cita, carpeta_doc, bases):
    for base in [carpeta_doc] + bases:
        ruta = os.path.normpath(os.path.join(base, cita))
        if os.path.isfile(ruta):
            return ruta
    return None


CANALES_PNG = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}
PROFUNDIDADES_PNG = {0: (1, 2, 4, 8, 16), 2: (8, 16), 3: (1, 2, 4, 8), 4: (8, 16), 6: (8, 16)}
# Adam7: (x0, y0, dx, dy) de cada pasada de un PNG entrelazado (especificación PNG, capítulo 8).
ADAM7 = [(0, 0, 8, 8), (4, 0, 8, 8), (0, 4, 4, 8), (2, 0, 4, 4), (0, 2, 2, 4), (1, 0, 2, 2), (0, 1, 1, 2)]
ERROR_TAMANO_PNG = "PNG: el tamaño de los datos de imagen no corresponde a las dimensiones"


def validar_datos_png(bruto, ancho, alto, profundidad, color, entrelazado):
    """Cada pasada tiene exactamente sus filas, cada fila empieza por un byte de filtro de 0 a 4 y no sobra nada."""
    pasadas = ADAM7 if entrelazado else [(0, 0, 1, 1)]
    pos = 0
    for x0, y0, dx, dy in pasadas:
        pw = max(0, (ancho - x0 + dx - 1) // dx)
        ph = max(0, (alto - y0 + dy - 1) // dy)
        if pw == 0 or ph == 0:
            continue
        tam_fila = 1 + (pw * CANALES_PNG[color] * profundidad + 7) // 8
        bloque = bruto[pos:pos + ph * tam_fila]
        if len(bloque) != ph * tam_fila:
            return ERROR_TAMANO_PNG
        if max(bloque[::tam_fila]) > 4:
            return "PNG: byte de filtro no válido en una fila (debe ser 0 a 4)"
        pos += ph * tam_fila
    return None if pos == len(bruto) else ERROR_TAMANO_PNG


def validar_png(datos):
    """Estructura: fragmentos con CRC, IHDR primero, IEND, cabecera válida, IDAT con los datos que pide IHDR."""
    pos, tipos, idat, ihdr = 8, [], b"", None
    while True:
        if pos + 8 > len(datos):
            return "PNG truncado (sin IEND)"
        longitud, tipo = struct.unpack(">I4s", datos[pos:pos + 8])
        fin = pos + 12 + longitud
        if fin > len(datos):
            return "PNG truncado (fragmento incompleto)"
        cuerpo = datos[pos + 8:pos + 8 + longitud]
        crc = struct.unpack(">I", datos[pos + 8 + longitud:fin])[0]
        if zlib.crc32(tipo + cuerpo) & 0xFFFFFFFF != crc:
            return f"PNG: CRC incorrecto en {tipo.decode('ascii', 'replace')}"
        if not tipos and tipo != b"IHDR":
            return "PNG: el primer fragmento no es IHDR"
        if tipo == b"IHDR":
            if b"IHDR" in tipos:
                return "PNG: IHDR duplicado"
            if longitud != 13:
                return "PNG: IHDR de longitud incorrecta"
            ihdr = struct.unpack(">IIBBBBB", cuerpo)
        if tipo == b"IEND":
            # DECISION-006, enmienda 6: IEND de longitud 0 y último byte del archivo.
            if longitud != 0:
                return "PNG: IEND con datos (debe tener longitud 0)"
            if fin != len(datos):
                return "PNG: bytes después de IEND"
        if tipo == b"IDAT":
            idat += cuerpo
        tipos.append(tipo)
        pos = fin
        if tipo == b"IEND":
            break
    if b"IDAT" not in tipos:
        return "PNG sin datos de imagen"
    ancho, alto, profundidad, color, compresion, filtro, entrelazado = ihdr
    if ancho == 0 or alto == 0:
        return "PNG sin dimensiones"
    if color not in PROFUNDIDADES_PNG or profundidad not in PROFUNDIDADES_PNG[color]:
        return "PNG: tipo de color o profundidad no válidos"
    if compresion != 0 or filtro != 0 or entrelazado not in (0, 1):
        return "PNG: método de compresión, de filtro o de entrelazado no válido"
    try:
        bruto = zlib.decompress(idat)
    except zlib.error:
        return "PNG: datos de imagen corruptos"
    return validar_datos_png(bruto, ancho, alto, profundidad, color, entrelazado)


def recorrer_fragmentos(buf):
    """Fragmentos RIFF de buf como [(tipo, cuerpo)], y un error si alguno está truncado."""
    fragmentos, pos = [], 0
    while pos < len(buf):
        if pos + 8 > len(buf):
            return fragmentos, "WebP truncado"
        tipo = buf[pos:pos + 4]
        longitud = struct.unpack("<I", buf[pos + 4:pos + 8])[0]
        fin = pos + 8 + longitud
        if fin > len(buf):
            return fragmentos, "WebP truncado (fragmento incompleto)"
        fragmentos.append((tipo, buf[pos + 8:fin]))
        pos = fin + (longitud & 1)
    if pos > len(buf):
        return fragmentos, "WebP truncado (falta el relleno del último fragmento)"
    return fragmentos, None


def validar_vp8(cuerpo):
    """Fotograma clave VP8 (RFC 6386, sección 9.1): etiqueta, código de inicio, dimensiones y primera partición completa."""
    if len(cuerpo) < 10:
        return "WebP: fragmento VP8 demasiado corto"
    etiqueta = cuerpo[0] | cuerpo[1] << 8 | cuerpo[2] << 16
    if etiqueta & 1:
        return "WebP: fragmento VP8 que no es un fotograma clave"
    if cuerpo[3:6] != b"\x9d\x01\x2a":
        return "WebP: fragmento VP8 sin código de inicio"
    ancho = struct.unpack("<H", cuerpo[6:8])[0] & 0x3FFF
    alto = struct.unpack("<H", cuerpo[8:10])[0] & 0x3FFF
    if ancho == 0 or alto == 0:
        return "WebP: fragmento VP8 sin dimensiones"
    # DECISION-006, enmienda 6: datos de imagen más allá de la cabecera.
    if (etiqueta >> 5) == 0 or len(cuerpo) <= 10:
        return "WebP: fragmento VP8 sin datos de imagen más allá de su cabecera"
    if 10 + (etiqueta >> 5) > len(cuerpo):
        return "WebP: fragmento VP8 con la primera partición incompleta"
    return None


def validar_vp8l(cuerpo):
    """Cabecera VP8L: signatura 0x2f, dimensiones (siempre válidas en 14 bits) y versión 0."""
    if len(cuerpo) < 5:
        return "WebP: fragmento VP8L demasiado corto"
    if cuerpo[0] != 0x2F:
        return "WebP: fragmento VP8L sin signatura"
    if struct.unpack("<I", cuerpo[1:5])[0] >> 29:
        return "WebP: fragmento VP8L con versión no válida"
    # DECISION-006, enmienda 6: la cabecera de 5 bytes no basta; debe haber datos de imagen.
    if len(cuerpo) <= 5:
        return "WebP: fragmento VP8L sin datos de imagen más allá de su cabecera"
    return None


def validar_imagenes_webp(fragmentos):
    """Valida los fragmentos VP8 y VP8L. Devuelve (error, hay_imagen)."""
    hay = False
    for tipo, cuerpo in fragmentos:
        if tipo == b"VP8 ":
            error = validar_vp8(cuerpo)
        elif tipo == b"VP8L":
            error = validar_vp8l(cuerpo)
        else:
            continue
        if error:
            return error, True
        hay = True
    return None, hay


def validar_webp(datos):
    """RIFF con tamaño exacto, fragmentos completos y al menos una imagen VP8 o VP8L válida.

    Alcance: no decodifica píxeles. VP8X y ALPH solos no cuentan como imagen. Un fotograma ANMF
    (animación) cuenta si contiene una imagen VP8 o VP8L válida.
    """
    if struct.unpack("<I", datos[4:8])[0] + 8 != len(datos):
        return "WebP: el tamaño RIFF no coincide con el archivo"
    fragmentos, error = recorrer_fragmentos(datos[12:])
    if error:
        return error
    hay_imagen = False
    for tipo, cuerpo in fragmentos:
        if tipo == b"ANMF":
            if len(cuerpo) < 16:
                return "WebP: fotograma ANMF demasiado corto"
            subfragmentos, error = recorrer_fragmentos(cuerpo[16:])
            if error:
                return error
            error, hay = validar_imagenes_webp(subfragmentos)
            if error:
                return error
            if not hay:
                return "WebP: fotograma ANMF sin imagen"
        else:
            error, hay = validar_imagenes_webp([(tipo, cuerpo)])
            if error:
                return error
        hay_imagen = hay_imagen or hay
    if not hay_imagen:
        return "WebP sin datos de imagen"
    return None


def error_formato(ruta):
    if os.path.getsize(ruta) == 0:
        return "pesa 0 bytes"
    with open(ruta, "rb") as f:
        datos = f.read()
    if datos[:8] == b"\x89PNG\r\n\x1a\n":
        return validar_png(datos)
    if datos[:4] == b"RIFF" and datos[8:12] == b"WEBP":
        return validar_webp(datos)
    return "no es PNG ni WebP válido"


def host_ascii(host):
    """Dominio en IDNA (TASK-007) para comparar; si no se puede codificar, el dominio tal cual."""
    try:
        return host.encode("idna").decode("ascii")
    except UnicodeError:
        return host


def sin_www(url):
    return host_ascii(urllib.parse.urlsplit(url).hostname or "").removeprefix("www.")


# TASK-007: lo que no es ASCII en la ruta y la consulta se codifica; lo ya codificado («%») se respeta tal cual.
SEGUROS_RUTA = "/:@!$&'()*+,;=-._~%"
SEGUROS_CONSULTA = SEGUROS_RUTA + "?"
SEGUROS_USUARIO = "%:!$&'()*+,;="


def _codificar(texto, seguros):
    if re.search(r"%(?![0-9A-Fa-f]{2})", texto):
        raise ValueError("«%» que no va seguido de dos dígitos hexadecimales")
    return urllib.parse.quote(texto, safe=seguros)


def url_de_peticion(url):
    """URL tal como se pide por la red (TASK-007): dominio en IDNA y ruta y consulta codificadas.

    Lanza ValueError si la URL está mal formada; el llamador lo convierte en FALLO que lo dice.
    """
    partes = urllib.parse.urlsplit(url)
    if partes.scheme not in ("http", "https") or not partes.hostname:
        raise ValueError("no es una URL http o https con dominio")
    puerto = partes.port  # ValueError si el puerto no es un número válido
    host = partes.hostname
    try:
        host = host.encode("idna").decode("ascii")
    except UnicodeError as e:
        raise ValueError(f"dominio no válido en IDNA ({partes.hostname}): {e}") from e
    if ":" in host:
        host = f"[{host}]"
    usuario = _codificar(partes.netloc.rpartition("@")[0], SEGUROS_USUARIO) + "@" if "@" in partes.netloc else ""
    netloc = usuario + host + (f":{puerto}" if puerto is not None else "")
    ruta = _codificar(partes.path, SEGUROS_RUTA)
    consulta = _codificar(partes.query, SEGUROS_CONSULTA)
    return urllib.parse.urlunsplit((partes.scheme, netloc, ruta, consulta, ""))


CABECERAS_NAVEGADOR = {
    # Con un User-Agent de bot, algunos sitios devuelven 404 donde un navegador ve 403 (antibot).
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es,en;q=0.8",
}


# TASK-005 (Clia, 2026-10-10): ante error de red, 404 o 5xx se reintenta; sólo es FALLO si fallan los 3 intentos.
# 403 y 429 (antibot) son AVISO y no se reintentan.
REINTENTOS = 2
ESPERA_REINTENTO = 2  # segundos


ANTIBOT = (401, 403, 429)  # DECISION-006, enmienda 4
CABECERAS_DESAFIO = ("sg-captcha", "x-amzn-waf-action")  # DECISION-006, enmienda 5: lista ampliable en el hilo


def _cabecera_de_desafio(cabeceras):
    """Nombre de la cabecera de desafío conocida que trae la respuesta, o None."""
    for nombre in CABECERAS_DESAFIO:
        if cabeceras.get(nombre) is not None:
            return nombre
    if (cabeceras.get("cf-mitigated") or "").strip().lower() == "challenge":
        return "cf-mitigated: challenge"
    return None


def _es_tiempo_agotado(error):
    """True si el error es un tiempo de espera, sea directo o envuelto en URLError (TASK-007)."""
    return isinstance(error, TimeoutError) or isinstance(getattr(error, "reason", None), TimeoutError)


MAX_REDIRECCIONES = 10
CODIGOS_REDIRECCION = (301, 302, 303, 307, 308)
MARGEN_PLAZO = 0.5  # s de cortesía tras el plazo del intento, por si el hilo tarda en acabar (p. ej., DNS)


class _SinRedirecciones(urllib.request.HTTPRedirectHandler):
    """Las redirecciones las sigue `_intentar_url` a mano, dentro del plazo del intento (REVIEW-007)."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_ABRIDOR = urllib.request.build_opener(_SinRedirecciones)


def _intentar_url(pedida, url, limite):
    """Un intento hasta `limite` (instante de time.monotonic()), redirecciones incluidas.

    Cada salto usa como timeout de socket el tiempo que queda del intento, así que ninguna conexión sobrevive al
    plazo. Devuelve (estado, motivo, reintentable, antibot, agotado).
    """
    actual = pedida
    for _ in range(MAX_REDIRECCIONES + 1):
        restante = limite - time.monotonic()
        if restante <= 0:
            return "FALLO", "tiempo de espera agotado", True, False, True
        peticion = urllib.request.Request(actual, headers=CABECERAS_NAVEGADOR)
        try:
            with _ABRIDOR.open(peticion, timeout=restante) as respuesta:
                final = respuesta.geturl()
                codigo, cabeceras = respuesta.status, respuesta.headers
            break
        except urllib.error.HTTPError as e:
            destino = e.headers.get("Location") if e.code in CODIGOS_REDIRECCION else None
            if destino:
                e.close()
                try:
                    actual = url_de_peticion(urllib.parse.urljoin(actual, destino))
                except ValueError as err:
                    return "FALLO", f"redirección a una URL mal formada: {err}", False, False, False
                continue
            # DECISION-006 (aclaración 1): solo 404 y 410 son FALLO; otros 4xx son bloqueos, AVISO.
            if e.code == 404:
                return "FALLO", "HTTP 404", True, False, False
            if e.code == 410:
                return "FALLO", "HTTP 410", False, False, False
            if 400 <= e.code < 500:
                return ("AVISO", f"HTTP {e.code} (bloqueo antibot o de región): respaldar con captura", False,
                        e.code in ANTIBOT, False)
            return "FALLO", f"HTTP {e.code}", 500 <= e.code < 600, False, False
        except (urllib.error.URLError, OSError, http.client.HTTPException) as e:
            if _es_tiempo_agotado(e):
                return "FALLO", "tiempo de espera agotado", True, False, True
            return "FALLO", f"error de red: {getattr(e, 'reason', e)}", True, False, False
        except ValueError as e:
            return "FALLO", f"error de red: {getattr(e, 'reason', e)}", False, False, False
    else:
        return "FALLO", f"demasiadas redirecciones (más de {MAX_REDIRECCIONES})", False, False, False
    # DECISION-006, enmienda 5: un 202 a un GET de página y un 2xx con cabecera de desafío no son la página.
    if codigo == 202:
        return ("AVISO", "HTTP 202 (respuesta de desafío o diferida, no la página): respaldar con captura", False, True,
                False)
    desafio = _cabecera_de_desafio(cabeceras)
    if desafio:
        return ("AVISO", f"HTTP {codigo} con cabecera de desafío antibot ({desafio}): respaldar con captura", False,
                True, False)
    if sin_www(final) != sin_www(url):
        return "AVISO", f"redirige a otro dominio: {final}", False, False, False
    return "OK", "responde", False, False, False


def _intentar_url_con_plazo(pedida, url, semaforo):
    """Un intento con plazo real de TIMEOUT_SEGUNDOS, desde que se llama (REVIEW-007).

    El llamador ya ha tomado `semaforo`; lo libera el hilo del intento al terminar, no el llamador al vencer el
    plazo. Así una conexión que sigue viva cuenta hasta que acaba, y no aparece otra por encima del límite del host.
    """
    limite = time.monotonic() + TIMEOUT_SEGUNDOS
    salida = []

    def objetivo():
        try:
            salida.append((True, _intentar_url(pedida, url, limite)))
        except Exception as e:  # se relanza en el hilo que llama
            salida.append((False, e))
        finally:
            semaforo.release()

    hilo = threading.Thread(target=objetivo, daemon=True)
    try:
        hilo.start()
    except BaseException:
        semaforo.release()
        raise
    hilo.join(max(0.0, limite - time.monotonic()) + MARGEN_PLAZO)
    if not salida:
        return "FALLO", "tiempo de espera agotado", True, False, True
    correcto, valor = salida[0]
    if not correcto:
        raise valor
    return valor


def _segundos(valor):
    return f"{valor:.1f}".replace(".", ",") + " s"


def comprobar_url(url, semaforo=None):
    """Hasta 3 intentos (TASK-005; TASK-007: 30 s por intento y 2 reintentos espaciados 2 s).

    Cada intento toma `semaforo` (el límite de conexiones del host) antes de empezar. Devuelve
    (estado, motivo, antibot): antibot si algún intento dio 401, 403 o 429.
    Una URL que no se puede codificar es FALLO sin reintentos, con el motivo.
    """
    try:
        pedida = url_de_peticion(url)
    except ValueError as e:
        return "FALLO", f"URL mal formada: {e}", False
    if semaforo is None:
        semaforo = threading.BoundedSemaphore(CONEXIONES_POR_DOMINIO)
    tiempos, antibot = [], False
    for intento in range(1, REINTENTOS + 2):
        if intento > 1:
            time.sleep(ESPERA_REINTENTO)
        semaforo.acquire()
        inicio = time.monotonic()
        estado, motivo, reintentable, visto, agotado = _intentar_url_con_plazo(pedida, url, semaforo)
        tiempos.append(time.monotonic() - inicio)
        antibot = antibot or visto
        if estado == "OK" or not reintentable:
            break
    if estado == "OK":
        return estado, motivo, antibot
    if agotado:
        medidos = ", ".join(_segundos(t) for t in tiempos)
        motivo = (f"sin respuesta: tiempo de espera agotado en {len(tiempos)} intentos "
                  f"(medido por intento: {medidos}; límite de {TIMEOUT_SEGUNDOS} s)")
    elif len(tiempos) > 1:
        motivo += f" (tras {len(tiempos)} intentos)"
    return estado, motivo, antibot


def comprobar_todas(urls, timeout_total):
    """Comprueba las URL en paralelo (TASK-007) y devuelve {url: (estado, motivo, antibot)}.

    HILOS_RED hilos como mucho y CONEXIONES_POR_DOMINIO conexiones simultáneas por host, contadas hasta que cada
    conexión acaba de verdad. El tiempo máximo de toda la ejecución es `timeout_total` segundos: una URL sin
    comprobar cuando se agota es FALLO, porque sin comprobar no puede dar OK. Los hilos son daemon, así que el
    proceso termina aunque quede alguno colgado.
    """
    pendientes = queue.Queue()
    for url in urls:
        pendientes.put(url)
    semaforos = {host: threading.BoundedSemaphore(CONEXIONES_POR_DOMINIO) for host in {host_de(u) for u in urls}}
    resultados, cerrojo = {}, threading.Lock()

    def trabajador():
        while True:
            try:
                url = pendientes.get_nowait()
            except queue.Empty:
                return
            resultado = comprobar_url(url, semaforos[host_de(url)])
            with cerrojo:
                resultados[url] = resultado

    hilos = [threading.Thread(target=trabajador, daemon=True) for _ in range(min(HILOS_RED, len(urls)))]
    for hilo in hilos:
        hilo.start()
    limite = time.monotonic() + timeout_total
    for hilo in hilos:
        hilo.join(max(0.0, limite - time.monotonic()))
    with cerrojo:
        comprobadas = dict(resultados)
    for url in urls:
        if url not in comprobadas:
            comprobadas[url] = ("FALLO", f"no comprobada: se agotó el tiempo máximo de la ejecución "
                                         f"({timeout_total:g} s; --timeout-total)", False)
    return comprobadas


def host_de(url):
    """Dominio de la URL, o "" si no se puede analizar: una URL mal formada no debe abortar la V8 (REVIEW-007)."""
    try:
        return urllib.parse.urlsplit(url).hostname or ""
    except ValueError:
        return ""


def clasificar_urls(resultados):
    """resultados: {url: (estado, motivo, antibot)}. Aplica la enmienda 4 de DECISION-006 y devuelve {url: (estado, motivo)}.

    - Un intento con 401, 403 o 429 ya da AVISO en esa URL (ver comprobar_url).
    - Un 404 final en un host donde otra URL de la misma ejecución dio señal antibot (401, 403, 429, 202 o
      cabecera de desafío, enmiendas 4 y 5) pasa a AVISO.
    - El resto no cambia: 404, 410, 5xx o error de red en los 3 intentos siguen siendo FALLO.
    """
    hosts_antibot = {host_de(u) for u, (_, _, antibot) in resultados.items() if antibot}
    salida = {}
    for url, (estado, motivo, _) in resultados.items():
        if estado == "FALLO" and motivo.startswith("HTTP 404") and host_de(url) in hosts_antibot:
            motivo = ("HTTP 404 en host con antibot (otra URL del host dio 401, 403, 429, 202 o cabecera de desafío "
                      "en esta ejecución): 404 no concluyente, respaldar con captura") + motivo[len("HTTP 404"):]
            estado = "AVISO"
        salida[url] = (estado, motivo)
    return salida


# --- Comprobaciones: cada una devuelve [(estado, motivo)] ---------------------

def v1_campos(texto):
    campos = campos_ficha(texto)
    problemas = []
    for campo in CAMPOS_OBLIGATORIOS:
        if campo not in campos or vacio(campos[campo][0]):
            problemas.append(f"{campo}: falta o está vacío")
    if "Fecha de consulta" in campos:
        fecha = campos["Fecha de consulta"][0].strip()
        if not fecha_valida(fecha):
            problemas.append(f"Fecha de consulta no es AAAA-MM-DD ({fecha})")
    if "Tamaño del equipo" in campos:
        tamano, fuente = (c.strip() for c in campos["Tamaño del equipo"])
        if tamano and sin_acentos(tamano).strip(" «»\"") != "no publicado":
            if not re.search(r"\d", tamano):
                problemas.append(f"Tamaño del equipo: ni «no publicado» ni un rango con fuente ({tamano})")
            elif vacio(fuente):
                problemas.append(f"Tamaño del equipo: cifra sin fuente ({tamano})")
    return [("FALLO", p) for p in problemas]


def medir_webp(datos):
    """Lienzo (VP8X) o, si no lo hay, dimensiones del primer VP8/VP8L o del primer ANMF."""
    fragmentos, _ = recorrer_fragmentos(datos[12:])
    lienzo = primera = animado = None
    for tipo, cuerpo in fragmentos:
        if tipo == b"VP8X" and lienzo is None:
            lienzo = (1 + int.from_bytes(cuerpo[4:7], "little"), 1 + int.from_bytes(cuerpo[7:10], "little"))
        elif tipo == b"VP8 " and primera is None:
            primera = (struct.unpack("<H", cuerpo[6:8])[0] & 0x3FFF, struct.unpack("<H", cuerpo[8:10])[0] & 0x3FFF)
        elif tipo == b"VP8L" and primera is None:
            bits = struct.unpack("<I", cuerpo[1:5])[0]
            primera = ((bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1)
        elif tipo == b"ANMF" and animado is None:
            animado = (int.from_bytes(cuerpo[6:9], "little") + 1, int.from_bytes(cuerpo[9:12], "little") + 1)
    return lienzo or primera or animado


def medir_captura(ruta):
    """Ancho y alto de una captura PNG o WebP ya validada, o None."""
    with open(ruta, "rb") as f:
        datos = f.read()
    if datos[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", datos[16:24])
    if datos[:4] == b"RIFF" and datos[8:12] == b"WEBP":
        return medir_webp(datos)
    return None


def v2_capturas(texto, ruta_doc, bases):
    problemas = []
    for cita in capturas_citadas(texto):
        ruta = buscar_captura(cita, os.path.dirname(ruta_doc), bases)
        if ruta is None:
            problemas.append(("FALLO", f"captura citada no existe: {cita}"))
            continue
        error = error_formato(ruta)
        if error:
            problemas.append(("FALLO", f"captura {cita}: {error}"))
            continue
        medida = medir_captura(ruta)
        if medida is None:
            continue
        # La clase la da la carpeta: docs/diseno/capturas/ son componentes; el resto, capturas de página.
        if os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(ruta)))) == "diseno":
            if min(medida) < MIN_COMPONENTE:
                problemas.append(("FALLO", f"captura de componente {cita}: {medida[0]}×{medida[1]} px; cada lado "
                                           f"debe medir al menos {MIN_COMPONENTE} px"))
        elif medida[0] < MIN_ANCHO or medida[1] < MIN_ALTO:
            problemas.append(("FALLO", f"captura {cita}: {medida[0]}×{medida[1]} px; el mínimo de captura de página "
                                       f"es {MIN_ANCHO}×{MIN_ALTO} (no es una captura de página)"))
    return problemas


def v3_capturas_propias(texto, ruta_ficha):
    slug = os.path.splitext(os.path.basename(ruta_ficha))[0]
    nombres = [os.path.basename(c) for c in capturas_citadas(texto)]
    faltan = [t for t in TIPOS_CAPTURA_PROPIA if not any(n.startswith(f"{slug}-{t}.") for n in nombres)]
    if faltan:
        return [("FALLO", f"faltan capturas propias ({', '.join(faltan)}); se exigen home, servicios y caso")]
    return []


def v4_duplicadas(carpetas):
    """Devuelve (nº de archivos, [(ruta, otras con el mismo SHA-256)])."""
    por_hash, total = {}, 0
    for carpeta in carpetas:
        for ruta in sorted(glob.glob(os.path.join(carpeta, "*"))):
            if not os.path.isfile(ruta) or os.path.basename(ruta).startswith("."):
                continue
            total += 1
            with open(ruta, "rb") as f:
                digest = hashlib.sha256(f.read()).hexdigest()
            por_hash.setdefault(digest, []).append(ruta)
    duplicadas = []
    for grupo in por_hash.values():
        if len(grupo) > 1:
            for ruta in grupo:
                duplicadas.append((ruta, [o for o in grupo if o != ruta]))
    return total, duplicadas


def v5_portada(texto):
    if not any(linea.startswith(FRENTE) for linea in texto.splitlines()):
        return [("FALLO", f"falta la sección «{FRENTE[3:]}»")]
    problemas = []
    filas = [c for c in filas_tabla(seccion(texto, FRENTE)) if c and c[0].isdigit()]
    if sorted(int(c[0]) for c in filas) != list(range(1, SERVICIOS_CATALOGO + 1)):
        problemas.append(("FALLO", f"la tabla de servicios debe tener las filas 1 a {SERVICIOS_CATALOGO} "
                                   f"(hay {len(filas)})"))
    for celdas in filas:
        if len(celdas) < 5:
            problemas.append(("FALLO", f"fila {celdas[0]} incompleta"))
            continue
        servicio, url_celda = celdas[1], celdas[4]
        oferta = sin_acentos(RE_MARCA.sub("", celdas[2])).strip().rstrip(".")
        if oferta not in ("si", "no"):
            problemas.append(("FALLO", f"«{servicio}»: valor no reconocido en «¿Lo ofrecen?» ({celdas[2]})"))
            continue
        if oferta == "no":
            continue
        if "portada unica" in sin_acentos(" ".join(celdas)):
            problemas.append(("AVISO", f"«{servicio}»: portada única declarada; respaldar con la captura de la home"))
            continue
        url = RE_URL.search(url_celda)
        if not url or urllib.parse.urlsplit(url.group(0)).path in ("", "/"):
            problemas.append(("FALLO", f"«{servicio}» marcado Sí sin URL de su página (valor: {url_celda or 'vacío'})"))
    return problemas


def v6_marcadores(texto):
    problemas = []
    for n, linea in enumerate(texto.splitlines(), 1):
        sin_citas = RE_CITA.sub("", linea)
        for marcador in MARCADORES:
            if marcador in sin_citas:
                problemas.append(("FALLO", f"marcador de plantilla «{marcador}» en la línea {n}"))
    return problemas


# --- Orquestación -------------------------------------------------------------

def _segundos_positivos(texto):
    try:
        valor = float(texto)
    except ValueError:
        raise argparse.ArgumentTypeError(f"no es un número de segundos: {texto}")
    if not (0 < valor < math.inf):
        raise argparse.ArgumentTypeError(f"debe ser un número de segundos mayor que 0: {texto}")
    return valor


def main():
    parser = argparse.ArgumentParser(description="Verifica la investigación (DECISION-006).")
    parser.add_argument("--raiz", default=os.path.join(RAIZ_REPO, "docs"),
                        help="carpeta que contiene investigacion/ y diseno/ (por defecto, docs/)")
    parser.add_argument("--sin-red", action="store_true",
                        help="salta V8 (enlaces vivos); para el gate se pega la salida con red")
    parser.add_argument("--timeout-total", type=_segundos_positivos, default=TIMEOUT_TOTAL_SEGUNDOS,
                        help=f"tiempo máximo de toda la ejecución de V8, en segundos (por defecto "
                             f"{TIMEOUT_TOTAL_SEGUNDOS}); las URL sin comprobar a tiempo son FALLO")
    args = parser.parse_args()

    raiz = os.path.abspath(args.raiz)
    inv = os.path.join(raiz, "investigacion")
    dis = os.path.join(raiz, "diseno")
    bases = [inv, dis]
    carpetas_capturas = [os.path.join(b, "capturas") for b in bases if os.path.isdir(os.path.join(b, "capturas"))]

    # Solo fichas de primer nivel: el glob no recursivo deja fuera anexo-medianas/.
    fichas = sorted(glob.glob(os.path.join(inv, "fichas", "*.md")))
    documentos = fichas + sorted(glob.glob(os.path.join(inv, "servicios", "*.md")))
    if os.path.isfile(os.path.join(inv, "prueba-social.md")):
        documentos.append(os.path.join(inv, "prueba-social.md"))
    documentos += sorted(glob.glob(os.path.join(dis, "*.md")))
    textos = {ruta: leer(ruta) for ruta in documentos}

    def rel(ruta):
        return os.path.relpath(ruta, raiz)

    resultados = []  # (verificación, estado, archivo, motivo)

    def anotar(v, archivo, problemas):
        if not problemas:
            resultados.append((v, "OK", archivo, "sin incidencias"))
        for estado, motivo in problemas:
            resultados.append((v, estado, archivo, motivo))

    for ruta in fichas:
        anotar("V1", rel(ruta), v1_campos(textos[ruta]))
    for ruta in documentos:
        anotar("V2", rel(ruta), v2_capturas(textos[ruta], ruta, bases))
    for ruta in fichas:
        anotar("V3", rel(ruta), v3_capturas_propias(textos[ruta], ruta))

    total, duplicadas = v4_duplicadas(carpetas_capturas)
    for ruta, otras in duplicadas:
        resultados.append(("V4", "FALLO", rel(ruta), "idéntica (mismo SHA-256) a " + ", ".join(rel(o) for o in otras)))
    if not duplicadas:
        resultados.append(("V4", "OK", f"capturas ({total} archivos)", "ninguna duplicada"))

    for ruta in fichas:
        anotar("V5", rel(ruta), v5_portada(textos[ruta]))
    for ruta in documentos:
        anotar("V6", rel(ruta), v6_marcadores(textos[ruta]))

    perfiles = Counter()
    for ruta in fichas:
        valor = campos_ficha(textos[ruta]).get("Bloque · perfil", ("", ""))[0].strip()
        perfil = valor.split("·")[-1].strip().lower() if "·" in valor else ""
        perfiles[perfil] += 1
        if perfil not in PERFILES_VALIDOS:
            resultados.append(("V7", "FALLO", rel(ruta), f"perfil no reconocido ({valor or 'vacío'})"))
    comparables = perfiles["comparable"]
    referentes = perfiles["referente"] + perfiles["especialista"]
    errores_composicion = []
    if len(fichas) != FICHAS_ESPERADAS:
        errores_composicion.append(f"hay {len(fichas)} fichas principales; se esperan {FICHAS_ESPERADAS}")
    if comparables != COMPARABLES_ESPERADOS:
        errores_composicion.append(f"{comparables} comparables; se esperan {COMPARABLES_ESPERADOS}")
    if referentes != REFERENTES_ESPECIALISTAS_ESPERADOS:
        errores_composicion.append(f"{referentes} referentes/especialistas; se esperan {REFERENTES_ESPECIALISTAS_ESPERADOS}")
    archivo_composicion = rel(inv) + "/fichas"
    for error in errores_composicion:
        resultados.append(("V7", "FALLO", archivo_composicion, error))
    if not errores_composicion:
        resultados.append(("V7", "OK", archivo_composicion,
                           f"{len(fichas)} fichas: {comparables} comparables, {referentes} referentes/especialistas"))

    if args.sin_red:
        resultados.append(("V8", "OMITIDA", "todos los documentos", "--sin-red: no se comprueba ningún enlace"))
    else:
        urls_por_doc = {ruta: sorted({u.rstrip(".,;:") for u in RE_URL.findall(textos[ruta])}) for ruta in documentos}
        todas = sorted({u for urls in urls_por_doc.values() for u in urls})
        estado_url = clasificar_urls(comprobar_todas(todas, args.timeout_total))
        for ruta in documentos:
            problemas = [(estado_url[u][0], f"{u} → {estado_url[u][1]}")
                         for u in urls_por_doc[ruta] if estado_url[u][0] != "OK"]
            anotar("V8", rel(ruta), problemas)

    v8 = "omitida (--sin-red)" if args.sin_red else (
        f"con red ({TIMEOUT_SEGUNDOS} s por intento, tiempo máximo {args.timeout_total:g} s en total)")
    print(f"Verificación de la investigación · raíz: {raiz} · V8: {v8}")
    for v, estado, archivo, motivo in resultados:
        print(f"{v}  {estado:<7} {archivo} — {motivo}")
    fallos = sum(1 for r in resultados if r[1] == "FALLO")
    avisos = sum(1 for r in resultados if r[1] == "AVISO")
    print(f"\n{fallos} FALLOS · {avisos} AVISOS")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
