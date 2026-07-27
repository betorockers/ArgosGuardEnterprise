# Reporte de Pruebas Unitarias - Suite Completa Argos Guard v4.0

**Fecha:** 2026-07-24  
**Entorno:** Python 3.13.13 / Django 6.0.7 / Windows 11  
**Herramienta:** `pytest`  

## Resumen Ejecutivo
Se ejecutaron 24 pruebas unitarias que abarcan todos los módulos del backend monolítico (`core`, `monitoring`, `osint`, `security`, `licensing`), incluyendo la verificación de la inicialización y soporte de idioma sin errores en Django.

## Casos de Prueba Ejecutados y Resultados

1. `tests_v4/test_osint_services.py::test_scrape_rut`: **PASSED**
2. `tests_v4/test_osint_services.py::test_scrape_ppu`: **PASSED**
3. `tests_v4/test_osint_services.py::test_query_fugas`: **PASSED**
4. `tests_v4/test_osint_services.py::test_query_reputacion`: **PASSED**
5. `tests_v4/test_osint_services.py::test_query_infra`: **PASSED**
6. `tests_v4/test_osint_services.py::test_resolve_dns_records`: **PASSED**
7. `tests_v4/test_osint_services.py::test_query_geografia`: **PASSED**
8. `tests_v4/test_osint_services.py::test_query_whois`: **PASSED**
9. `tests_v4/test_osint_services.py::test_query_ipgeo`: **PASSED**
10. `tests_v4/test_osint_services.py::test_query_web`: **PASSED**
11. `tests_v4/test_osint_services.py::test_query_puertos`: **PASSED**
12. `tests_v4/test_osint_services.py::test_query_subdominios`: **PASSED**
13. `tests_v4/test_osint_services.py::test_query_email`: **PASSED**
14. `tests_v4/test_osint_services.py::test_query_traceroute`: **PASSED**
15. `backend_v4/apps/monitoring/test_monitoring.py::test_target_node_creation`: **PASSED**
16. `backend_v4/apps/monitoring/test_monitoring.py::test_dashboard_view`: **PASSED**
17. `backend_v4/apps/monitoring/test_monitoring.py::test_telemetry_nodes_partial`: **PASSED**
18. `backend_v4/apps/core/test_core.py::test_path_resolver_singleton`: **PASSED**
19. `backend_v4/apps/core/test_core.py::test_network_probe_runner`: **PASSED**
20. `backend_v4/apps/licensing/test_licensing.py::test_get_system_hwid`: **PASSED**
21. `backend_v4/apps/osint/test_osint.py::test_format_rut_with_dots`: **PASSED**
22. `backend_v4/apps/osint/test_osint.py::test_dns_resolution_local`: **PASSED**
23. `backend_v4/apps/security/test_security.py::test_django_native_hashing`: **PASSED**
24. `backend_v4/apps/security/test_security.py::test_jwt_generation`: **PASSED**

## Conclusión de Fase 1
**ESTADO:** Éxito (24/24 Passed - 100%)  
Ninguna falla bloqueante.
