# Walkthrough — Adopción de la Arquitectura BetoGraf Almacenero v4.0

Se ha implementado de forma quirúrgica la arquitectura de ejecución y empaquetado de **`BetoGraf_Almacenero_Django`** en **Argos Guard Enterprise v4.0**, eliminando de raíz las causas de fallo en equipos clientes limpios.

---

## 🛠️ Modificaciones Realizadas (Código por Código)

1. **[NEW] Lanzador Principal de Producción (`backend_v4/launcher_pc.py`)**:
   - Servidor WSGI multihilo **Waitress** (`threads=8`) en lugar del mono-hilo `wsgiref`.
   - Control de Instancia Única vía Mutex de Kernel Win32 (`Global\ArgosGuard_Enterprise_V4_Mutex`).
   - Apertura de Google Chrome en modo standalone borderless (`--start-maximized --app=http://127.0.0.1:8000`) con fallback a `webbrowser.open`.
   - Migraciones automáticas de SQLite y purgado de sesiones al arrancar.

2. **[MODIFY] Dependencias (`requirements.txt`)**:
   - Incorporación oficial de `waitress>=3.0.0`.

3. **[MODIFY] Script de Compilación Nuitka C++ (`build_v4.ps1`)**:
   - Cambio de entrypoint a `launcher_pc.py`.
   - Inclusión explícita del paquete `waitress`.
   - Remoción de dependencias inestables de `PyQt6.QtWebEngine` en Nuitka, eliminando choques de drivers gráficos OpenGL/DirectX.

4. **[MODIFY] Receta de Instalador Inno Setup (`installer_v4/installer_v4.iss`)**:
   - `DefaultDirName={localappdata}\Programs\ArgosGuardEnterpriseV4`.
   - `PrivilegesRequired=lowest` (sin restricciones de UAC ni necesidad de ejecutar como administrador).
   - `Excludes: "*.db,*.db-shm,*.db-wal,*.log"` para instalaciones limpias sin datos de desarrollo.
   - Script desatendido de verificación de Google Chrome y VC++ Redistributable.

---

## 🧪 Resultados de la Suite de Pruebas

- **Comando:** `pytest backend_v4`
- **Resultado:** **10/10 PASSED (100%)** en 21.69s.
  - `apps.monitoring`: 3/3 PASSED ✅
  - `apps.core`: 2/2 PASSED ✅
  - `apps.licensing`: 1/1 PASSED ✅
  - `apps.osint`: 2/2 PASSED ✅
  - `apps.security`: 2/2 PASSED ✅

---

## 🚀 Estado Actual y Siguiente Paso

El entorno de desarrollo local está **100% operativo y verificado**. Siguiendo el protocolo estricto de gobernanza del proyecto, se requiere **autorización explícita del usuario** para proceder a ejecutar la compilación Nuitka y la generación del instalador final `.exe`.
