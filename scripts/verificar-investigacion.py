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
import concurrent.futures
import datetime
import glob
import hashlib
import http.client
import os
import re
import struct
import sys
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
TIMEOUT_SEGUNDOS = 20
HILOS_RED = 8

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


def validar_png(datos):
    """Estructura completa: fragmentos con CRC, IHDR primero, IDAT con tamaño de imagen correcto, IEND."""
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
            if longitud != 13:
                return "PNG: IHDR de longitud incorrecta"
            ihdr = struct.unpack(">IIBBBBB", cuerpo)
        if tipo == b"IDAT":
            idat += cuerpo
        tipos.append(tipo)
        pos = fin
        if tipo == b"IEND":
            break
    if b"IDAT" not in tipos:
        return "PNG sin datos de imagen"
    ancho, alto, profundidad, color, _, _, entrelazado = ihdr
    if ancho == 0 or alto == 0:
        return "PNG sin dimensiones"
    try:
        bruto = zlib.decompress(idat)
    except zlib.error:
        return "PNG: datos de imagen corruptos"
    if entrelazado == 0:
        canales = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}.get(color)
        if canales is None:
            return "PNG: tipo de color no válido"
        bytes_fila = (ancho * canales * profundidad + 7) // 8
        if len(bruto) != alto * (1 + bytes_fila):
            return "PNG: el tamaño de los datos de imagen no corresponde a las dimensiones"
    return None


def validar_webp(datos):
    """RIFF con tamaño que cuadra con el archivo, fragmentos completos y uno de imagen VP8/VP8L/VP8X."""
    if struct.unpack("<I", datos[4:8])[0] + 8 != len(datos):
        return "WebP: el tamaño RIFF no coincide con el archivo"
    pos, imagen = 12, False
    while pos < len(datos):
        if pos + 8 > len(datos):
            return "WebP truncado"
        tipo = datos[pos:pos + 4]
        longitud = struct.unpack("<I", datos[pos + 4:pos + 8])[0]
        fin = pos + 8 + longitud + (longitud & 1)
        if fin > len(datos):
            return "WebP truncado (fragmento incompleto)"
        imagen = imagen or tipo in (b"VP8 ", b"VP8L", b"VP8X")
        pos = fin
    if not imagen:
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


def sin_www(url):
    return (urllib.parse.urlsplit(url).hostname or "").removeprefix("www.")


CABECERAS_NAVEGADOR = {
    # Con un User-Agent de bot, algunos sitios devuelven 404 donde un navegador ve 403 (antibot).
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es,en;q=0.8",
}


def comprobar_url(url):
    peticion = urllib.request.Request(url, headers=CABECERAS_NAVEGADOR)
    try:
        with urllib.request.urlopen(peticion, timeout=TIMEOUT_SEGUNDOS) as respuesta:
            final = respuesta.geturl()
    except urllib.error.HTTPError as e:
        # DECISION-006 (aclaración 1): solo 404 y 410 son FALLO; otros 4xx son bloqueos, AVISO.
        if e.code in (404, 410):
            return "FALLO", f"HTTP {e.code}"
        if 400 <= e.code < 500:
            return "AVISO", f"HTTP {e.code} (bloqueo antibot o de región): respaldar con captura"
        return "FALLO", f"HTTP {e.code}"
    except (urllib.error.URLError, OSError, ValueError, http.client.HTTPException) as e:
        return "FALLO", f"error de red: {getattr(e, 'reason', e)}"
    if sin_www(final) != sin_www(url):
        return "AVISO", f"redirige a otro dominio: {final}"
    return "OK", "responde"


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

def main():
    parser = argparse.ArgumentParser(description="Verifica la investigación (DECISION-006).")
    parser.add_argument("--raiz", default=os.path.join(RAIZ_REPO, "docs"),
                        help="carpeta que contiene investigacion/ y diseno/ (por defecto, docs/)")
    parser.add_argument("--sin-red", action="store_true",
                        help="salta V8 (enlaces vivos); para el gate se pega la salida con red")
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
        with concurrent.futures.ThreadPoolExecutor(max_workers=HILOS_RED) as pool:
            estado_url = dict(zip(todas, pool.map(comprobar_url, todas)))
        for ruta in documentos:
            problemas = [(estado_url[u][0], f"{u} → {estado_url[u][1]}")
                         for u in urls_por_doc[ruta] if estado_url[u][0] != "OK"]
            anotar("V8", rel(ruta), problemas)

    print(f"Verificación de la investigación · raíz: {raiz} · V8: {'omitida (--sin-red)' if args.sin_red else 'con red'}")
    for v, estado, archivo, motivo in resultados:
        print(f"{v}  {estado:<7} {archivo} — {motivo}")
    fallos = sum(1 for r in resultados if r[1] == "FALLO")
    avisos = sum(1 for r in resultados if r[1] == "AVISO")
    print(f"\n{fallos} FALLOS · {avisos} AVISOS")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
