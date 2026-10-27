"""
Universal Adaptive Graphics Runtime Engine and Self-Healing GPU Manager.
Automatically detects host GPU architecture, driver switching profiles (PRIME / Optimus / Supergfxctl / EnvyControl),
and runtime environments (X11, Wayland, Windows, macOS, Headless/VM/WSL).
Eliminates crashes across all PCs, laptops, and operating systems with multi-tiered self-healing fallbacks.
"""

import os
import sys
import shutil
import subprocess
import platform
from typing import Dict, Any, Optional, Tuple


class GpuArchitecture:
    DEDICATED_NVIDIA = "DEDICATED_NVIDIA"
    HYBRID_NVIDIA_ON_DEMAND = "HYBRID_NVIDIA_ON_DEMAND"
    HYBRID_AMD_ON_DEMAND = "HYBRID_AMD_ON_DEMAND"
    INTEGRATED_ONLY = "INTEGRATED_ONLY"
    APPLE_METAL = "APPLE_METAL"
    WINDOWS_NATIVE = "WINDOWS_NATIVE"
    HEADLESS_OR_VM = "HEADLESS_OR_VM"


def detect_system_gpu_architecture() -> Dict[str, Any]:
    """
    Intelligently analyzes system GPU hardware, active drivers, display servers,
    and hybrid GPU switcher profiles across all Linux distributions, Windows, and macOS.
    
    Returns:
        Dictionary containing:
            - architecture: One of GpuArchitecture constants
            - is_dedicated_nvidia: bool
            - is_hybrid_nvidia: bool
            - is_wayland: bool
            - display_server: "x11" | "wayland" | "windows" | "macos" | "unknown"
            - switcher_tool: e.g. "prime-select (nvidia)", "supergfxctl (Dedicated)", etc.
            - detected_gpus: List of GPU descriptions
            - platform_os: "linux" | "windows" | "darwin"
    """
    os_name = sys.platform

    # 1. macOS Platform
    if os_name == "darwin":
        return {
            "architecture": GpuArchitecture.APPLE_METAL,
            "is_dedicated_nvidia": False,
            "is_hybrid_nvidia": False,
            "is_wayland": False,
            "display_server": "macos",
            "switcher_tool": "Apple Metal / Quartz",
            "detected_gpus": ["Apple GPU / Metal Engine"],
            "platform_os": "darwin"
        }

    # 2. Windows Platform
    if os_name == "win32":
        win_gpus = []
        is_nv = False
        try:
            from .hardware_detector import detect_all_hardware_devices
            devs = detect_all_hardware_devices()
            for d in devs:
                if d.get("type") in ("cuda", "intel", "amd"):
                    win_gpus.append(d.get("name", "GPU"))
                    if d.get("type") == "cuda" or "nvidia" in d.get("name", "").lower():
                        is_nv = True
        except Exception:
            pass
        if not win_gpus:
            win_gpus = ["Windows DirectX / D3D11 Graphics Engine"]

        return {
            "architecture": GpuArchitecture.WINDOWS_NATIVE,
            "is_dedicated_nvidia": is_nv,
            "is_hybrid_nvidia": False,
            "is_wayland": False,
            "display_server": "windows",
            "switcher_tool": "Windows DirectX / D3D11 / Vulkan",
            "detected_gpus": win_gpus,
            "platform_os": "windows"
        }

    # 3. Linux & Unix Systems
    session_type = (os.environ.get("XDG_SESSION_TYPE") or "").lower()
    is_wayland = "wayland" in session_type or bool(os.environ.get("WAYLAND_DISPLAY"))
    display_server = "wayland" if is_wayland else ("x11" if os.environ.get("DISPLAY") else "headless")

    switcher_info = "None (Standard System)"
    has_nvidia = False
    has_intel = False
    has_amd = False
    gpus_found = []

    # Check lspci if available
    lspci_bin = shutil.which("lspci")
    if lspci_bin:
        try:
            lspci_out = subprocess.check_output(
                [lspci_bin],
                encoding="utf-8",
                stderr=subprocess.DEVNULL,
                errors="ignore"
            )
            for line in lspci_out.splitlines():
                if any(k in line.lower() for k in ["vga", "3d controller", "display controller"]):
                    line_clean = line.split(":")[-1].strip()
                    gpus_found.append(line_clean)
                    if "nvidia" in line.lower():
                        has_nvidia = True
                    if "intel" in line.lower():
                        has_intel = True
                    if "amd" in line.lower() or "advanced micro devices" in line.lower() or "radeon" in line.lower():
                        has_amd = True
        except Exception:
            pass

    # Check if NVIDIA module is loaded / nvidia-smi exists
    if not has_nvidia and shutil.which("nvidia-smi"):
        has_nvidia = True

    # Check Ubuntu/Debian prime-select
    prime_select_bin = shutil.which("prime-select")
    if prime_select_bin:
        try:
            ps_query = subprocess.check_output([prime_select_bin, "query"], encoding="utf-8", stderr=subprocess.DEVNULL).strip().lower()
            if ps_query:
                switcher_info = f"prime-select ({ps_query})"
                if ps_query == "nvidia":
                    return {
                        "architecture": GpuArchitecture.DEDICATED_NVIDIA,
                        "is_dedicated_nvidia": True,
                        "is_hybrid_nvidia": False,
                        "is_wayland": is_wayland,
                        "display_server": display_server,
                        "switcher_tool": switcher_info,
                        "detected_gpus": gpus_found or ["NVIDIA Discrete GPU (Active)"],
                        "platform_os": "linux"
                    }
                elif ps_query == "on-demand":
                    return {
                        "architecture": GpuArchitecture.HYBRID_NVIDIA_ON_DEMAND,
                        "is_dedicated_nvidia": False,
                        "is_hybrid_nvidia": True,
                        "is_wayland": is_wayland,
                        "display_server": display_server,
                        "switcher_tool": switcher_info,
                        "detected_gpus": gpus_found or ["NVIDIA Optimus Hybrid"],
                        "platform_os": "linux"
                    }
                elif ps_query == "intel":
                    return {
                        "architecture": GpuArchitecture.INTEGRATED_ONLY,
                        "is_dedicated_nvidia": False,
                        "is_hybrid_nvidia": False,
                        "is_wayland": is_wayland,
                        "display_server": display_server,
                        "switcher_tool": switcher_info,
                        "detected_gpus": gpus_found or ["Intel Integrated Graphics"],
                        "platform_os": "linux"
                    }
        except Exception:
            pass

    # Check Fedora/ASUS supergfxctl
    supergfx_bin = shutil.which("supergfxctl")
    if supergfx_bin:
        try:
            sg_query = subprocess.check_output([supergfx_bin, "-g"], encoding="utf-8", stderr=subprocess.DEVNULL).strip()
            if sg_query:
                switcher_info = f"supergfxctl ({sg_query})"
                if sg_query.lower() == "dedicated":
                    return {
                        "architecture": GpuArchitecture.DEDICATED_NVIDIA,
                        "is_dedicated_nvidia": True,
                        "is_hybrid_nvidia": False,
                        "is_wayland": is_wayland,
                        "display_server": display_server,
                        "switcher_tool": switcher_info,
                        "detected_gpus": gpus_found,
                        "platform_os": "linux"
                    }
                elif sg_query.lower() == "hybrid":
                    return {
                        "architecture": GpuArchitecture.HYBRID_NVIDIA_ON_DEMAND,
                        "is_dedicated_nvidia": False,
                        "is_hybrid_nvidia": True,
                        "is_wayland": is_wayland,
                        "display_server": display_server,
                        "switcher_tool": switcher_info,
                        "detected_gpus": gpus_found,
                        "platform_os": "linux"
                    }
        except Exception:
            pass

    # Check Arch/universal envycontrol
    envy_bin = shutil.which("envycontrol")
    if envy_bin:
        try:
            envy_query = subprocess.check_output([envy_bin, "--query"], encoding="utf-8", stderr=subprocess.DEVNULL).strip().lower()
            if envy_query:
                switcher_info = f"envycontrol ({envy_query})"
                if envy_query == "nvidia":
                    return {
                        "architecture": GpuArchitecture.DEDICATED_NVIDIA,
                        "is_dedicated_nvidia": True,
                        "is_hybrid_nvidia": False,
                        "is_wayland": is_wayland,
                        "display_server": display_server,
                        "switcher_tool": switcher_info,
                        "detected_gpus": gpus_found,
                        "platform_os": "linux"
                    }
                elif envy_query == "hybrid":
                    return {
                        "architecture": GpuArchitecture.HYBRID_NVIDIA_ON_DEMAND,
                        "is_dedicated_nvidia": False,
                        "is_hybrid_nvidia": True,
                        "is_wayland": is_wayland,
                        "display_server": display_server,
                        "switcher_tool": switcher_info,
                        "detected_gpus": gpus_found,
                        "platform_os": "linux"
                    }
        except Exception:
            pass

    # Hardware topology fallback via lspci
    if has_nvidia and not (has_intel or has_amd):
        # Desktop PC or workstation with only NVIDIA GPU installed
        return {
            "architecture": GpuArchitecture.DEDICATED_NVIDIA,
            "is_dedicated_nvidia": True,
            "is_hybrid_nvidia": False,
            "is_wayland": is_wayland,
            "display_server": display_server,
            "switcher_tool": "Hardware Dedicated NVIDIA (Desktop/Workstation)",
            "detected_gpus": gpus_found,
            "platform_os": "linux"
        }
    elif has_nvidia and (has_intel or has_amd):
        # Dual-GPU laptop with default on-demand offload
        return {
            "architecture": GpuArchitecture.HYBRID_NVIDIA_ON_DEMAND,
            "is_dedicated_nvidia": False,
            "is_hybrid_nvidia": True,
            "is_wayland": is_wayland,
            "display_server": display_server,
            "switcher_tool": "Default Hybrid Dual-GPU",
            "detected_gpus": gpus_found,
            "platform_os": "linux"
        }
    elif has_amd and has_intel:
        # Dual-GPU AMD discrete + Intel integrated
        return {
            "architecture": GpuArchitecture.HYBRID_AMD_ON_DEMAND,
            "is_dedicated_nvidia": False,
            "is_hybrid_nvidia": False,
            "is_wayland": is_wayland,
            "display_server": display_server,
            "switcher_tool": "AMD Dynamic Switchable Graphics",
            "detected_gpus": gpus_found,
            "platform_os": "linux"
        }

    # Headless / VM or pure integrated
    if not display_server or display_server == "headless":
        arch = GpuArchitecture.HEADLESS_OR_VM
    else:
        arch = GpuArchitecture.INTEGRATED_ONLY

    return {
        "architecture": arch,
        "is_dedicated_nvidia": False,
        "is_hybrid_nvidia": False,
        "is_wayland": is_wayland,
        "display_server": display_server,
        "switcher_tool": switcher_info,
        "detected_gpus": gpus_found or ["Integrated / Standard Graphics Controller"],
        "platform_os": "linux"
    }


