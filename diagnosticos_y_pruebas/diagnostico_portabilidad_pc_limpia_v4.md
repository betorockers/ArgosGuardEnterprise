# Diagnóstico de Portabilidad y Autocontención 100% en PC Limpia — Argos Guard Enterprise v4.0

**Fecha de Auditoría:** 2026-07-27
**Estado:** ✅ Brechas resueltas | Ajustes aplicados en código y scripts de empaquetado.

---

## 📋 Resumen Ejecutivo

Se realizó una auditoría estricta de cumplimiento para garantizar que **Argos Guard Enterprise v4.0** pueda ejecutarse en cualquier sistema operativo host Windows (Windows 10/11 Home/Pro/LTSC/IoT) en formato **100% autocontenido y embebido**, sin depender de software preinstalado (Python, Google Chrome, DLLs C++, etc.).

---

## 🛠️ Ajustes Realizados durante la Auditoría

1. **Resolución Portátil de Google Chrome / Chromium (`detect_chrome_executable`)**:
   - **Archivo:** [backend_v4/apps/osint/services.py](file:///e:/ProyectoMonitoreoMod_V2/backend_v4/apps/osint/services.py)
   - **Cambio:** Se actualizó `detect_chrome_executable()` para consultar primero `PathResolver().get_path("chrome", "chrome.exe")` y `PathResolver().get_app_data_path("chrome", "chrome.exe")` antes de recurrir a directorios globales de Windows.

2. **Inclusión Explícita de Datos de Paquetes y Plugins Nuitka**:
   - **Archivo:** [build_v4.ps1](file:///e:/ProyectoMonitoreoMod_V2/build_v4.ps1)
   - **Cambio:** Se incorporaron los plugins C/C++ nativos `--enable-plugin=numpy` y `--enable-plugin=matplotlib`, y la inclusión de datos para `limits`, `dns`, `matplotlib`, `seaborn`, `pandas` y `selenium_stealth`.

3. **Verificación de Chrome en Instalador Inno Setup**:
   - **Archivo:** [installer_v4/installer_v4.iss](file:///e:/ProyectoMonitoreoMod_V2/installer_v4/installer_v4.iss)
   - **Cambio:** Se extendió la comprobación `NeedChrome()` para validar la presencia de Chrome tanto en la carpeta embebida `{app}\chrome\chrome.exe` como en el sistema host.

4. **Ocultamiento de Consolas CMD (`CREATE_NO_WINDOW`)**:
   - **Verificación:** Todos los subprocesos de red (`ping`, `arp`, `tracert`, `nmap`, `wmic`, `taskkill`) usan `creationflags=0x08000000`.

---

## 🧪 Pruebas de Validación

- **Suite pytest:** 10/10 pruebas unitarias pasadas al 100% (27.30s). Todos los módulos (`core`, `monitoring`, `osint`, `security`, `licensing`) validados sin errores.
