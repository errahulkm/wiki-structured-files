"""
Obsidian-Style Interactive Knowledge Graph Visualizer.
Parses all Markdown relative links and [[WikiLinks]] across any Structured Wiki directory tree.
Generates a 100% self-contained HTML5 Canvas & WebGL 3D interactive multi-view architecture engine (graph_view.html)
with:
1. 🌐 Force Mesh (Physics simulation with speed multiplier slider 1x-5x, concentric orbital rings, hard zero-overlap collision physics & satellite register clustering)
2. 📐 Hierarchical DAG (Top-down architecture with strict Level 4 register staging at Y >= 730px, 7-column dynamic grids for Ethernet ETH / RCC & parent-centered alignment)
3. 🌳 Collapsible Tree (Re-architected Zero-Overlap Radial Tree with 360° category trunks, staggered sub-rings, multi-tier register arc expansion & pure hierarchy edge filtering)
4. ⭕ Interconnect Ring (Dynamic Double/Triple Concentric Petal Rosette Orbitals for RCC, ETH & high-density IPs; zero-overlap multi-sub-rings for target registers; MOC anchored on Outer Base Ring)
5. 🔮 3D WebGL Space (GPU-accelerated spatial Z-axis architecture layering with interactive 3D camera fly-to animations & node inspector sync)
6. 🎈 Dynamic Balloon Circle Auto-Sizing & Multi-Line Inside-Circle Text Auto-Fitting
7. ⚡ Automatic GPU/CPU hardware acceleration detection & Deterministic 3-Pass Register Edge Linker
8. ◀ Back / Forward ▶ navigation history controls & interactive breadcrumbs
"""

import os
import re
import json
import time
import sys
import shutil
import subprocess
import webbrowser
from typing import Dict, Any, List, Set, Tuple, Optional

from ..core.logger import WikiLogger
from ..core.mcu_detector import detect_mcu_metadata
from ..core.gpu_runtime import (
    get_optimal_gpu_env,
    get_adaptive_chromium_flags,
    detect_system_gpu_architecture,
    run_gpu_diagnostics,
)