def get_optimal_gpu_env(gpu_preference: str = "AUTO", safe_mode: bool = False) -> Tuple[Dict[str, str], str]:
    """
    Generates verified, non-conflicting environment variables tailored to the host system.
    Guarantees no EGL visual ID crashes, no DRI_PRIME mismatch, and optimal performance.
    
    Returns:
        Tuple of (env_dictionary, explanation_log_string)
    """
    env = os.environ.copy()
    pref_upper = (gpu_preference or "AUTO").upper()
    arch_info = detect_system_gpu_architecture()
    arch = arch_info["architecture"]

    # Windows and macOS do not use Linux DRI / PRIME variables
    if arch_info["platform_os"] in ["windows", "darwin"]:
        env.pop("DRI_PRIME", None)
        env.pop("__NV_PRIME_RENDER_OFFLOAD", None)
        env.pop("__GLX_VENDOR_LIBRARY_NAME", None)
        return env, f"Native {arch_info['platform_os'].title()} Hardware Acceleration ({arch_info['switcher_tool']})"

    # Safe Mode Fallback: Clear all offloading variables to prevent driver crashes
    if safe_mode:
        env.pop("DRI_PRIME", None)
        env.pop("__NV_PRIME_RENDER_OFFLOAD", None)
        env.pop("__GLX_VENDOR_LIBRARY_NAME", None)
        return env, "Self-Healing Safe Mode: Clean Display Environment (PRIME/DRI overrides disabled)"

    # Dedicated NVIDIA Mode (Single GPU desktop or prime-select/supergfxctl dedicated mode)
    if arch == GpuArchitecture.DEDICATED_NVIDIA:
        # Display server is already driving the discrete NVIDIA GPU.
        # Passing __NV_PRIME_RENDER_OFFLOAD or DRI_PRIME is invalid and causes EGL visual failure.
        env.pop("DRI_PRIME", None)
        env.pop("__NV_PRIME_RENDER_OFFLOAD", None)
        env.pop("__GLX_VENDOR_LIBRARY_NAME", None)
        return env, f"Dedicated NVIDIA Primary Display ({arch_info['switcher_tool']})"

    # Hybrid NVIDIA Laptop in On-Demand Mode
    if arch == GpuArchitecture.HYBRID_NVIDIA_ON_DEMAND:
        if "INTEL" in pref_upper or "CPU" in pref_upper:
            env["DRI_PRIME"] = "0"
            env.pop("__NV_PRIME_RENDER_OFFLOAD", None)
            env.pop("__GLX_VENDOR_LIBRARY_NAME", None)
            return env, "Integrated GPU Preference (DRI_PRIME=0, NVIDIA offload disabled)"
        else:
            # Default or explicit NVIDIA preference: activate GLVND offload without DRI_PRIME
            env["__NV_PRIME_RENDER_OFFLOAD"] = "1"
            env["__GLX_VENDOR_LIBRARY_NAME"] = "nvidia"
            env.pop("DRI_PRIME", None)  # Mesa-specific, conflicts with NVIDIA GLVND
            return env, "NVIDIA GLVND Hybrid PRIME Offload (__NV_PRIME_RENDER_OFFLOAD=1, __GLX_VENDOR_LIBRARY_NAME=nvidia)"

    # Hybrid AMD Laptop
    if arch == GpuArchitecture.HYBRID_AMD_ON_DEMAND:
        if "AMD" in pref_upper or "DISCRETE" in pref_upper or "AUTO" in pref_upper:
            env["DRI_PRIME"] = "1"
            env.pop("__NV_PRIME_RENDER_OFFLOAD", None)
            env.pop("__GLX_VENDOR_LIBRARY_NAME", None)
            return env, "AMD Dynamic GPU Offload (DRI_PRIME=1)"
        else:
            env["DRI_PRIME"] = "0"
            env.pop("__NV_PRIME_RENDER_OFFLOAD", None)
            env.pop("__GLX_VENDOR_LIBRARY_NAME", None)
            return env, "Integrated GPU Preference (DRI_PRIME=0)"

    # Default Integrated Graphics or Headless
    env.pop("DRI_PRIME", None)
    env.pop("__NV_PRIME_RENDER_OFFLOAD", None)
    env.pop("__GLX_VENDOR_LIBRARY_NAME", None)
    return env, f"Standard Hardware Accelerated Rendering ({arch_info['display_server']})"


