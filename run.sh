#!/bin/bash
# ==============================================================================
# Zero-Friction One-Click Launcher for STM32 Structured Wiki Generator & Graph Engine
# ==============================================================================

set -e
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

echo "======================================================================"
echo "🚀 Launching STM32 Structured Wiki Generator & Multi-View Graph Engine"
echo "======================================================================"

# 1. Automatically setup Python virtual environment if missing
NEED_INSTALL=0
if [ ! -d "venv" ]; then
    echo "[INFO] Creating isolated Python virtual environment ('venv')..."
    python3 -m venv venv
    NEED_INSTALL=1
elif ! ./venv/bin/python -c "import PyQt6, customtkinter, pydantic" >/dev/null 2>&1; then
    echo "[INFO] Detected incomplete or missing dependencies. Running automatic self-heal..."
    NEED_INSTALL=1
fi

# 2. Automatically resolve and install pinned dependencies if needed
if [ "$NEED_INSTALL" -eq 1 ]; then
    REQ_FILE="requirements.txt"
    if [ ! -f "$REQ_FILE" ]; then
        REQ_FILE="project/requirements.txt"
    fi

    if [ -d "wheels" ] && [ -n "$(ls -A wheels/*.whl 2>/dev/null)" ]; then
        echo "[INFO] 📦 Offline wheelhouse detected in ./wheels. Installing dependencies offline (zero internet required)..."
        ./venv/bin/pip install --no-index --find-links=wheels -r "$REQ_FILE"
    else
        echo "[INFO] 🌐 Automatically resolving and installing pinned dependencies via PyPI..."
        ./venv/bin/pip install -r "$REQ_FILE"
    fi
fi

# 3. Set PYTHONPATH
export PYTHONPATH="$ROOT_DIR/project"

# 4. Launch Application GUI
echo "[INFO] Starting GUI Application..."
./venv/bin/python project/main.py "$@"
