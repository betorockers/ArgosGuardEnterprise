# Reporte de Pruebas de Estrés (`k6`) - Servidor Kiosko v4.0

**Fecha:** 2026-07-24  
**Módulo:** Servidor Django embebido (`run_kiosk.py` / `wsgiref`)  
**Herramienta:** `k6`  

## Resumen Ejecutivo
Se realizó la prueba de estrés de rendimiento sobre el servidor Django embebido del Kiosko v4.0 simulando 20 usuarios virtuales concurrentes (`VUs`) durante 20 segundos.

## Configuración de la Carga (Ramp-up)
- **Subida (Ramp-up):** 0 a 20 VUs en 5 segundos.
- **Sostenimiento (Plateau):** 20 VUs concurrentes por 10 segundos.
- **Bajada (Ramp-down):** 20 a 0 VUs en 5 segundos.

## Métricas Clave de Rendimiento
- **Peticiones Totales (`http_reqs`):** 620 peticiones
- **Rendimiento de Servidor (`http_req_duration`):**
  - **Promedio (avg):** 3.00 ms
  - **Mediana (med):** 2.57 ms
  - **Percentil 95 (p95):** 6.62 ms (Excelente desempeño, muy por debajo del límite de 500 ms)
  - **Máximo (max):** 31.53 ms
- **Tasa de Iteraciones Completadas:** 310 iteraciones sostenidas a 15 req/s.

## Conclusión de Fase 2
**ESTADO:** Éxito (100% Passed - Latencia ultra baja < 7ms en p95)  
El servidor Django responde de manera inmediata y estable sin saturación de hilos ante concurrencia.
