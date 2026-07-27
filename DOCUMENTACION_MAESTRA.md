# DOCUMENTACIÓN MAESTRA — ARGOS GUARD ENTERPRISE V4.0.0

**Última Sincronización:** 2026-07-27 12:00 UTC-4  
**Estado General:** ❄️ **PRODUCTION RELEASE V4.0.0 CONGELADA Y EMPAQUETADA TODO EN 1 (411.95 MB)**

---

## 1. Visión General y Filosofía de Diseño
Argos Guard Enterprise v4.0.0 es una plataforma monolítica modular de alta ciberseguridad, monitoreo táctico de nodos en tiempo real y suite de inteligencia OSINT, empaquetada como una aplicación nativa de escritorio Kiosko en **PyQt6 QWebEngineView** impulsada por un backend **Django 5.x** con base de datos local cifrada **SQLite / SQLCipher (AES-256)**.

El sistema funciona de forma **100% autocontenida, embebida e independiente** de la máquina host Windows (compatible con Windows 10/11 Home, Pro, LTSC e IoT), sin requerir software o dependencias preinstaladas.

---

## 2. Puntos Clave de la Arquitectura v4.0.0
- **Backend Monolítico Modular**: Django 5.x (`backend_v4/`) dividido en 5 módulos desacoplados (`core`, `monitoring`, `osint`, `security`, `licensing`).
- **UI/UX Táctica**: Renderizado híbrido servidor/cliente (HTMX + Alpine.js + PyQt6 WebEngine). 6 pestañas principales (Monitoreo Activo, Mapa Táctico, Historial de Eventos, Videovigilancia, OSINT, Configuración).
- **Motor de Monitoreo en Segundo Plano**: Demonio síncrono/asíncrono (`TelemetryDaemon`) ejecutor de verificaciones ICMP/TCP de alta densidad sin bloqueo de interfaz.
- **Supresión Total de Consolas CMD (`CREATE_NO_WINDOW`)**: Todos los subprocesos de red (`ping`, `arp`, `tracert`, `nmap`, `wmic`, `taskkill`) utilizan `creationflags=0x08000000` para garantizar 0 ventanas emergentes.
- **Portabilidad & PathResolver**: Módulo Singleton `PathResolver` que detecta ejecutable congelado con Nuitka (`sys.executable`) y asigna directorios seguros en AppData para SQLite y logs.

---

## 3. Especificaciones de Empaquetado y Distribución "Todo en 1"
- **Compilación C++ (Nuitka)**: Script [build_v4.ps1](file:///e:/ProyectoMonitoreoMod_V2/build_v4.ps1) que compila el monolito Python a ejecutable nativo C++ [ArgosGuardV4.exe](file:///e:/ProyectoMonitoreoMod_V2/backend_v4/build/run_kiosk.dist/ArgosGuardV4.exe).
- **Plugins y Paquetes de Datos Embebidos**:
  - Plugins Nuitka: `pyqt6`, `numpy`, `matplotlib`, `anti-bloat`.
  - Paquetes de datos completos: `matplotlib`, `seaborn`, `pandas`, `dns`, `limits`, `fpdf`, `tzdata` (zonas horarias universales).
- **Librerías C++ y Qt Config**: Generación automática de `qt.conf` (`Prefix = PyQt6/Qt6`) y copia de DLLs de runtime (`vcruntime140.dll`, `msvcp140.dll`, `d3dcompiler_47.dll`, `opengl32sw.dll`, `concrt140.dll`, `vccorlib140.dll`).
- **Instalador Inno Setup (`ISCC`)**: Script [installer_v4/installer_v4.iss](file:///e:/ProyectoMonitoreoMod_V2/installer_v4/installer_v4.iss) que genera el ejecutable final:
  - **Ubicación:** [dist/ArgosGuard_Installer_v4.0.0.exe](file:///e:/ProyectoMonitoreoMod_V2/dist/ArgosGuard_Installer_v4.0.0.exe) (**411.95 MB**, compresión sólida `lzma2/ultra64`).
  - **Prerrequisitos Embebidos (Desatendidos)**:
    1. Google Chrome 64-bit Offline Setup (`chrome_installer.exe` - v152.0.7933.0, 148.2 MB).
    2. Microsoft Visual C++ 2015-2022 Redistributable (`vc_redist.x64.exe`, 25.6 MB).

---

## 4. Resultados de la Suite de Pruebas Unitarias (`pytest`)
- **Ejecución:** `pytest backend_v4`
- **Resultado:** **10/10 PASSED (100%)** en 27.30s.
  - `apps.monitoring`: 3/3 PASSED ✅
  - `apps.core`: 2/2 PASSED ✅
  - `apps.licensing`: 1/1 PASSED ✅
  - `apps.osint`: 2/2 PASSED ✅
  - `apps.security`: 2/2 PASSED ✅

---

## 5. Roadmap de Ciberdefensa v4.1 (Próximo Desarrollo)
Plan técnico de desarrollo aprobado en [estudio y mejoras/implementation_plan_v4.1_cyberdefense.md](file:///e:/ProyectoMonitoreoMod_V2/estudio%20y%20mejoras/implementation_plan_v4.1_cyberdefense.md):

1. **Botón Resumen Táctico OSINT & Reporte PDF de Riesgos**:
   - Botón `📄 Resumen Táctico` debajo del input principal OSINT.
   - Evaluación automatizada de vulnerabilidades, matriz de vectores de ataque explotables (Phishing, MITM, Ransomware RDP) y guía de hardening accionable.
2. **Módulo IDS (Intrusion Detection System)**:
   - NIDS: Detección de escaneos de puertos masivos (Port Scanning), barridos ICMP y envenenamiento ARP (ARP Spoofing / MITM).
   - HIDS: Monitoreo de Integridad de Archivos (FIM SHA-256) sobre `ArgosGuardV4.exe` y la DB local.
   - Respuesta Activa IPS: Aislamiento táctico de IP en Windows Firewall (`netsh advfirewall`).
3. **Integración SIEM (Security Information & Event Management)**:
   - Conector bidireccional Wazuh API REST.
   - Exportador Elastic SIEM / ECS JSON.
   - Emisor Syslog CEF/LEEF para Splunk, IBM QRadar y Microsoft Sentinel.

---

## 6. Registro de Archivos Clave del Proyecto
- 📄 [ancla.md](file:///e:/ProyectoMonitoreoMod_V2/ancla.md): Punto de retoma para la siguiente sesión.
- 📄 [bitacora.md](file:///e:/ProyectoMonitoreoMod_V2/bitacora.md): Bitácora histórica completa.
- 📁 [estudio y mejoras/implementation_plan_v4.1_cyberdefense.md](file:///e:/ProyectoMonitoreoMod_V2/estudio%20y%20mejoras/implementation_plan_v4.1_cyberdefense.md): Plan de arquitectura v4.1.
- 📁 [estudio y mejoras/walkthrough.md](file:///e:/ProyectoMonitoreoMod_V2/estudio%20y%20mejoras/walkthrough.md): Informe de compilación e instalador v4.0.0.
- 📁 [diagnosticos_y_pruebas/diagnostico_portabilidad_pc_limpia_v4.md](file:///e:/ProyectoMonitoreoMod_V2/diagnosticos_y_pruebas/diagnostico_portabilidad_pc_limpia_v4.md): Diagnóstico de portabilidad.
