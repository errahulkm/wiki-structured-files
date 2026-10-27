# 🚀 One-Click Launch Instructions (Windows, Linux & macOS)

Launching the **STM32 Karpathy-Wiki Generator & Multi-View Knowledge Graph Engine** requires zero installation hassle. It runs seamlessly out-of-the-box on all PCs, laptops, and operating systems.

---

## ⚡ Quick Start by Operating System

### 🪟 Windows 10 / Windows 11 (Command Prompt or File Explorer)
1. **Option A (One-Click GUI)**: Double-click **`run.bat`** in Windows Explorer.
2. **Option B (CMD)**:
   ```cmd
   run.bat
   ```
3. **Option C (PowerShell)**:
   ```powershell
   .\run.ps1
   ```

### 🐧 Linux (Ubuntu, Debian, Fedora, Arch, RHEL)
```bash
chmod +x run.sh
./run.sh
```

### 🍎 macOS (Apple Silicon M1/M2/M3/M4 & Intel)
```bash
chmod +x run.sh
./run.sh
```

---

## 🛠 What the Launchers Automatically Handle:
1. **Virtual Environment Isolation**: Detects system Python 3.10+ and provisions `venv` if missing.
2. **Automated Dependency Synchronization**: Installs and verifies all required packages (`customtkinter`, `pydantic`, `reportlab`, `svgwrite`, `pytest`, etc.).
3. **Cross-Platform Path Configuration**: Dynamically configures `PYTHONPATH` using the platform-native delimiter (`;` on Windows, `:` on Linux/macOS).
4. **Console Window Suppression**: On Windows, suppresses background command prompt popups during live GPU telemetry polling.
5. **Instant GUI Startup**: Automatically boots the CustomTkinter desktop interface.

---

## 💻 Universal Hardware & Laptop/PC Compatibility Matrix

The application embeds an **Automated Adaptive Graphics Runtime** (`gpu_runtime.py` and `hardware_detector.py`) that auto-tunes itself to your exact machine configuration:

| Hardware Configuration | Detection Mechanism | Runtime Strategy | Acceleration Tier |
| :--- | :--- | :--- | :--- |
| **Windows Dedicated GPU (NVIDIA/AMD)** | Windows CIM/WMI & PyTorch CUDA | Direct3D11 / Vulkan & CUDA Cores | 🟢 Tier 1: Max Hardware Acceleration |
| **Windows Dual-GPU Laptops (Optimus)** | Windows VideoController Enumeration | Windows GPU Scheduling + Direct3D | 🟢 Tier 1: Hardware Acceleration |
| **Windows Integrated (Intel Iris Xe/Arc/UHD)** | Win32 VideoController Detection | Direct3D ANGLE Rasterization | 🟢 Tier 1 / 2: Native Acceleration |
| **Linux Dedicated NVIDIA Desktops/Laptops** | `prime-select nvidia` / `supergfxctl` | Direct CUDA Offloading | 🟢 Tier 1: Maximum Hardware |
| **Linux Hybrid Optimus / AMD Switchable** | Dynamic PRIME / DRI detection | Intelligent On-Demand Offload | 🟢 Tier 1: Hybrid Hardware Offload |
| **Apple Silicon (M1/M2/M3/M4)** | macOS Quartz & Metal Engine | Apple Metal / CoreGraphics | 🟢 Tier 1: Native Metal WebGL |
| **Low-End / Thin & Light / Virtual Machines** | CPU multithreaded fallback | Universal SwiftShader WebGL | 🟡 Tier 3: CPU Multithreaded Engine |

---

## 🛡️ Multi-Tier Automated Self-Healing:
If your graphics driver or display server encounters visual ID mismatches or driver crashes, the engine automatically recovers through 4 self-healing fallback tiers:
1. **Tier 1 (Max Performance)**: Hardware WebGL2 + Direct3D / Metal / Vulkan.
2. **Tier 2 (Safe Mode)**: Sanitizes environment, disables GPU sandbox, forces clean ANGLE.
3. **Tier 3 (Universal Software Fallback)**: SwiftShader software WebGL rasterizer.
4. **Tier 4 (Browser Handshake Fallback)**: Launches system Chrome, Edge, Brave, or Firefox via `file:///` URI.

---

## 🩺 Hardware Diagnostic Self-Test (CLI):
To inspect your computer's detected GPU architecture, display server, and WebGL capabilities:

- **Windows**:
  ```cmd
  .\venv\Scripts\python.exe project\src\visualizer\native_viewer.py --diagnose
  ```
- **Linux / macOS**:
  ```bash
  ./venv/bin/python project/src/visualizer/native_viewer.py --diagnose
  ```

---

## 🧪 Automated Test Verification:
Run the full 15-test unit and integration test suite:

- **Windows**:
  ```cmd
  set PYTHONPATH=%cd%\project
  .\venv\Scripts\python.exe -m pytest project\tests -q
  ```
- **Linux / macOS**:
  ```bash
  PYTHONPATH=project ./venv/bin/pytest project/tests -q
  ```
