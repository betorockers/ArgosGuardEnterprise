# Plan de Auditoría y Refuerzo de Autocontención 100% — Argos Guard Enterprise v4.0

Este documento especifica la auditoría estricta de cumplimiento de normas de portabilidad e independencia del sistema operativo host (Windows 10/11 Home/Pro/LTSC/IoT) para **Argos Guard Enterprise v4.0**, resolviendo cualquier dependencia residual de software o recursos preinstalados en la PC del cliente.

---

## 🔍 Diagnóstico y Brechas Identificadas en la Auditoría

Tras la inspección minuciosa del código fuente (`backend_v4`), scripts de compilación (`build_v4.ps1`) y receta de empaquetado (`installer_v4.iss`), se han identificado las siguientes brechas que impedían la autocontención del 100% en equipos limpios/air-gapped:

| Componente | Estado Actual | Riesgo en PC Limpia | Solución Propuesta |
|---|---|---|---|
| **Motor OSINT (Selenium / Chrome)** | `services.py` solo busca `chrome.exe` en rutas del host (`C:\Program Files\...`). | Si la PC host no tiene Google Chrome instalado, el raspado OSINT falla. | 1. Modificar `detect_chrome_executable()` para buscar en `{app}\chrome\chrome.exe` mediante `PathResolver`. <br>2. Incluir instalador desatendido de Google Chrome en `installer_v4.iss` (o carpeta portátil `{app}\chrome`). |
| **Plugins Nuitka Faltantes (`build_v4.ps1`)** | Solo se incluyen `--enable-plugin=pyqt6` y `anti-bloat`. | Faltan optimizaciones C/C++ nativas para `numpy` y `matplotlib` (gráficos PDF). | Agregar `--enable-plugin=numpy` y `--enable-plugin=matplotlib` en `build_v4.ps1`. |
| **Archivos de Datos de Paquetes Python** | No se incluyen `--include-package-data` para `matplotlib`, `seaborn`, `pandas`, `dns`, `limits` ni `selenium_stealth`. | En PCs sin Python, la generación de gráficos PDF o evasión de Cloudflare falla por fuentes/JS faltantes. | Agregar todas las banderas `--include-package-data` requeridas por las normas del proyecto en `build_v4.ps1`. |
| **Supresión de Consolas CMD (`CREATE_NO_WINDOW`)** | Implementado en `async_runner.py`, `security`, `licensing`. | 0 ventanas emergentes durante escaneo de red. | Mantenido y validado al 100%. |
| **Runtime C++ (VC++ Redistributable)** | Copia de DLLs de System32 + `vc_redist.x64.exe` embebido con `/passive /norestart`. | Garantiza ejecución en Windows recién instalado. | Mantenido y reinforced con verificación estricta. |
| **`qt.conf` y WebEngine Portable** | Generado automáticamente con `Prefix = PyQt6/Qt6`. | PyQt6 WebEngine resuelve librerías sin importar el PATH del sistema. | Mantenido y verificado. |

---

## 🛠️ Cambios Propuestos

### 1. [backend_v4/apps/osint/services.py](file:///e:/ProyectoMonitoreoMod_V2/backend_v4/apps/osint/services.py)
- **Modificación**: Actualizar `detect_chrome_executable()` para que utilice `PathResolver().get_path('chrome', 'chrome.exe')` antes de verificar las rutas globales de Windows.

### 2. [build_v4.ps1](file:///e:/ProyectoMonitoreoMod_V2/build_v4.ps1)
- **Modificación**: Incorporar los plugins de Nuitka y la inclusión explícita del 100% de los datos de paquetes Python requeridos:
  - `--enable-plugin=numpy`
  - `--enable-plugin=matplotlib`
  - `--include-package=limits`
  - `--include-package=selenium_stealth`
  - `--include-package-data=matplotlib`
  - `--include-package-data=seaborn`
  - `--include-package-data=pandas`
  - `--include-package-data=dns`
  - `--include-package-data=limits`
  - `--include-package-data=selenium_stealth`

### 3. [installer_v4/installer_v4.iss](file:///e:/ProyectoMonitoreoMod_V2/installer_v4/installer_v4.iss)
- **Modificación**: Vincular la función `NeedChrome` a la ejecución desatendida del instalador de Chrome en caso de que la PC de destino no disponga de una instalación previa de Chromium/Chrome.

---

## 🧪 Plan de Verificación

1. **Pruebas Unitarias (`pytest`)**:
   - Ejecutar la suite completa para asegurar que la resolución de rutas de Chrome y el empaquetado de paquetes no rompan las pruebas existentes (`24/24 PASSED`).
2. **Auditoría de Código y Manejo de Rutas**:
   - Validar que no exista ninguna ruta quemada a directorios personales del desarrollador ni dependencias externas de librerías globales.
3. **Solicitud de Autorización para Compilación**:
   - Presentar los resultados y esperar la orden explícita del usuario antes de proceder a cualquier compilación o empaquetado.
