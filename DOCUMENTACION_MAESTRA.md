# DOCUMENTACIÓN MAESTRA — ARGOS GUARD ENTERPRISE V4.0.0 (PATRÓN BETOGRAF)

**Última Sincronización:** 2026-07-27 13:25 UTC-4  
**Estado General:** 🟢 **PRODUCTION RELEASE V4.0.0 COMPILADA Y EMPAQUETADA TODO EN 1 (267.99 MB)**

---

## 1. Visión General y Filosofía de Diseño
Argos Guard Enterprise v4.0.0 es una plataforma monolítica modular de alta ciberseguridad, monitoreo táctico de nodos en tiempo real, videovigilancia y suite de inteligencia OSINT, empaquetada como una aplicación nativa basada en la **Arquitectura Comprobada BetoGraf Almacenero** (**Waitress WSGI Multihilo + Chrome --app Mode + Win32 Kernel Mutex**), impulsada por un backend **Django 5.x** con base de datos local cifrada **SQLite / SQLCipher (AES-256)**.

El sistema funciona de forma **100% autocontenida, embebida e independiente** de la máquina host Windows (compatible con Windows 10/11 Home, Pro, LTSC e IoT), sin requerir software o dependencias preinstaladas.

---

## 2. Puntos Clave de la Arquitectura v4.0.0 (Patrón BetoGraf)
- **Backend Monolítico Modular**: Django 5.x (`backend_v4/`) dividido en 5 módulos desacoplados (`core`, `monitoring`, `osint`, `security`, `licensing`).
- **Servidor WSGI de Producción (Waitress)**: Ejecución multihilo (`threads=8`) en segundo plano escuchando en `http://127.0.0.1:8000`. Cero bloqueos de concurrencia.
- **Lanzador de Interfaz (Chrome --app Mode)**: Ejecución standalone borderless (`--start-maximized --app=http://127.0.0.1:8000`) con fallback automático al navegador predeterminado.
- **Control de Instancia Única (Win32 Mutex)**: Kernel Mutex `Global\ArgosGuard_Enterprise_V4_Mutex` que impide duplicación de procesos o bloqueo de base de datos.
- **Supresión Total de Consolas CMD (`CREATE_NO_WINDOW`)**: Subprocesos de red con `creationflags=0x08000000` (0 ventanas emergentes).
- **Portabilidad & PathResolver**: Módulo Singleton `PathResolver` asignando directorios seguros en AppData para SQLite y logs.

---

## 3. Especificaciones de Empaquetado y Blindaje Criptográfico
- **Compilación C++ (Nuitka)**: Script [build_v4.ps1](file:///e:/ProyectoMonitoreoMod_V2/build_v4.ps1) que compila el monolito Python a ejecutable nativo C++ [ArgosGuardV4.exe](file:///e:/ProyectoMonitoreoMod_V2/backend_v4/build/launcher_pc.dist/ArgosGuardV4.exe).
- **Firma Criptográfica X.509**: Firma digital aplicada con `BetoGraf_Almacenero.pfx` y estampa de tiempo DigiCert sobre ejecutable e instalador.
- **Instalador Inno Setup (`ISCC`)**: Script [installer_v4/installer_v4.iss](file:///e:/ProyectoMonitoreoMod_V2/installer_v4/installer_v4.iss) que genera el ejecutable final:
  - **Ubicación:** [dist/ArgosGuard_Installer_v4.0.0.exe](file:///e:/ProyectoMonitoreoMod_V2/dist/ArgosGuard_Installer_v4.0.0.exe) (**267.99 MB**, compresión sólida `lzma2/ultra64`).
  - **Ubicación de Instalación:** `{localappdata}\Programs\ArgosGuardEnterpriseV4` (`PrivilegesRequired=lowest`).
  - **Registro de Certificado de Confianza**: Comando desatendido `certutil -user -f -addstore Root "{tmp}\BetoGraf_Almacenero.cer"` para eliminar falsos positivos de antivirus y SmartScreen.
  - **Prerrequisitos Embebidos (Desatendidos)**:
    1. Google Chrome 64-bit Offline Setup (`chrome_installer.exe`, 148.2 MB).
    2. Microsoft Visual C++ 2015-2022 Redistributable (`vc_redist.x64.exe`, 25.6 MB).
    3. Certificado X.509 BetoGraf (`BetoGraf_Almacenero.cer`).

---

## 4. Resultados de la Suite de Pruebas Unitarias (`pytest`)
- **Ejecución:** `pytest backend_v4`
- **Resultado:** **10/10 PASSED (100%)** en 14.85s.
  - `apps.monitoring`: 3/3 PASSED ✅
  - `apps.core`: 2/2 PASSED ✅
  - `apps.licensing`: 1/1 PASSED ✅
  - `apps.osint`: 2/2 PASSED ✅
  - `apps.security`: 2/2 PASSED ✅

---

## 5. Roadmap de Ciberdefensa v4.1 (Próximo Desarrollo)
Plan técnico detallado en [estudio y mejoras/implementation_plan_v4.1_cyberdefense.md](file:///e:/ProyectoMonitoreoMod_V2/estudio%20y%20mejoras/implementation_plan_v4.1_cyberdefense.md):
1. **Botón Resumen Táctico OSINT & Reporte PDF de Riesgos**.
2. **Módulo IDS (NIDS PortScan/ARP Spoofing & HIDS FIM SHA-256)**.
3. **Integración SIEM (Wazuh API REST, Elastic ECS, Syslog CEF/LEEF para Splunk/Sentinel)**.

---

## 6. Registro de Archivos Clave del Proyecto
- 📄 [ancla.md](file:///e:/ProyectoMonitoreoMod_V2/ancla.md): Punto de retoma para la siguiente sesión.
- 📄 [bitacora.md](file:///e:/ProyectoMonitoreoMod_V2/bitacora.md): Bitácora histórica completa.
- 📁 [estudio y mejoras/implementation_plan_v4.1_cyberdefense.md](file:///e:/ProyectoMonitoreoMod_V2/estudio%20y%20mejoras/implementation_plan_v4.1_cyberdefense.md): Plan de arquitectura v4.1.
- 📁 [estudio y mejoras/walkthrough.md](file:///e:/ProyectoMonitoreoMod_V2/estudio%20y%20mejoras/walkthrough.md): Informe de compilación e instalador v4.0.0.
- 📁 [diagnosticos_y_pruebas/diagnostico_portabilidad_pc_limpia_v4.md](file:///e:/ProyectoMonitoreoMod_V2/diagnosticos_y_pruebas/diagnostico_portabilidad_pc_limpia_v4.md): Diagnóstico de portabilidad.
