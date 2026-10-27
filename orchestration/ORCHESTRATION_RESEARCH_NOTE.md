# Orchestration Research Note & Fine-Tuning History (Git-Style Log)

## Executive Summary
This document records the architectural design, initial failure modes, iterative fine-tuning phases, and final flawless orchestration state for the **STM32H7 (RM0468) Karpathy-Wiki Generator & Multi-View Knowledge Graph Engine**.

---

## 📜 Git-Style Orchestration Version History

### `v1.0.0` - Initial Prototype (Monolithic Ingestion & Unlinked Directory Structure)
- **Architecture**: Single-pass ingestion of PDF files.
- **Failures Identified**:
  - Manual processing of 3,000+ pages caused LLM context overflow and severe token exhaustion.
  - Inter-IP dependency links were missing or broken.
  - Multi-document confusion when combining Reference Manual, Datasheet, Errata Sheet, and Programming Manual simultaneously.
  - Register data was embedded directly as flat markdown text, bloating context windows.
- **User Feedback 1**: *"We did mistake. Remove datasheet, errata sheet, programming manual for now... focus strictly on reference manual. Process bottom-up."*

---

### `v1.1.0` - Scope Refinement & Deterministic Directory Schema
- **Fixes Applied**:
  - Restructured target domain exclusively to the **STM32H7 Reference Manual (RM0468)**.
  - Implemented 5-layer virtual directory hierarchy:
    - `/memory/` (`memory_map.md`)
    - `/system/` (`bus_matrix.md`, `rcc.md`, `pwr.md`, `syscfg.md`)
    - `/core/` (`nvic.md`, `systick.md`, `exti.md`)
    - `/peripherals/` (`gpio.md`, `usart.md`, `i2c.md`, `spi.md`, `timers.md`, `adc.md`, `eth.md`, `usb.md`)
    - `/security/` (`trustzone.md`, `cryp.md`, `rng.md`)
    - `/registers_json/` (Isolated Pydantic JSON schemas)
  - Enforced universal 4-part Markdown section template.
- **User Feedback 2**: *"Not all IP covered in peripheral directory... add button for graphical view of nodes like Obsidian tool."*

---

### `v1.2.0` - Interactive Graph Visualization & Memory Map Ground Truth
- **Fixes Applied**:
  - Built standalone HTML5 Canvas force-directed graph visualizer (`graph_view.html`).
  - Added full architectural coverage across 30+ hardware IP blocks.
  - Enforced mandatory **bidirectional Memory Map interlinking** across all IP files back to `memory/memory_map.md`.
- **User Feedback 3**: *"Selection of sub-nodes should highlight nicely... add topology layer highlight buttons."*

---

### `v1.3.0` - Visual Intelligence & Selection Repulsion Clearing
- **Fixes Applied**:
  - Implemented **Glowing Cyan Double-Ring Highlighting** for connected sub-nodes.
  - Added **Radial Selection Repulsion Force** (`16000 / dist^2` clearing force pushing non-connected background nodes away from selected clusters).
  - Added **Automatic Hardware GPU Detection** via WebGL (`WEBGL_debug_renderer_info`) with CPU SIMD fallback.
- **User Feedback 4**: *"When browsing sub-nodes I lose parent node context... add Back and Forward arrow buttons like a web browser."*

---

### `v1.4.0` - Navigation History Stack & Breadcrumbs
- **Fixes Applied**:
  - Implemented Selection History Stack (`navHistory`, `navHistoryIndex`).
  - Added **`◀ Back`** and **`Forward ▶`** top control bar buttons.
  - Rendered an interactive **Breadcrumb Trail** (`MOC (Index) ➔ USART ➔ MEMORY_MAP`) inside the Inspector Drawer.
- **User Feedback 5**: *"Make physics slower... look still hairball like... add options for DAG top-down view, collapsible tree, and chord diagram... make register selection names visible."*

---

### `v2.0.0` - Final Flawless Orchestration (Multi-View Engine & Illuminated Badges)
- **Final Architecture**:
  1. **Modular Multi-View Layout Switcher**:
     - `🌐 Force Mesh`: Slower, damped physics simulation (`dampening = 0.80`) with dynamic cluster radial expansion (`springRest = 180px`).
     - `📐 Hierarchical DAG`: Top-down system architecture view (Core -> Memory -> System -> Peripherals -> Registers).
     - `🌳 Collapsible Tree`: Interactive dendrogram layout.
     - `⭕ Interconnect Ring`: Peripheral memory & bus mapping circular arc view.
  2. **High-Contrast Illuminated Text Badges**:
     - Selected nodes and register nodes ALWAYS display high-contrast illuminated dark pill badges (`#00e5ff` / `#ffffff`) so node names are 100% readable regardless of zoom level or layer filter.
  3. **Continuous Instruction & DNA Synchronization**:
     - Fine-tuned `01_chief_orchestrator.md`, `instruction_karpathy.md`, `karpathy-prompt.md`, `RM0468_STM32H7_DNA.md`, and `PRD.md` to reflect all architectural lessons learned.

---

## 🛠 Reusable Orchestration Framework for Future Applications

When orchestrating large-scale hardware reference manuals or complex codebases for LLMs, follow this master checklist:
1. **Layered Ingestion (Ground Truth First)**: Always extract master memory maps, bus matrices, and core power/clock trees before extracting leaf peripherals.
2. **Hybrid Content Separation**: Keep human-readable overviews and dependencies in Markdown; isolate quantitative schemas (register bitfields, address offsets, reset values) into strict JSON files.
3. **Multi-View Visual Analytics**: Provide multiple visual layouts (Mesh, DAG, Tree, Ring) so users can analyze hierarchical flow as well as dynamic mesh interconnects.
4. **State Persistence & Warm Boot**: Maintain an append-only log and atomic state file (`memory/state.json`) after every ingestion chunk.
5. **Continuous Agent Instruction Synchronization**: Update system prompts, PRD documents, and agent instructions whenever user feedback reveals operational edge cases.
