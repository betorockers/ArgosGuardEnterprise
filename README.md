# 🛡️ Argos Guard Enterprise v3.0

[![Python Version](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Next.js Version](https://img.shields.io/badge/Next.js-16.2-black.svg)](https://nextjs.org/)
[![Package Manager](https://img.shields.io/badge/pnpm-11.5-orange.svg)](https://pnpm.io/)
[![Security Level](https://img.shields.io/badge/Security-Military%20%2F%20Industrial-red.svg)](#-arquitectura-de-seguridad-y-blindaje-militar)
[![License](https://img.shields.io/badge/License-Commercial%20Enterprise-gold.svg)](#-licenciamiento)

**Argos Guard Enterprise** es la solución definitiva de monitoreo activo de redes locales (LAN) y servicios aplicativos en la nube (L7). Diseñada bajo la filosofía de "Caja Negra" (Black-Box Agentless), permite vigilar la disponibilidad, latencia y salud de infraestructura crítica de seguridad (como cámaras LPR, tótems de control de acceso, gateways de pago, servidores web, bases de datos y dispositivos de red) sin requerir agentes instalados en los destinos.

Esta versión 3.6.2 consolida la evolución hacia una **Arquitectura de Escritorio Nativa (PyWebView)** y un backend asíncrono robusto, eliminando dependencias de navegadores externos y parpadeos molestos, y sumando integraciones con la nube de Supabase y alertas de Telegram.

---

## 🚀 Capacidades y Funcionalidades Clave

### 🔹 Funciones Principales (Core)
*   **Interfaz Nativa de Escritorio:** Interfaz impulsada por PyWebView que actúa como aplicación de Windows sin depender de Chrome o Edge, integrándose con cuadros de diálogo nativos del explorador de archivos.
*   **Anti-Parpadeo (Flicker-Free):** Integración profunda con la API de subprocesos de Windows (`CREATE_NO_WINDOW`) que permite ejecuciones de ICMP/Nmap asíncronas totalmente silenciosas y limpias de fondo.
*   **Monitoreo L3 Asíncrono de Alto Rendimiento:** Ping ICMP no bloqueante e independiente en paralelo para cientos de direcciones IP concurrentes usando `asyncio` de Python.
*   **Monitoreo L7 (Web Probes):** Consultas periódicas a endpoints HTTP/HTTPS con validación de códigos de estado de respuesta (ej: 200 OK) y búsqueda de palabras clave dentro del cuerpo de la respuesta para garantizar que las páginas web operen correctamente.
*   **Monitoreo de Certificados SSL/TLS:** Análisis automatizado de las cadenas de confianza HTTP y cálculo predictivo de días de expiración con alertas proactivas si restan menos de 15 días de validez.
*   **Escaneo de Puertos Activo (Port Auditing):** Detección asíncrona periódica de puertos abiertos para control de vulnerabilidades e intrusiones.
*   **Auditoría y Mapeo ARP:** Resolución automática y mapeo constante de direcciones MAC físicas de la red local para verificar la autenticidad física de las IPs (Detección de spoofing).
*   **Alertas Asíncronas Multicanal (Telegram):** Integración nativa con la API de bots de Telegram para notificar de inmediato caídas, recuperaciones de dispositivos, creación/eliminación de equipos y eliminación de usuarios.

### 🔹 Funciones Secundarias (Control y Operación)
*   **Telemetría en Tiempo Real:** Dashboard dinámico Next.js que se actualiza instantáneamente sin necesidad de recargar la página mediante canales persistentes de WebSockets.
*   **Log de Auditoría Completo:** Trazabilidad inalterable de cada evento de red, cambios de configuración, inicios de sesión y bloqueos en una base de datos segura.
*   **Histórico y Métricas en Serie Temporal:** Gráficos intuitivos de rendimiento de latencia histórica y tiempos de respuesta.
*   **Sistema de Licencias RSA-2048 / HWID:** Control estricto de despliegues comerciales bloqueado a la huella digital física del hardware del servidor cliente.

---

## 🛡️ Arquitectura de Seguridad y Blindaje Militar

Argos Guard Enterprise ha sido auditado y blindado contra vectores de ataque del OWASP Top 10 bajo estrictos estándares militares e industriales:

1.  **Protección de Credenciales (Argon2id):** Almacenamiento seguro de contraseñas utilizando hashing unidireccional con Argon2id configurado según los estándares OWASP (64MB de coste de memoria, 3 iteraciones de CPU, 4 hilos en paralelo). Este algoritmo es altamente resistente al agrietamiento por GPU y ASICs.
2.  **Autenticación Multifactor (MFA/TOTP):** Integración nativa para la configuración de un segundo factor dinámico usando tokens TOTP con cualquier aplicación autenticadora (Google Authenticator, Authy, etc.) mediante códigos QR temporales.
3.  **Control de Acceso Basado en Roles Jerárquicos (RBAC Estricto):**
    *   `super_admin`: Control absoluto del sistema. Es **invisible e intocable** para los administradores de menor rango.
    *   `admin`: Gestión de equipos, creación y gestión de usuarios menores, y acceso a logs. No puede escalar ni comprometer al super_admin.
    *   `operator`: Creación, actualización y monitoreo activo de equipos y sondas.
    *   `reader`: Visualización en tiempo real del dashboard y métricas (Solo Lectura).
4.  **Anti-Fuerza Bruta (Login Rate Limiter):** Limitador de tasa asíncrono en memoria usando el algoritmo Token Bucket que restringe los inicios de sesión a un máximo de **5 intentos cada 30 segundos por IP**, previniendo ataques de diccionario y recolección de usuarios (scraping).
5.  **Anti-WebScraping y Protección de Endpoints:** Límite general de la API de **60 peticiones por minuto por IP** en todos los endpoints de datos sensibles (métricas, logs, equipos) para evitar descargas automatizadas masivas de la estructura de la red local.
6.  **Cabeceras de Seguridad Militar HTTP:**
    *   `X-Frame-Options: DENY` para mitigar ataques de secuestro de clics (Clickjacking).
    *   `X-Content-Type-Options: nosniff` para desactivar el rastreo MIME no seguro.
    *   `Content-Security-Policy (CSP)` restrictivo para prevenir inyecciones XSS bloqueando recursos no autorizados.
    *   `Strict-Transport-Security (HSTS)` forzado en entornos de producción.
7.  **Inyección de Comandos Bloqueada:** Todos los comandos de red externos (Pings, ARP) son ejecutados a través de listas sanitizadas con `asyncio.create_subprocess_exec` desactivando de forma estricta el procesador del shell del sistema operativo (`shell=False`), lo que hace técnicamente imposible una inyección de comandos remota.

---

## 📈 Análisis de Tendencias de Mercado y Dolores que Solucionamos

### 📉 Dolores del Mercado Solucionados
1.  **Costos Exorbitantes de SaaS:** En 2026, la mayoría de herramientas de monitoreo de red (Datadog, LogicMonitor, Kentik) cobran tarifas recurrentes elevadas basadas en la cantidad de hosts y el volumen de telemetría. Para una organización con cientos de cámaras o terminales IoT, esto es financieramente inviable. **Argos Guard Enterprise soluciona esto mediante un licenciamiento de pago único auto-alojado sin costes ocultos.**
2.  **Soberanía de Datos e Infraestructura Crítica:** Muchas agencias de seguridad física, aeropuertos y plantas industriales tienen prohibido enviar la topología de su red local, direcciones IP o logs de eventos a la nube (nube SaaS). **Argos Guard es 100% On-Premise, manteniendo toda la información confidencial de forma local en SQLite encriptado (WAL) o bases de datos internas.**
3.  **Complejidad de Agentes:** El monitoreo tradicional con Zabbix o Nagios requiere la configuración compleja de demonios SNMP o agentes residentes en cada equipo. En cámaras IP o controladores IoT de acceso esto no es factible. **Argos Guard es completamente "Agentless" (L3/L7 Black-Box).**
4.  **Fatiga por Alertas y Spam:** Los administradores sufren de fatiga de notificaciones al recibir alertas a altas horas de la noche. **Nuestra función de Telegram permite acotar el horario de envío en una ventana personalizada de alertas laborales.**

### 📊 Comparativa de Mercado

| Característica | Argos Guard Enterprise v3.0 | Datadog / SaaS | PRTG Monitor | Nagios / Zabbix |
| :--- | :--- | :--- | :--- | :--- |
| **Arquitectura de Despliegue** | On-Premise (Local/Docker) | Cloud (SaaS Externo) | Windows Server local | On-Premise / Agentes |
| **Modelo de Costos** | Licencia Única / Perpetua | Suscripción Mensual Excesiva | Licencia por Sensores (Caras) | Open Source (Alto costo de soporte) |
| **Instalación de Agentes** | **No requiere (Agentless)** | Requiere agente instalado | No requiere | Requiere agentes y SNMP |
| **Seguridad de Acceso** | Argon2id + MFA + RBAC | Autenticación Cloud | Acceso Básico local | Parches de Seguridad manuales |
| **Control Anti-Scraping / Rate Limit** | **Sí (Token Bucket nativo)** | Sí (General) | No cuenta | No cuenta de forma nativa |
| **Instalador Inteligente** | **Sí (Autoinstalador de dependencias)** | Sí | Complejo | Extremadamente complejo |
| **Integración de Alertas** | Telegram / Ventana Horaria | Multi-integración | Correos / SMS | Scripts complejos |

---

## ⚙️ Arquitectura Técnica de Despliegue

```
┌─────────────────────────────────────────────────────────────┐
│                    ARGOS GUARD ENTERPRISE v3.0               │
├──────────────────────┬──────────────────────────────────────┤
│   FRONTEND           │   BACKEND                             │
│   Next.js 16         │   FastAPI + Uvicorn                   │
│   (Turbopack)        │   Python 3.13                         │
│   :3000              │   :8000                               │
│                      │                                        │
│  ┌──────────────┐    │  ┌─────────────────────────────────┐  │
│  │  Login Page  │    │  │  Routers (Rate limited API)      │  │
│  │  Dashboard   │◄───┤  │  ├─ /api/v1/auth/*              │  │
│  │  Devices     │    │  │  ├─ /api/v1/devices/*            │  │
│  │  Metrics     │    │  │  ├─ /api/v1/metrics/*            │  │
│  │  License     │    │  │  └─ /ws/monitor (WebSockets)     │  │
│  └──────────────┘    │  └─────────────────────────────────┘  │
│         ▲            │                │                        │
│         │ WS         │  ┌─────────────▼───────────────────┐  │
│  ┌──────┴───────┐    │  │  AsyncPingEngine                  │  │
│  │ WebSocket    │    │  │  - Ping (L3) & HTTP Probes (L7)  │  │
│  │ Context      │◄───┤  │  - Telegram Alerts (Asíncrono)  │  │
│  └──────────────┘    │  └─────────────────────────────────┘  │
│                      │                │                        │
│                      │  ┌─────────────▼───────────────────┐  │
│                      │  │  AsyncDatabaseManager            │  │
│                      │  │  SQLite WAL / PostgreSQL pool    │  │
│                      │  └─────────────────────────────────┘  │
└──────────────────────┴──────────────────────────────────────┘
```

---

## 🛠️ Guía Rápida de Despliegue

### Requisitos Previos
*   **Docker Desktop** y **Docker Compose** instalados (entorno de producción).
*   **Python 3.13+** y **Node.js 20+** (entorno de desarrollo local).

### Despliegue en Producción (Docker)
1.  Clonar el repositorio en el servidor de destino.
2.  Configurar las variables de entorno en el archivo `.env`.
3.  Ejecutar el instalador automatizado para Windows:
    ```powershell
    .\installer.bat
    ```
    *Este script validará prerrequisitos, comprobará si existe Edge/Chrome (instalándolo de forma silenciosa y segura en caso de ausencia), compilará las imágenes Docker y levantará el servicio completo.*

### Ejecución en Modo Nativo (Escritorio)
Para arrancar Argos Guard con una experiencia idéntica a una aplicación de escritorio nativa:
1.  Asegúrese de tener activado su entorno virtual y los servidores corriendo.
2.  Ejecute el lanzador en la raíz:
    ```powershell
    python main.py
    ```
    *Este comando detectará la API, compilará y abrirá automáticamente Microsoft Edge o Google Chrome en modo de aplicación borderless (`--app`) a pantalla completa.*

---

## 👥 Equipo y Soporte

Desarrollado de forma exclusiva por **Betograf_inc**  
*Staff Architect:* **betorock**
