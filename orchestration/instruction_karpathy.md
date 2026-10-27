# STM32 Karpathy-Wiki Pipeline: Comprehensive Instruction Guide

This document provides the step-by-step operational guide for building, managing, and visualizing the Karpathy-style Wiki structure for STM32 Microcontrollers (Reference Manual RM0468).

---

## 1. Core Directory Schema & Directory Topology

The pipeline outputs a deterministic, 100% LLM-readable directory tree:

```
karpathy-wiki/
├── index.md                 # Master Map of Content (MOC Dashboard)
├── SCHEMA.md                # Taxonomies, agent workflows & rules
├── memory/                  # Ground truth memory architecture
│   └── memory_map.md        # Master System Memory Map & Base Addresses
├── system/                  # System infrastructure (RCC, PWR, SYSCFG, BUS_MATRIX)
├── core/                    # Processor core & interrupts (NVIC, EXTI, MPU, SYSTICK)
├── peripherals/             # Hardware peripherals (USART, I2C, SPI, TIMERS, ADC, ETH, USB)
├── security/                # Security IP blocks (TRUSTZONE, CRYP, HASH, RNG, OTFDEC)
├── registers_json/          # Isolated hardware register JSONs (e.g. RCC_CR.json)
└── graph_view.html          # Interactive multi-view HTML5 Canvas Knowledge Graph
```

---

## 2. Layered Processing Order (Ground-Truth First)

Do not ingest pages linearly. Process in strict architectural layers:
1. **Layer 1: Master Memory Map & Bus Architecture** (`memory/memory_map.md`, `system/bus_matrix.md`)
2. **Layer 2: System Infrastructure** (`system/rcc.md`, `system/pwr.md`, `system/syscfg.md`)
3. **Layer 3: Core & Interrupts** (`core/nvic.md`, `core/exti.md`, `peripherals/gpio.md`)
4. **Layer 4: Hardware Peripherals** (`peripherals/usart.md`, `peripherals/adc.md`, etc.)
5. **Layer 5: Security IPs** (`security/trustzone.md`, `security/cryp.md`, etc.)

---

## 3. Mandatory Bidirectional Memory Map Interlinking Rules

- **Universal Rule**: Every single IP block file across `system/`, `core/`, `peripherals/`, and `security/` **MUST** bidirectionally link to `[System Memory Map](../memory/memory_map.md)` in Section 3.
- **Master Index Entry**: `index.md` must link to all 30+ IP blocks and `memory/memory_map.md`.

---

## 4. Multi-View Knowledge Graph Engine Specifications

The generated `graph_view.html` visualizer MUST support:
1. **Multi-View Modes**:
   - `🌐 Force Mesh`: Slower, damped physics simulation (`velocity dampening = 0.80`) with dynamic cluster radial expansion (`springRest = 180px`).
   - `📐 Hierarchical DAG`: Top-down layered architecture (Core/Memory -> System -> Peripherals -> Registers).
   - `🌳 Collapsible Tree`: Interactive dendrogram where child nodes expand/collapse.
   - `⭕ Interconnect Ring`: Peripheral memory & bus mapping circular arc view.
2. **Automatic Hardware Acceleration Detection**:
   - Detects GPU WebGL context via `WEBGL_debug_renderer_info` and displays active renderer badge in the header.
3. **Selection Repulsion Physics Clearing**:
   - Non-connected background nodes experience a radial repulsion force (`16000 / dist^2`) away from the active cluster.
4. **Navigation History Controls & Breadcrumbs**:
   - Includes **`◀ Back`** and **`Forward ▶`** header buttons and an interactive clickable **Breadcrumb Trail** (`MOC (Index) ➔ USART ➔ MEMORY_MAP`).
5. **Illuminated Text Badges**:
   - Selected nodes and sub-nodes/registers always display high-contrast illuminated text badges (`#00e5ff` / `#ffffff`) so node names are never hidden.
