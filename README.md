<div align="center">

<img src="https://raw.githubusercontent.com/betorockers/ArgosGuardEnterprise/main/assets/img/LogoArgosGuard.png" alt="Argos Guard Enterprise" width="120"/>

# ARGOS GUARD ENTERPRISE

### Plataforma Profesional de Monitoreo de Red & Seguridad Operacional

[![Version](https://img.shields.io/badge/Version-3.6.2-cyan?style=for-the-badge&logo=shield)](https://github.com/betorockers/ArgosGuardEnterprise/releases)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge&logo=windows)](https://github.com/betorockers/ArgosGuardEnterprise/releases)
[![Backend](https://img.shields.io/badge/Backend-FastAPI%20%2B%20Python-green?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Frontend](https://img.shields.io/badge/Frontend-Next.js%2015-black?style=for-the-badge&logo=nextdotjs)](https://nextjs.org)
[![License](https://img.shields.io/badge/License-Commercial-orange?style=for-the-badge)](https://betograf.cl)

---

**🛡️ Monitoreo continuo · Alertas en tiempo real · Seguridad de red empresarial**

[⬇️ Descargar Ahora](#-descarga-directa) · [📄 Documentación](#-características-principales) · [💬 Soporte](#-soporte-y-contacto)

</div>

---

## ¿Qué es Argos Guard Enterprise?

**Argos Guard Enterprise** es una plataforma de monitoreo de infraestructura de red diseñada para equipos de TI, administradores de sistemas y equipos de operaciones que necesitan **visibilidad total, alertas instantáneas y control de seguridad** sobre su red en tiempo real.

Desarrollado con arquitectura moderna (FastAPI + Next.js), compilado como **ejecutable standalone nativo de Windows**, no requiere instalación de Python ni dependencias externas. Un solo archivo `.exe` y tu infraestructura queda bajo vigilancia las 24/7.

> _"Diseñado por administradores de red, para administradores de red."_

---

## 🏆 ¿Por qué elegir Argos Guard Enterprise?

| Característica | Argos Guard | Herramientas Tradicionales |
|---|:---:|:---:|
| **Instalación en 1 clic** | ✅ `.exe` standalone | ❌ Múltiples dependencias |
| **Dashboard en tiempo real (WebSocket)** | ✅ | ⚠️ Polling manual |
| **Alertas Telegram instantáneas** | ✅ GuardBot nativo | ❌ Requiere plugins |
| **Monitoreo L3 + L7 unificado** | ✅ ICMP + HTTP/S | ⚠️ Herramientas separadas |
| **Auditoría de puertos TCP** | ✅ Integrado | ❌ Herramienta externa |
| **Certificados SSL — alerta 15 días antes** | ✅ Automático | ❌ Manual |
| **Control de licencias por HWID + Cloud** | ✅ Supabase | ❌ |
| **Bug Reporter con envío automático** | ✅ | ❌ |
| **MFA / TOTP integrado** | ✅ | ⚠️ Configuración compleja |
| **Generación de Reportes PDF** | ✅ | ⚠️ Exportación manual |

---

## 🚀 Características Principales

### 🌐 Motor de Monitoreo Asíncrono (L3 · L4 · L7)
- **Ping ICMP de alta frecuencia** — hasta 16 dispositivos simultáneos en Enterprise
- **HTTP/S Probe L7** — verifica disponibilidad de portales web con validación de contenido esperado
- **Escáner de puertos TCP** — auditoría de superficie de ataque en tiempo real
- **WebSocket Broadcast** — el dashboard se actualiza al instante sin recargar la página
- **Detección de latencia** — gráficas históricas de respuesta por dispositivo

### 🚨 Sistema de Alertas Inteligente
- **GuardBot (Telegram)** — recibe alertas al instante en tu teléfono con formato enterprise profesional
- **Ventana horaria configurable** — define entre qué horas quieres recibir notificaciones (ej: 09:00–17:00)
- **Tiempo de caída calculado** — cada alerta de recuperación incluye el tiempo exacto fuera de línea
- **Sonido de alerta local** — señal auditiva en el sistema cuando se detecta una caída

### 📊 Dashboard Unificado
- **Vista de Monitoreo Activo** — estado en tiempo real de todos los equipos con indicadores visuales
- **Gestión de Equipos & L7 Probes** — agrega, edita y elimina equipos desde la interfaz
- **Métricas y SLA** — historial de conectividad, latencia promedio e incidentes
- **Auditoría de Seguridad** — log completo de incidentes, cambios de estado y acciones de usuarios

### 🔐 Seguridad & Licenciamiento
- **Validación de licencias cloud** — verificación contra Supabase con HWID binding
- **Cache offline seguro** — si cae la red, el sistema sigue operando con caché local cifrado
- **Trial 21 días protegido** — firma criptográfica HMAC-SHA256 anti-manipulación
- **Autenticación MFA/TOTP** — segundo factor de autenticación para el acceso al panel
- **Roles de usuario** — Super Admin, Operador y Lector con permisos diferenciados

### 📄 Reportes & Exportación
- **Generación de PDF** — reportes de estado, incidentes y métricas SLA exportables
- **Bug Reporter integrado** — captura automática de errores con envío a soporte técnico por correo

---

## 📥 Descarga Directa

> ⚠️ **Requiere Windows 10/11 (64-bit)**. No necesita Python instalado.

| Versión | Archivo | Tamaño |
|---------|---------|--------|
| **v3.6.2 — Producción** | [ArgosGuard.exe](https://github.com/betorockers/ArgosGuardEnterprise/releases/latest/download/ArgosGuard.exe) | ~4.4 MB |

### Ejecución rápida

1. Descarga `ArgosGuard.exe` desde la sección [Releases](https://github.com/betorockers/ArgosGuardEnterprise/releases)
2. Ejecuta el archivo — el sistema iniciará el backend automáticamente
3. Abre tu navegador en `http://localhost:3000`
4. En el primer inicio, crea tu Super Administrador
5. ¡Comienza a monitorear tu red!

---

## 🏷️ Planes y Licencias

| Plan | Dispositivos | Capacidades | HWID | Precio |
|------|:---:|---|:---:|:---:|
| **Trial / Demo** | 1 equipo | L3 + L7 + Puertos · 21 días | — | Gratis |
| **Básico** | 2 equipos | Monitoreo L3 (Ping ICMP) | ✅ | Contactar |
| **Estándar** | 5 equipos | L3 + L7 (HTTP/S Probe) | ✅ | Contactar |
| **Enterprise** | 16 equipos | L3 + L7 + Puertos TCP | ✅ | Contactar |

> Las licencias se validan en la nube vía **Supabase** y quedan vinculadas al hardware del equipo (HWID) para prevenir uso no autorizado.

---

## 🛠️ Stack Tecnológico

```
┌─────────────────────────────────────────────────────┐
│                  ARGOS GUARD ENTERPRISE             │
├─────────────────┬───────────────────────────────────┤
│   FRONTEND      │   Next.js 15 · React · TypeScript │
│                 │   WebSocket · Tailwind CSS         │
├─────────────────┼───────────────────────────────────┤
│   BACKEND       │   Python 3.13 · FastAPI · asyncio │
│                 │   SQLite (WAL) · JWT · MFA/TOTP   │
├─────────────────┼───────────────────────────────────┤
│   CLOUD         │   Supabase (PostgreSQL + RLS)      │
│                 │   Validación de licencias HWID     │
├─────────────────┼───────────────────────────────────┤
│   ALERTAS       │   Telegram Bot API (GuardBot)      │
│                 │   Ventana horaria configurable     │
├─────────────────┼───────────────────────────────────┤
│   COMPILACIÓN   │   Nuitka → C++ nativo Windows     │
│                 │   Ejecutable standalone 4.4 MB     │
└─────────────────┴───────────────────────────────────┘
```

---

## 💬 Soporte y Contacto

¿Necesitas ayuda técnica, quieres adquirir una licencia o tienes preguntas comerciales?

| Canal | Contacto |
|-------|----------|
| 🛠️ **Soporte Técnico** | [soporte@betograf.cl](mailto:soporte@betograf.cl) |
| 💼 **Atención Comercial** | [contacto@betograf.cl](mailto:contacto@betograf.cl) |
| 🌐 **Sitio Web** | [betograf.cl](https://betograf.cl) |
| 🐛 **Reportar un Bug** | [Issues](https://github.com/betorockers/ArgosGuardEnterprise/issues) |

---

## ⚖️ Licencia y Términos

Argos Guard Enterprise es un software comercial propietario desarrollado por **Betograf**.

- ✅ Uso personal y empresarial permitido con licencia activa
- ❌ Redistribución, ingeniería inversa o modificación no autorizadas
- ✅ Trial gratuito de 21 días sin tarjeta de crédito

© 2026 Betograf · Anvic Security · Todos los derechos reservados.

---

<div align="center">

**Hecho con 🛡️ en Chile por [Betograf](https://betograf.cl)**

_Argos Guard Enterprise — Porque tu infraestructura merece vigilancia de clase mundial._

</div>
