# Knowledge Item: STM32 Orchestration & Multi-View Knowledge Graph Fine-Tuning

## Overview
This Knowledge Item documents the fine-tuned orchestration pattern for parsing massive micro-controller reference manuals (RM0468) into a deterministic Karpathy-Wiki structure and an interactive multi-view knowledge graph.

## Key Architectural Principles
1. **Scope Boundary**: Restrict processing exclusively to the Reference Manual (RM0468) during initial ingestion.
2. **Layered Processing Hierarchy**:
   - Layer 1: System Memory Map (`memory/memory_map.md`) & Bus Matrix (`system/bus_matrix.md`).
   - Layer 2: System Infrastructure (`system/rcc.md`, `system/pwr.md`, `system/syscfg.md`).
   - Layer 3: Core Execution & Interrupts (`core/nvic.md`, `core/exti.md`, `core/mpu.md`).
   - Layer 4: Hardware Peripherals (`peripherals/usart.md`, `peripherals/adc.md`, etc.).
   - Layer 5: Security Architecture (`security/trustzone.md`, `security/cryp.md`, etc.).
   - Layer 6: Isolated Register JSONs (`registers_json/`).
3. **Universal Memory Map Interlinking**: Every single IP block MUST bidirectionally link to `[System Memory Map](../memory/memory_map.md)` in Section 3.
4. **Multi-View Visualizer Architecture**:
   - `🌐 Force Mesh`: Damped physics with dynamic cluster radial expansion.
   - `📐 Hierarchical DAG`: Top-down layered architecture.
   - `🌳 Collapsible Tree`: Interactive dendrogram layout.
   - `⭕ Interconnect Ring`: Circular bus interconnect view.
5. **Selection History Stack**: `◀ Back` / `Forward ▶` navigation controls + interactive breadcrumbs.
6. **Illuminated Text Badges**: High-contrast white/cyan pill badges ensuring full visibility for selected nodes and register names.
