@echo off
rem ==============================================================================
rem Zero-Friction One-Click Windows Launcher for STM32 Structured Wiki Generator
rem Compatible with Windows 10, Windows 11, and Windows Server (CMD & PowerShell)
rem ==============================================================================

setlocal enabledelayedexpansion
cd /d "%~dp0"

echo ======================================================================
echo 🚀 Launching STM32 Structured Wiki Generator ^& Multi-View Graph Engine
echo ======================================================================

rem 1. Check if Python is installed (check py launcher or python in PATH)
where py >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=py -3"
) else (
    where python >nul 2>&1
    if %ERRORLEVEL% equ 0 (
        set "PY_CMD=python"
    ) else (
        echo [ERROR] Python 3.10+ was not found on your system!
        echo Please download and install Python from: https://www.python.org/downloads/
        echo (Make sure to check "Add Python to PATH" during installation)
        echo.
        pause
        exit /b 1
    )
)

rem 2. Automatically setup Python virtual environment if missing
if not exist "venv\Scripts\python.exe" (
    echo [INFO] Python virtual environment not found. Creating 'venv'...
    %PY_CMD% -m venv venv
    if %ERRORLEVEL% neq 0 (
        echo [ERROR] Failed to create virtual environment!
        pause
        exit /b 1
    )
    
    set "REQ_FILE=requirements.txt"
    if not exist "!REQ_FILE!" (
        set "REQ_FILE=project\requirements.txt"
    )

    if exist "wheels\*.whl" (
        echo [INFO] 📦 Offline wheelhouse detected in .\wheels. Installing dependencies offline ^(zero internet required^)...
        .\venv\Scripts\pip.exe install --no-index --find-links=wheels -r !REQ_FILE!
    ) else (
        echo [INFO] 🌐 Automatically resolving and installing pinned dependencies via PyPI...
        .\venv\Scripts\python.exe -m pip install --upgrade pip
        .\venv\Scripts\pip.exe install -r !REQ_FILE!
    )

    if %ERRORLEVEL% neq 0 (
        echo [ERROR] Dependency installation encountered an issue.
        pause
        exit /b 1
    )
)

rem 3. Set PYTHONPATH to include project directory
set "PYTHONPATH=%~dp0project;%PYTHONPATH%"

rem 4. Launch Desktop GUI Application
echo [INFO] Starting GUI Application...
.\venv\Scripts\python.exe project\main.py %*

if %ERRORLEVEL% neq 0 (
    echo.
    echo [NOTICE] Application closed with return code %ERRORLEVEL%.
    pause
)
endlocal