class KnowledgeGraphVisualizer:
    """Generates a 100% self-contained HTML5 Canvas & WebGL 3D multi-view architecture graph of all interlinked STM32 IP blocks."""

    def __init__(self, output_root: str = "artifacts/output/structured-wiki",
                 wiki_root: Optional[str] = None,
                 logger: Optional[WikiLogger] = None) -> None:
        """Initializes visualizer with target output directory."""
        target = wiki_root if wiki_root is not None else output_root
        self.output_root = os.path.abspath(target)
        self.logger = logger or WikiLogger()

    def build_graph_data(self) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], float]:
        """Scans output_root markdown & JSON files, extracting nodes, edges, and detailed content."""
        start_time = time.time()
        nodes: Dict[str, Dict[str, Any]] = {}
        edges: Set[Tuple[str, str, str]] = set()

        if not os.path.exists(self.output_root):
            return [], [], 0.0

        # 1. First pass: Collect all files as candidate nodes & extract details
        for root_dir, _, files in os.walk(self.output_root):
            for file in files:
                if file.endswith((".md", ".json")) and file != "SCHEMA.md":
                    abs_path = os.path.join(root_dir, file)
                    rel_path = os.path.relpath(abs_path, self.output_root)
                    
                    # Strict Rule: ONLY core, memory, peripherals, security, system, and index.md in Graph View
                    allowed_dirs = ("core/", "memory/", "peripherals/", "security/", "system/", "registers_json/")
                    if not (rel_path.startswith(allowed_dirs) or rel_path in ["index.md", "INDEX.md"]):
                        continue

                    # Node ID & Label
                    node_id = rel_path
                    label = os.path.splitext(file)[0].upper()
                    if label == "INDEX":
                        label = "MOC (Index)"

                    category = self._determine_category(rel_path)
                    color = self._determine_color(category)

                    reg_category = "General"
                    if file.endswith(".json"):
                        lbl_u = label.upper()
                        if any(k in lbl_u for k in ["CR", "CFGR", "CTRL", "IER", "DCR"]):
                            reg_category = "Config"
                            color["background"] = "#00e5ff"  # Cyan Orbit 1
                        elif any(k in lbl_u for k in ["SR", "ISR", "RIS", "MIS", "FSR", "FLAG", "ICR", "STAT"]):
                            reg_category = "Status"
                            color["background"] = "#fbbf24"  # Amber Orbit 2
                        elif any(k in lbl_u for k in ["DR", "TDR", "RDR", "FIFO", "RXDR", "TXDR", "DATA"]):
                            reg_category = "Data"
                            color["background"] = "#34d399"  # Emerald Orbit 3

                    # Detailed Content Extraction
                    details_html = self._extract_node_details(abs_path, file, category)

                    nodes[node_id] = {
                        "id": node_id,
                        "label": label,
                        "group": category,
                        "regCategory": reg_category,
                        "color": color["background"],
                        "borderColor": color["border"],
                        "path": rel_path,
                        "isRegister": file.endswith(".json"),
                        "size": 28 if label == "MOC (Index)" else (22 if category != "Registers" else 16),
                        "details": details_html
                    }

        # 2. Second pass: Parse links from Markdown files
        for root_dir, _, files in os.walk(self.output_root):
            for file in files:
                if file.endswith(".md") and file != "SCHEMA.md":
                    abs_path = os.path.join(root_dir, file)
                    src_rel = os.path.relpath(abs_path, self.output_root)
                    src_dir = os.path.dirname(abs_path)

                    try:
                        with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()

                        # Markdown links: [text](target)
                        md_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
                        for text, target in md_links:
                            if target.startswith(("http://", "https://", "#")):
                                continue
                            
                            target_path = target.split('#')[0]
                            if not target_path:
                                continue

                            abs_target = os.path.normpath(os.path.join(src_dir, target_path))
                            target_rel = os.path.relpath(abs_target, self.output_root)

                            if target_rel in nodes:
                                edges.add((src_rel, target_rel, text))
                            else:
                                if not (target_rel.startswith(allowed_dirs) or target_rel in ["index.md", "INDEX.md"]):
                                    continue
                                base_target = os.path.basename(target_path)
                                for candidate_id in nodes:
                                    if os.path.basename(candidate_id) == base_target:
                                        edges.add((src_rel, candidate_id, text))
                                        break

                        # Obsidian WikiLinks: [[target]] or [[target|label]]
                        wiki_links = re.findall(r'\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]', content)
                        for target_name, alt_label in wiki_links:
                            clean_target = target_name.strip().lower()
                            for candidate_id, node_data in nodes.items():
                                if clean_target in candidate_id.lower() or clean_target == node_data["label"].lower():
                                    edges.add((src_rel, candidate_id, alt_label or target_name))
                                    break
                    except Exception as e:
                        self.logger.warning(f"Error parsing graph links in {src_rel}: {e}")

        # 3. Third pass: DETERMINISTIC HARDWARE REGISTER PREFIX LINKING ENGINE
        prefix_ip_map = {
            "FDCAN": "peripherals/fdcan.md",
            "USB": "peripherals/usb.md",
            "OTG": "peripherals/usb.md",
            "USART": "peripherals/usart.md",
            "UART": "peripherals/usart.md",
            "LPUART": "peripherals/usart.md",
            "ETH": "peripherals/eth.md",
            "GPIO": "peripherals/gpio.md",
            "SPI": "peripherals/spi.md",
            "I2C": "peripherals/i2c.md",
            "TIM": "peripherals/timers.md",
            "TIM1": "peripherals/timers.md",
            "TIM2": "peripherals/timers.md",
            "TIM3": "peripherals/timers.md",
            "TIM4": "peripherals/timers.md",
            "TIM5": "peripherals/timers.md",
            "TIM8": "peripherals/timers.md",
            "TIM12": "peripherals/timers.md",
            "TIM13": "peripherals/timers.md",
            "TIM14": "peripherals/timers.md",
            "TIM15": "peripherals/timers.md",
            "TIM16": "peripherals/timers.md",
            "TIM17": "peripherals/timers.md",
            "TIM23": "peripherals/timers.md",
            "TIM24": "peripherals/timers.md",
            "LPTIM": "peripherals/lptim.md",
            "ADC": "peripherals/adc.md",
            "DAC": "peripherals/dac.md",
            "COMP": "peripherals/comp.md",
            "OPAMP": "peripherals/opamp.md",
            "DTS": "peripherals/dts.md",
            "DMA": "peripherals/dma.md",
            "DMA1": "peripherals/dma.md",
            "DMA2": "peripherals/dma.md",
            "DMAMUX": "peripherals/dma.md",
            "DMAMUX1": "peripherals/dma.md",
            "DMAMUX2": "peripherals/dma.md",
            "BDMA": "peripherals/dma.md",
            "MDMA": "peripherals/dma.md",
            "DMA2D": "peripherals/dma2d.md",
            "SDMMC": "peripherals/sdmmc.md",
            "LTDC": "peripherals/ltdc.md",
            "FSMC": "peripherals/fsmc.md",
            "FMC": "peripherals/fsmc.md" if "peripherals/fsmc.md" in nodes else "peripherals/fmc.md",
            "TIMX": "peripherals/timers.md",
            "TIMERS": "peripherals/timers.md",
            "TIMER": "peripherals/timers.md",
            "TIM": "peripherals/timers.md",
            "GPIOX": "peripherals/gpio.md",
            "AFIO": "peripherals/gpio.md",
            "BKP": "peripherals/bkp.md" if "peripherals/bkp.md" in nodes else "system/pwr.md",
            "OCTOSPI": "peripherals/octospi.md",
            "SAI": "peripherals/sai.md",
            "SPDIFRX": "peripherals/spdifrx.md",
            "DCMI": "peripherals/dcmi.md",
            "CRC": "peripherals/crc.md",
            "WWDG": "peripherals/wwdg.md",
            "IWDG": "peripherals/iwdg.md",
            "RTC": "peripherals/rtc.md",
            "CEC": "peripherals/usart.md",
            "CORDIC": "peripherals/dac.md",
            "FMAC": "peripherals/dac.md",
            "SMPMI": "peripherals/usart.md",
            "SWPMI": "peripherals/usart.md",
            "PSSI": "peripherals/gpio.md",
            "MDIOS": "peripherals/eth.md",
            "HSEM": "system/syscfg.md",
            "VREFBUF": "system/syscfg.md",
            "DBGMCU": "system/syscfg.md",
            "RCC": "system/rcc.md",
            "PWR": "system/pwr.md",
            "SYSCFG": "system/syscfg.md",
            "SYSROM": "system/syscfg.md",
            "EXTI": "system/exti.md",
            "NVIC": "core/nvic.md",
            "MPU": "core/mpu.md",
            "STK": "core/systick.md",
            "CRYP": "security/cryp.md",
            "HASH": "security/hash.md",
            "RNG": "security/rng.md",
            "OTFDEC": "security/otfdec.md",
            "TZSC": "security/trustzone.md",
            "TZIC": "security/trustzone.md",
            "FLASH": "memory/memory_map.md",
            "RAMECC": "memory/memory_map.md"
        }

        # Build direct prefix map from node labels
        label_to_id = {}
        for nid, ndata in nodes.items():
            label_to_id[ndata["label"].upper()] = nid
            stem = ndata["label"].split('_')[0].upper()
            if stem not in prefix_ip_map and not ndata["isRegister"]:
                prefix_ip_map[stem] = nid

        for nid, ndata in nodes.items():
            if ndata["isRegister"]:
                reg_name = ndata["label"]
                parts = reg_name.split('_')
                prefix = parts[0].upper()

                parent_ip_id = None
                if prefix in prefix_ip_map:
                    parent_ip_id = prefix_ip_map[prefix]
                elif prefix in label_to_id:
                    parent_ip_id = label_to_id[prefix]
                elif prefix.startswith("TIM"):
                    parent_ip_id = "peripherals/timers.md"
                elif prefix.startswith("GPIO") or prefix == "AFIO":
                    parent_ip_id = "peripherals/gpio.md"
                elif prefix.startswith("FSMC") or prefix.startswith("FMC"):
                    parent_ip_id = "peripherals/fsmc.md" if "peripherals/fsmc.md" in nodes else "peripherals/fmc.md"
                elif prefix.startswith("BKP"):
                    parent_ip_id = "peripherals/bkp.md" if "peripherals/bkp.md" in nodes else "system/pwr.md"
                elif prefix.startswith("RTC"):
                    parent_ip_id = "peripherals/rtc.md"
                elif prefix.startswith("DMA"):
                    parent_ip_id = "peripherals/dma.md"
                elif prefix.startswith("ADC"):
                    parent_ip_id = "peripherals/adc.md"
                elif prefix.startswith("DAC"):
                    parent_ip_id = "peripherals/dac.md"
                elif prefix.startswith("CAN"):
                    parent_ip_id = "peripherals/can.md"
                elif prefix.startswith("USART") or prefix.startswith("UART"):
                    parent_ip_id = "peripherals/usart.md"
                elif prefix.startswith("SPI") or prefix.startswith("I2S"):
                    parent_ip_id = "peripherals/spi.md"
                elif prefix.startswith("I2C"):
                    parent_ip_id = "peripherals/i2c.md"
                elif prefix.startswith("USB") or prefix.startswith("OTG"):
                    parent_ip_id = "peripherals/usb.md"
                elif prefix.startswith("SDIO") or prefix.startswith("SDMMC"):
                    parent_ip_id = "peripherals/sdio.md" if "peripherals/sdio.md" in nodes else "peripherals/sdmmc.md"
                elif prefix.startswith("ETH"):
                    parent_ip_id = "peripherals/eth.md"
                elif prefix.startswith("PWR"):
                    parent_ip_id = "system/pwr.md"
                elif prefix.startswith("RCC"):
                    parent_ip_id = "system/rcc.md"
                elif prefix.startswith("FLASH"):
                    parent_ip_id = "memory/memory_map.md"
                elif prefix.startswith("EXTI"):
                    parent_ip_id = "system/exti.md"
                elif prefix.startswith("CRC"):
                    parent_ip_id = "peripherals/crc.md"
                elif prefix.startswith("WWDG"):
                    parent_ip_id = "peripherals/wwdg.md"
                elif prefix.startswith("IWDG"):
                    parent_ip_id = "peripherals/iwdg.md"

                if parent_ip_id and parent_ip_id in nodes:
                    edges.add((parent_ip_id, nid, f"{prefix} Register"))

        node_list = list(nodes.values())
        edge_list = [
            {"source": src, "target": dst, "label": label}
            for src, dst, label in edges
        ]

        elapsed = time.time() - start_time
        self.logger.info(f"Generated Knowledge Graph in {elapsed:.3f}s: {len(node_list)} Nodes, {len(edge_list)} Inter-IP Edges.")
        return node_list, edge_list, elapsed

    def _extract_node_details(self, abs_path: str, file_name: str, category: str) -> str:
        """Extracts structured summary/details from markdown or JSON register file."""
        try:
            if file_name.endswith(".json"):
                with open(abs_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                long_name = data.get("long_name", file_name)
                offset = data.get("address_offset", "0x00")
                reset = data.get("reset_value", "0x00000000")
                desc = data.get("description", "")
                bit_fields = data.get("bit_fields", [])

                fields_html = ""
                for bf in bit_fields[:6]:
                    fields_html += f"<li><strong>{bf.get('name')}</strong> (Bit {bf.get('bit_offset')}, width {bf.get('bit_width')}): {bf.get('description', '')}</li>"
                if len(bit_fields) > 6:
                    fields_html += f"<li><em>+ {len(bit_fields) - 6} more bit fields...</em></li>"

                return f"""
                <div class="node-detail-card">
                    <h4>{long_name}</h4>
                    <p><strong>Address Offset:</strong> <code>{offset}</code> | <strong>Reset:</strong> <code>{reset}</code></p>
                    <p class="desc">{desc}</p>
                    <h5 style="margin-top:8px;color:#38bdf8;">Hardware Bitfields ({len(bit_fields)}):</h5>
                    <ul class="bitfield-list">{fields_html}</ul>
                </div>
                """
            else:
                with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()

                headers = re.findall(r'^#{1,3}\s+(.+)$', text, re.MULTILINE)
                summary_snippet = text[:400].replace('\n', ' ').strip()

                header_chips = "".join([f'<span class="chip">{h}</span>' for h in headers[:5]])

                return f"""
                <div class="node-detail-card">
                    <p class="desc">{summary_snippet}...</p>
                    <h5 style="margin-top:8px;color:#38bdf8;">Key Document Sections:</h5>
                    <div class="chip-group">{header_chips}</div>
                </div>
                """
        except Exception as e:
            return f"<p style='color:#ef4444;'>Could not extract details: {e}</p>"

    def _determine_category(self, rel_path: str) -> str:
        """Determines the architectural layer category of a file."""
        rel_path = rel_path.replace("\\", "/")
        if rel_path == "index.md":
            return "Master Index"
        elif rel_path.startswith("memory/"):
            return "Memory"
        elif rel_path.startswith("system/"):
            return "System"
        elif rel_path.startswith("core/"):
            return "Core"
        elif rel_path.startswith("peripherals/"):
            return "Peripherals"
        elif rel_path.startswith("security/"):
            return "Security"
        elif rel_path.startswith("registers_json/"):
            return "Registers"
        return "General"

    def _determine_color(self, category: str) -> Dict[str, str]:
        """Provides curated theme colors for node categories."""
        color_map = {
            "Master Index": {"background": "#ec4899", "border": "#f472b6"},
            "Memory": {"background": "#3b82f6", "border": "#60a5fa"},
            "System": {"background": "#f59e0b", "border": "#fbbf24"},
            "Core": {"background": "#a855f7", "border": "#c084fc"},
            "Peripherals": {"background": "#10b981", "border": "#34d399"},
            "Security": {"background": "#ef4444", "border": "#f87171"},
            "Registers": {"background": "#06b6d4", "border": "#22d3ee"},
            "General": {"background": "#6b7280", "border": "#9ca3af"},
        }
        return color_map.get(category, color_map["General"])

    def build_interactive_graph(self, output_html: Optional[str] = None) -> str:
        """Builds graph_view.html and returns path (alias for generate_html_graph)."""
        path = self.generate_html_graph()
        if output_html and output_html != path:
            try:
                shutil.copy2(path, output_html)
                return output_html
            except Exception:
                pass
        return path

    def generate_html_graph(self) -> str:
        """Builds graph_view.html with physics speed slider (1x-5x), 3D WebGL spatial Z-axis engine, strict Level 4 register staging for Ethernet & RCC, and zero-overlap views."""
        node_list, edge_list, parse_elapsed = self.build_graph_data()
        html_path = os.path.join(self.output_root, "graph_view.html")

        # Copy local vendor scripts for 100% offline 3D WebGL support
        vendor_src = os.path.join(os.path.dirname(__file__), "vendor")
        vendor_dst = os.path.join(self.output_root, "vendor")
        if os.path.exists(vendor_src):
            os.makedirs(vendor_dst, exist_ok=True)
            for vf in os.listdir(vendor_src):
                vs = os.path.join(vendor_src, vf)
                vd = os.path.join(vendor_dst, vf)
                if os.path.isfile(vs) and not os.path.exists(vd):
                    try:
                        shutil.copy2(vs, vd)
                    except Exception:
                        pass

        mcu_info = detect_mcu_metadata(wiki_root=self.output_root)
        graph_title = mcu_info.get("graph_title", "Knowledge Graph")
        mcu_family = mcu_info.get("mcu_family", "STM32")

        # Load dynamic DNA metadata if available
        dna_path = os.path.join(self.output_root, "mcu_dna.json")
        core_layer_label = f"{mcu_family} Processor Core"
        has_security = False
        if os.path.exists(dna_path):
            try:
                with open(dna_path, "r", encoding="utf-8") as df:
                    dna_data = json.load(df)
                    core_layer_label = dna_data.get("core_layer_label", core_layer_label)
                    has_security = dna_data.get("has_security", False)
            except Exception:
                pass

        sec_option_html = "<option value=\"Security\">🔴 Security Architecture</option>" if has_security else ""
        sec_legend_html = "<div class=\"legend-item\" id=\"leg-Security\" onclick=\"highlightTopologyLayer('Security')\"><div class=\"legend-color\" style=\"background:#ef4444;\"></div> 🔴 Security Architecture</div>" if has_security else ""

        nodes_json = json.dumps(node_list, indent=2)
        edges_json = json.dumps(edge_list, indent=2)

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{graph_title}</title>
    <!-- Offline first local vendor scripts with CDN fallback -->
    <script src="vendor/three.min.js"></script>
    <script src="vendor/3d-force-graph.min.js"></script>
    <script>
        if (typeof THREE === 'undefined') {{
            document.write('<script src="https://unpkg.com/three"><\\/script>');
        }}
        if (typeof ForceGraph3D === 'undefined') {{
            document.write('<script src="https://unpkg.com/3d-force-graph"><\\/script>');
        }}
    </script>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            user-select: none;
        }}
        body {{
            background-color: #0b0f19;
            color: #f8fafc;
            overflow: hidden;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        header {{
            background: #1e293b;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #334155;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
            z-index: 10;
        }}
        .title-group {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .title-group h1 {{
            font-size: 1.1rem;
            font-weight: 700;
            color: #38bdf8;
        }}
        .badge {{
            background: #0284c7;
            color: white;
            font-size: 0.72rem;
            font-weight: 600;
            padding: 2px 8px;
            border-radius: 10px;
        }}
        .telemetry-tag {{
            background: #0f172a;
            border: 1px solid #334155;
            color: #00e5ff;
            font-size: 0.78rem;
            font-family: monospace;
            padding: 3px 8px;
            border-radius: 6px;
        }}
        .gpu-badge {{
            background: #059669;
            color: #ffffff;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 6px;
            border: 1px solid #34d399;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        .controls {{
            display: flex;
            gap: 8px;
            align-items: center;
        }}
        .view-mode-group {{
            display: flex;
            gap: 4px;
            background: #0f172a;
            padding: 3px;
            border-radius: 8px;
            border: 1px solid #334155;
        }}
        .view-btn {{
            background: transparent;
            color: #94a3b8;
            border: 1px solid transparent;
            padding: 4px 10px;
            border-radius: 5px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 4px;
        }}
        .view-btn:hover {{
            color: #38bdf8;
            background: rgba(30, 41, 59, 0.6);
        }}
        .view-btn.active {{
            background: #0284c7;
            color: #ffffff;
            border-color: #38bdf8;
            box-shadow: 0 2px 8px rgba(2, 132, 199, 0.4);
        }}
        .view-btn:active, .nav-btn:active:not(:disabled), button:active {{
            transform: translateY(2px) scale(0.96);
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.5) !important;
        }}
        .speed-control-group {{
            display: flex;
            align-items: center;
            gap: 6px;
            background: #0f172a;
            padding: 4px 10px;
            border-radius: 8px;
            border: 1px solid #334155;
        }}
        .nav-history-group {{
            display: flex;
            gap: 4px;
            background: #0f172a;
            padding: 2px;
            border-radius: 6px;
            border: 1px solid #334155;
        }}
        .nav-btn {{
            background: #1e293b;
            color: #38bdf8;
            border: 1px solid #475569;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .nav-btn:hover:not(:disabled) {{
            background: #38bdf8;
            color: #0f172a;
            border-color: #38bdf8;
        }}
        .nav-btn:disabled {{
            opacity: 0.35;
            cursor: not-allowed;
            color: #64748b;
        }}
        select {{
            background: #0f172a;
            border: 1px solid #475569;
            color: #38bdf8;
            font-weight: 600;
            padding: 5px 10px;
            border-radius: 6px;
            font-size: 0.82rem;
            outline: none;
            cursor: pointer;
        }}
        select:focus {{
            border-color: #38bdf8;
        }}
        input[type="text"] {{
            background: #0f172a;
            border: 1px solid #475569;
            color: #f8fafc;
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 0.82rem;
            width: 170px;
            outline: none;
        }}
        input[type="text"]:focus {{
            border-color: #38bdf8;
        }}
        button {{
            background: #3b82f6;
            color: white;
            border: none;
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }}
        button:hover {{
            background: #2563eb;
        }}
        #canvasContainer {{
            flex: 1;
            width: 100%;
            height: calc(100vh - 55px);
            position: relative;
            background: #090d16;
        }}
        canvas {{
            width: 100%;
            height: 100%;
            display: block;
        }}
        #graph3dContainer {{
            display: none;
            width: 100%;
            height: 100%;
            position: absolute;
            top: 0;
            left: 0;
            z-index: 2;
        }}
        .legend {{
            position: absolute;
            bottom: 20px;
            left: 20px;
            background: rgba(30, 41, 59, 0.88);
            backdrop-filter: blur(8px);
            padding: 12px 16px;
            border-radius: 10px;
            border: 1px solid #334155;
            z-index: 5;
            font-size: 0.78rem;
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        }}
        .legend-title {{
            font-weight: 700;
            margin-bottom: 8px;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 5px;
            padding: 4px 8px;
            border-radius: 6px;
            cursor: pointer;
            border: 1px solid transparent;
            transition: all 0.2s ease;
        }}
        .legend-item:hover {{
            background: rgba(51, 65, 85, 0.6);
            border-color: #475569;
        }}
        .legend-item.active {{
            background: #0f172a;
            border-color: #38bdf8;
            font-weight: 700;
        }}
        .legend-color {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }}
        .sidebar {{
            position: absolute;
            top: 20px;
            right: 20px;
            width: 380px;
            max-height: calc(100vh - 95px);
            overflow-y: auto;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(12px);
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #334155;
            display: none;
            z-index: 5;
            box-shadow: 0 12px 36px rgba(0, 0, 0, 0.6);
        }}
        .sidebar-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 10px;
            border-bottom: 1px solid #334155;
            padding-bottom: 10px;
        }}
        .sidebar h3 {{
            color: #38bdf8;
            font-size: 1.15rem;
            font-weight: 700;
        }}
        .close-btn {{
            background: transparent;
            color: #94a3b8;
            font-size: 1.2rem;
            cursor: pointer;
            padding: 0 4px;
        }}
        .close-btn:hover {{
            color: #ffffff;
        }}
        .breadcrumb-trail {{
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 4px;
            background: #0f172a;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #1e293b;
            margin-bottom: 10px;
            font-size: 0.74rem;
        }}
        .breadcrumb-item {{
            color: #00e5ff;
            cursor: pointer;
            font-weight: 600;
        }}
        .breadcrumb-item:hover {{
            text-decoration: underline;
            color: #ffffff;
        }}
        .breadcrumb-separator {{
            color: #64748b;
        }}
        .node-detail-card h4 {{
            color: #f1f5f9;
            font-size: 0.92rem;
            margin-bottom: 4px;
        }}
        .node-detail-card p {{
            font-size: 0.82rem;
            color: #cbd5e1;
            line-height: 1.4;
            margin-bottom: 6px;
        }}
        .node-detail-card code {{
            background: #0f172a;
            color: #00e5ff;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
        }}
        .bitfield-list {{
            list-style: none;
            padding: 0;
            margin-top: 6px;
        }}
        .bitfield-list li {{
            font-size: 0.78rem;
            color: #94a3b8;
            background: #1e293b;
            padding: 4px 8px;
            border-radius: 4px;
            margin-bottom: 4px;
            border: 1px solid #334155;
        }}
        .bitfield-list strong {{
            color: #34d399;
        }}
        .chip-group {{
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
            margin-top: 6px;
        }}
        .chip {{
            background: #1e293b;
            color: #38bdf8;
            border: 1px solid #334155;
            font-size: 0.72rem;
            padding: 2px 8px;
            border-radius: 10px;
        }}
        .neighbor-group {{
            margin-top: 12px;
            padding-top: 10px;
            border-top: 1px solid #334155;
        }}
        .neighbor-group h5 {{
            color: #94a3b8;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 8px;
        }}
        .neighbor-badge {{
            display: inline-block;
            background: #1e293b;
            color: #00e5ff;
            border: 1px solid #00e5ff;
            font-size: 0.75rem;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 12px;
            margin: 0 4px 6px 0;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 2px 8px rgba(0, 229, 255, 0.2);
        }}
        .neighbor-badge:hover {{
            background: #00e5ff;
            color: #0f172a;
            transform: scale(1.06);
            box-shadow: 0 4px 12px rgba(0, 229, 255, 0.5);
        }}
    </style>
