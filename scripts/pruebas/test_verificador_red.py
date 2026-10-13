#!/usr/bin/env python3
"""Regresiones de la comprobación de enlaces (V8) de verificar-investigacion.py (TASK-007).

Solo biblioteca estándar. Un servidor HTTP local en 127.0.0.1 con rutas que responden (`/rapida`), tardan 8 s
(`/lenta`, debe dar OK) o no responden nunca (`/colgada`, debe dar FALLO dentro del tiempo máximo). Los dominios
IDN se comprueban con `url_de_peticion` y con un dominio `.invalid` (falla el DNS, pero no por codificación).

    python3 scripts/pruebas/test_verificador_red.py -v
"""

import argparse
import ast
import http.server
import select
import socket
import importlib.util
import os
import subprocess
import sys
import threading
import time
import unittest
import urllib.parse
from unittest import mock

RAIZ_SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_SCRIPT = os.path.join(RAIZ_SCRIPTS, "verificar-investigacion.py")

_spec = importlib.util.spec_from_file_location("verificar_investigacion", RUTA_SCRIPT)
v = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v)


class Servidor(http.server.ThreadingHTTPServer):
    daemon_threads = True


class Manejador(http.server.BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def _responder(self, codigo):
        cuerpo = b"ok"
        self.send_response(codigo)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def _retener(self, segundos):
        """Espera hasta `segundos` salvo que el cliente cierre la conexión. True si sigue conectado."""
        fin = time.monotonic() + segundos
        while time.monotonic() < fin:
            listos, _, _ = select.select([self.connection], [], [], 0.02)
            if listos and self.connection.recv(1, socket.MSG_PEEK) == b"":
                return False
        return True

    def do_GET(self):
        try:
            self._atender()
        except OSError:
            pass  # el cliente ya cerró (plazo vencido): no es un fallo del servidor

    def _atender(self):
        self.server.rutas_pedidas.append(self.path)
        if urllib.parse.urlsplit(self.path).path == "/retiene":  # 1,5 s, o hasta que el cliente cierre
            with self.server.cerrojo:
                self.server.en_vuelo += 1
                self.server.maximo = max(self.server.maximo, self.server.en_vuelo)
            try:
                if self._retener(1.5):
                    return self._responder(200)
                return None
            finally:
                with self.server.cerrojo:
                    self.server.en_vuelo -= 1
        ruta = urllib.parse.urlsplit(self.path).path
        if ruta == "/rapida":
            return self._responder(200)
        if ruta == "/lenta":  # tarda 8 s y responde 200: debe dar OK
            time.sleep(8)
            return self._responder(200)
        if ruta == "/concurrente":  # tarda 0,5 s y lleva la cuenta de peticiones simultáneas
            with self.server.cerrojo:
                self.server.en_vuelo += 1
                self.server.maximo = max(self.server.maximo, self.server.en_vuelo)
            time.sleep(0.5)
            with self.server.cerrojo:
                self.server.en_vuelo -= 1
            return self._responder(200)
        if ruta.startswith("/cadena/"):  # cada respuesta tarda 0,7 s; /cadena/0 y /cadena/1 redirigen, /cadena/2 da 200
            n = int(ruta.rsplit("/", 1)[1])
            time.sleep(0.7)
            if n < 2:
                self.send_response(302)
                self.send_header("Location", f"/cadena/{n + 1}")
                self.send_header("Content-Length", "0")
                self.end_headers()
                return
            return self._responder(200)
        if ruta == "/colgada":  # no responde nunca: no envía nada hasta que termina el test
            self.server.fin.wait()
            return
        # Se decodifica la ruta recibida: si llega doblemente codificada, no coincide y responde 404.
        if urllib.parse.unquote(self.path) == "/año.html":
            return self._responder(200)
        return self._responder(404)


class PruebasSinRed(unittest.TestCase):
    def test_dominio_idn_en_idna(self):
        self.assertEqual(v.url_de_peticion("https://árkos.com/ruta"), "https://xn--rkos-4na.com/ruta")

    def test_ruta_y_consulta_con_n_se_codifican(self):
        self.assertEqual(v.url_de_peticion("https://ejemplo.com/año/niño?q=ñ"),
                         "https://ejemplo.com/a%C3%B1o/ni%C3%B1o?q=%C3%B1")

    def test_lo_ya_codificado_no_se_vuelve_a_codificar(self):
        self.assertEqual(v.url_de_peticion("https://ejemplo.com/a%C3%B1o?x=%20"),
                         "https://ejemplo.com/a%C3%B1o?x=%20")

    def test_url_mal_formada_es_fallo_con_motivo_y_sin_reintentos(self):
        for url in ["https://ejemplo.com/100%", "https://ejemplo.com:puerto/", "https://" + "a" * 64 + ".com/"]:
            with self.subTest(url=url):
                estado, motivo, antibot = v.comprobar_url(url)
                self.assertEqual(estado, "FALLO")
                self.assertTrue(motivo.startswith("URL mal formada"), motivo)
                self.assertFalse(antibot)

    def test_host_de_no_aborta_con_url_mal_formada(self):
        self.assertEqual(v.host_de("https://[malo/ruta"), "")
        self.assertEqual(v.host_de("https://ejemplo.com/ruta"), "ejemplo.com")

    def test_redireccion_comparada_en_idna(self):
        self.assertEqual(v.sin_www("https://árkos.com/"), v.sin_www("https://xn--rkos-4na.com/"))
        self.assertEqual(v.sin_www("https://www.árkos.com/"), "xn--rkos-4na.com")

    def test_limites_del_metodo(self):
        self.assertEqual(v.TIMEOUT_SEGUNDOS, 30)
        self.assertEqual(v.REINTENTOS, 2)
        self.assertGreater(v.TIMEOUT_TOTAL_SEGUNDOS, 0)

    def test_timeout_total_solo_acepta_segundos_positivos(self):
        self.assertEqual(v._segundos_positivos("2.5"), 2.5)
        for valor in ["0", "-3", "abc", "inf", "nan"]:
            with self.subTest(valor=valor):
                with self.assertRaises(argparse.ArgumentTypeError):
                    v._segundos_positivos(valor)

    def test_solo_biblioteca_estandar(self):
        with open(RUTA_SCRIPT, encoding="utf-8") as f:
            arbol = ast.parse(f.read())
        modulos = set()
        for nodo in ast.walk(arbol):
            if isinstance(nodo, ast.Import):
                modulos |= {alias.name.split(".")[0] for alias in nodo.names}
            elif isinstance(nodo, ast.ImportFrom) and nodo.module:
                modulos.add(nodo.module.split(".")[0])
        self.assertTrue(modulos <= set(sys.stdlib_module_names), modulos - set(sys.stdlib_module_names))

    def test_argumento_timeout_total_invalido_sale_con_error(self):
        proceso = subprocess.run([sys.executable, RUTA_SCRIPT, "--raiz", os.path.join(RAIZ_SCRIPTS, "pruebas"),
                                  "--timeout-total", "0"], capture_output=True, text=True)
        self.assertEqual(proceso.returncode, 2)
        self.assertIn("debe ser un número de segundos mayor que 0", proceso.stderr)


class PruebasDeRed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.servidor = Servidor(("127.0.0.1", 0), Manejador)
        cls.servidor.fin = threading.Event()
        cls.servidor.rutas_pedidas = []
        cls.servidor.cerrojo = threading.Lock()
        cls.servidor.en_vuelo = 0
        cls.servidor.maximo = 0
        cls.base = f"http://127.0.0.1:{cls.servidor.server_address[1]}"
        cls.hilo = threading.Thread(target=cls.servidor.serve_forever, daemon=True)
        cls.hilo.start()

    @classmethod
    def tearDownClass(cls):
        cls.servidor.fin.set()
        cls.servidor.shutdown()
        cls.servidor.server_close()

    def pedidas(self, ruta):
        return sum(1 for p in self.servidor.rutas_pedidas if urllib.parse.urlsplit(p).path == ruta)

    def test_maximo_dos_conexiones_vivas_aunque_venza_el_plazo(self):
        # REVIEW-007 (segunda ronda): cada intento vence a los 0,3 s. La conexión sigue viva mientras el hilo del
        # intento no acaba, y el límite debe contarla. El servidor cuenta las peticiones que aún esperan al cliente.
        self.servidor.maximo = 0
        self.servidor.en_vuelo = 0
        urls = [self.base + f"/retiene?n={i}" for i in range(4)]
        with mock.patch.multiple(v, TIMEOUT_SEGUNDOS=0.3, ESPERA_REINTENTO=0):
            resultado = v.comprobar_todas(urls, timeout_total=30)
        self.assertTrue(all(estado == "FALLO" for estado, _, _ in resultado.values()), resultado)
        self.assertLessEqual(self.servidor.maximo, 2)
        self.assertGreaterEqual(self.servidor.maximo, 1)

    def test_maximo_dos_conexiones_por_dominio(self):
        # Seis URL del mismo host: con 8 hilos, el límite por dominio es lo que impide más de 2 a la vez.
        self.servidor.maximo = 0
        self.servidor.en_vuelo = 0
        urls = [self.base + f"/concurrente?n={i}" for i in range(6)]
        resultado = v.comprobar_todas(urls, timeout_total=30)
        self.assertTrue(all(estado == "OK" for estado, _, _ in resultado.values()), resultado)
        self.assertEqual(self.servidor.maximo, 2)  # valor fijo: no depende de la constante del script

    def test_lote_mixto_con_url_mal_formada_no_aborta_la_v8(self):
        # REVIEW-007: una URL con «[» sin cerrar no debe abortar el lote; las demás se comprueban igual.
        malformada, buena = "https://[malo/ruta", self.base + "/rapida"
        resultado = v.comprobar_todas([malformada, buena], timeout_total=30)
        self.assertEqual(resultado[malformada][0], "FALLO")
        self.assertTrue(resultado[malformada][1].startswith("URL mal formada"), resultado[malformada][1])
        self.assertEqual(resultado[buena][0], "OK", resultado[buena])

    def test_cadena_de_redirecciones_respeta_el_plazo_por_intento(self):
        # REVIEW-007: 0,7 s por respuesta y dos redirecciones suman 2,1 s; con 1 s por intento debe ser FALLO.
        inicio = time.monotonic()
        with mock.patch.multiple(v, TIMEOUT_SEGUNDOS=1, ESPERA_REINTENTO=0.1):
            estado, motivo, _ = v.comprobar_url(self.base + "/cadena/0")
        medido = time.monotonic() - inicio
        self.assertEqual(estado, "FALLO", motivo)
        self.assertIn("tiempo de espera agotado en 3 intentos", motivo)
        self.assertLess(medido, 5)

    def test_cadena_de_redirecciones_con_plazo_suficiente_da_ok(self):
        # Control: la misma cadena con 3 s por intento sí responde OK.
        with mock.patch.multiple(v, TIMEOUT_SEGUNDOS=3):
            estado, motivo, _ = v.comprobar_url(self.base + "/cadena/0")
        self.assertEqual(estado, "OK", motivo)

    def test_ruta_que_tarda_8_s_da_ok(self):
        inicio = time.monotonic()
        estado, motivo, _ = v.comprobar_url(self.base + "/lenta")
        medido = time.monotonic() - inicio
        self.assertEqual(estado, "OK", motivo)
        self.assertGreaterEqual(medido, 8)

    def test_ruta_que_no_responde_da_fallo_con_tiempos_e_intentos(self):
        antes = self.pedidas("/colgada")
        inicio = time.monotonic()
        with mock.patch.multiple(v, TIMEOUT_SEGUNDOS=2, ESPERA_REINTENTO=0.1):
            estado, motivo, _ = v.comprobar_url(self.base + "/colgada")
        medido = time.monotonic() - inicio
        self.assertEqual(estado, "FALLO")
        self.assertIn("tiempo de espera agotado en 3 intentos", motivo)
        self.assertIn("medido por intento: 2,0 s, 2,0 s, 2,0 s", motivo)
        self.assertEqual(self.pedidas("/colgada") - antes, 3)
        self.assertLess(medido, 10)

    def test_tiempo_maximo_global_corta_una_ruta_colgada(self):
        inicio = time.monotonic()
        resultado = v.comprobar_todas([self.base + "/colgada"], timeout_total=2)
        medido = time.monotonic() - inicio
        estado, motivo, _ = resultado[self.base + "/colgada"]
        self.assertEqual(estado, "FALLO")
        self.assertIn("no comprobada: se agotó el tiempo máximo de la ejecución (2 s; --timeout-total)", motivo)
        self.assertLess(medido, 6)

    def test_dominio_idn_falla_por_dns_y_no_por_codificacion(self):
        # Depende de la red: hace una consulta DNS real para un dominio .invalid.
        with mock.patch.multiple(v, ESPERA_REINTENTO=0.1):
            estado, motivo, _ = v.comprobar_url("https://árkos.invalid/")
        self.assertEqual(estado, "FALLO")
        self.assertIn("error de red", motivo)
        self.assertNotIn("ordinal", motivo)
        self.assertNotIn("codific", motivo.lower())

    def test_ruta_con_n_llega_codificada_una_sola_vez(self):
        estado, motivo, _ = v.comprobar_url(self.base + "/año.html")
        self.assertEqual(estado, "OK", motivo)
        self.assertEqual(self.servidor.rutas_pedidas[-1], "/a%C3%B1o.html")
        estado, motivo, _ = v.comprobar_url(self.base + "/a%C3%B1o.html")
        self.assertEqual(estado, "OK", motivo)
        self.assertEqual(self.servidor.rutas_pedidas[-1], "/a%C3%B1o.html")

    def test_lote_mezcla_ok_y_404(self):
        urls = [self.base + "/rapida", self.base + "/año.html", self.base + "/no-existe"]
        with mock.patch.multiple(v, ESPERA_REINTENTO=0.1):
            resultado = v.comprobar_todas(urls, timeout_total=30)
        self.assertEqual(resultado[self.base + "/rapida"][0], "OK")
        self.assertEqual(resultado[self.base + "/año.html"][0], "OK")
        self.assertEqual(resultado[self.base + "/no-existe"][:2], ("FALLO", "HTTP 404 (tras 3 intentos)"))


if __name__ == "__main__":
    unittest.main()
