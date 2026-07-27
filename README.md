# Argos Guard Enterprise v4.0.0 — Production Release (Todo en 1)

Plataforma empresarial monolítica modular de alta ciberseguridad, monitoreo táctico de nodos en tiempo real y suite de inteligencia OSINT.

---

## 🌟 Características Principales

- **Arquitectura Monolítica Modular (Django 5.x)**: 5 aplicaciones desacopladas (`core`, `monitoring`, `osint`, `security`, `licensing`).
- **Contenedor Nativo Kiosko (PyQt6 QWebEngineView)**: Interfaz gráfica de alta densidad, cero ventanas de consola popups (`CREATE_NO_WINDOW`), soporte de hot-reload y notificaciones omnicanal (Toasts + Audio + Telegram).
- **Compilación Nativa a C++ (Nuitka)**: Traducción de código Python a binario ejecutable C++ nativo `ArgosGuardV4.exe` sin requerir interprete Python preinstalado.
- **Base de Datos Cifrada Local**: SQLite / SQLCipher (AES-256) administrada en AppData seguro mediante `PathResolver`.
- **100% Autocontenido y Portable**: Instalador ejecutable unico `dist/ArgosGuard_Installer_v4.0.0.exe` (**411.95 MB**) empaquetado con compresión sólida `lzma2/ultra64`, incluyendo instaladores desatendidos de **Microsoft Visual C++ Redistributable 2015-2022** y **Google Chrome 64-bit Offline Setup**.

---

## 📁 Estructura del Monorepo v4.0.0

```text
ProyectoMonitoreoMod_V2/
├── backend_v4/                # Monolito Django 5.x + PyQt6 Kiosk Runner
│   ├── config/                # Configuración global Django WSGI/ASGI
│   ├── apps/
│   │   ├── core/              # PathResolver, AsyncRunner, Loggers
│   │   ├── monitoring/        # TelemetryDaemon, TargetNodes, Events
│   │   ├── osint/             # Scrapers Selenium/HTTP, DNS Resolver
│   │   ├── security/          # RBAC, JWT, Argon2id, Firewall Controls
│   │   └── licensing/         # RSA HWID System Licensing
│   ├── static/                # Temas CSS, imágenes, efectos sonoros MP3
│   ├── templates/             # Plantillas HTML5 HTMX / Alpine.js
│   └── run_kiosk.py           # Entrypoint Kiosko Nativo PyQt6
├── build_v4.ps1               # Script de Compilación Nuitka C++ Standalone
├── installer_v4/              # Inno Setup Script (installer_v4.iss) + Prerrequisitos (Chrome/VC++)
├── dist/                      # Salida del Instalador (ArgosGuard_Installer_v4.0.0.exe)
├── diagnosticos_y_pruebas/    # Centralización de reportes de pruebas (pytest 10/10)
└── estudio y mejoras/         # Planes de implementación (v4.0 y v4.1) y Walkthroughs
```

---

## 🛠️ Ejecución en Desarrollo

```powershell
cd backend_v4
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run_kiosk.py
```

---

## 📦 Compilación C++ y Empaquetado

```powershell
# 1. Compilar binario C++ con Nuitka:
powershell -ExecutionPolicy Bypass -File .\build_v4.ps1

# 2. Generar Instalador Inno Setup:
ISCC.exe installer_v4\installer_v4.iss
```

---

## 📄 Documentación y Registros
- 📄 [DOCUMENTACION_MAESTRA.md](file:///e:/ProyectoMonitoreoMod_V2/DOCUMENTACION_MAESTRA.md)
- 📄 [ancla.md](file:///e:/ProyectoMonitoreoMod_V2/ancla.md)
- 📄 [bitacora.md](file:///e:/ProyectoMonitoreoMod_V2/bitacora.md)
- 📁 [estudio y mejoras/implementation_plan_v4.1_cyberdefense.md](file:///e:/ProyectoMonitoreoMod_V2/estudio%20y%20mejoras/implementation_plan_v4.1_cyberdefense.md)