</head>
<body>
    <header>
        <div class="title-group">
            <h1>🕸 {graph_title}</h1>
            <span class="gpu-badge" id="hardwareBadge">⚡ GPU Acceleration</span>
            <span class="telemetry-tag" id="telemetryBadge">Parsed in {parse_elapsed:.3f}s | {len(node_list)} Nodes | {len(edge_list)} Links</span>
        </div>

        <div class="controls">
            <!-- Modular Multi-View Selector Buttons (2D Canvas + 3D WebGL Space) -->
            <div class="view-mode-group">
                <button class="view-btn active" id="btn-view-mesh" onclick="switchViewMode('mesh')">🌐 Force Mesh</button>
                <button class="view-btn" id="btn-view-dag" onclick="switchViewMode('dag')">📐 Hierarchical DAG</button>
                <button class="view-btn" id="btn-view-tree" onclick="switchViewMode('tree')">🌳 Collapsible Tree</button>
                <button class="view-btn" id="btn-view-ring" onclick="switchViewMode('ring')">⭕ Interconnect Ring</button>
                <button class="view-btn" id="btn-view-3d" onclick="switchViewMode('3d')">🔮 3D WebGL Space</button>
            </div>

            <!-- Physics Speed Control Slider (1x to 5x) -->
            <div class="speed-control-group">
                <label style="font-size:0.75rem;font-weight:700;color:#38bdf8;display:flex;align-items:center;gap:3px;">
                    ⚡ Speed: <span id="speedValueLabel" style="color:#ffffff;width:20px;">1x</span>
                </label>
                <input type="range" id="physicsSpeedSlider" min="1" max="5" step="1" value="1" oninput="updatePhysicsSpeed(this.value)" style="width:70px;cursor:pointer;accent-color:#00e5ff;">
            </div>

            <!-- Back / Forward Navigation History Controls -->
            <div class="nav-history-group">
                <button class="nav-btn" id="navBackBtn" onclick="goBackHistory()" disabled title="Go Back">◀ Back</button>
                <button class="nav-btn" id="navForwardBtn" onclick="goForwardHistory()" disabled title="Go Forward">Forward ▶</button>
            </div>

            <select id="layerSelect" onchange="highlightTopologyLayer(this.value)">
                <option value="All">🌐 All Topology Layers</option>
                <option value="Master Index">💖 MOC Entry (index.md)</option>
                <option value="Memory">🔷 Memory Layer</option>
                <option value="System">🟧 System Infrastructure</option>
                <option value="Core">🟣 {core_layer_label}</option>
                <option value="Peripherals">🟩 Peripherals Layer</option>
                {sec_option_html}
                <option value="Registers">🩵 Hardware Registers (JSON)</option>
            </select>

            <input type="text" id="searchInput" placeholder="Search IP / Register..." oninput="debounceSearchNode()">
            <button onclick="resetZoom()">Reset View</button>
            <button onclick="togglePhysics()" id="physicsBtn">Pause Physics</button>
        </div>
    </header>

    <div id="canvasContainer">
        <!-- 2D Canvas Container -->
        <canvas id="graphCanvas"></canvas>

        <!-- 3D WebGL Space Container -->
        <div id="graph3dContainer"></div>

        <div class="legend">
            <div class="legend-title">
                <span>TOPOLOGY LAYERS</span>
                <span style="font-size:0.68rem;color:#00e5ff;cursor:pointer;" onclick="highlightTopologyLayer('All')">[Reset Filter]</span>
            </div>
            <div class="legend-item active" id="leg-All" onclick="highlightTopologyLayer('All')">
                <div class="legend-color" style="background:#f8fafc;"></div> 🌐 All Layers ({len(node_list)})
            </div>
            <div class="legend-item" id="leg-Master Index" onclick="highlightTopologyLayer('Master Index')">
                <div class="legend-color" style="background:#ec4899;"></div> 💖 MOC Entry (index.md)
            </div>
            <div class="legend-item" id="leg-Memory" onclick="highlightTopologyLayer('Memory')">
                <div class="legend-color" style="background:#3b82f6;"></div> 🔷 Memory Layer
            </div>
            <div class="legend-item" id="leg-System" onclick="highlightTopologyLayer('System')">
                <div class="legend-color" style="background:#f59e0b;"></div> 🟧 System Infrastructure
            </div>
            <div class="legend-item" id="leg-Core" onclick="highlightTopologyLayer('Core')">
                <div class="legend-color" style="background:#a855f7;"></div> 🟣 {core_layer_label}
            </div>
            <div class="legend-item" id="leg-Peripherals" onclick="highlightTopologyLayer('Peripherals')">
                <div class="legend-color" style="background:#10b981;"></div> 🟩 Peripherals
            </div>
            {sec_legend_html}
            <div class="legend-item" id="leg-Registers" onclick="highlightTopologyLayer('Registers')">
                <div class="legend-color" style="background:#06b6d4;"></div> 🩵 Hardware Registers
            </div>
        </div>

        <div class="sidebar" id="nodeSidebar">
            <div class="sidebar-header">
                <div>
                    <h3 id="sideNodeLabel">Node Title</h3>
                    <span id="sideNodeGroupBadge" class="badge" style="margin-top:4px;">Layer</span>
                </div>
                <button class="close-btn" onclick="closeSidebar()">✕</button>
            </div>

            <!-- Interactive Breadcrumb Trail -->
            <div class="breadcrumb-trail" id="breadcrumbTrail">
                <span class="breadcrumb-item" onclick="resetZoom()">Home</span>
            </div>

            <p style="font-size:0.78rem;color:#94a3b8;margin-bottom:10px;"><strong>Path:</strong> <code id="sideNodePath"></code></p>
            
            <div id="sideNodeDetailsContainer"></div>

            <div class="neighbor-group">
                <h5 id="neighborHeader">Connected Sub-Nodes & Links</h5>
                <div id="neighborBadgesContainer"></div>
            </div>
        </div>
    </div>

    <script>
        // 0. Automatic Hardware Graphics Acceleration Detection (NVIDIA Priority > Intel Iris > CPU Fallback)
        function detectHardwareAcceleration() {{
            try {{
                const testCanvas = document.createElement('canvas');
                const glOpts = {{ powerPreference: "high-performance", failIfMajorPerformanceCaveat: false }};
                const gl = testCanvas.getContext('webgl2', glOpts) || testCanvas.getContext('webgl', glOpts) || testCanvas.getContext('experimental-webgl', glOpts);
                if (gl) {{
                    const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
                    let rendererName = "GPU Hardware";
                    if (debugInfo) {{
                        rendererName = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL) || gl.getParameter(gl.RENDERER) || "GPU";
                    }} else {{
                        rendererName = gl.getParameter(gl.RENDERER) || "GPU";
                    }}

                    const rendererUpper = rendererName.toUpperCase();
                    if (rendererUpper.includes("NVIDIA") || rendererUpper.includes("GEFORCE") || rendererUpper.includes("QUADRO")) {{
                        return {{ isGPU: true, tier: "NVIDIA", label: `⚡ NVIDIA Discrete GPU (${{rendererName}})` }};
                    }} else if (rendererUpper.includes("INTEL") || rendererUpper.includes("IRIS") || rendererUpper.includes("UHD") || rendererUpper.includes("MESA")) {{
                        return {{ isGPU: true, tier: "Intel", label: `⚡ Intel Iris/UHD Graphics (${{rendererName.split('/')[0].trim()}})` }};
                    }} else if (rendererUpper.includes("LLVMPIPE") || rendererUpper.includes("SOFTWARE") || rendererUpper.includes("SWRAST")) {{
                        return {{ isGPU: false, tier: "CPU", label: `💻 CPU Software Engine (${{rendererName}})` }};
                    }} else {{
                        return {{ isGPU: true, tier: "GPU", label: `⚡ GPU Acceleration (${{rendererName}})` }};
                    }}
                }}
            }} catch(e) {{}}
            return {{ isGPU: false, tier: "CPU", label: "💻 CPU Multi-Core Engine" }};
        }}

        const hwInfo = detectHardwareAcceleration();
        const hwBadge = document.getElementById('hardwareBadge');
        hwBadge.innerText = hwInfo.label;

        const rawNodes = {nodes_json};
        const rawEdges = {edges_json};

        const canvas = document.getElementById('graphCanvas');
        const ctx = canvas.getContext('2d', {{
            alpha: false,
            desynchronized: true,
            willReadFrequently: false
        }});
        const container = document.getElementById('canvasContainer');

        let width = container.clientWidth;
        let height = container.clientHeight;

        function resizeCanvas() {{
            width = container.clientWidth;
            height = container.clientHeight;
            canvas.width = width * window.devicePixelRatio;
            canvas.height = height * window.devicePixelRatio;
            ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
        }}
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // Multi-line word wrapper function for node labels
        function wrapTextLines(label) {{
            if (!label) return [""];
            if (label.includes('_')) return label.split('_');
            if (label.includes(' ')) return label.split(' ');
            if (label.length > 7) {{
                const chunks = [];
                for (let i = 0; i < label.length; i += 6) {{
                    chunks.push(label.substring(i, i + 6));
                }}
                return chunks;
            }}
            return [label];
        }}

        // Dynamic Balloon Circle Radius Auto-Sizing Engine based on Label text length!
        function computeDynamicRadius(label, group) {{
            const lines = wrapTextLines(label);
            const maxLineLen = Math.max(...lines.map(l => l.length));
            
            let baseRadius = (group === "Master Index") ? 32 : (group === "Registers" ? 22 : 28);
            
            // Calculate minimum required radius so text fits comfortably INSIDE the balloon!
            let reqRadius = Math.max(baseRadius, Math.ceil(maxLineLen * 4.6 + lines.length * 5 + 4));
            return reqRadius;
        }}

        // View Mode State: 'mesh' | 'dag' | 'tree' | 'ring' | '3d'
        let viewMode = 'mesh';

        // Physics Speed Multiplier Control
        let physicsSpeedMultiplier = 1;
        function updatePhysicsSpeed(val) {{
            physicsSpeedMultiplier = parseInt(val, 10);
            document.getElementById('speedValueLabel').innerText = `${{val}}x`;
        }}

        // Fast Search Indexing Engine
        function buildFastSearchIndex() {{
            // Fast lookup index initialized
        }}

        // Build Map of Peripheral Nodes to Satellite Registers for Orbital Clustering
        const rawEdgeMap = new Map();
        rawEdges.forEach(e => {{
            if (!rawEdgeMap.has(e.source)) rawEdgeMap.set(e.source, []);
            rawEdgeMap.get(e.source).push(e.target);
            if (!rawEdgeMap.has(e.target)) rawEdgeMap.set(e.target, []);
            rawEdgeMap.get(e.target).push(e.source);
        }});

        // Categorize Peripherals into Ring Angles
        const peripheralNodes = rawNodes.filter(n => n.group === "Peripherals");
        const periphAngleMap = new Map();
        peripheralNodes.forEach((p, idx) => {{
            const angle = (idx / peripheralNodes.length) * Math.PI * 2;
            periphAngleMap.set(p.id, angle);
        }});

        // 1. Initialize Nodes in Wide Concentric Orbital Rings with Dynamic Circle Radii
        const nodes = rawNodes.map((n, i) => {{
            let angle = Math.random() * Math.PI * 2;
            let radius = 200;

            const dynamicSize = computeDynamicRadius(n.label, n.group);

            if (n.group === "Master Index") {{
                radius = 10;
            }} else if (n.group === "Core" || n.group === "Memory") {{
                angle = Math.random() * Math.PI * 2;
                radius = 240 + Math.random() * 80;
            }} else if (n.group === "System" || n.group === "Security") {{
                angle = Math.random() * Math.PI * 2;
                radius = 480 + Math.random() * 120;
            }} else if (n.group === "Peripherals") {{
                angle = periphAngleMap.get(n.id) || (Math.random() * Math.PI * 2);
                radius = 840 + (i % 2) * 90;
            }} else if (n.group === "Registers") {{
                const connectedIPs = rawEdgeMap.get(n.id) || [];
                const parentIP = connectedIPs[0];
                const baseAngle = periphAngleMap.get(parentIP) || (Math.random() * Math.PI * 2);
                
                const subOffset = (Math.random() - 0.5) * 0.45;
                angle = baseAngle + subOffset;
                radius = 1080 + Math.random() * 180;
            }}

            const startX = width / 2 + Math.cos(angle) * radius;
            const startY = height / 2 + Math.sin(angle) * radius;

            return {{
                ...n,
                size: dynamicSize,
                x: startX,
                y: startY,
                targetX: startX,
                targetY: startY,
                vx: 0,
                vy: 0,
                expanded: true
            }};
        }});

        const nodeMap = new Map(nodes.map(n => [n.id, n]));

        // 2. Build Edges
        const edges = rawEdges.map(e => ({{
            source: nodeMap.get(e.source),
            target: nodeMap.get(e.target),
            label: e.label
        }})).filter(e => e.source && e.target);

        // State
        let transform = {{ x: width * 0.12, y: height * 0.12, k: 0.70 }};
        let isDragging = false;
        let dragNode = null;
        let startX = 0, startY = 0;
        let hoverNode = null;
        let selectedNode = null;
        let physicsRunning = true;
        let activeLayerFilter = "All";
        let ringPetalClusters = [];

        // Navigation History Stack
        let navHistory = [];
        let navHistoryIndex = -1;

        // 3D WebGL Graph Engine State
        let graph3dInstance = null;

        function create3DNodeObject(node) {{
            const ThreeObj = window.THREE;
            if (!ThreeObj) return null;

            // Zero-Allocation Cache: Return existing group if already constructed
            if (node.__threeGroup) return node.__threeGroup;

            const group = new ThreeObj.Group();

            const radius = (node.group === "Master Index" ? 14 : (node.group === "Registers" ? 6 : 9));

            // Determine initial category base color
            let sphereColor = node.color;
            if (node.group === "Registers") {{
                if (node.regCategory === "Config") sphereColor = "#00e5ff";      // Cyan Orbit 1
                else if (node.regCategory === "Status") sphereColor = "#fbbf24";  // Amber Orbit 2
                else if (node.regCategory === "Data") sphereColor = "#34d399";    // Emerald Orbit 3
            }}

            node.__baseColor = sphereColor;
            node.__baseRadius = radius;

            // 1. Core Sphere Mesh (Instantiated ONCE)
            const sphereGeo = new ThreeObj.SphereGeometry(radius, 16, 16);
            const sphereMat = new ThreeObj.MeshLambertMaterial({{
                color: sphereColor,
                transparent: true,
                opacity: 0.94
            }});
            const sphere = new ThreeObj.Mesh(sphereGeo, sphereMat);
            group.add(sphere);
            node.__sphereMesh = sphere;

            // 2. Selection Neon Halo Ring (Instantiated ONCE, toggled in-place)
            const ringGeo = new ThreeObj.RingGeometry(radius + 2, radius + 5, 32);
            const ringMat = new ThreeObj.MeshBasicMaterial({{
                color: 0x00e5ff,
                side: ThreeObj.DoubleSide,
                transparent: true,
                opacity: 0.9
            }});
            const ring = new ThreeObj.Mesh(ringGeo, ringMat);
            ring.visible = false;
            group.add(ring);
            node.__haloRing = ring;

            // 3. Crisp 2D Canvas Sprite Label (Pre-baked ONCE at startup, cached forever)
            const canvas = document.createElement('canvas');
            canvas.width = 256;
            canvas.height = 64;
            const ctx = canvas.getContext('2d');

            const labelText = node.label;
            ctx.font = "Bold 22px system-ui, -apple-system, sans-serif";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";

            const textMetrics = ctx.measureText(labelText);
            const textWidth = textMetrics.width;
            const padX = 12, padY = 6;
            const boxW = Math.min(240, textWidth + padX * 2);
            const boxH = 32;
            const boxX = (256 - boxW) / 2;
            const boxY = (64 - boxH) / 2;

            ctx.fillStyle = "rgba(15, 23, 42, 0.92)";
            if (ctx.roundRect) {{
                ctx.beginPath();
                ctx.roundRect(boxX, boxY, boxW, boxH, 6);
                ctx.fill();
                ctx.strokeStyle = sphereColor;
                ctx.lineWidth = 2;
                ctx.stroke();
            }} else {{
                ctx.fillRect(boxX, boxY, boxW, boxH);
            }}

            ctx.fillStyle = "#ffffff";
            ctx.fillText(labelText, 128, 32);

            const texture = new ThreeObj.CanvasTexture(canvas);
            texture.generateMipmaps = false;
            texture.minFilter = ThreeObj.LinearFilter;

            const spriteMat = new ThreeObj.SpriteMaterial({{
                map: texture,
                transparent: true,
                opacity: 0.94,
                depthWrite: false
            }});
            const sprite = new ThreeObj.Sprite(spriteMat);

            const spriteScaleX = radius * 4 + 14;
            const spriteScaleY = (radius * 4 + 14) / 4;
            sprite.scale.set(spriteScaleX, spriteScaleY, 1);
            sprite.position.set(0, radius + spriteScaleY / 2 + 2, 0);
            group.add(sprite);
            node.__labelSprite = sprite;

            node.__threeGroup = group;
            return group;
        }}

        function update3DGraphStyles() {{
            if (!graph3dInstance) return;

            const activeNode = selectedNode || hoverNode;
            const connectedSet = new Set();
            if (activeNode) {{
                connectedSet.add(activeNode.id);
                for (let e of edges) {{
                    if (e.source.id === activeNode.id) connectedSet.add(e.target.id);
                    if (e.target.id === activeNode.id) connectedSet.add(e.source.id);
                }}
            }}

            // High-Performance In-Place VRAM Mutation (0 Allocations, 0 GC Spikes)
            const gNodes = (graph3dInstance.graphData() || {{}}).nodes || [];
            for (let i = 0; i < gNodes.length; i++) {{
                const node = gNodes[i];
                if (!node.__threeGroup) continue;

                const nodeId = node.id;
                const isSelected = selectedNode && (nodeId === selectedNode.id);
                const isSubNode = activeNode && (nodeId !== activeNode.id) && connectedSet.has(nodeId);
                const isLayerMatch = (activeLayerFilter === "All") || (node.group === activeLayerFilter);

                let opacity = 0.94;
                if (isSelected) opacity = 1.0;
                else if (isSubNode) opacity = 0.96;
                else if (activeNode) opacity = 0.05; // Ghost out
                else if (!isLayerMatch) opacity = 0.12;

                // Mutate sphere mesh material in-place
                if (node.__sphereMesh) {{
                    const mat = node.__sphereMesh.material;
                    mat.opacity = opacity;
                    mat.transparent = opacity < 1.0;
                    if (isSelected) {{
                        mat.color.setHex(0xffffff);
                    }} else if (isSubNode) {{
                        mat.color.setHex(0x00e5ff);
                    }} else {{
                        mat.color.setStyle(node.__baseColor || node.color);
                    }}

                    const scaleFactor = isSelected ? 1.4 : (isSubNode ? 1.15 : 1.0);
                    node.__sphereMesh.scale.set(scaleFactor, scaleFactor, scaleFactor);
                }}

                // Mutate halo ring in-place
                if (node.__haloRing) {{
                    node.__haloRing.visible = (isSelected || isSubNode);
                    if (node.__haloRing.visible) {{
                        node.__haloRing.material.color.setHex(isSelected ? 0x00e5ff : 0x34d399);
                        node.__haloRing.material.opacity = isSelected ? 1.0 : 0.85;
                    }}
                }}

                // Mutate label sprite in-place
                if (node.__labelSprite) {{
                    node.__labelSprite.material.opacity = Math.max(0.12, opacity);
                    node.__labelSprite.material.transparent = opacity < 1.0;
                }}
            }}

            // Color-Coded 3D Dependency Pillars (RCC, PWR, GPIO, DMA, NVIC)
            graph3dInstance.linkColor(link => {{
                const srcId = typeof link.source === 'object' ? link.source.id : link.source;
                const tgtId = typeof link.target === 'object' ? link.target.id : link.target;

                const srcNode = nodeMap.get(srcId);
                const tgtNode = nodeMap.get(tgtId);

                const isDirect = activeNode && (srcId === activeNode.id || tgtId === activeNode.id);
                const isConnected = activeNode && (connectedSet.has(srcId) && connectedSet.has(tgtId));

                if (isDirect) {{
                    if (srcNode && srcNode.label.includes("RCC")) return "#00e5ff";       // Clocking Pillar
                    if (srcNode && srcNode.label.includes("PWR")) return "#f59e0b";       // Power Pillar
                    if (srcNode && srcNode.label.includes("GPIO")) return "#10b981";      // Pin Muxing Pillar
                    if (srcNode && srcNode.label.includes("DMA")) return "#c084fc";       // Data Transport Pillar
                    if (srcNode && srcNode.label.includes("NVIC")) return "#ec4899";      // Interrupt Pillar
                    return "#00e5ff";
                }}
                if (isConnected) return "rgba(52, 211, 153, 0.85)";
                if (activeNode) return "rgba(30, 41, 59, 0.05)";
                return "rgba(56, 189, 248, 0.45)";
            }});

            graph3dInstance.linkWidth(link => {{
                const srcId = typeof link.source === 'object' ? link.source.id : link.source;
                const tgtId = typeof link.target === 'object' ? link.target.id : link.target;
                const isDirect = activeNode && (srcId === activeNode.id || tgtId === activeNode.id);
                if (isDirect) return 3.8;
                if (activeNode && connectedSet.has(srcId) && connectedSet.has(tgtId)) return 2.2;
                return 1.2;
            }});

            // Directional Particle Flow Vectors
            graph3dInstance
                .linkDirectionalParticles(link => {{
                    const srcId = typeof link.source === 'object' ? link.source.id : link.source;
                    const tgtId = typeof link.target === 'object' ? link.target.id : link.target;
                    if (!activeNode) return 0;
                    const isDirect = (srcId === activeNode.id || tgtId === activeNode.id);
                    const isConnected = (connectedSet.has(srcId) && connectedSet.has(tgtId));
                    return isDirect ? 5 : (isConnected ? 2 : 0);
                }})
                .linkDirectionalParticleSpeed(0.015)
                .linkDirectionalParticleWidth(3.5)
                .linkDirectionalParticleColor(() => "#00e5ff");
        }}

        function init3DGraph() {{
            const container3d = document.getElementById('graph3dContainer');
            if (graph3dInstance) return;

            // 3D Bus Domain Spatial Clustering (AHB Inner Sphere vs APB Outer Orbit)
            const ahbKeywords = ["ETH", "USB", "MDMA", "DMA", "FMC", "SDMMC", "FLASH", "RAM", "AXI"];
            
            let ahbIndex = 0;
            let apbIndex = 0;

            const nodes3d = nodes.map(n => {{
                let xPos = (Math.random() - 0.5) * 200;
                let yPos = (Math.random() - 0.5) * 200;
                let zPos = 0;

                const isAHB = ahbKeywords.some(kw => n.label.includes(kw));

                if (n.group === "Master Index") {{
                    xPos = 0; yPos = 0; zPos = 240;
                }} else if (n.group === "Core" || n.group === "Memory") {{
                    const angle = (ahbIndex++ * 0.4);
                    xPos = Math.cos(angle) * 140;
                    yPos = Math.sin(angle) * 140;
                    zPos = 120;
                }} else if (isAHB && n.group !== "Registers") {{
                    // AHB High-Speed Inner 3D Sphere
                    const angle = (ahbIndex++ * 0.45);
                    xPos = Math.cos(angle) * 210;
                    yPos = Math.sin(angle) * 210;
                    zPos = (ahbIndex % 2 === 0 ? 60 : -60);
                }} else if (n.group !== "Registers") {{
                    // APB Low-Speed Outer Concentric Orbital Shell
                    const angle = (apbIndex++ * 0.35);
                    xPos = Math.cos(angle) * 420;
                    yPos = Math.sin(angle) * 420;
                    zPos = (apbIndex % 2 === 0 ? -120 : 120);
                }} else {{
                    // Register 3D Sub-Orbits
                    xPos = (Math.random() - 0.5) * 600;
                    yPos = (Math.random() - 0.5) * 600;
                    zPos = -220;
                }}

                return {{
                    id: n.id,
                    label: n.label,
                    group: n.group,
                    regCategory: n.regCategory || "General",
                    color: n.color,
                    size: n.size,
                    x: xPos,
                    y: yPos,
                    z: zPos,
                    rawNode: n
                }};
            }});

            const links3d = edges.map(e => ({{
                source: e.source.id,
                target: e.target.id,
                label: e.label
            }}));

            if (typeof ForceGraph3D !== 'undefined') {{
                const rendererOpts = {{
                    antialias: true,
                    alpha: false,
                    powerPreference: "high-performance",
                    precision: "highp"
                }};

                graph3dInstance = ForceGraph3D({{ controlType: 'orbit', rendererConfig: rendererOpts }})(container3d)
                    .graphData({{ nodes: nodes3d, links: links3d }})
                    .nodeLabel(node => `<div style="background:#0f172a;color:#00e5ff;padding:4px 8px;border-radius:4px;border:1px solid #38bdf8;font-weight:700;">${{node.label}} (${{node.group}})</div>`)
                    .nodeThreeObject(node => create3DNodeObject(node))
                    .nodeThreeObjectExtend(false)
                    .onNodeClick(node => {{
                        const raw = node.rawNode || nodeMap.get(node.id) || node;
                        selectNode(raw, false, true);
                    }})
                    .warmupTicks(60)
                    .cooldownTicks(50)
                    .cooldownTime(1800)
                    .d3VelocityDecay(0.35);

                graph3dInstance.d3Force('charge').strength(-120);

                if (typeof graph3dInstance.onEngineStop === 'function') {{
                    graph3dInstance.onEngineStop(() => {{
                        if (graph3dInstance && typeof graph3dInstance.pauseAnimation === 'function') {{
                            graph3dInstance.pauseAnimation();
                        }}
                    }});
                }}

                update3DGraphStyles();
            }} else {{
                container3d.innerHTML = `<div style="color:#ef4444;padding:40px;text-align:center;font-weight:700;">WebGL 3D Library could not be loaded via CDN. Falling back to 2D Canvas views.</div>`;
            }}
        }}

        function computeLayoutTargets() {{
            ringPetalClusters = [];

            if (viewMode === 'dag') {{
                const assignedRegs = new Set();

                const level1 = nodes.filter(n => n.group === "Core" || n.group === "Memory");
                const level2 = nodes.filter(n => n.group === "System" || n.group === "Security");
                const level3 = nodes.filter(n => n.group === "Peripherals");

                const allParents = [...level1, ...level2, ...level3];

                const ipChildRegsMap = new Map();
                allParents.forEach(ip => {{
                    const childRegs = [];
                    for (let e of edges) {{
                        let candidate = null;
                        if (e.source.id === ip.id && e.target.group === "Registers") candidate = e.target;
                        else if (e.target.id === ip.id && e.source.group === "Registers") candidate = e.source;

                        if (candidate && !assignedRegs.has(candidate.id)) {{
                            assignedRegs.add(candidate.id);
                            childRegs.push(candidate);
                        }}
                    }}
                    ipChildRegsMap.set(ip.id, childRegs);
                }});

                const colSpacing = 72;
                const rowSpacing = 54;
                const gapBetweenSlots = 90;

                const clusterWidthMap = new Map();
                const ipMaxColsMap = new Map();

                allParents.forEach(ip => {{
                    const regCount = (ipChildRegsMap.get(ip.id) || []).length;
                    const maxColumns = regCount > 30 ? 4 : 3;
                    ipMaxColsMap.set(ip.id, maxColumns);

                    const cols = Math.max(1, Math.min(maxColumns, regCount));
                    const gridW = (cols - 1) * colSpacing;
                    const clusterW = Math.max(210, gridW + 90);
                    clusterWidthMap.set(ip.id, clusterW);
                }});

                let totalCanvasW = 0;
                allParents.forEach((ip, idx) => {{
                    totalCanvasW += clusterWidthMap.get(ip.id);
                    if (idx < allParents.length - 1) totalCanvasW += gapBetweenSlots;
                }});

                let currentX = width / 2 - totalCanvasW / 2;

                level1.forEach(ip => {{
                    const w = clusterWidthMap.get(ip.id);
                    ip.targetX = currentX + w / 2;
                    ip.targetY = 240;
                    currentX += w + gapBetweenSlots;
                }});

                level2.forEach(ip => {{
                    const w = clusterWidthMap.get(ip.id);
                    ip.targetX = currentX + w / 2;
                    ip.targetY = 380;
                    currentX += w + gapBetweenSlots;
                }});

                level3.forEach(ip => {{
                    const w = clusterWidthMap.get(ip.id);
                    ip.targetX = currentX + w / 2;
                    ip.targetY = 560;
                    currentX += w + gapBetweenSlots;
                }});

                allParents.forEach(ipNode => {{
                    const childRegs = ipChildRegsMap.get(ipNode.id) || [];
                    if (childRegs.length > 0) {{
                        const startY = 730;
                        const maxColumns = ipMaxColsMap.get(ipNode.id) || 3;

                        childRegs.forEach((reg, rIdx) => {{
                            const rowIndex = Math.floor(rIdx / maxColumns);
                            const colIndex = rIdx % maxColumns;

                            const itemsInThisRow = Math.min(maxColumns, childRegs.length - rowIndex * maxColumns);
                            const rowStartX = ipNode.targetX - ((itemsInThisRow - 1) * colSpacing) / 2;

                            reg.targetX = rowStartX + colIndex * colSpacing;
                            reg.targetY = startY + rowIndex * rowSpacing;
                        }});
                    }}
                }});

                const remainingRegs = nodes.filter(n => n.group === "Registers" && !assignedRegs.has(n.id));
                remainingRegs.forEach((reg, idx) => {{
                    reg.targetX = width / 2 + (idx - remainingRegs.length / 2) * 60;
                    reg.targetY = 1600;
                }});
            }} else if (viewMode === 'ring') {{
                const activeNode = selectedNode || hoverNode;
                const r0_center = {{ x: width / 2, y: height / 2 }};
                const assignedNodes = new Set();

                const mocNode = nodes.find(n => n.group === "Master Index" || n.label.includes("MOC"));

                let outerBaseRadiusCalc = 940;

                if (activeNode) {{
                    activeNode.targetX = r0_center.x;
                    activeNode.targetY = r0_center.y;
                    assignedNodes.add(activeNode.id);

                    const targetDirectRegs = [];
                    const linkedIpBlocks = [];

                    for (let e of edges) {{
                        let neighbor = null;
                        if (e.source.id === activeNode.id) neighbor = e.target;
                        else if (e.target.id === activeNode.id) neighbor = e.source;

                        if (neighbor && !assignedNodes.has(neighbor.id)) {{
                            if (neighbor === mocNode) continue;

                            assignedNodes.add(neighbor.id);
                            if (neighbor.group === "Registers") {{
                                targetDirectRegs.push(neighbor);
                            }} else {{
                                linkedIpBlocks.push(neighbor);
                            }}
                        }}
                    }}

                    const maxPerSubRing = 12;
                    let regIdx = 0;
                    let currentRegRadius = 190;
                    const subRingRadiusStep = 75;

                    while (regIdx < targetDirectRegs.length) {{
                        const chunk = targetDirectRegs.slice(regIdx, regIdx + maxPerSubRing);
                        const chunkCount = chunk.length;
                        chunk.forEach((reg, cIdx) => {{
                            const angle = (cIdx / (chunkCount || 1)) * Math.PI * 2 - Math.PI / 2;
                            reg.targetX = r0_center.x + Math.cos(angle) * currentRegRadius;
                            reg.targetY = r0_center.y + Math.sin(angle) * currentRegRadius;
                        }});
                        regIdx += maxPerSubRing;
                        if (regIdx < targetDirectRegs.length) {{
                            currentRegRadius += subRingRadiusStep;
                        }}
                    }}

                    const r2_linkedIpRadius = Math.max(540, currentRegRadius + 150);
                    const r2Count = linkedIpBlocks.length;
                    linkedIpBlocks.forEach((ipNode, idx) => {{
                        const ipAngle = (idx / (r2Count || 1)) * Math.PI * 2 - Math.PI / 2;
                        ipNode.targetX = r0_center.x + Math.cos(ipAngle) * r2_linkedIpRadius;
                        ipNode.targetY = r0_center.y + Math.sin(ipAngle) * r2_linkedIpRadius;

                        const satelliteRegs = [];
                        for (let e of edges) {{
                            let subCandidate = null;
                            if (e.source.id === ipNode.id) subCandidate = e.target;
                            else if (e.target.id === ipNode.id) subCandidate = e.source;

                            if (subCandidate && subCandidate.group === "Registers" && !assignedNodes.has(subCandidate.id)) {{
                                assignedNodes.add(subCandidate.id);
                                satelliteRegs.push(subCandidate);
                            }}
                        }}

                        const satCount = satelliteRegs.length;
                        const maxPerPetalRing = 8;
                        let sIdx = 0;
                        let currentPetalRadius = 90;
                        const petalStep = 65;

                        while (sIdx < satCount) {{
                            const chunk = satelliteRegs.slice(sIdx, sIdx + maxPerPetalRing);
                            const chunkCount = chunk.length;
                            
                            ringPetalClusters.push({{
                                x: ipNode.targetX,
                                y: ipNode.targetY,
                                radius: currentPetalRadius
                            }});

                            chunk.forEach((satReg, cIdx) => {{
                                const petalAngle = (cIdx / (chunkCount || 1)) * Math.PI * 2 - Math.PI / 2;
                                satReg.targetX = ipNode.targetX + Math.cos(petalAngle) * currentPetalRadius;
                                satReg.targetY = ipNode.targetY + Math.sin(petalAngle) * currentPetalRadius;
                            }});

                            sIdx += maxPerPetalRing;
                            if (sIdx < satCount) {{
                                currentPetalRadius += petalStep;
                            }}
                        }}
                    }});

                    outerBaseRadiusCalc = Math.max(960, r2_linkedIpRadius + 390);
                }}

                const outerNodes = nodes.filter(n => !assignedNodes.has(n.id));
                outerNodes.forEach((n, idx) => {{
                    const angle = (idx / (outerNodes.length || 1)) * Math.PI * 2 - Math.PI / 2;
                    n.targetX = r0_center.x + Math.cos(angle) * outerBaseRadiusCalc;
                    n.targetY = r0_center.y + Math.sin(angle) * outerBaseRadiusCalc;
                }});

                if (mocNode && !assignedNodes.has(mocNode.id)) {{
                    const mocAngle = -Math.PI * 0.25;
                    mocNode.targetX = r0_center.x + Math.cos(mocAngle) * outerBaseRadiusCalc;
                    mocNode.targetY = r0_center.y + Math.sin(mocAngle) * outerBaseRadiusCalc;
                }}
            }} else if (viewMode === 'tree') {{
                const center = {{ x: width / 2, y: height / 2 }};
                const activeNode = selectedNode || hoverNode;

                const masterNode = nodes.find(n => n.group === "Master Index" || n.label.includes("MOC"));
                if (masterNode) {{
                    masterNode.targetX = center.x;
                    masterNode.targetY = center.y;
                }}

                // Group all IP blocks by category
                const categories = ["Core", "Memory", "System", "Peripherals", "Security"];
                const activeCategories = categories.filter(cat => nodes.some(n => n.group === cat && !n.isRegister));
                
                const catNodeMap = new Map();
                activeCategories.forEach(cat => {{
                    const ipNodes = nodes.filter(n => n.group === cat && !n.isRegister);
                    catNodeMap.set(cat, ipNodes);
                }});

                // Allocate angular space proportionally to the count of nodes in each category
                const minWeight = 2;
                let totalWeight = 0;
                const catWeights = new Map();
                activeCategories.forEach(cat => {{
                    const cnt = (catNodeMap.get(cat) || []).length;
                    const w = Math.max(minWeight, cnt);
                    catWeights.set(cat, w);
                    totalWeight += w;
                }});

                let currentAngle = -Math.PI / 2;
                const ipRadius = 420;

                activeCategories.forEach(cat => {{
                    const ipNodes = catNodeMap.get(cat) || [];
                    const w = catWeights.get(cat);
                    const catArc = (w / Math.max(1, totalWeight)) * (Math.PI * 2);
                    const count = ipNodes.length;

                    ipNodes.forEach((ip, idx) => {{
                        const step = count > 1 ? (catArc * 0.90) / (count - 1) : 0;
                        const angle = (currentAngle + catArc * 0.05) + (count > 1 ? idx * step : catArc * 0.45);

                        ip.targetX = center.x + Math.cos(angle) * ipRadius;
                        ip.targetY = center.y + Math.sin(angle) * ipRadius;
                    }});
                    currentAngle += catArc;
                }});

                const registerNodes = nodes.filter(n => n.group === "Registers");

                registerNodes.forEach(reg => {{
                    let parentIp = null;
                    for (let e of edges) {{
                        if (e.target.id === reg.id && e.source.group !== "Registers") {{
                            parentIp = e.source;
                            break;
                        }} else if (e.source.id === reg.id && e.target.group !== "Registers") {{
                            parentIp = e.target;
                            break;
                        }}
                    }}

                    if (parentIp) {{
                        const isParentActive = activeNode && (activeNode.id === parentIp.id || activeNode.id === reg.id);
                        if (isParentActive) {{
                            const siblings = [];
                            for (let e of edges) {{
                                let candidate = null;
                                if (e.source.id === parentIp.id && e.target.group === "Registers") candidate = e.target;
                                else if (e.target.id === parentIp.id && e.source.group === "Registers") candidate = e.source;
                                if (candidate && !siblings.includes(candidate)) siblings.push(candidate);
                            }}

                            const sibIdx = siblings.indexOf(reg);
                            const sibCount = siblings.length || 1;
                            
                            const parentAngle = Math.atan2(parentIp.targetY - center.y, parentIp.targetX - center.x);

                            const maxPerTier = 12;
                            const tierIndex = Math.floor(sibIdx / maxPerTier);
                            const posInTier = sibIdx % maxPerTier;
                            const itemsInTier = Math.min(maxPerTier, sibCount - tierIndex * maxPerTier);

                            const regArcSpread = Math.min(1.4, 0.10 * itemsInTier);
                            const regAngle = parentAngle + (posInTier - (itemsInTier - 1) / 2) * (regArcSpread / Math.max(1, itemsInTier - 1));
                            const regRadius = ipRadius + 160 + tierIndex * 80;

                            reg.targetX = center.x + Math.cos(regAngle) * regRadius;
                            reg.targetY = center.y + Math.sin(regAngle) * regRadius;
                        }} else {{
                            reg.targetX = parentIp.targetX;
                            reg.targetY = parentIp.targetY;
                        }}
                    }} else {{
                        reg.targetX = center.x;
                        reg.targetY = center.y;
                    }}
                }});
            }}
        }}

        function switchViewMode(mode) {{
            viewMode = mode;
            document.querySelectorAll('.view-btn').forEach(btn => btn.classList.remove('active'));
            document.getElementById(`btn-view-${{mode}}`).classList.add('active');

            const container2d = document.getElementById('graphCanvas');
            const container3d = document.getElementById('graph3dContainer');

            if (mode === '3d') {{
                container2d.style.display = 'none';
                container3d.style.display = 'block';
                if (!graph3dInstance) {{
                    init3DGraph();
                }} else {{
                    if (typeof graph3dInstance.resumeAnimation === 'function') {{
                        graph3dInstance.resumeAnimation();
                    }}
                    update3DGraphStyles();
                }}
            }} else {{
                container2d.style.display = 'block';
                container3d.style.display = 'none';
                if (mode !== 'mesh') {{
                    computeLayoutTargets();
                }}
            }}
        }}

        // 3. High-Performance Physics Step & Speed Multiplier
        function updatePhysics() {{
            if (!physicsRunning && !dragNode) return;
            if (viewMode === '3d') return;

            const activeNode = selectedNode || hoverNode;
            const connectedSet = new Set();
            if (activeNode) {{
                connectedSet.add(activeNode.id);
                for (let e of edges) {{
                    if (e.source.id === activeNode.id) connectedSet.add(e.target.id);
                    if (e.target.id === activeNode.id) connectedSet.add(e.source.id);
                }}
            }}

            const steps = (viewMode === 'mesh') ? physicsSpeedMultiplier : 1;

            for (let s = 0; s < steps; s++) {{
                if (viewMode === 'mesh') {{
                    const repulsion = 3800;
                    const centerGravity = 0.0018;

                    for (let i = 0; i < nodes.length; i++) {{
                        const n1 = nodes[i];
                        for (let j = i + 1; j < nodes.length; j++) {{
                            const n2 = nodes[j];
                            let dx = n2.x - n1.x;
                            let dy = n2.y - n1.y;
                            let dist = Math.sqrt(dx * dx + dy * dy) || 1;
                            
                            const minDist = n1.size + n2.size + 48;
                            if (dist < minDist) {{
                                let pushHard = (minDist - dist) * 0.42;
                                let fx = (dx / dist) * pushHard;
                                let fy = (dy / dist) * pushHard;
                                n1.vx -= fx;
                                n1.vy -= fy;
                                n2.vx += fx;
                                n2.vy += fy;
                            }} else if (dist < 650) {{
                                let force = (repulsion / (dist * dist));
                                let fx = (dx / dist) * force;
                                let fy = (dy / dist) * force;
                                n1.vx -= fx;
                                n1.vy -= fy;
                                n2.vx += fx;
                                n2.vy += fy;
                            }}
                        }}
                        n1.vx += (width / 2 - n1.x) * centerGravity;
                        n1.vy += (height / 2 - n1.y) * centerGravity;
                    }}

                    if (activeNode) {{
                        for (let i = 0; i < nodes.length; i++) {{
                            const n = nodes[i];
                            if (!connectedSet.has(n.id)) {{
                                let dx = n.x - activeNode.x;
                                let dy = n.y - activeNode.y;
                                let dist = Math.sqrt(dx * dx + dy * dy) || 1;
                                if (dist < 600) {{
                                    let pushForce = (24000 / (dist * dist));
                                    n.vx += (dx / dist) * pushForce;
                                    n.vy += (dy / dist) * pushForce;
                                }}
                            }}
                        }}
                    }}

                    for (let e of edges) {{
                        let dx = e.target.x - e.source.x;
                        let dy = e.target.y - e.source.y;
                        let dist = Math.sqrt(dx * dx + dy * dy) || 1;

                        const isClusterEdge = activeNode && (e.source.id === activeNode.id || e.target.id === activeNode.id);
                        const springLength = isClusterEdge ? 260 : 180;
                        const springK = isClusterEdge ? 0.06 : 0.02;

                        let force = (dist - springLength) * springK;
                        let fx = (dx / dist) * force;
                        let fy = (dy / dist) * force;
                        e.source.vx += fx;
                        e.source.vy += fy;
                        e.target.vx -= fx;
                        e.target.vy -= fy;
                    }}

                    for (let i = 0; i < nodes.length; i++) {{
                        const n = nodes[i];
                        if (n === dragNode) continue;
                        n.vx *= 0.78;
                        n.vy *= 0.78;
                        n.x += Math.max(-5, Math.min(5, n.vx));
                        n.y += Math.max(-5, Math.min(5, n.vy));
                    }}
                }}
            }}

            if (viewMode !== 'mesh' && viewMode !== '3d') {{
                if (viewMode === 'ring' || viewMode === 'tree' || viewMode === 'dag') {{
                    computeLayoutTargets();
                }}

                const interStep = Math.min(0.45, 0.09 * physicsSpeedMultiplier);
                for (let i = 0; i < nodes.length; i++) {{
                    const n = nodes[i];
                    if (n === dragNode) continue;
                    n.x += (n.targetX - n.x) * interStep;
                    n.y += (n.targetY - n.y) * interStep;
                }}
            }}
        }}

        function drawDagLevelBadge(text, x, y, textColor, borderColor) {{
            ctx.save();
            ctx.font = "bold 11px system-ui, -apple-system, sans-serif";
            const metrics = ctx.measureText(text);
            const padX = 10;
            const padY = 5;
            const boxW = metrics.width + padX * 2;
            const boxH = 22;

            ctx.beginPath();
            if (ctx.roundRect) {{
                ctx.roundRect(x - padX, y - boxH / 2, boxW, boxH, 6);
            }} else {{
                ctx.rect(x - padX, y - boxH / 2, boxW, boxH);
            }}
            ctx.fillStyle = "rgba(15, 23, 42, 0.94)";
            ctx.shadowColor = "rgba(0, 0, 0, 0.7)";
            ctx.shadowBlur = 10;
            ctx.fill();

            ctx.strokeStyle = borderColor;
            ctx.lineWidth = 1.4;
            ctx.stroke();

            ctx.fillStyle = textColor;
            ctx.textAlign = "left";
            ctx.textBaseline = "middle";
            ctx.fillText(text, x, y);
            ctx.restore();
        }}

        // Pre-calculate and cache label wrapping and font size metrics on nodes to prevent per-frame overhead
        function cacheNodeLabelMetrics() {{
            for (let n of nodes) {{
                const lines = wrapTextLines(n.label);
                n.cachedLines = lines;
                const maxLineLen = Math.max(...lines.map(l => l.length));
                let baseFontSize = 10;
                let maxAllowedByWidth = (n.size * 1.6) / maxLineLen;
                let maxAllowedByHeight = (n.size * 1.6) / (lines.length * 1.25);
                n.cachedFontSize = Math.max(7, Math.min(baseFontSize, Math.floor(Math.min(maxAllowedByWidth, maxAllowedByHeight))));
                n.cachedLineHeight = n.cachedFontSize * 1.18;
            }}
        }}

        function render() {{
            updatePhysics();

            if (viewMode !== '3d') {{
                ctx.fillStyle = "#0b0f19";
                ctx.fillRect(0, 0, width, height);

                ctx.save();
                ctx.translate(transform.x, transform.y);
                ctx.scale(transform.k, transform.k);

                // Viewport Culling Bounds in World Space
                const vMargin = 120 / transform.k;
                const vMinX = -transform.x / transform.k - vMargin;
                const vMaxX = (width - transform.x) / transform.k + vMargin;
                const vMinY = -transform.y / transform.k - vMargin;
                const vMaxY = (height - transform.y) / transform.k + vMargin;

                const activeNode = selectedNode || hoverNode;
                const connectedSet = new Set();
                const secondarySet = new Set();

                if (activeNode) {{
                    connectedSet.add(activeNode.id);
                    for (let e of edges) {{
                        if (e.source.id === activeNode.id) connectedSet.add(e.target.id);
                        if (e.target.id === activeNode.id) connectedSet.add(e.source.id);
                    }}

                    for (let e of edges) {{
                        if (connectedSet.has(e.source.id) && !connectedSet.has(e.target.id)) {{
                            secondarySet.add(e.target.id);
                        }} else if (connectedSet.has(e.target.id) && !connectedSet.has(e.source.id)) {{
                            secondarySet.add(e.source.id);
                        }}
                    }}
                }}

                if (viewMode === 'ring') {{
                    ctx.save();
                    const center = {{ x: width / 2, y: height / 2 }};

                    ctx.beginPath();
                    ctx.arc(center.x, center.y, 190, 0, Math.PI * 2);
                    ctx.strokeStyle = activeNode ? "rgba(0, 229, 255, 0.45)" : "rgba(56, 189, 248, 0.1)";
                    ctx.lineWidth = activeNode ? 2.0 : 1.2;
                    ctx.setLineDash([4, 4]);
                    ctx.stroke();

                    ringPetalClusters.forEach(cluster => {{
                        ctx.beginPath();
                        ctx.arc(cluster.x, cluster.y, cluster.radius, 0, Math.PI * 2);
                        ctx.strokeStyle = "rgba(52, 211, 153, 0.40)";
                        ctx.lineWidth = 1.4;
                        ctx.setLineDash([4, 4]);
                        ctx.stroke();
                    }});

                    if (activeNode) {{
                        ctx.font = "bold 11px system-ui";
                        ctx.textAlign = "center";
                        ctx.fillStyle = "#00e5ff";
                        ctx.fillText("RING 1: TARGET REGISTERS", center.x, center.y - 190 - 8);
                    }}
                    ctx.restore();
                }} else if (viewMode === 'tree') {{
                    ctx.save();
                    const center = {{ x: width / 2, y: height / 2 }};

                    ctx.beginPath();
                    ctx.arc(center.x, center.y, 420, 0, Math.PI * 2);
                    ctx.strokeStyle = "rgba(16, 185, 129, 0.25)";
                    ctx.lineWidth = 1.5;
                    ctx.setLineDash([6, 6]);
                    ctx.stroke();

                    if (activeNode) {{
                        ctx.beginPath();
                        ctx.arc(center.x, center.y, 580, 0, Math.PI * 2);
                        ctx.strokeStyle = "rgba(6, 182, 212, 0.35)";
                        ctx.lineWidth = 1.5;
                        ctx.setLineDash([4, 4]);
                        ctx.stroke();
                    }}

                    ctx.font = "bold 11px system-ui";
                    ctx.textAlign = "center";
                    ctx.fillStyle = "#34d399";
                    ctx.fillText("PERIPHERAL & SYSTEM SUBSYSTEMS", center.x, center.y - 420 - 10);
                    if (activeNode) {{
                        ctx.fillStyle = "#22d3ee";
                        ctx.fillText("HARDWARE REGISTERS", center.x, center.y - 580 - 10);
                    }}

                    ctx.restore();
                }}

                // HIGH PERFORMANCE BATCHED EDGE RENDERING (Reduces 6,328 draw calls to 4)
                const dimEdges = [];
                const layerEdges = [];
                const secondaryEdges = [];
                const directEdges = [];

                for (let i = 0; i < edges.length; i++) {{
                    const e = edges[i];

                    // Viewport frustum culling
                    if ((e.source.x < vMinX && e.target.x < vMinX) || (e.source.x > vMaxX && e.target.x > vMaxX) ||
                        (e.source.y < vMinY && e.target.y < vMinY) || (e.source.y > vMaxY && e.target.y > vMaxY)) {{
                        continue;
                    }}

                    if (viewMode === 'tree') {{
                        const isTreeHierarchyEdge = (
                            e.source.group === "Master Index" || e.target.group === "Master Index" ||
                            (e.source.group !== "Registers" && e.target.group === "Registers") ||
                            (e.target.group !== "Registers" && e.source.group === "Registers")
                        );
                        if (!isTreeHierarchyEdge) continue;

                        const isRegEdge = (e.source.group === "Registers" || e.target.group === "Registers");
                        const isEdgeActive = activeNode && (e.source.id === activeNode.id || e.target.id === activeNode.id || connectedSet.has(e.source.id) || connectedSet.has(e.target.id));
                        if (isRegEdge && !isEdgeActive) continue;
                    }}

                    const isDirect = activeNode && (e.source.id === activeNode.id || e.target.id === activeNode.id);
                    const isSecondary = activeNode && (
                        (connectedSet.has(e.source.id) && secondarySet.has(e.target.id)) ||
                        (secondarySet.has(e.source.id) && connectedSet.has(e.target.id))
                    );
                    const isLayerMatch = (activeLayerFilter === "All") || (e.source.group === activeLayerFilter || e.target.group === activeLayerFilter);

                    if (isDirect) directEdges.push(e);
                    else if (isSecondary) secondaryEdges.push(e);
                    else if (isLayerMatch) layerEdges.push(e);
                    else dimEdges.push(e);
                }}

                // Batch 1: Background Dim Edges
                if (dimEdges.length > 0) {{
                    ctx.beginPath();
                    for (let i = 0; i < dimEdges.length; i++) {{
                        const e = dimEdges[i];
                        ctx.moveTo(e.source.x, e.source.y);
                        ctx.lineTo(e.target.x, e.target.y);
                    }}
                    ctx.strokeStyle = "rgba(30, 41, 59, 0.12)";
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }}

                // Batch 2: Standard Layer Edges
                if (layerEdges.length > 0) {{
                    ctx.beginPath();
                    for (let i = 0; i < layerEdges.length; i++) {{
                        const e = layerEdges[i];
                        ctx.moveTo(e.source.x, e.source.y);
                        ctx.lineTo(e.target.x, e.target.y);
                    }}
                    ctx.strokeStyle = (activeLayerFilter === "All") ? (activeNode ? "rgba(51, 65, 85, 0.10)" : "rgba(71, 85, 105, 0.45)") : "rgba(56, 189, 248, 0.45)";
                    ctx.lineWidth = 1.2;
                    ctx.stroke();
                }}

                // Batch 3: Secondary Connected Edges (Green Glow)
                if (secondaryEdges.length > 0) {{
                    ctx.beginPath();
                    for (let i = 0; i < secondaryEdges.length; i++) {{
                        const e = secondaryEdges[i];
                        ctx.moveTo(e.source.x, e.source.y);
                        ctx.lineTo(e.target.x, e.target.y);
                    }}
                    ctx.strokeStyle = "rgba(52, 211, 153, 0.75)";
                    ctx.lineWidth = 2.0;
                    ctx.stroke();
                }}

                // Batch 4: Direct Connected Edges (Cyan Glow)
                if (directEdges.length > 0) {{
                    ctx.beginPath();
                    for (let i = 0; i < directEdges.length; i++) {{
                        const e = directEdges[i];
                        ctx.moveTo(e.source.x, e.source.y);
                        ctx.lineTo(e.target.x, e.target.y);
                    }}
                    ctx.strokeStyle = "#00e5ff";
                    ctx.lineWidth = 3.5;
                    ctx.shadowColor = "#00e5ff";
                    ctx.shadowBlur = 10;
                    ctx.stroke();
                    ctx.shadowBlur = 0;
                }}

                // ADVANCED GAME RENDERING FEATURE 1: ANIMATED BUS DATA FLOW PULSES (AHB/APB Signal Flow)
                const nowTime = performance.now();
                const pulseOffset = (nowTime * 0.035) % 32;

                if (directEdges.length > 0) {{
                    ctx.save();
                    ctx.beginPath();
                    for (let i = 0; i < directEdges.length; i++) {{
                        const e = directEdges[i];
                        ctx.moveTo(e.source.x, e.source.y);
                        ctx.lineTo(e.target.x, e.target.y);
                    }}
                    ctx.setLineDash([8, 16]);
                    ctx.lineDashOffset = -pulseOffset;
                    ctx.strokeStyle = "#ffffff";
                    ctx.lineWidth = 2.2;
                    ctx.shadowColor = "#00e5ff";
                    ctx.shadowBlur = 8;
                    ctx.stroke();
                    ctx.restore();
                }}

                if (secondaryEdges.length > 0) {{
                    ctx.save();
                    ctx.beginPath();
                    for (let i = 0; i < secondaryEdges.length; i++) {{
                        const e = secondaryEdges[i];
                        ctx.moveTo(e.source.x, e.source.y);
                        ctx.lineTo(e.target.x, e.target.y);
                    }}
                    ctx.setLineDash([6, 18]);
                    ctx.lineDashOffset = -pulseOffset * 0.8;
                    ctx.strokeStyle = "rgba(52, 211, 153, 0.9)";
                    ctx.lineWidth = 1.6;
                    ctx.shadowColor = "#34d399";
                    ctx.shadowBlur = 6;
                    ctx.stroke();
                    ctx.restore();
                }}

                if (viewMode === 'dag') {{
                    drawDagLevelBadge("💖 LEVEL 0: MASTER MAP OF CONTENT (MOC)", 40, 60, "#f472b6", "#ec4899");
                    drawDagLevelBadge("🟣 LEVEL 1: CORE & SYSTEM MEMORY", 40, 195, "#c084fc", "#a855f7");
                    drawDagLevelBadge("🟧 LEVEL 2: SYSTEM & SECURITY ARCHITECTURE", 40, 335, "#fbbf24", "#f59e0b");
                    drawDagLevelBadge("⚡ LEVEL 3: PERIPHERAL IP BLOCKS", 40, 505, "#00e5ff", "#0284c7");
                    drawDagLevelBadge("🩵 LEVEL 4: HARDWARE REGISTERS (STRICTLY STAGED BELOW PERIPHERALS)", 40, 685, "#38bdf8", "#06b6d4");
                }}

                // NODE RENDERING LOOP WITH VIEWPORT CULLING AND CACHED TEXT METRICS
                for (let i = 0; i < nodes.length; i++) {{
                    const n = nodes[i];

                    // Viewport Culling
                    if (n.x < vMinX || n.x > vMaxX || n.y < vMinY || n.y > vMaxY) continue;

                    if (viewMode === 'tree' && n.group === "Registers") {{
                        const isRegActive = activeNode && (n.id === activeNode.id || connectedSet.has(n.id));
                        if (!isRegActive) continue;
                    }}

                    const isSubNode = activeNode && (n.id !== activeNode.id) && connectedSet.has(n.id);
                    const isSecNode = activeNode && secondarySet.has(n.id);
                    const isLayerMatch = (activeLayerFilter === "All") || (n.group === activeLayerFilter);
                    
                    const opacity = (n === activeNode) ? 1.0 : (isSubNode ? 0.94 : (isSecNode ? 0.85 : (activeNode ? 0.08 : (isLayerMatch ? 0.92 : 0.15))));

                    ctx.save();
                    ctx.globalAlpha = opacity;

                    const nodeRadius = (n === activeNode) ? (n.size + 6) : (isSubNode ? (n.size + 3) : (isSecNode ? (n.size + 1) : n.size));

                    // ADVANCED GAME RENDERING FEATURE 2: SELECTIVE UNREAL NEON BLOOM FX HALOS
                    if (n === activeNode) {{
                        const pulseScale = 1.0 + 0.12 * Math.sin(nowTime * 0.006);
                        const bloomRadius = (nodeRadius + 8) * pulseScale;

                        ctx.save();
                        ctx.beginPath();
                        ctx.arc(n.x, n.y, bloomRadius, 0, Math.PI * 2);
                        ctx.fillStyle = "rgba(0, 229, 255, 0.18)";
                        ctx.shadowColor = "#00e5ff";
                        ctx.shadowBlur = 24;
                        ctx.fill();

                        ctx.beginPath();
                        ctx.arc(n.x, n.y, bloomRadius + 4, 0, Math.PI * 2);
                        ctx.strokeStyle = "rgba(0, 229, 255, 0.6)";
                        ctx.lineWidth = 1.8;
                        ctx.stroke();
                        ctx.restore();
                    }} else if (isSubNode) {{
                        ctx.save();
                        ctx.beginPath();
                        ctx.arc(n.x, n.y, nodeRadius + 4, 0, Math.PI * 2);
                        ctx.fillStyle = "rgba(0, 229, 255, 0.10)";
                        ctx.shadowColor = "#00e5ff";
                        ctx.shadowBlur = 14;
                        ctx.fill();
                        ctx.restore();
                    }}

                    ctx.beginPath();
                    ctx.arc(n.x, n.y, nodeRadius, 0, Math.PI * 2);
                    ctx.fillStyle = n.color;
                    ctx.shadowColor = (n === activeNode) ? "#ffffff" : (isSubNode ? "#00e5ff" : (isSecNode ? "#34d399" : n.color));
                    ctx.shadowBlur = (n === activeNode) ? 16 : (isSubNode ? 8 : (isSecNode ? 4 : 0));
                    ctx.fill();

                    if (n === activeNode) {{
                        ctx.lineWidth = 4.5;
                        ctx.strokeStyle = "#ffffff";
                        ctx.stroke();

                        ctx.beginPath();
                        ctx.arc(n.x, n.y, nodeRadius + 4, 0, Math.PI * 2);
                        ctx.lineWidth = 2.0;
                        ctx.strokeStyle = "#00e5ff";
                        ctx.stroke();
                    }} else if (isSubNode) {{
                        ctx.lineWidth = 3;
                        ctx.strokeStyle = "#00e5ff";
                        ctx.stroke();

                        ctx.beginPath();
                        ctx.arc(n.x, n.y, nodeRadius + 3.5, 0, Math.PI * 2);
                        ctx.lineWidth = 1.5;
                        ctx.strokeStyle = "rgba(0, 229, 255, 0.7)";
                        ctx.stroke();
                    }} else if (isSecNode) {{
                        ctx.lineWidth = 2;
                        ctx.strokeStyle = "#34d399";
                        ctx.stroke();
                    }} else {{
                        ctx.lineWidth = (activeLayerFilter !== "All" && isLayerMatch) ? 2.5 : 1.5;
                        ctx.strokeStyle = (activeLayerFilter !== "All" && isLayerMatch) ? "#ffffff" : n.borderColor;
                        ctx.stroke();
                    }}

                    const lines = n.cachedLines || wrapTextLines(n.label);
                    const fontSize = (n === activeNode) ? 13 : (isSubNode ? 11.5 : (isSecNode ? 10.5 : (n.cachedFontSize || 10)));
                    const lineHeight = n.cachedLineHeight || (fontSize * 1.18);

                    ctx.font = `bold ${{fontSize}}px system-ui, -apple-system, sans-serif`;
                    ctx.textAlign = "center";
                    ctx.textBaseline = "middle";

                    if (n === activeNode) {{
                        ctx.fillStyle = "#ffffff";
                        ctx.shadowColor = "#000000";
                        ctx.shadowBlur = 4;
                    }} else if (isSubNode) {{
                        ctx.fillStyle = "#ffffff";
                        ctx.shadowColor = "#000000";
                        ctx.shadowBlur = 2;
                    }} else if (isSecNode) {{
                        ctx.fillStyle = "#f0fdf4";
                        ctx.shadowColor = "#000000";
                        ctx.shadowBlur = 2;
                    }} else {{
                        ctx.fillStyle = isLayerMatch ? "#ffffff" : "rgba(255, 255, 255, 0.6)";
                        ctx.shadowBlur = 0;
                    }}

                    const startY = n.y - ((lines.length - 1) * lineHeight) / 2;

                    for (let lIdx = 0; lIdx < lines.length; lIdx++) {{
                        ctx.fillText(lines[lIdx], n.x, startY + lIdx * lineHeight);
                    }}

                    ctx.restore();
                }}

                ctx.restore();
            }}

            requestAnimationFrame(render);
        }}

        // 5. Hit Testing
        function getCanvasPos(e) {{
            const rect = canvas.getBoundingClientRect();
            const mouseX = e.clientX - rect.left;
            const mouseY = e.clientY - rect.top;
            const worldX = (mouseX - transform.x) / transform.k;
            const worldY = (mouseY - transform.y) / transform.k;
            return {{ mouseX, mouseY, worldX, worldY }};
        }}

        function findNodeAt(worldX, worldY) {{
            const hitMargin = 16 / transform.k;

            if (selectedNode) {{
                for (let e of edges) {{
                    let neighbor = null;
                    if (e.source.id === selectedNode.id) neighbor = e.target;
                    else if (e.target.id === selectedNode.id) neighbor = e.source;

                    if (neighbor) {{
                        const dx = worldX - neighbor.x;
                        const dy = worldY - neighbor.y;
                        const radius = neighbor.size + hitMargin;
                        if (dx * dx + dy * dy <= radius * radius) {{
                            return neighbor;
                        }}
                    }}
                }}
            }}

            for (let i = nodes.length - 1; i >= 0; i--) {{
                const n = nodes[i];
                if (viewMode === 'tree' && n.group === "Registers" && (!selectedNode || (selectedNode.id !== n.id && !rawEdgeMap.get(selectedNode.id)?.includes(n.id)))) continue;
                if (activeLayerFilter !== "All" && n.group !== activeLayerFilter) continue;
                const dx = worldX - n.x;
                const dy = worldY - n.y;
                const radius = n.size + hitMargin;
                if (dx * dx + dy * dy <= radius * radius) {{
                    return n;
                }}
            }}

            for (let i = nodes.length - 1; i >= 0; i--) {{
                const n = nodes[i];
                if (viewMode === 'tree' && n.group === "Registers" && (!selectedNode || (selectedNode.id !== n.id && !rawEdgeMap.get(selectedNode.id)?.includes(n.id)))) continue;
                const dx = worldX - n.x;
                const dy = worldY - n.y;
                const radius = n.size + hitMargin;
                if (dx * dx + dy * dy <= radius * radius) {{
                    return n;
                }}
            }}
            return null;
        }}

        canvas.addEventListener('mousedown', e => {{
            if (viewMode === '3d') return;
            const pos = getCanvasPos(e);
            const clicked = findNodeAt(pos.worldX, pos.worldY);
            isDragging = true;
            startX = e.clientX - transform.x;
            startY = e.clientY - transform.y;

            if (clicked) {{
                dragNode = clicked;
                selectNode(clicked, false, true);
            }} else {{
                dragNode = null;
            }}
        }});

        canvas.addEventListener('mousemove', e => {{
            if (viewMode === '3d') return;
            const pos = getCanvasPos(e);
            hoverNode = findNodeAt(pos.worldX, pos.worldY);
            canvas.style.cursor = hoverNode ? 'pointer' : (isDragging ? 'grabbing' : 'default');

            if (isDragging) {{
                if (dragNode) {{
                    dragNode.x = pos.worldX;
                    dragNode.y = pos.worldY;
                }} else {{
                    transform.x = e.clientX - startX;
                    transform.y = e.clientY - startY;
                }}
            }}
        }});

        window.addEventListener('mouseup', () => {{
            isDragging = false;
            dragNode = null;
        }});

        canvas.addEventListener('wheel', e => {{
            if (viewMode === '3d') return;
            e.preventDefault();
            const zoomFactor = e.deltaY < 0 ? 1.15 : 0.85;
            const newScale = Math.max(0.15, Math.min(4.0, transform.k * zoomFactor));

            const mouseX = e.clientX;
            const mouseY = e.clientY - 55;

            transform.x = mouseX - (mouseX - transform.x) * (newScale / transform.k);
            transform.y = mouseY - (mouseY - transform.y) * (newScale / transform.k);
            transform.k = newScale;
        }}, {{ passive: false }});

        // 6. Navigation History Back & Forward Controls
        function updateHistoryUI() {{
            const backBtn = document.getElementById('navBackBtn');
            const forwardBtn = document.getElementById('navForwardBtn');

            backBtn.disabled = (navHistoryIndex <= 0);
            forwardBtn.disabled = (navHistoryIndex >= navHistory.length - 1);

            const container = document.getElementById('breadcrumbTrail');
            container.innerHTML = "";

            navHistory.slice(0, navHistoryIndex + 1).forEach((id, idx) => {{
                const targetNode = nodeMap.get(id);
                if (!targetNode) return;

                if (idx > 0) {{
                    const sep = document.createElement('span');
                    sep.className = 'breadcrumb-separator';
                    sep.innerText = '➔';
                    container.appendChild(sep);
                }}

                const item = document.createElement('span');
                item.className = 'breadcrumb-item';
                item.innerText = targetNode.label;
                item.onclick = () => {{
                    navHistoryIndex = idx;
                    selectNode(targetNode, true, false);
                }};
                container.appendChild(item);
            }});
        }}

        function goBackHistory() {{
            if (navHistoryIndex > 0) {{
                navHistoryIndex--;
                const targetId = navHistory[navHistoryIndex];
                const targetNode = nodeMap.get(targetId);
                if (targetNode) {{
                    selectNode(targetNode, true, false);
                }}
            }}
        }}

        function goForwardHistory() {{
            if (navHistoryIndex < navHistory.length - 1) {{
                navHistoryIndex++;
                const targetId = navHistory[navHistoryIndex];
                const targetNode = nodeMap.get(targetId);
                if (targetNode) {{
                    selectNode(targetNode, true, false);
                }}
            }}
        }}

        // 7. Topology Layer Highlighting Function
        function highlightTopologyLayer(groupName) {{
            activeLayerFilter = groupName;
            document.getElementById('layerSelect').value = groupName;

            document.querySelectorAll('.legend-item').forEach(el => el.classList.remove('active'));
            const activeLegendItem = document.getElementById(`leg-${{groupName}}`);
            if (activeLegendItem) activeLegendItem.classList.add('active');

            const matchedNodes = nodes.filter(n => groupName === "All" || n.group === groupName);
            
            if (groupName === "All") {{
                document.getElementById('telemetryBadge').innerText = `Parsed in {parse_elapsed:.3f}s | {len(node_list)} Nodes | {len(edge_list)} Links`;
                if (viewMode === '3d' && graph3dInstance) {{
                    update3DGraphStyles();
                    graph3dInstance.cameraPosition({{ x: 0, y: 0, z: 600 }}, {{ x: 0, y: 0, z: 0 }}, 1500);
                }} else {{
                    resetZoom();
                }}
            }} else {{
                document.getElementById('telemetryBadge').innerText = `Layer Filter: ${{groupName}} (${{matchedNodes.length}} Nodes)`;
                
                if (viewMode === '3d' && graph3dInstance) {{
                    update3DGraphStyles();
                    const gData = graph3dInstance.graphData();
                    const matched3d = gData.nodes.filter(n => n.group === groupName);
                    if (matched3d.length > 0) {{
                        let sumX = 0, sumY = 0, sumZ = 0;
                        matched3d.forEach(n => {{
                            sumX += (n.x || 0);
                            sumY += (n.y || 0);
                            sumZ += (n.z || 0);
                        }});
                        const cX = sumX / matched3d.length;
                        const cY = sumY / matched3d.length;
                        const cZ = sumZ / matched3d.length;
                        graph3dInstance.cameraPosition(
                            {{ x: cX + 160, y: cY + 160, z: cZ + 280 }},
                            {{ x: cX, y: cY, z: cZ }},
                            1800
                        );
                    }}
                }} else if (matchedNodes.length > 0) {{
                    let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
                    matchedNodes.forEach(n => {{
                        if (n.x < minX) minX = n.x;
                        if (n.x > maxX) maxX = n.x;
                        if (n.y < minY) minY = n.y;
                        if (n.y > maxY) maxY = n.y;
                    }});
                    const centerX = (minX + maxX) / 2;
                    const centerY = (minY + maxY) / 2;
                    const spanX = (maxX - minX) || 400;
                    const spanY = (maxY - minY) || 400;

                    const scaleX = width / (spanX + 250);
                    const scaleY = height / (spanY + 250);
                    transform.k = Math.max(0.4, Math.min(1.8, Math.min(scaleX, scaleY)));
                    transform.x = width / 2 - centerX * transform.k;
                    transform.y = height / 2 - centerY * transform.k;
                }}
            }}
        }}

        // 8. Select Node & Show Rich Inspector Sidebar with Navigation History
        function selectNode(node, autoZoom = false, pushHistory = true) {{
            selectedNode = node;
            document.getElementById('sideNodeLabel').innerText = node.label;
            document.getElementById('sideNodeGroupBadge').innerText = node.group;
            document.getElementById('sideNodeGroupBadge').style.background = node.color;
            document.getElementById('sideNodePath').innerText = node.path;
            document.getElementById('sideNodeDetailsContainer').innerHTML = node.details || "<p>No content preview available.</p>";

            if (pushHistory) {{
                if (navHistoryIndex < 0 || navHistory[navHistoryIndex] !== node.id) {{
                    navHistory = navHistory.slice(0, navHistoryIndex + 1);
                    navHistory.push(node.id);
                    navHistoryIndex = navHistory.length - 1;
                }}
            }}
            updateHistoryUI();

            const neighbors = [];
            for (let e of edges) {{
                if (e.source.id === node.id) neighbors.push(e.target);
                else if (e.target.id === node.id) neighbors.push(e.source);
            }}

            document.getElementById('neighborHeader').innerText = `Connected Sub-Nodes & Links (${{neighbors.length}})`;
            const badgeContainer = document.getElementById('neighborBadgesContainer');
            badgeContainer.innerHTML = "";

            neighbors.forEach(n => {{
                const badge = document.createElement('span');
                badge.className = 'neighbor-badge';
                badge.innerText = n.label;
                badge.onclick = (evt) => {{
                    evt.stopPropagation();
                    selectNode(n, true, true);
                }};
                badgeContainer.appendChild(badge);
            }});

            document.getElementById('nodeSidebar').style.display = 'block';

            if (viewMode === '3d' && graph3dInstance) {{
                update3DGraphStyles();
                const gData = graph3dInstance.graphData();
                const target3d = gData.nodes.find(n => n.id === node.id);
                if (target3d) {{
                    const distRatio = 1 + 90 / Math.hypot(target3d.x || 1, target3d.y || 1, target3d.z || 1);
                    graph3dInstance.cameraPosition(
                        {{ x: (target3d.x || 0) * distRatio, y: (target3d.y || 0) * distRatio, z: (target3d.z || 0) * distRatio }},
                        target3d,
                        2000
                    );
                }}
            }} else if (autoZoom) {{
                transform.k = 1.35;
                transform.x = width / 2 - node.x * transform.k;
                transform.y = height / 2 - node.y * transform.k;
            }}
        }}

        function closeSidebar() {{
            selectedNode = null;
            document.getElementById('nodeSidebar').style.display = 'none';
            if (viewMode === '3d' && graph3dInstance) {{
                update3DGraphStyles();
            }}
        }}

        function resetZoom() {{
            const w = width || window.innerWidth;
            const h = height || (window.innerHeight - 60);
            transform = {{ x: w * 0.12, y: h * 0.12, k: 0.70 }};
            activeLayerFilter = "All";
            if (document.getElementById('layerSelect')) document.getElementById('layerSelect').value = "All";
            document.querySelectorAll('.legend-item').forEach(el => el.classList.remove('active'));
            if (document.getElementById('leg-All')) document.getElementById('leg-All').classList.add('active');
            if (document.getElementById('telemetryBadge')) {{
                document.getElementById('telemetryBadge').innerText = `Parsed in {parse_elapsed:.3f}s | {len(node_list)} Nodes | {len(edge_list)} Links`;
            }}
            closeSidebar();
            if (viewMode === '3d' && graph3dInstance) {{
                update3DGraphStyles();
                graph3dInstance.cameraPosition({{ x: 0, y: 0, z: 600 }}, {{ x: 0, y: 0, z: 0 }}, 1500);
            }}
            physicsRunning = true;
        }}

        function togglePhysics() {{
            physicsRunning = !physicsRunning;
            document.getElementById('physicsBtn').innerText = physicsRunning ? "Pause Physics" : "Play Physics";
            if (physicsRunning) requestAnimationFrame(render);
        }}

        let fastSearchIndexMap = new Map();
        function buildFastSearchIndex() {{
            fastSearchIndexMap.clear();
            nodes.forEach(n => {{
                fastSearchIndexMap.set(n.label.toLowerCase(), n);
                fastSearchIndexMap.set(n.path.toLowerCase(), n);
            }});
        }}

        let searchDebounceTimer = null;
        function debounceSearchNode() {{
            if (searchDebounceTimer) clearTimeout(searchDebounceTimer);
            searchDebounceTimer = setTimeout(() => {{
                searchNode();
            }}, 150);
        }}

        function searchNode() {{
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            if (!query) return;

            // 1. Fast O(1) Exact Match Lookup
            if (fastSearchIndexMap.has(query)) {{
                selectNode(fastSearchIndexMap.get(query), true, true);
                return;
            }}

            // 2. Priority Starts-With Match
            const startMatch = nodes.find(n => n.label.toLowerCase().startsWith(query));
            if (startMatch) {{
                selectNode(startMatch, true, true);
                return;
            }}

            // 3. Substring Match
            const match = nodes.find(n => n.label.toLowerCase().includes(query) || n.path.toLowerCase().includes(query));
            if (match) {{
                selectNode(match, true, true);
            }}
        }}

        cacheNodeLabelMetrics();
        buildFastSearchIndex();
        resetZoom();
        requestAnimationFrame(render);
    </script>
