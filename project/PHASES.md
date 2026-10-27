# STM32 Karpathy-Wiki Generator: Application Execution & Phase Roadmap

This document outlines the testable, modular phase execution strategy for the **STM32 Karpathy-Wiki Generator** application. Each phase is independently testable, state-persistent, and fully modular to ensure resumption at any step.

---

## 🎯 Architectural Principles & Anti-Goals
1. **Zero AI / Zero LLM at Runtime**: 100% deterministic parsing using IBM Docling, Regex, Pydantic validation, and Markdown interlinking generators. Zero hallucination.
2. **Hybrid Storage Standard**:
   - Theory, architectural overviews, subsystem links -> `.md` files.
   - All register definitions -> `.json` files in `registers_json/`.
3. **State Checkpointing & Resume Architecture**:
   - Continuous state tracking in `memory/state.json`.
   - Chunk-based processing (20-page or chapter blocks).
   - Atomic writes & warm-boot resumption.
   - Append-only chronological logging in `wiki/log.md`.
4. **Cross-Platform GUI**: Built with `CustomTkinter` supporting file inputs (Reference Manual, Datasheet, Errata, Programming Manual), dark/light theme, progress tracking, and smart output routing defaulting to `artifacts/output/karpathy-wiki/`.

---

## 📌 Phase Roadmap & Test Plan

### Phase 1: Core Data Schemas & Architecture Models
- **Goal**: Define Pydantic models for hardware registers, bitfields, memory maps, Karpathy-Wiki catalog structure, and state checkpoint schema.
- **Deliverables**:
  - `project/src/models/register_model.py`
  - `project/src/models/memory_map_model.py`
  - `project/src/models/state_model.py`
- **Test Criteria**: Unit test instantiation, validation of bit ranges (0-31), access permissions (R/W/RO), hex address regex validation (`0x[0-9A-Fa-f]+`).

### Phase 2: Checkpoint Engine & Append-Only Logger
- **Goal**: Build atomic state manager and logging infrastructure.
- **Deliverables**:
  - `project/src/core/checkpoint_manager.py`
  - `project/src/core/logger.py`
- **Test Criteria**: Test atomic writes, crash recovery, page range progress tracking, and append-only log updates.

### Phase 3: Docling PDF Parser & Register Extraction Pipeline
- **Goal**: Implement IBM Docling PDF extractor and deterministic register parser.
- **Deliverables**:
  - `project/src/parsers/docling_extractor.py`
  - `project/src/parsers/register_parser.py`
- **Test Criteria**: Parse sample pages of RM0468 PDF, extract register blocks, verify bitfield bounds, output valid `registers_json/RCC_CR.json`.

### Phase 4: Karpathy-Wiki Markdown Generator & Hyper-Accurate Cross-Linker
- **Goal**: Build Markdown knowledge base generator and cross-referencing engine.
- **Deliverables**:
  - `project/src/generators/wiki_generator.py`
  - `project/src/generators/cross_linker.py`
- **Test Criteria**: Generate `SCHEMA.md`, `index.md`, `backlinks.md`, `stm32_advanced/` directories, verify all Markdown links resolve cleanly without broken references.

### Phase 5: Cross-Platform CustomTkinter GUI
- **Goal**: Build modern GUI interface for desktop users.
- **Deliverables**:
  - `project/src/gui/app.py`
  - `project/src/gui/theme.py`
- **Test Criteria**: Verify file dialogs, output path defaulting, dark/light mode toggle, dynamic progress bar, log viewer, and non-blocking execution worker thread.

### Phase 6: System Integration & QA Auditing Suite
- **Goal**: Execute end-to-end processing test on RM0468, verify 100% deterministic (no AI calls) behavior, test pause/resume checkpoint recovery.
- **Deliverables**:
  - `project/tests/` unit & integration test suite.
  - Final Audit Report confirming zero hallucination & schema compliance.
