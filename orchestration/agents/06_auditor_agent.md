# Agent 06: Independent Karpathy-Wiki Corpus Auditor & Health Report Generator

## 🎯 Role & Mission
The **Wiki Corpus Auditor Agent** functions as an autonomous, independent quality assurance and verification engine. Its primary objective is to perform exhaustive, multi-algorithmic cross-verification between the **STM32H7 Reference Manual PDF (RM0468)** and the **Generated Karpathy-Style Wiki Corpus** (`/memory/`, `/system/`, `/core/`, `/peripherals/`, `/security/`, `/figures/`, `/tables/`, `/registers_json/`).

---

## 🛠️ Verification Algorithms & Audit Mechanics

### 1. Structural & Chapter Completeness Audit
* Validates all 69 reference manual chapters and front matter pages.
* Verifies page ranges (Pages 1 to 3357), section heading hierarchy (`#`, `##`, `###`), and raw prose completeness.

### 2. Hardware Register Schema & Bit-Field Audit
* Audits 640+ hardware register JSON schemas under `/registers_json/`.
* Verifies address offsets (`0x00`..`0x400`), bit masks (`[31:0]`), access permissions (`R/W`, `RO`, `WOR`), and reset states.

### 3. GFM Table Semantic Parity Audit
* Scans all 642 Markdown tables under `/tables/`.
* Verifies header column preservation, cell count parity, and presence of `TableSelfValidator` semantic fidelity stamps.

### 4. Reference Figure & Visual Asset Audit
* Audits all 866 figure files under `/figures/`.
* Verifies Mermaid ASCII architecture diagrams, asset links (`/assets/figure_X_diagram.png`), and parent IP module back-links.

### 5. Bidirectional Link & Anchor Audit
* Scans 100% of relative Markdown links `[Link Text](../path/to/file.md)`.
* Verifies zero broken links, zero orphan files, and valid MOC (`index.md`) entry points.

---

## 📊 HTML Audit Dashboard Features (`audit_report.html`)
* **Executive Health Score**: Overall Karpathy Wiki Corpus Quality Score (0–100%).
* **Visual Charts**: Interactive Chart.js / SVG donut metrics for Tables, Registers, Figures, Chapters, and Links.
* **Color-Coded Risk Matrix**:
  * 🔴 **High Risk**: Broken register bit masks or missing memory address ranges.
  * 🟡 **Medium Risk**: Missing diagram asset links or unlinked figure references.
  * 🟢 **Pass**: 100% Verified GFM table or validated link.
* **Immediate Action Plan**: Concise recommendation checklist for instant resolution.
