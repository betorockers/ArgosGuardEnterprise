# Plan de Implementación Quirúrgico — Adopción de Arquitectura Probada BetoGraf Almacenero v4.0

Este plan detalla los cambios quirúrgicos exactos para transformar la infraestructura de ejecución de **Argos Guard Enterprise v4.0**, adoptando la arquitectura indestructible comprobada en `BetoGraf_Almacenero_Django` (**Waitress + Chrome --app Mode + Win32 Mutex + Instalación LocalAppData sin UAC**).

---

## 🔍 Análisis de Cambios Quirúrgicos

| Componente | Estado Actual | Estado Propuesto (Patrón BetoGraf) | Beneficio Técnico |
|---|---|---|---|
| **Servidor WSGI Backend** | `wsgiref.simple_server` (Mono-hilo, se bloquea ante peticiones concurrentes). | **`Waitress`** (`from waitress import serve` con 8 hilos en segundo plano). | Servidor de producción multihilo 100% estable en Windows. No se congela nunca. |
| **Lanzador / Contenedor UI** | `PyQt6.QtWebEngineWidgets` (Colapsa en PCs sin drivers DirectX/OpenGL específicos). | **`launcher_pc.py`** con Chrome en modo `--start-maximized --app=http://127.0.0.1:8000` y fallback a `webbrowser.open`. | Cero choques de drivers gráficos. Funciona en el 100% de PCs con Windows 10/11 o Linux. |
| **Control de Instancia Única** | Sin control de Mutex Win32 nativo. | **Mutex Win32 Kernel** (`Global\ArgosGuard_Enterprise_V4_Mutex` vía `ctypes`). | Impide ejecuciones dobles que corrompan SQLite o bloqueen puertos. |
| **Ubicación de Instalación Inno Setup** | `C:\Program Files\...` (`PrivilegesRequired=admin`). | **`{localappdata}\Programs\ArgosGuardEnterpriseV4`** (`PrivilegesRequired=lowest`). | Cero bloqueos de permisos Windows UAC. Lectura/escritura limpia en AppData. |
| **Empaquetado Inno Setup** | Incluye bases de datos de desarrollo y requiere admin. | Excluye `.db`, `.db-shm`, `.db-wal` y logs locales. Instalador liviano en modo usuario. | Instalación limpia en 1 clic. |

---

## 🛠️ Cambios por Archivo (Paso a Paso)

### 1. [NEW] [backend_v4/launcher_pc.py](file:///e:/ProyectoMonitoreoMod_V2/backend_v4/launcher_pc.py)
- **Propósito**: Lanzador principal de producción para Argos Guard Enterprise v4.0.
- **Funcionalidad**:
  - Verificación de Mutex Win32 (`Global\ArgosGuard_Enterprise_V4_Mutex`).
  - Hilo de servidor Waitress escuchando en `127.0.0.1:8000` (o puerto libre).
  - Purgado automático de sesiones antiguas al iniciar.
  - Ejecución de migraciones automáticas de SQLite.
  - Apertura de Google Chrome en modo `--start-maximized --app=http://127.0.0.1:8000` o navegador predeterminado como fallback.
  - Hilo guardián de ventana para minimización limpia y exterminación de procesos al cerrar.

### 2. [MODIFY] [requirements.txt](file:///e:/ProyectoMonitoreoMod_V2/requirements.txt)
- **Modificación**: Incorporar `waitress>=3.0.0`.

### 3. [MODIFY] [backend_v4/apps/core/path_resolver.py](file:///e:/ProyectoMonitoreoMod_V2/backend_v4/apps/core/path_resolver.py)
- **Modificación**: Asegurar que `base_dir` resuelva correctamente tanto en modo desarrollo interpretado como congelado con Nuitka (`launcher_pc.exe`).

### 4. [MODIFY] [build_v4.ps1](file:///e:/ProyectoMonitoreoMod_V2/build_v4.ps1)
- **Modificación**:
  - Cambiar entrypoint de `run_kiosk.py` a `launcher_pc.py`.
  - Agregar `--include-package=waitress` a Nuitka.
  - Remover la dependencia problemática de `QtWebEngine` en Nuitka, simplificando la compilación y eliminando más de 180 MB de basura pesada e inestable.
  - Copia de `staticfiles` y `templates` a `launcher_pc.dist`.

### 5. [MODIFY] [installer_v4/installer_v4.iss](file:///e:/ProyectoMonitoreoMod_V2/installer_v4/installer_v4.iss)
- **Modificación**:
  - Actualizar `DefaultDirName` a `{localappdata}\Programs\ArgosGuardEnterpriseV4`.
  - Configurar `PrivilegesRequired=lowest` y `UsedUserAreasWarning=no`.
  - Excluir archivos locales: `Excludes: "*.db,*.db-shm,*.db-wal,*.log"`.
  - Agregar script de verificación e instalación desatendida de Google Chrome si no existe.

---

## 🧪 Plan de Verificación

1. **Instalación de Dependencias**:
   - `pip install waitress` en el entorno virtual `.venv`.
2. **Prueba de Ejecución Local**:
   - Ejecutar `python launcher_pc.py` en `backend_v4` para verificar arranque de Waitress y apertura en modo `--app`.
3. **Ejecución de Suite de Pruebas Unitarias (`pytest`)**:
   - Confirmar que los 10/10 tests unitarios continúen pasando sin fallos.
4. **Presentación de Resultados al Usuario**:
   - Esperar autorización explícita antes de ejecutar compilación e Inno Setup.
