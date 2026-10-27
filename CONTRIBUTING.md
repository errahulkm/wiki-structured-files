# 🤝 Contributing to Wiki File Structured Silicon Engine

First off, thank you for considering contributing to the **Wiki File Structured Silicon Engine**! It's people like you that make open source such an incredible tool for embedded engineers worldwide.

---

## 🧭 How You Can Contribute

1. **Adding Support for New Silicon Families**:
   - Ingest new STMicroelectronics reference manuals (e.g. STM32H7, STM32F4, STM32L5, STM32U5).
   - Expand beyond ST to other major semiconductor vendors: **NXP (i.MX RT, LPC)**, **Texas Instruments (MSPM0, CC26xx)**, **Espressif (ESP32-S3, ESP32-C3)**, **Raspberry Pi (RP2040, RP2350)**, and **RISC-V**.
2. **Improving Parser Accuracy**:
   - Enhance table extraction and bitfield enumeration fidelity in `register_parser.py`.
   - Add new dynamic visualizer modes in `graph_visualizer.py`.
3. **Ecosystem Bridges**:
   - Export register schemas directly into **CMSIS-SVD** files.
   - Build automated bindings for **Zephyr RTOS dts/dtsi** and **Rust `svd2rust` HAL crates**.

---

## 🛠️ Development Setup

1. Fork the repository and clone your fork locally:
   ```bash
   git clone https://github.com/<your-username>/wiki-file-structured-ref-man.git
   cd wiki-file-structured-ref-man
   ```
2. Launch via the zero-friction launcher:
   - **Windows**: `run.bat` or `.\run.ps1`
   - **Linux / macOS**: `./run.sh`
3. Run the automated test suite before opening a pull request:
   ```bash
   PYTHONPATH=project ./venv/bin/pytest project/tests -q
   ```

---

## 📜 Developer Certificate of Origin (DCO)

All contributions to this project must be licensed under the project's **MIT License**. By submitting a Pull Request, you certify that you have the right to submit the code under the MIT License according to the [Developer Certificate of Origin 1.1](https://developercertificate.org/).

---

## 💬 Community & Discussions

- **Questions & Ideas**: Open an issue or join our community discussions.
- **Security Vulnerabilities**: For responsible disclosure, please contact security@silicon-wiki.com.
