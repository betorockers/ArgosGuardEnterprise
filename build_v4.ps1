param(
    [switch]$CleanOnly
)

$ErrorActionPreference = "Stop"

$BaseDir = (Get-Item .).FullName
$BackendV4Dir = Join-Path $BaseDir "backend_v4"
$BuildOut = Join-Path $BackendV4Dir "build"

function Clear-CompilationState {
    Write-Host "-> [Limpieza Total] Terminando subprocesos y purgando carpetas de compilación..." -ForegroundColor DarkGray
    Get-Process -Name zig, scons, chromedriver -ErrorAction SilentlyContinue | Stop-Process -Force
    if (Test-Path $BuildOut) {
        Remove-Item -Recurse -Force $BuildOut -ErrorAction SilentlyContinue
    }
}

if ($CleanOnly) {
    Clear-CompilationState
    Write-Host "-> Estado de compilación limpiado al 100%." -ForegroundColor Green
    exit 0
}

Clear-CompilationState

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Compilación Argos Guard v4.0 (Nuitka C++ / Waitress Engine) " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

try {
    Set-Location $BackendV4Dir

    $NuitkaArgs = @(
        "--standalone",
        "--remove-output",
        "--windows-console-mode=disable",
        "--windows-icon-from-ico=static/icono_argos.ico",
        "--include-data-dir=templates=templates",
        "--include-data-dir=static=static",
        "--module-parameter=django-settings-module=config.settings",
        
        # Módulos de la App Monolito Modular
        "--include-package=config",
        "--include-package=apps",
        "--include-package=apps.core",
        "--include-package=apps.monitoring",
        "--include-package=apps.osint",
        "--include-package=apps.security",
        "--include-package=apps.licensing",

        # Framework Django y Servidor Waitress
        "--include-package=django",
        "--include-package=django.core",
        "--include-package=django.core.management",
        "--include-package=django.db.migrations",
        "--include-package=django.db.backends",
        "--include-package=django.db.backends.sqlite3",
        "--include-package=django.contrib.admin",
        "--include-package=django.contrib.auth",
        "--include-package=django.contrib.contenttypes",
        "--include-package=django.contrib.sessions",
        "--include-package=django.contrib.messages",
        "--include-package=django.contrib.staticfiles",
        "--include-package=waitress",
        "--include-package=wsgiref",
        "--include-package-data=django",

        # Automation, OSINT, Cryptography & Analytics
        "--include-package=requests",
        "--include-package=bs4",
        "--include-package=undetected_chromedriver",
        "--include-package=selenium",
        "--include-package=dns",
        "--include-package=cryptography",
        "--include-package=argon2",
        "--include-package=jwt",
        "--include-package=urllib3",
        "--include-package=certifi",
        "--include-package=asgiref",
        "--include-package=fpdf",
        "--include-package=pandas",
        "--include-package=matplotlib",
        "--include-package=seaborn",
        "--include-package=limits",
        "--include-package-data=fpdf",
        "--include-package-data=matplotlib",
        "--include-package-data=seaborn",
        "--include-package-data=pandas",
        "--include-package-data=dns",
        "--include-package-data=limits",

        # Plugins Nuitka
        "--enable-plugin=numpy",
        "--enable-plugin=matplotlib",
        "--enable-plugin=anti-bloat",

        "--no-deployment-flag=excluded-module-usage",
        "--assume-yes-for-downloads",
        "--output-dir=build",
        "--output-filename=ArgosGuardV4.exe",
        "launcher_pc.py"
    )

    Write-Host "-> Ejecutando: python -m nuitka $($NuitkaArgs -join ' ')" -ForegroundColor DarkGray
    python -m nuitka @NuitkaArgs

    if ($LASTEXITCODE -ne 0) {
        throw "La compilación de Nuitka falló con código $LASTEXITCODE"
    }

    # Inclusión post-compilación de DLLs runtime Visual C++ para compatibilidad total
    $DistFolder = Join-Path $BuildOut "launcher_pc.dist"
    if (Test-Path $DistFolder) {
        $System32Dlls = @(
            "vcruntime140.dll", "vcruntime140_1.dll", "vcruntime140_threads.dll",
            "msvcp140.dll", "msvcp140_1.dll", "msvcp140_2.dll", "msvcp140_atomic_wait.dll", "msvcp140_codecvt_ids.dll",
            "concrt140.dll", "vccorlib140.dll"
        )
        foreach ($dll in $System32Dlls) {
            $src = Join-Path "C:\Windows\System32" $dll
            if (Test-Path $src) {
                Copy-Item -Path $src -Destination $DistFolder -Force
                Write-Host "-> System32 DLL Copiada: $dll" -ForegroundColor DarkGray
            }
        }

        # Firma digital con certificado corporativo BetoGraf si signtool está disponible
        $PfxPath = Join-Path $BaseDir "installer_v4\prereqs\BetoGraf_Almacenero.pfx"
        $SignTool = (Get-ChildItem -Path "C:\Program Files (x86)\Windows Kits" -Filter signtool.exe -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty FullName)
        if ($SignTool -and (Test-Path $PfxPath)) {
            $ExeToSign = Join-Path $DistFolder "ArgosGuardV4.exe"
            Write-Host "-> Firmando ejecutable con certificado criptográfico X.509..." -ForegroundColor DarkGray
            & $SignTool sign /f $PfxPath /p "betograf2026" /t "http://timestamp.digicert.com" /v $ExeToSign 2>$null
        }
    }

    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host " Compilación Exitosa v4.0 (Patrón BetoGraf + Certificado de Confianza) en backend_v4/build/launcher_pc.dist " -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Cyan
}
catch {
    Clear-CompilationState
    Write-Error "Fallo durante la compilación: $_"
}
finally {
    Set-Location $BaseDir
}
