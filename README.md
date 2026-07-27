# Argos Guard Enterprise v4.0.0 — Software Corporativo Táctico de Monitoreo & Ciberdefensa (Todo en 1)

[![Release v4.0.0](https://img.shields.io/badge/Release-v4.0.0-blue.svg)](https://github.com/betorockers/ArgosGuardEnterprise/releases/tag/v4.0.0)
[![Descargar Instalador](https://img.shields.io/badge/Descargar-Instalador_v4.0.0_(411MB)-green.svg)](https://github.com/betorockers/ArgosGuardEnterprise/releases/tag/v4.0.0)
[![Licencia Perpetua](https://img.shields.io/badge/Licencia-Perpetua_HWID-purple.svg)](#-tiers-de-licenciamiento-comercial)
[![Windows 10/11](https://img.shields.io/badge/OS-Windows_10%2F11_Home%2FPro%2FLTSC-0078D6.svg)](#-puntos-fuertes--filosofía-de-diseño-v400)

Plataforma monolítica modular nativa para monitoreo táctico de nodos en tiempo real, videovigilancia multi-protocolo, inteligencia OSINT y suite de ciberdefensa, empaquetada en un ejecutable **100% autocontenido y portable** para Windows.

---

## 🚀 Enlace Directo de Descarga del Release

> [!IMPORTANT]
> 📥 **[Descargar Argos Guard Enterprise v4.0.0 (Instalador Todo en 1 - 411 MB)](https://github.com/betorockers/ArgosGuardEnterprise/releases/tag/v4.0.0)**  
> *Incluye binario nativo C++ `ArgosGuardV4.exe`, instaladores desatendidos de Google Chrome 64-bit y Microsoft Visual C++ 2015-2022 Redistributable, base de datos cifrada SQLCipher (AES-256) y runtime completo.*

---

## 🌟 Puntos Fuertes & Filosofía de Diseño v4.0.0

- **100% Autocontenido & Air-Gapped**: Funciona en cualquier equipo host con Windows 10/11 sin necesidad de conexión a internet previa, Python ni dependencias de software preinstaladas.
- **Arquitectura Monolítica Modular (Django 5.x + C++ Nuitka)**: 5 submódulos aislados (`core`, `monitoring`, `osint`, `security`, `licensing`) traducidos a binario ejecutable C++ nativo.
- **Contenedor Nativo Kiosko (PyQt6 QWebEngineView)**: Interfaz gráfica táctica anti-flicker con supresión total de consolas emergentes (`CREATE_NO_WINDOW`) y notificaciones omnicanal (Toasts + Audio + Telegram).
- **Seguridad Criptográfica**: Hashing Argon2id (OWASP 2024), JWT Dual-Token y licencias atadas a la huella digital física del procesador/tarjeta madre (HWID RSA-2048).

---

## 📈 Análisis Competitivo del Mercado (2026)

| Competidor | Modelo Comercial | Costo Estimado (500 Nodos) | Ventajas Únicas de Argos Guard Enterprise |
| :--- | :--- | :--- | :--- |
| **PRTG Paessler** | Suscripción recurrente por sensor | **$3,500 - $5,000 USD / Año** | **Pago Único Perpetuo**. Sin cobros por sensores ni suscripciones. |
| **Nagios XI** | Licencia inicial + mant. anual | **$3,500+ USD inicial** | **Kiosko Nativo Windows**. Instalación en 1 clic sin Linux complejo. |
| **Datadog** | SaaS Nube | **$30,000+ USD / Año** | **100% Local / On-Premise**. Soberanía total de datos sin enviar IP a la nube. |
| **Argos Guard Enterprise** | **Pago Único Perpetuo (HWID)** | **Desde $299 USD** | **Agentless L3/L7, SQLCipher Cifrado, OSINT + Videovigilancia Integrada**. |

---

## 💰 Tiers de Licenciamiento Comercial

*Licenciamiento perpetuo de pago único sin mensualidades:*

### 🟢 Argos Guard BASIC — $299 USD (Pago Único)
- Hasta 50 nodos / IPs monitoreadas.
- Ping ICMP/TCP de alta frecuencia y alertas sonoras.
- Base de datos cifrada SQLite / SQLCipher.

### 🔵 Argos Guard STANDARD — $699 USD (Pago Único - Recomendado)
- Hasta 250 nodos / IPs monitoreadas.
- Todo lo del plan Basic + Bot de Notificaciones Telegram en tiempo real.
- Módulo de Videovigilancia (MJPEG/HLS/RTSP) y 3 usuarios RBAC.

### 🟣 Argos Guard ENTERPRISE — $1,499 USD (Pago Único)
- Nodos e IPs **ILIMITADAS**.
- Todo lo del plan Standard + Auditoría de Red OSINT avanzada y exportación de reportes PDF.
- Soporte prioritario y usuarios ilimitados.

---

## ⚙️ Arquitectura Técnica v4.0.0

```text
┌─────────────────────────────────────────────────────────────┐
│               ARGOS GUARD ENTERPRISE V4.0.0                 │
├─────────────────────────────────────────────────────────────┤
│  PyQt6 QWebEngineView (Contenedor Kiosko Nativo Borderless) │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ UI HTMX + Alpine.js (6 Tabs Tácticas Anti-Flicker)    │  │
│  └───────────────────────────▲───────────────────────────┘  │
│                              │ WS / REST                    │
│  ┌───────────────────────────▼───────────────────────────┐  │
│  │ Django 5.x WSGI Server (Monolito C++ Nuitka)          │  │
│  │ ├─ TelemetryDaemon (ICMP/TCP Probes Asíncronas)       │  │
│  │ ├─ OSINT Automation & Scrapers (Selenium / DNS)       │  │
│  │ └─ Security & Auth (Argon2id, Dual-Token JWT, RBAC)   │  │
│  └───────────────────────────▲───────────────────────────┘  │
│                              │                              │
│  ┌───────────────────────────▼───────────────────────────┐  │
│  │ Base de Datos Cifrada Local (SQLCipher AES-256)       │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Instalación y Requisitos

- **Sistema Operativo**: Windows 10 / 11 (Home, Pro, LTSC, IoT) de 64 bits.
- **Instalación en 1-Clic**: Descargar y ejecutar `ArgosGuard_Installer_v4.0.0.exe`. El instalador configurará automáticamente los binarios y prerrequisitos.

---

## 👥 Empresa y Desarrollador

Desarrollado de forma exclusiva por **Betograf_inc**  
*Staff Architect:* **betorock**  
*Repositorio Oficial:* [github.com/betorockers/ArgosGuardEnterprise](https://github.com/betorockers/ArgosGuardEnterprise)
