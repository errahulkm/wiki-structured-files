"""
Hardware Device Detector for GPU Acceleration, Multi-GPU Selection, and CPU Fallback.
Detects NVIDIA CUDA GPUs (dGPU), Intel Integrated Graphics (iGPU), CPU acceleration, and selects optimal execution device.
"""

from typing import Dict, Any, List


def detect_hardware_device() -> Dict[str, Any]:
    """
    Detects GPU and CPU hardware capabilities.
    Returns primary hardware info dictionary.
    """
    devices = detect_all_hardware_devices()
    # Default to the most powerful discrete GPU if present
    primary = devices[0] if devices else {
        "id": "cpu",
        "name": "CPU Multithreaded Engine",
        "type": "cpu",
        "vram_gb": 0.0,
        "is_default": True
    }
    
    return {
        "device": primary["id"],
        "gpu_available": primary["type"] == "cuda",
        "device_name": primary["name"],
        "cuda_version": primary.get("cuda_version"),
        "vram_gb": primary.get("vram_gb", 0.0),
        "all_devices": devices
    }


def detect_all_hardware_devices() -> List[Dict[str, Any]]:
    """
    Scans system hardware for all available compute accelerators:
    - Discrete NVIDIA CUDA GPUs (dGPU)
    - Intel Integrated Graphics / OpenVINO (iGPU)
    - System CPU Engine
    Orders devices by compute performance (Most powerful discrete GPU first).
    """
    devices: List[Dict[str, Any]] = []

    # 1. Detect NVIDIA CUDA GPUs
    try:
        import torch
        if torch.cuda.is_available():
            cuda_ver = torch.version.cuda
            cnt = torch.cuda.device_count()
            for i in range(cnt):
                dev_name = torch.cuda.get_device_name(i)
                total_bytes = torch.cuda.get_device_properties(i).total_memory
                vram_gb = round(total_bytes / (1024 ** 3), 2)
                
                devices.append({
                    "id": f"cuda:{i}",
                    "name": f"🚀 NVIDIA {dev_name} (CUDA:{i} - {vram_gb} GB VRAM)",
                    "short_name": f"NVIDIA {dev_name}",
                    "type": "cuda",
                    "index": i,
                    "vram_gb": vram_gb,
                    "cuda_version": cuda_ver,
                    "is_discrete": True
                })
    except Exception:
        pass

    # 2. Detect Windows Graphics Adapters (NVIDIA, Intel Iris/Arc, AMD Radeon)
    import sys
    if sys.platform == "win32":
        try:
            import subprocess
            creationflags = 0x08000000  # CREATE_NO_WINDOW
            wmic_out = ""
            try:
                wmic_out = subprocess.check_output(
                    ["wmic", "path", "win32_VideoController", "get", "name"],
                    encoding="utf-8", stderr=subprocess.DEVNULL, errors="ignore",
                    creationflags=creationflags
                )
            except Exception:
                # Modern Windows 11 fallback when WMIC is deprecated/removed
                wmic_out = subprocess.check_output(
                    ["powershell", "-NoProfile", "-Command", "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"],
                    encoding="utf-8", stderr=subprocess.DEVNULL, errors="ignore",
                    creationflags=creationflags
                )

            for line in wmic_out.splitlines():
                gpu_name = line.strip()
                if not gpu_name or gpu_name.lower() == "name":
                    continue
                if not any(gpu_name in d["name"] for d in devices):
                    is_nvidia = "nvidia" in gpu_name.lower()
                    is_intel = "intel" in gpu_name.lower()
                    is_amd = "amd" in gpu_name.lower() or "radeon" in gpu_name.lower()
                    icon = "🚀" if is_nvidia else ("⚙️" if is_intel else "🎮")
                    devices.append({
                        "id": "cuda:0" if is_nvidia else "cpu",
                        "name": f"{icon} {gpu_name}",
                        "short_name": gpu_name[:30],
                        "type": "cuda" if is_nvidia else ("intel" if is_intel else "amd"),
                        "vram_gb": 4.0 if is_nvidia else (2.0 if is_amd else 1.0),
                        "is_discrete": is_nvidia or is_amd
                    })
        except Exception:
            pass

    # 3. Detect Intel Graphics / OpenVINO / OneAPI on Linux
    if sys.platform.startswith("linux"):
        try:
            import subprocess
            intel_res = subprocess.check_output("lspci | grep -i 'vga\\|3d\\|display' | grep -i 'intel'", shell=True, encoding="utf-8", errors="ignore").strip()
            if intel_res:
                intel_name = intel_res.split(":")[-1].strip()
                devices.append({
                    "id": "cpu",
                    "name": f"⚙️ Intel Integrated Graphics / OpenVINO ({intel_name[:35]})",
                    "short_name": f"Intel Graphics ({intel_name[:25]})",
                    "type": "intel",
                    "vram_gb": 1.0,
                    "is_discrete": False
                })
        except Exception:
            pass

    # 3. Always include CPU Fallback Engine
    devices.append({
        "id": "cpu",
        "name": "💻 System CPU Multithreaded Engine",
        "short_name": "System CPU Engine",
        "type": "cpu",
        "vram_gb": 0.0,
        "is_discrete": False
    })

    # Sort devices so most powerful discrete GPU is index 0 (Default)
    devices.sort(key=lambda d: (not d.get("is_discrete", False), -d.get("vram_gb", 0.0)))
    return devices


if __name__ == "__main__":
    devs = detect_all_hardware_devices()
    print("Detected Hardware Accelerators:")
    for d in devs:
        print(f" - {d['name']}")
