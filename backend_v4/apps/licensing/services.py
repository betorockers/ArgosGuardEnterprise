"""
Argos Guard Enterprise v4.0 - HWID Identification & Validation Service.
"""
import uuid
import platform
import subprocess

def get_system_hwid() -> str:
    """Genera una huella digital única HWID para la máquina host Air-Gapped."""
    try:
        if platform.system() == "Windows":
            flags = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)
            output = subprocess.check_output("wmic csproduct get uuid", shell=True, creationflags=flags).decode()
            lines = [line.strip() for line in output.split("\n") if line.strip()]
            if len(lines) >= 2:
                return lines[1]
    except Exception:
        pass
    return str(uuid.getnode())
