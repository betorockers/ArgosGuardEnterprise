# Reporte de Diagnóstico: Error Crítico de Inicialización en Kiosko v4.0

**Fecha:** 2026-07-24  
**Modulo:** `backend_v4 / run_kiosk.py`  
**Incidente:** El ejecutable / kiosko `Argos Guard v4.0` lanza una ventana emergente nativa con el mensaje:
> *"Error crítico de inicialización: El servidor interno de Argos Guard no pudo iniciar en el tiempo límite."*

---

## 🔍 Análisis de Causa Raíz (Empírico desde `kiosk_engine.log`)

Al inspeccionar la bitácora de ejecución runtime en `%LOCALAPPDATA%\ArgosGuardEnterpriseV4\kiosk_engine.log`, se detectó el siguiente traceback en el hilo del servidor Django:

```text
[2026-07-24 15:25:31] ERROR en Servidor Django: Traceback (most recent call last):
  File "C:\PROGRA~1\ARGOSG~1\run_kiosk.py", line 49, in run_django_server
  File "C:\PROGRA~1\ARGOSG~1\django\core\wsgi.py", line 12, in get_wsgi_application
  File "C:\PROGRA~1\ARGOSG~1\django\__init__.py", line 24, in setup
  ...
  File "C:\PROGRA~1\ARGOSG~1\django\utils\translation\trans_real.py", line 180, in __init__
OSError: No translation files found for default language es-cl.
```

### 1. Fallo Principal: Idioma `es-cl` Desconocido por Django (`OSError`)
- En `backend_v4/config/settings.py`, el parámetro `LANGUAGE_CODE` estaba configurado como `'es-cl'`.
- Django nativo no incluye un paquete de idioma por defecto para la variante regional `'es-cl'`, sino para `'es'`. Al compilar o ejecutar sin la carpeta de traducción nativa de esa variante, `django.setup()` interrumpe abruptamente el arranque levantando una excepción `OSError`.
- Al fallar `get_wsgi_application()`, el servidor WSGI `make_server()` jamás se inicia y el socket en el puerto `127.0.0.1:port` nunca se abre.
- Tras 12 segundos, `wait_for_server()` concluye el timeout y activa la alerta nativa `MessageBoxW`.

### 2. Fallo Secundario: Falta de Migraciones Automáticas en Instalación Limpia
- Al instalar el software por primera vez, la base de datos `%LOCALAPPDATA%\ArgosGuardEnterpriseV4\argos_guard_v4.db` no existe o no tiene las tablas iniciales creadas (`auth_user`, `django_session`, `monitoring_targetnode`).
- `run_kiosk.py` no ejecutaba automáticamente `call_command('migrate')` previo al inicio del servidor WSGI.

### 3. Advertencia: Comando Deprecado `wmic` en Windows 11
- La función `kill_zombie_processes()` usaba `wmic process ...`, comando discontinuado y deshabilitado por defecto en Windows 11 24H2+, generando errores no fatales en el log.

---

## 🛠️ Plan de Fórmulas y Soluciones

1. **Ajuste de Idioma en `config/settings.py`**:
   - Cambiar `LANGUAGE_CODE = 'es-cl'` por `LANGUAGE_CODE = 'es'`, que es el estándar oficial soportado sin dependencias externas por Django.

2. **Auto-Migración en `run_kiosk.py`**:
   - Insertar la ejecución automática de `django.setup()` y `call_command('migrate', interactive=False)` antes de inicializar `get_wsgi_application()` en `run_django_server()`.

3. **Optimización de Limpieza de Procesos**:
   - Reemplazar la llamada a `wmic` por un método seguro basado en `subprocess` con supresión de fallos o filtrado directo vía `tasklist` / `taskkill`.
