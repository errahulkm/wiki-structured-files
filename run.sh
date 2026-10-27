#!/bin/bash
# ==============================================================================
# Zero-Friction One-Click Launcher for STM32 Karpathy-Wiki Generator & Graph Engine
# ==============================================================================

set -e
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

echo "======================================================================"
echo "🚀 Launching STM32 Karpathy-Wiki Generator & Multi-View Graph Engine"
echo "======================================================================"

# 1. Automatically setup Python virtual environment if missing
if [ ! -d "venv" ]; then
    echo "[INFO] Creating isolated Python virtual environment ('venv')..."
    python3 -m venv venv
    
    REQ_FILE="requirements.txt"
    if [ ! -f "$REQ_FILE" ]; then
        REQ_FILE="project/requirements.txt"
    fi

    if [ -d "wheels" ] && [ -n "$(ls -A wheels 2>/dev/null)" ]; then
        echo "[INFO] 📦 Offline wheelhouse detected in ./wheels. Installing dependencies offline (zero internet required)..."
        ./venv/bin/pip install --no-index --find-links=wheels -r "$REQ_FILE"
    else
        echo "[INFO] 🌐 Automatically resolving and installing pinned dependencies via PyPI..."
        ./venv/bin/pip install -r "$REQ_FILE"
    fi
fi

# 2. Set PYTHONPATH
export PYTHONPATH="$ROOT_DIR/project"

# 3. Launch Application GUI
echo "[INFO] Starting GUI Application..."
./venv/bin/python project/main.py "$@"