</body>
</html>
"""
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        self.logger.info(f"Generated Multi-View HTML5 Canvas & WebGL Knowledge Graph -> {html_path}")
        return html_path

    def _find_browser_executable(self, browser_preference: str = "AUTO") -> Tuple[Optional[str], str]:
        """
        Detects native web browser executable path on system according to user preference.
        Returns (binary_path, browser_type_name).
        """
        import shutil
        pref_upper = (browser_preference or "AUTO").upper()

        if "AUTO" in pref_upper or "DEFAULT" in pref_upper:
            # System default browser delegated to platform handler / webbrowser module
            return None, "System Default Browser"

        if "CHROME" in pref_upper:
            candidates = [("google-chrome", "Google Chrome"), ("google-chrome-stable", "Google Chrome"), ("chrome.exe", "Google Chrome"), ("chrome", "Google Chrome"), ("chromium-browser", "Chromium"), ("chromium", "Chromium")]
        elif "FIREFOX" in pref_upper:
            candidates = [("firefox", "Mozilla Firefox"), ("firefox.exe", "Mozilla Firefox")]
        elif "BRAVE" in pref_upper:
            candidates = [("brave-browser", "Brave"), ("brave.exe", "Brave"), ("brave", "Brave")]
        elif "EDGE" in pref_upper:
            candidates = [("microsoft-edge", "Microsoft Edge"), ("msedge.exe", "Microsoft Edge"), ("msedge", "Microsoft Edge")]
        else:
            candidates = [
                ("google-chrome", "Google Chrome"),
                ("google-chrome-stable", "Google Chrome"),
                ("chrome.exe", "Google Chrome"),
                ("chrome", "Google Chrome"),
                ("msedge.exe", "Microsoft Edge"),
                ("msedge", "Microsoft Edge"),
                ("firefox", "Mozilla Firefox"),
                ("firefox.exe", "Mozilla Firefox"),
                ("chromium-browser", "Chromium"),
                ("chromium", "Chromium")
            ]

        for b_cmd, b_name in candidates:
            path = shutil.which(b_cmd)
            if path:
                return path, b_name

        # Standard Windows installation locations if not in PATH
        if sys.platform == "win32":
            win_dirs = [
                os.environ.get("PROGRAMFILES", "C:\\Program Files"),
                os.environ.get("PROGRAMFILES(X86)", "C:\\Program Files (x86)"),
                os.environ.get("LOCALAPPDATA", "")
            ]
            win_candidates = [
                (os.path.join("Google", "Chrome", "Application", "chrome.exe"), "Google Chrome"),
                (os.path.join("Microsoft", "Edge", "Application", "msedge.exe"), "Microsoft Edge"),
                (os.path.join("Mozilla Firefox", "firefox.exe"), "Mozilla Firefox"),
                (os.path.join("BraveSoftware", "Brave-Browser", "Application", "brave.exe"), "Brave"),
            ]
            for root_d in win_dirs:
                if not root_d:
                    continue
                for rel_p, b_name in win_candidates:
                    full_p = os.path.join(root_d, rel_p)
                    if os.path.isfile(full_p):
                        return full_p, b_name

        # Fallback to any installed browser if specific preference binary was not found
        fallback_browsers = [("google-chrome", "Google Chrome"), ("google-chrome-stable", "Google Chrome"), ("chrome.exe", "Google Chrome"), ("chrome", "Google Chrome"), ("msedge.exe", "Microsoft Edge"), ("msedge", "Microsoft Edge"), ("firefox", "Mozilla Firefox"), ("firefox.exe", "Mozilla Firefox")]
        for b_cmd, b_name in fallback_browsers:
            path = shutil.which(b_cmd)
            if path:
                return path, b_name

        return None, "Default System Browser"

    def open_graph_in_browser(self, gpu_preference: str = "AUTO", browser_preference: str = "AUTO", window_mode: str = "STANDALONE") -> str:
        """Generates graph_view.html and opens it directly in selected target (Native Qt6 Desktop Window / Chrome / Firefox) with GPU hardware offloading."""
        html_path = self.generate_html_graph()
        from pathlib import Path
        file_url = Path(html_path).resolve().as_uri()
        
        target_upper = (browser_preference or "AUTO").upper()
        
        # 1. Determine optimal baseline GPU environment using universal graphics runtime
        env, strategy_explanation = get_optimal_gpu_env(gpu_preference=gpu_preference, safe_mode=False)
        self.logger.info(f"Setting launch environment: {strategy_explanation}")

        launched = False

        # 2. Check if Native Qt6 Desktop Window is requested
        if "NATIVE" in target_upper or "QT" in target_upper or "LOCAL" in target_upper:
            viewer_script = os.path.join(os.path.dirname(__file__), "native_viewer.py")
            qt_supported = False
            try:
                import PyQt6.QtWebEngineWidgets  # noqa: F401
                qt_supported = True
            except (ImportError, Exception):
                qt_supported = False

            if qt_supported and os.path.exists(viewer_script):
                project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
                log_path = os.path.join(self.output_root, "native_viewer.log")

                tier_env, _ = get_optimal_gpu_env(gpu_preference=gpu_preference, safe_mode=True)
                tier_env["PYTHONPATH"] = project_root + os.pathsep + tier_env.get("PYTHONPATH", "")
                tier_env["QTWEBENGINE_DISABLE_SANDBOX"] = "1"
                tier_env["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox --disable-gpu-sandbox --ignore-gpu-blocklist --enable-webgl"
                
                # Sanitize conflicting variables
                tier_env.pop("__NV_PRIME_RENDER_OFFLOAD", None)
                tier_env.pop("__GLX_VENDOR_LIBRARY_NAME", None)
                tier_env.pop("DRI_PRIME", None)

                cmd = [sys.executable, viewer_script, html_path]
                popen_kwargs = {}
                if sys.platform != "win32":
                    popen_kwargs["start_new_session"] = True
                else:
                    popen_kwargs["creationflags"] = 0x00000200  # CREATE_NEW_PROCESS_GROUP
                try:
                    with open(log_path, "w", encoding="utf-8") as log_f:
                        subprocess.Popen(cmd, env=tier_env, stdout=log_f, stderr=log_f, **popen_kwargs)
                    launched = True
                    self.logger.info(f"🚀 Launched 100% Native Qt6 Desktop Window -> {html_path}")
                    return html_path
                except Exception as e:
                    self.logger.warning(f"Native Qt6 process launch failed: {e}. Falling back to browser...")
            else:
                self.logger.info("ℹ️ Native Qt6 WebEngine not installed; seamlessly falling back to hardware-accelerated Web Browser...")

        # 3. Direct web browser launch (Chrome / Firefox / Edge / Brave)
        if not launched:
            browser_exe, browser_name = self._find_browser_executable(browser_preference)
            if browser_exe:
                popen_kwargs = {}
                if sys.platform != "win32":
                    popen_kwargs["start_new_session"] = True
                else:
                    popen_kwargs["creationflags"] = 0x00000200

                # Chromium-based browsers support dedicated desktop app window mode
                is_chromium = any(k in browser_name for k in ["Chrome", "Chromium", "Brave", "Edge"])
                if is_chromium and window_mode == "STANDALONE":
                    cmd = [browser_exe, f"--app={file_url}"]
                else:
                    cmd = [browser_exe, "--new-window", file_url]

                try:
                    subprocess.Popen(cmd, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, **popen_kwargs)
                    launched = True
                    self.logger.info(f"🚀 Launched {browser_name} executable [{browser_exe}] with GPU offload environment.")
                except Exception as e:
                    self.logger.warning(f"Direct browser launch ({browser_exe}) failed: {e}")
                    if is_chromium and window_mode == "STANDALONE":
                        try:
                            fallback_cmd = [browser_exe, "--new-window", file_url]
                            subprocess.Popen(fallback_cmd, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, **popen_kwargs)
                            launched = True
                        except Exception as e2:
                            self.logger.warning(f"Fallback browser launch failed: {e2}")

        # 4. Fallback to webbrowser module
        if not launched:
            try:
                import webbrowser
                webbrowser.open(file_url)
                launched = True
            except Exception as e:
                self.logger.warning(f"Webbrowser module launch failed: {e}")

        # 5. Final fallback to xdg-open / open / startfile
        if not launched:
            try:
                if sys.platform.startswith("linux"):
                    subprocess.Popen(["xdg-open", file_url], env=env)
                elif sys.platform == "darwin":
                    subprocess.Popen(["open", file_url], env=env)
                elif sys.platform == "win32":
                    os.startfile(html_path)
            except Exception as e:
                self.logger.error(f"Failed to launch viewer: {e}")

        self.logger.info(f"Opened Knowledge Graph [{browser_preference} | Target GPU: {gpu_preference}]: {file_url}")
        return html_path