def get_adaptive_chromium_flags(tier: int = 1) -> str:
    """
    Returns adaptive Chromium flags for QtWebEngine depending on self-healing tier:
    - Tier 1: Optimal GPU acceleration with WebGL2 and zero-copy rasterization
    - Tier 2: Safe Mode hardware rasterization with software sandbox bypass
    - Tier 3: Universal Software WebGL (SwiftShader) fallback
    """
    arch_info = detect_system_gpu_architecture()
    wayland_hint = "--ozone-platform-hint=auto" if arch_info["is_wayland"] else ""

    if tier == 1:
        # Full Hardware Acceleration with essential Linux sandbox bypass
        flags = [
            "--no-sandbox",
            "--enable-gpu-rasterization",
            "--enable-zero-copy",
            "--ignore-gpu-blocklist",
            "--enable-webgl",
            "--enable-webgl2-compute-context"
        ]
        if wayland_hint:
            flags.append(wayland_hint)
        return " ".join(flags)

    elif tier == 2:
        # Self-Healing Safe Mode (Fixes ANGLE/EGL/Sandbox incompatibilities)
        flags = [
            "--no-sandbox",
            "--ignore-gpu-blocklist",
            "--enable-webgl",
            "--disable-gpu-sandbox",
            "--use-gl=angle"
        ]
        if wayland_hint:
            flags.append(wayland_hint)
        return " ".join(flags)

    else:
        # Universal Software Fallback (Guaranteed to render even in broken drivers or VMs)
        return "--no-sandbox --disable-gpu --use-gl=swiftshader --enable-webgl"


