# Plan de Arquitectura v4.1 — Suite de Ciberdefensa Táctica (OSINT PDF Summary + IDS + SIEM + Firma Criptográfica Military-Grade)

Este documento contiene las especificaciones técnicas completas de arquitectura y diseño para la versión **v4.1**, incorporando los servicios de Ciberdefensa Táctica (IDS/NIDS/HIDS), Integración SIEM corporativa, Generador de Resumen OSINT en PDF y el blindaje criptográfico de nivel militar mediante certificados X.509.

---

## 🔒 1. Blindaje Criptográfico y Certificación X.509 de Nivel Militar

Para garantizar la integridad industrial, confiabilidad del 100% y neutralización total de alertas de falsos positivos en antivirus o Windows SmartScreen en cualquier equipo cliente:

1. **Inyección y Registro de Certificado de Confianza (`BetoGraf_Almacenero.cer`)**:
   - Inclusión del certificado digital X.509 en la rutina de instalación de Inno Setup (`installer_v4.iss`).
   - Comando desatendido: `certutil -user -f -addstore Root "{tmp}\BetoGraf_Almacenero.cer"` ejecutado durante la instalación.
   - Otorga estatus de software de confianza registrado en el almacén de raíces del sistema host.

2. **Firma Digital Criptográfica de Código (`signtool.exe`)**:
   - Firma digital automatizada con el archivo de certificado de clave privada `.pfx` (`BetoGraf_Almacenero.pfx`) y sello de tiempo de la autoridad Certum/DigiCert (`http://timestamp.digicert.com`).
   - Firma aplicada quirúrgicamente sobre el binario ejecutable compilado `ArgosGuardV4.exe` y sobre el instalador final `ArgosGuard_Installer_v4.0.0.exe`.

---

## 📑 2. Módulo A: Botón "Resumen Táctico OSINT" & Reporte Executivo PDF

- **Interfaz Táctica**: Botón `📄 Resumen Táctico` ubicado bajo el cuadro de búsqueda principal de la Pestaña OSINT (`templates/osint/osint.html`).
- **Comportamiento Asíncrono**: Despacho de escaneo completo de vulnerabilidades web (encabezados de seguridad CSP/HSTS/X-Frame, puertos abiertos expuestos, fugas DNS y certificados SSL/TLS).
- **Generador de Reporte PDF (fpdf2)**:
  - Exportación automática a la carpeta `Descargas` del usuario host.
  - Matriz de Vectores de Ataque Explotables (Phishing, Man-in-the-Middle, RDP Brute Force, Exposición de Servicios).
  - Recomendaciones de Hardening accionables categorizadas por nivel de severidad (Crítica, Alta, Media, Informativa).

---

## 🛡️ 3. Módulo B: Sistema de Detección de Intrusos (IDS / NIDS / HIDS)

1. **NIDS (Network Intrusion Detection System)**:
   - **Detección de Port Scanning**: Sensor de inspección de densidad de conexiones TCP SYN / FIN / NULL en ventanas cortas de tiempo (detección de escaneos masivos Nmap/Masscan).
   - **Detección de ARP Spoofing / MITM**: Guardián de tabla ARP que detecta duplicidad de direcciones MAC o cambios repentinos de la MAC del Gateway predeterminado.
   - **ICMP Flood Detection**: Telemetría anti-DDoS de paquetes eco masivos.
2. **HIDS (Host Intrusion Detection System)**:
   - **FIM (File Integrity Monitoring)**: Hash SHA-256 periódico del ejecutable del sistema `ArgosGuardV4.exe` y la base de datos `argos_v4.db` contra firmas criptográficas maestras guardadas al compilar.
3. **Respuesta Activa (IPS)**:
   - Capacidad opcional para añadir reglas de bloqueo inmediato en el Firewall de Windows (`netsh advfirewall firewall add rule name="ArgosGuard_Block_IP" dir=in action=block remoteip=X.X.X.X`).

---

## 📊 4. Módulo C: Integración con Herramientas SIEM

1. **Conector Wazuh (REST API v4.x)**:
   - Integración nativa bidireccional mediante `WazuhAPIClient` con autenticación JWT Bearer.
   - Envío de eventos de seguridad y sincronización de agentes activos.
2. **Exportador Elastic SIEM / ECS JSON**:
   - Formateador de eventos en estándar **Elastic Common Schema (ECS 8.x)** listo para ingesta en Elasticsearch, Logstash o Kibana.
3. **Emisor Syslog CEF / LEEF (Splunk & Microsoft Sentinel)**:
   - Soporte de transporte UDP/TCP Syslog transmitiendo en formato CEF (Common Event Format para Splunk y Micro Focus ArcSight) y LEEF (Log Event Extended Format para IBM QRadar).

---

## 🧪 Plan de Verificación de Integridad

- **Pruebas Unitarias (`pytest`)**: Cobertura del 100% sobre conectores SIEM, firmas FIM y generador PDF.
- **Pruebas de Estrés (`k6`)**: Ingesta masiva simulada de alertas IDS sin pérdida de paquetes.
- **Verificación de Firma**: Comprobación con `Get-AuthenticodeSignature` en PowerShell.
