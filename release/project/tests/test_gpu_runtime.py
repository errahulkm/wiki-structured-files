"""
Unit and Integration Tests for Universal Adaptive Graphics Runtime and Self-Healing Engine.
Tests cross-platform architecture detection, environment sanitation, safe mode fallbacks,
and multi-tier Chromium flag generation.
"""

import os
import sys
import pytest

from src.core.gpu_runtime import (
    detect_system_gpu_architecture,
    get_optimal_gpu_env,
    get_adaptive_chromium_flags,
    sanitize_process_env,
    run_gpu_diagnostics,
    GpuArchitecture,
)


def test_detect_system_gpu_architecture():
    """Verifies system GPU architecture detection returns complete schema."""
    arch_info = detect_system_gpu_architecture()
    
    assert "architecture" in arch_info
    assert "is_dedicated_nvidia" in arch_info
    assert "is_hybrid_nvidia" in arch_info
    assert "display_server" in arch_info
    assert "switcher_tool" in arch_info
    assert "detected_gpus" in arch_info
    assert "platform_os" in arch_info
    assert isinstance(arch_info["detected_gpus"], list)
    assert arch_info["platform_os"] in ["linux", "windows", "darwin"]


def test_get_optimal_gpu_env_safe_mode():
    """Verifies that safe mode purges all PRIME/DRI overrides to prevent EGL crashes."""
    # Pre-populate dirty env vars
    os.environ["DRI_PRIME"] = "1"
    os.environ["__NV_PRIME_RENDER_OFFLOAD"] = "1"
    os.environ["__GLX_VENDOR_LIBRARY_NAME"] = "nvidia"

    env, explanation = get_optimal_gpu_env(safe_mode=True)
    
    assert "DRI_PRIME" not in env
    assert "__NV_PRIME_RENDER_OFFLOAD" not in env
    assert "__GLX_VENDOR_LIBRARY_NAME" not in env
    assert "Safe Mode" in explanation

    # Cleanup
    os.environ.pop("DRI_PRIME", None)
    os.environ.pop("__NV_PRIME_RENDER_OFFLOAD", None)
    os.environ.pop("__GLX_VENDOR_LIBRARY_NAME", None)


def test_adaptive_chromium_flags_tiers():
    """Verifies Chromium flags for Tier 1, 2, and 3 self-healing."""
    flags_t1 = get_adaptive_chromium_flags(tier=1)
    flags_t2 = get_adaptive_chromium_flags(tier=2)
    flags_t3 = get_adaptive_chromium_flags(tier=3)

    # Tier 1 should contain WebGL and hardware rasterization
    assert "--enable-gpu-rasterization" in flags_t1
    assert "--enable-webgl" in flags_t1

    # Tier 2 (Safe Mode) must bypass GPU sandbox and use ANGLE
    assert "--disable-gpu-sandbox" in flags_t2
    assert "--use-gl=angle" in flags_t2

    # Tier 3 (Software Fallback) must use SwiftShader
    assert "--use-gl=swiftshader" in flags_t3
    assert "--disable-gpu" in flags_t3


def test_sanitize_process_env():
    """Verifies that sanitize_process_env removes invalid conflicting flags."""
    arch_info = detect_system_gpu_architecture()
    
    # Set conflicting DRI_PRIME with NVIDIA
    os.environ["__NV_PRIME_RENDER_OFFLOAD"] = "1"
    os.environ["DRI_PRIME"] = "1"

    sanitize_process_env()

    # DRI_PRIME must always be purged if NVIDIA is active
    assert "DRI_PRIME" not in os.environ

    if arch_info["architecture"] == GpuArchitecture.DEDICATED_NVIDIA:
        # In dedicated NVIDIA mode, offload flags must be purged
        assert "__NV_PRIME_RENDER_OFFLOAD" not in os.environ

    # Clean up test env
    os.environ.pop("DRI_PRIME", None)
    os.environ.pop("__NV_PRIME_RENDER_OFFLOAD", None)


def test_run_gpu_diagnostics_schema():
    """Verifies that run_gpu_diagnostics generates a valid diagnostic report."""
    diag = run_gpu_diagnostics()
    
    assert "platform" in diag
    assert "python_version" in diag
    assert "system_architecture" in diag
    assert "display_server" in diag
    assert "switcher_tool" in diag
    assert "recommended_launch_strategy" in diag
    assert "chromium_flags_tier1" in diag
    assert "chromium_flags_tier2" in diag


def test_browser_preference_resolution(tmp_path):
    """Verifies that KnowledgeGraphVisualizer resolves browser targets accurately."""
    from src.visualizer.graph_visualizer import KnowledgeGraphVisualizer
    viz = KnowledgeGraphVisualizer(output_root=str(tmp_path))

    # Auto / Default should delegate to system handler
    auto_exe, auto_name = viz._find_browser_executable("⚙️ Auto / System Default Browser")
    assert auto_exe is None
    assert "Default" in auto_name

    # Chrome preference should resolve to Chrome/Chromium if installed
    chrome_exe, chrome_name = viz._find_browser_executable("🌐 Google Chrome Browser")
    if chrome_exe:
        assert any(k in chrome_name for k in ["Chrome", "Chromium"])
        assert os.path.exists(chrome_exe)

    # Firefox preference should resolve to Firefox if installed
    firefox_exe, firefox_name = viz._find_browser_executable("🦊 Mozilla Firefox Browser")
    if firefox_exe:
        assert "Firefox" in firefox_name
        assert os.path.exists(firefox_exe)


def test_qt6_native_viewer_support():
    """Verifies that PyQt6 WebEngine is fully available for native desktop graph viewing."""
    import PyQt6.QtWebEngineWidgets
    from src.visualizer.native_viewer import launch_native_window

    assert PyQt6.QtWebEngineWidgets is not None
    assert callable(launch_native_window)