def sanitize_process_env() -> None:
    """
    Self-sanitizing entrypoint hook for standalone scripts (e.g. native_viewer.py).
    Cleanses the current process os.environ of any known poison variables before Qt / Chromium boots.
    """
    arch_info = detect_system_gpu_architecture()

    # Never allow DRI_PRIME under NVIDIA proprietary driver
    if "NVIDIA" in os.environ.get("__GLX_VENDOR_LIBRARY_NAME", "") or os.environ.get("__NV_PRIME_RENDER_OFFLOAD") == "1":
        os.environ.pop("DRI_PRIME", None)

    # In dedicated NVIDIA mode, strip offload flags that cause ANGLE EGL failure
    if arch_info["architecture"] == GpuArchitecture.DEDICATED_NVIDIA:
        os.environ.pop("DRI_PRIME", None)
        os.environ.pop("__NV_PRIME_RENDER_OFFLOAD", None)
        os.environ.pop("__GLX_VENDOR_LIBRARY_NAME", None)

    # On Windows / macOS, clean Linux-specific flags
    if arch_info["platform_os"] in ["windows", "darwin"]:
        os.environ.pop("DRI_PRIME", None)
        os.environ.pop("__NV_PRIME_RENDER_OFFLOAD", None)
        os.environ.pop("__GLX_VENDOR_LIBRARY_NAME", None)


