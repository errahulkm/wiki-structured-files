# STM32H72x/73x Reference Manual (RM0468) Architectural DNA & Graph Blueprint

This document defines the architectural DNA, system taxonomy, and visual graph specifications for the STM32H7 reference manual (RM0468).

---

## 1. System Taxonomy & Topographic Layers

The microcontroller system is structured into 7 primary architectural layers:
1. **Master Index Layer (`Master Index`)**: Entry MOC (`index.md`) dashboard.
2. **Memory Layer (`Memory`)**: Master system memory map (`memory/memory_map.md`) defining Flash, AXI SRAM, SRAM1-4, and ITCM/DTCM address space.
3. **System Infrastructure Layer (`System`)**: System control IPs (`RCC`, `PWR`, `SYSCFG`, `BUS_MATRIX`, `GTZC`).
4. **Cortex-M7 Core Layer (`Core`)**: CPU execution and interrupt management (`NVIC`, `EXTI`, `MPU`, `SYSTICK`).
5. **Peripherals Layer (`Peripherals`)**: Autonomous & communication hardware IPs (`USART`, `SPI`, `I2C`, `TIMERS`, `ADC`, `DAC`, `ETH`, `USB`, `SDMMC`, `FDCAN`).
6. **Security Architecture Layer (`Security`)**: Cryptographic & hardware protection (`TRUSTZONE`, `CRYP`, `HASH`, `RNG`, `OTFDEC`).
7. **Hardware Register Layer (`Registers`)**: Isolated register JSON specifications (`registers_json/`).

---

## 2. Universal Interlink Ground Truth

- **Master Memory Map (`memory/memory_map.md`)**: Represents physical silicon truth. Every IP block across all categories MUST link bidirectionally to `memory/memory_map.md`.
- **Clock Tree & Power Mesh**: Every IP block connects back to `system/rcc.md` for clock gating and `system/pwr.md` for power domains.

---

## 3. Knowledge Graph Engine & Visualization Architecture

- **Multi-View Modes**:
  - `🌐 Force Mesh`: Physics simulation with damped velocity (dampening = 0.80) and dynamic cluster radial expansion.
  - `📐 Hierarchical DAG`: Top-down layered architecture (Core -> Memory -> System -> Peripherals -> Registers).
  - `🌳 Collapsible Tree`: Interactive dendrogram layout.
  - `⭕ Interconnect Ring`: Peripheral memory & bus mapping circular arc view.
- **Hardware Acceleration**: Automatic GPU WebGL detection with CPU vector fallback.
- **Navigation Controls**: Back `◀` and Forward `▶` selection history stack with interactive breadcrumb trail (`MOC ➔ USART ➔ MEMORY_MAP`).
- **Illuminated Text Badges**: High-contrast text labels inside dark pill tags (`#00e5ff` / `#ffffff`) to ensure full register name visibility.
