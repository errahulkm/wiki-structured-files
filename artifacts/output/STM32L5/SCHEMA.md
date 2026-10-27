# Karpathy-Wiki Directory & Linking Schema (STM32L5 Series (RM0438))

## 1. Virtual Directory Taxonomy (8-Layer Loss-Less Architecture)
- `/index.md`: Master Map of Content (MOC Entry Dashboard interlinking Chapters, IPs, Figures, and Tables).
- `/chapters/`: Dedicated technical ingestion of ALL official reference manual chapters.
- `/memory/`: Master System Memory Map (`memory_map.md`), Flash and RAM partition maps.
- `/system/`: Power (`pwr.md`), Clocks (`rcc.md`), and System Configuration (`syscfg.md`, `bkp.md`).
- `/core/`: CPU Core architecture, Interrupts (`interrupts.md` or `nvic.md`), and Debug (`debug.md`).
- `/peripherals/`: Dedicated autonomous hardware IP documentation.
- `/security/`: Cryptographic accelerators and hardware protection (if equipped on silicon).
- `/figures/`: Architectural block diagrams and signal flowcharts.
- `/tables/`: Hardware register tables, bit definitions, and configuration matrices.
- `/registers_json/`: Isolated 32-bit hardware register JSON schemas.
- `/assets/`: Standardized diagram image assets.

## 2. Zero-Dangling Bidirectional Cross-Linking Rules
Every node across the 8-layer virtual directory has zero dangling references:
1. Every Chapter file in `/chapters/` connects to `index.md`, `/figures/`, `/tables/`, and parent IP modules.
2. Every Figure file in `/figures/` connects to `index.md`, `/memory/`, and parent IP modules.
3. Every Table file in `/tables/` connects to `index.md`, `/memory/`, and parent IP modules.
4. Every Register JSON schema in `/registers_json/` connects deterministically to its parent IP module.
