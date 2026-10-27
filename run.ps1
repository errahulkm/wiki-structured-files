# ==============================================================================
# Zero-Friction One-Click PowerShell Launcher for STM32 Structured Wiki Generator
# Compatible with PowerShell 5.1 & PowerShell Core 7+ on Windows, Linux, and macOS
# ==============================================================================

[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$AppArgs
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "🚀 Launching STM32 Structured Wiki Generator & Multi-View Graph Engine" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

# 1. Determine platform and venv Python path
$IsWindows = ($env:OS -eq "Windows_NT") -or ($PSVersionTable.PSEdition -ne "Core" -and [System.Environment]::OSVersion.Platform -match "Win")
if ($IsWindows) {
    $VenvPython = Join-Path $ScriptDir "venv\Scripts\python.exe"
    $VenvPip    = Join-Path $ScriptDir "venv\Scripts\pip.exe"
} else {
    $VenvPython = Join-Path $ScriptDir "venv/bin/python"
    $VenvPip    = Join-Path $ScriptDir "venv/bin/pip"
}

# 2. Check if virtual environment exists; if not, create it
$NeedDeps = $false
if (-not (Test-Path $VenvPython)) {
    Write-Host "[INFO] Creating isolated Python virtual environment..." -ForegroundColor Yellow
    
    $SystemPython = $null
    if ($IsWindows) {
        if (Get-Command py -ErrorAction SilentlyContinue) {
            $SystemPython = "py -3"
        } elseif (Get-Command python -ErrorAction SilentlyContinue) {
            $SystemPython = "python"
        }
    } else {
        if (Get-Command python3 -ErrorAction SilentlyContinue) {
            $SystemPython = "python3"
        } elseif (Get-Command python -ErrorAction SilentlyContinue) {
            $SystemPython = "python"
        }
    }

    if (-not $SystemPython) {
        Write-Error "[ERROR] Python 3.10+ was not found on your system! Please install Python from https://www.python.org/downloads/"
        exit 1
    }

    Invoke-Expression "$SystemPython -m venv venv"
    $NeedDeps = $true
} else {
    & $VenvPython -c "import PyQt6, customtkinter, pydantic" 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[INFO] Detected incomplete or missing dependencies. Running automatic self-heal..." -ForegroundColor Yellow
        $NeedDeps = $true
    }
}

if ($NeedDeps) {
    $ReqFile = Join-Path $ScriptDir "requirements.txt"
    if (-not (Test-Path $ReqFile)) {
        $ReqFile = Join-Path $ScriptDir "project\requirements.txt"
    }

    $WheelsDir = Join-Path $ScriptDir "wheels"
    if ((Test-Path $WheelsDir) -and (Get-ChildItem $WheelsDir -Filter *.whl -ErrorAction SilentlyContinue)) {
        Write-Host "[INFO] 📦 Offline wheelhouse detected in .\wheels. Installing dependencies offline (zero internet required)..." -ForegroundColor Green
        & $VenvPip install --no-index --find-links=$WheelsDir -r $ReqFile
    } else {
        Write-Host "[INFO] 🌐 Automatically resolving and installing pinned dependencies via PyPI..." -ForegroundColor Yellow
        & $VenvPython -m pip install --upgrade pip
        & $VenvPip install -r $ReqFile
    }
}

# 3. Configure PYTHONPATH
$ProjectDir = Join-Path $ScriptDir "project"
$PathSep = if ($IsWindows) { ";" } else { ":" }
if ($env:PYTHONPATH) {
    $env:PYTHONPATH = "$ProjectDir$PathSep$($env:PYTHONPATH)"
} else {
    $env:PYTHONPATH = $ProjectDir
}

# 4. Launch Desktop Application
Write-Host "[INFO] Starting GUI Application..." -ForegroundColor Green
$MainPy = Join-Path $ScriptDir "project\main.py"
& $VenvPython $MainPy @AppArgs