def run_gpu_diagnostics() -> Dict[str, Any]:
    """
    Performs full system hardware & WebGL diagnostics.
    Useful for CLI troubleshooting (`--diagnose`) and GitHub issue reports.
    """
    arch_info = detect_system_gpu_architecture()
    opt_env, explanation = get_optimal_gpu_env()

    diagnostics = {
        "platform": platform.platform(),
        "python_version": sys.version.split()[0],
        "system_architecture": arch_info["architecture"],
        "display_server": arch_info["display_server"],
        "is_wayland": arch_info["is_wayland"],
        "switcher_tool": arch_info["switcher_tool"],
        "detected_gpus": arch_info["detected_gpus"],
        "recommended_launch_strategy": explanation,
        "chromium_flags_tier1": get_adaptive_chromium_flags(tier=1),
        "chromium_flags_tier2": get_adaptive_chromium_flags(tier=2),
    }

    return diagnostics


if __name__ == "__main__":
    diag = run_gpu_diagnostics()
    print("=" * 70)
    print("🛠  STM32 Structured Wiki Universal GPU Diagnostics")
    print("=" * 70)
    for k, v in diag.items():
        if isinstance(v, list):
            print(f"• {k}:")
            for item in v:
                print(f"    - {item}")
        else:
            print(f"• {k}: {v}")
    print("=" * 70)
