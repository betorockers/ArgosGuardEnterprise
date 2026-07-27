"""
Argos Guard Enterprise v4.0 - Production Desktop Launcher.

Servidor WSGI Multihilo: Waitress (8 hilos)
Interfaz Gráfica: Google Chrome en Modo App Borderless (--start-maximized --app)
Blindaje: Mutex Win32 Kernel + Guardián de Procesos + Supresión de Consola
"""
import os
import sys
import time
import socket
import threading
import subprocess
import webbrowser
import logging
import traceback
from pathlib import Path
from waitress import serve

# Importar PathResolver Singleton
from apps.core.path_resolver import PathResolver

resolver = PathResolver()

# Configuración de Logging
log_file = resolver.get_app_data_path("logs", "launcher_pc.log")
logging.basicConfig(
    level=logging.INFO,
    format='[ArgosLauncher] %(asctime)s [%(levelname)s]: %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(log_file, encoding='utf-8')
    ]
)
logger = logging.getLogger("ArgosLauncher")

PORT = 8000
HOST = "127.0.0.1"
SERVER_START_ERROR = None
_instance_lock_socket = None


def check_single_instance():
    """Garantiza una única instancia activa del sistema vía Mutex de Kernel Win32."""
    if sys.platform != "win32":
        global _instance_lock_socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((HOST, 18000))
            _instance_lock_socket = s
            return True
        except socket.error:
            return False

    try:
        import ctypes
        mutex_name = "Global\\ArgosGuard_Enterprise_V4_Mutex"
        mutex = ctypes.windll.kernel32.CreateMutexW(None, False, mutex_name)
        if ctypes.windll.kernel32.GetLastError() == 183:  # ERROR_ALREADY_EXISTS
            return False
        return mutex
    except Exception as e:
        logger.error(f"Error al verificar Mutex: {e}")
        return True


def find_chrome():
    """Busca el ejecutable de Google Chrome (portátil o instalado en el sistema)."""
    # 1. Buscar Chrome portátil dentro de la carpeta de la aplicación
    portable_paths = [
        str(resolver.get_path("chrome", "chrome.exe")),
        str(resolver.get_path("chrome.exe")),
        str(resolver.get_app_data_path("chrome", "chrome.exe"))
    ]
    for p in portable_paths:
        if os.path.exists(p):
            return p

    # 2. Buscar Chrome instalado en el sistema operativo Windows / Linux
    if sys.platform != "win32":
        import shutil
        for cmd in ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]:
            path = shutil.which(cmd)
            if path:
                return path
        return None

    system_paths = [
        os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
    ]
    for p in system_paths:
        if os.path.exists(p):
            return p
    return None


def start_server():
    """Inicia el servidor WSGI multihilo Waitress en un hilo secundario dedicado."""
    global SERVER_START_ERROR
    try:
        logger.info("Inicializando configuración Django...")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
        import django
        django.setup()

        # Migraciones automáticas de la base de datos local SQLite
        try:
            logger.info("Ejecutando migraciones automáticas de base de datos...")
            from django.core.management import call_command
            call_command('migrate', interactive=False)
            logger.info("Migraciones aplicadas con éxito.")
        except Exception as e:
            logger.warning(f"Advertencia en migraciones: {e}")

        # Purgar sesiones antiguas
        try:
            from django.contrib.sessions.models import Session
            Session.objects.all().delete()
            logger.info("Sesiones antiguas limpiadas.")
        except Exception as e:
            logger.warning(f"Advertencia al limpiar sesiones: {e}")

        from config.wsgi import application
        logger.info(f"Servidor Waitress escuchando en http://{HOST}:{PORT}")
        serve(application, host=HOST, port=PORT, threads=8)
    except Exception as exc:
        SERVER_START_ERROR = exc
        logger.critical(f"ERROR FATAL al arrancar el servidor Waitress: {exc}")
        logger.critical(traceback.format_exc())


def kill_zombie_processes():
    """Destruye procesos de ejecuciones previas para evitar puertos o archivos bloqueados."""
    if os.name == 'nt':
        try:
            flags = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)
            subprocess.run("taskkill /F /IM chromedriver.exe /T", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=flags)
        except Exception as e:
            logger.warning(f"Advertencia al limpiar procesos: {e}")


def main():
    logger.info("=== Iniciando Argos Guard Enterprise v4.0 ===")
    
    # 0. Control de instancia única (Mutex)
    mutex = check_single_instance()
    if not mutex:
        logger.error("Argos Guard Enterprise ya se encuentra en ejecución. Cerrando segunda instancia.")
        sys.exit(0)

    # 1. Limpieza preventiva de zombies
    kill_zombie_processes()

    # 2. Iniciar servidor Waitress en hilo secundario
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # 3. Esperar confirmación de apertura del puerto HTTP
    retries = 15
    while retries > 0:
        if SERVER_START_ERROR is not None:
            logger.error("Error fatal detectado al iniciar el servidor.")
            sys.exit(1)
        try:
            with socket.create_connection((HOST, PORT), timeout=0.5):
                break
        except (OSError, socket.error):
            time.sleep(0.2)
            retries -= 1
    else:
        logger.error(f"El servidor Waitress no respondió en {HOST}:{PORT} después del tiempo de espera.")
        sys.exit(1)

    # 4. Lanzar la interfaz en Google Chrome (--app) o Navegador Predeterminado
    chrome_path = find_chrome()
    app_url = f"http://{HOST}:{PORT}"
    chrome_proc = None

    if chrome_path:
        logger.info(f"Lanzando Chrome en Modo App Standalone: {chrome_path}")
        flags = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000) if sys.platform == "win32" else 0
        chrome_proc = subprocess.Popen(
            [chrome_path, "--start-maximized", f"--app={app_url}"],
            creationflags=flags
        )
    else:
        logger.warning("Chrome no detectado en rutas estándar. Abriendo en navegador predeterminado...")
        webbrowser.open(app_url)

    # 5. Bucle guardián para monitorear el estado de la ventana principal
    logger.info("Argos Guard Enterprise v4.0 está operando exitosamente.")
    try:
        while True:
            # Si el usuario cierra la ventana de Chrome, finalizar el servidor limpiamente
            if chrome_proc and chrome_proc.poll() is not None:
                logger.info("Se detectó el cierre de la ventana del navegador. Finalizando Argos Guard...")
                break
            time.sleep(1.0)
    except (KeyboardInterrupt, SystemExit):
        logger.info("Recibida señal de detención...")
    finally:
        logger.info("Finalizando todos los servicios y saliendo.")
        kill_zombie_processes()
        os._exit(0)

if __name__ == "__main__":
    main()
