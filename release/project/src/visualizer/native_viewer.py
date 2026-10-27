"""
Native Qt6 Desktop Window Viewer for STM32 Karpathy-Wiki Knowledge Graph.
Runs as a 100% standalone, GPU-accelerated native desktop window with zero browser tabs or URL bars.
Includes universal adaptive graphics runtime detection and self-healing Safe Mode.
"""

import sys
import os
from typing import Optional

# Ensure project root is in sys.path for standalone script execution
_current_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.abspath(os.path.join(_current_dir, "..", ".."))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

try:
    from src.core.gpu_runtime import (
        sanitize_process_env,
        get_adaptive_chromium_flags,
        run_gpu_diagnostics,
        detect_system_gpu_architecture,
    )
    from src.core.mcu_detector import detect_mcu_metadata
except ImportError:
    from project.src.core.gpu_runtime import (
        sanitize_process_env,
        get_adaptive_chromium_flags,
        run_gpu_diagnostics,
        detect_system_gpu_architecture,
    )
    from project.src.core.mcu_detector import detect_mcu_metadata

# 1. Sanitize environment before importing Qt / Chromium
sanitize_process_env()
os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"

# 2. Configure adaptive Chromium flags if not already provided
if "QTWEBENGINE_CHROMIUM_FLAGS" not in os.environ:
    if "--software-render" in sys.argv:
        os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = get_adaptive_chromium_flags(tier=3)
    elif "--safe-mode" in sys.argv:
        os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = get_adaptive_chromium_flags(tier=2)
    else:
        os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox --disable-gpu-sandbox --ignore-gpu-blocklist --enable-webgl"


def launch_native_window(html_path: str, title: Optional[str] = None) -> None:
    """Launches standalone Qt6 WebEngine native desktop window with full WebGL2 hardware acceleration."""
    try:
        from PyQt6.QtWidgets import QApplication, QMainWindow
        from PyQt6.QtWebEngineWidgets import QWebEngineView
        from PyQt6.QtWebEngineCore import QWebEngineSettings, QWebEngineProfile
        from PyQt6.QtCore import QUrl
        from PyQt6.QtGui import QIcon
    except ImportError as e:
        print(f"[ERROR] PyQt6 or PyQt6-WebEngine not installed: {e}", file=sys.stderr)
        sys.exit(1)

    mcu_info = detect_mcu_metadata(wiki_root=os.path.dirname(os.path.abspath(html_path)))

    if not title:
        title = f"{mcu_info['mcu_family']} Karpathy-Wiki Multi-View Knowledge Graph (GPU Accelerated)"

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    app.setApplicationName(f"{mcu_info['mcu_family']} Karpathy-Wiki Graph Engine")

    # Configure WebEngine Settings for WebGL and offline local assets
    profile = QWebEngineProfile.defaultProfile()
    settings = profile.settings()
    settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.Accelerated2dCanvasEnabled, True)

    window = QMainWindow()
    window.setWindowTitle(title)
    window.resize(1600, 1000)

    webview = QWebEngineView()
    file_url = QUrl.fromLocalFile(os.path.abspath(html_path))
    webview.load(file_url)

    def _on_load_finished(ok: bool):
        status_str = "loaded successfully" if ok else "load reported warning/incomplete"
        print(f"WEBVIEW_STATUS: {status_str} ({html_path})", flush=True)

    webview.loadFinished.connect(_on_load_finished)

    window.setCentralWidget(webview)
    window.show()
    window.raise_()
    window.activateWindow()

    # Flush stdout readiness handshake so launching parent can immediately detect success
    print(f"READY: {title} mapped and viewable -> {html_path}", flush=True)

    sys.exit(app.exec())


if __name__ == "__main__":
    if "--diagnose" in sys.argv:
        diag = run_gpu_diagnostics()
        print("=" * 70)
        print("🛠  STM32 Karpathy-Wiki Universal GPU Diagnostics")
        print("=" * 70)
        for k, v in diag.items():
            if isinstance(v, list):
                print(f"• {k}:")
                for item in v:
                    print(f"    - {item}")
            else:
                print(f"• {k}: {v}")
        print("=" * 70)
        sys.exit(0)

    clean_args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if len(clean_args) < 1:
        default_path = os.path.abspath("artifacts/output/karpathy-wiki/graph_view.html")
        if os.path.exists(default_path):
            launch_native_window(default_path)
        else:
            print("Usage: python -m src.visualizer.native_viewer <path_to_graph_view.html> [--safe-mode] [--software-render] [--diagnose]")
            sys.exit(1)
    else:
        target_html = clean_args[0]
        launch_native_window(target_html)
