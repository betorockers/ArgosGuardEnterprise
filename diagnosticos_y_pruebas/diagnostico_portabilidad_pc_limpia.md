# Diagnóstico de Portabilidad Total: Corrección de Inicio en PCs Limpias

**Proyecto:** Argos Guard Enterprise v4.0.0  
**Fecha:** 2026-07-24  
**Estado:** 🟢 CAUSAS RAÍZ DIAGNOSTICADAS Y CORREGIDAS EN CÓDIGO Y BUILD  

---

## 🔍 Análisis de Causas Raíz (Arranque Fallido en PCs Comunes)

Al instalar en una computadora estándar sin entorno de desarrollo previo, el software no iniciaba debido a 3 fallos estructurales de empaquetado:

### 1. Ausencia del archivo `qt.conf` en la raíz del ejecutable
- **Problema:** Nuitka ubicaba `qt.conf` en `PyQt6/Qt6/bin/qt.conf`. Al ejecutar `ArgosGuardV4.exe` en una PC limpia, Qt buscaba el plugin gráfico `platforms\qwindows.dll` y los recursos de WebEngine en la raíz ejecutable y fallaba sin mostrar interfaz.
- **Solución:** Se añadió a `build_v4.ps1` la generación automática de `qt.conf` en la raíz ejecutable (`run_kiosk.dist\qt.conf`) con `Prefix = PyQt6/Qt6`.

### 2. Incompletes de DLLs de Runtime de Visual C++ (CRT)
- **Problema:** El script de compilación solo copiaba 3 DLLs de C++. Si la PC destino no tenía instalado *Microsoft Visual C++ Redistributable 2015-2022*, faltaban librerías como `vcruntime140_threads.dll`, `msvcp140_atomic_wait.dll`, `concrt140.dll` y `vccorlib140.dll`.
- **Solución:** Se expandió el script de compilación para incluir el paquete completo de 10 DLLs de runtime C++ desde `C:\Windows\System32`, permitiendo la carga en modo **App-Local / Portable** sin requerir instaladores externos.

### 3. Detección Errónea de la Ruta Base en `PathResolver`
- **Problema:** En `path_resolver.py`, la condición `if getattr(sys, 'frozen', False) or '__compiled__' in globals():` retornaba `False` en Nuitka dentro del alcance de módulo. Como consecuencia, `self.base_dir` apuntaba a la ruta del entorno de desarrollo original `E:\ProyectoMonitoreoMod_V2` (inexistente en la PC destino), impidiendo que Django cargara `templates\` y `static\`.
- **Solución:** Se actualizó `path_resolver.py` para detectar ejecutables compilados mediante `not sys.executable.lower().endswith(('python.exe', 'pythonw.exe'))`, garantizando que `base_dir` sea siempre `{app}`.

---

## 🛠️ Cambios Aplicados en el Código Fuente

1. **[path_resolver.py](file:///e:/ProyectoMonitoreoMod_V2/backend_v4/apps/core/path_resolver.py)**: Detección infalible de entorno compilado.
2. **[build_v4.ps1](file:///e:/ProyectoMonitoreoMod_V2/build_v4.ps1)**: Generación de `qt.conf` portable y empaquetado del 100% de DLLs C++.
3. **[services.py](file:///e:/ProyectoMonitoreoMod_V2/backend_v4/apps/osint/services.py)**: Supresión total de ventanas de consola popups (`CREATE_NO_WINDOW`).
