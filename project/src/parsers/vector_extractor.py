"""
Universal Vector Artwork Extractor, Multi-Page Diagram Stitcher & SVG Validator.
Extracts native, infinite-resolution vector SVGs directly from any MCU Reference Manual PDF,
stitches multi-page schematics (e.g. Clock Tree, Bus Matrix), and performs evidence-based validation.
Works across ALL MCU families (STM32F1, STM32G4, STM32H7, STM32U3, etc.) without hardcoding.
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from typing import Dict, Any, List, Optional, Tuple

from ..core.logger import WikiLogger


class VectorArtworkExtractor:
    """Extracts, stitches, and validates native vector SVG artwork from MCU Reference Manuals."""

    def __init__(self, output_root: str, logger: Optional[WikiLogger] = None) -> None:
        self.output_root = os.path.abspath(output_root)
        self.figures_dir = os.path.join(self.output_root, "figures")
        self.assets_dir = os.path.join(self.output_root, "assets")
        self.logger = logger or WikiLogger()
        os.makedirs(self.figures_dir, exist_ok=True)
        os.makedirs(self.assets_dir, exist_ok=True)

    def extract_figures_from_pdf(self, pdf_path: str, max_figures: int = 25) -> Dict[str, Any]:
        """
        Dynamically scans any MCU Reference Manual PDF for key technical schematics
        (Clock Tree, Bus Matrix, Power Distribution, Waveforms) and extracts them as native SVGs.
        """
        if not os.path.exists(pdf_path):
            self.logger.error(f"PDF file not found: {pdf_path}")
            return {"total_extracted": 0, "figures": [], "error": "File not found"}

        try:
            import pymupdf
        except ImportError:
            try:
                import fitz as pymupdf
            except ImportError:
                self.logger.error("PyMuPDF / fitz is not installed.")
                return {"total_extracted": 0, "figures": [], "error": "PyMuPDF not installed"}

        doc = pymupdf.open(pdf_path)
        total_pages = len(doc)
        self.logger.info(f"Scanning {total_pages} pages in {os.path.basename(pdf_path)} for vector artwork...")

        extracted_figures: List[Dict[str, Any]] = []
        clock_tree_pages: List[int] = []
        bus_matrix_pages: List[int] = []

        # Target figure detection patterns
        patterns = [
            (r'figure\s+\d+[\.:\s]+(.*clock\s+tree.*)', "CLOCK_TREE", "Clock Tree Architecture"),
            (r'figure\s+\d+[\.:\s]+(.*bus\s+matrix.*|.*system\s+architecture.*)', "BUS_MATRIX", "System Bus Matrix Architecture"),
            (r'figure\s+\d+[\.:\s]+(.*power\s+supply.*|.*power\s+tree.*)', "POWER_TREE", "Power Supply Architecture"),
            (r'figure\s+\d+[\.:\s]+(.*memory\s+map.*)', "MEMORY_MAP_FIG", "System Memory Map Schematic"),
            (r'figure\s+\d+[\.:\s]+(.*dma.*interconnect.*|.*dma.*block.*)', "DMA_BLOCK", "DMA Controller Block Diagram"),
            (r'figure\s+\d+[\.:\s]+(.*timer.*waveform.*|.*pwm.*timing.*)', "TIMER_WAVEFORM", "Timer Signal Waveform Diagram"),
            (r'figure\s+\d+[\.:\s]+(.*adc.*block\s+diagram.*)', "ADC_BLOCK", "ADC Functional Block Diagram"),
            (r'figure\s+\d+[\.:\s]+(.*usart.*block\s+diagram.*)', "USART_BLOCK", "USART Functional Block Diagram"),
        ]

        found_categories = set()

        for page_idx in range(total_pages):
            page = doc[page_idx]
            page_text = page.get_text()
            if not page_text or len(page_text.strip()) < 20:
                continue

            # Skip Table of Contents / List of figures pages (detected by dot leaders and low drawing count)
            if re.search(r'\.\s*\.\s*\.\s*\.\s*\d+', page_text):
                continue

            drawings = page.get_drawings()
            if len(drawings) < 20:
                continue  # Skip text-only pages without real vector schematic drawings

            # Check for figure title patterns
            for pat, cat_id, default_title in patterns:
                m = re.search(pat, page_text, re.IGNORECASE)
                if m:
                    raw_title = m.group(1).strip() if m.groups() else default_title
                    clean_title = re.sub(r'[\r\n\t]+', ' ', raw_title).strip()
                    clean_title = re.sub(r'\s+', ' ', clean_title)

                    if cat_id == "CLOCK_TREE":
                        clock_tree_pages.append(page_idx)
                    elif cat_id == "BUS_MATRIX":
                        bus_matrix_pages.append(page_idx)

                    # Extract single page SVG if not yet extracted for this category
                    fig_key = f"{cat_id}_{page_idx+1}"
                    if cat_id not in found_categories or len(extracted_figures) < max_figures:
                        svg_filename = f"fig_{cat_id.lower()}_p{page_idx+1}.svg"
                        svg_path = os.path.join(self.figures_dir, svg_filename)

                        try:
                            svg_content = page.get_svg_image()
                            with open(svg_path, "w", encoding="utf-8") as f_svg:
                                f_svg.write(svg_content)

                            val_res = self.validate_svg_asset(svg_path)
                            extracted_figures.append({
                                "figure_id": fig_key,
                                "category": cat_id,
                                "title": f"{default_title}: {clean_title[:80]}",
                                "page_number": page_idx + 1,
                                "is_multi_page": False,
                                "svg_filename": svg_filename,
                                "svg_path": svg_path,
                                "relative_path": f"figures/{svg_filename}",
                                "validation": val_res
                            })
                            found_categories.add(cat_id)
                            self.logger.info(f"Extracted vector SVG: {svg_filename} (Page {page_idx+1}, {len(drawings)} drawings) - {val_res['status']}")
                        except Exception as e:
                            self.logger.warning(f"Could not extract SVG on page {page_idx+1}: {e}")

        # Multi-Page Diagram Stitching for Clock Tree (if multi-page found)
        if len(clock_tree_pages) >= 2:
            self.logger.info(f"Multi-page Clock Tree detected across pages: {[p+1 for p in clock_tree_pages]}")
            stitched_svg = self.stitch_multi_page_svg(doc, clock_tree_pages[:3], "fig_rcc_clock_tree_panoramic.svg", "Panoramic Clock Tree Architecture")
            if stitched_svg:
                extracted_figures.insert(0, stitched_svg)

        # Multi-Page Diagram Stitching for Bus Matrix (if multi-page found)
        if len(bus_matrix_pages) >= 2:
            self.logger.info(f"Multi-page Bus Matrix detected across pages: {[p+1 for p in bus_matrix_pages]}")
            stitched_svg = self.stitch_multi_page_svg(doc, bus_matrix_pages[:2], "fig_bus_matrix_panoramic.svg", "Panoramic Bus Matrix Interconnect")
            if stitched_svg:
                extracted_figures.insert(1, stitched_svg)

        doc.close()

        # Save manifest
        manifest_path = os.path.join(self.output_root, "vector_figures_manifest.json")
        summary_data = {
            "total_extracted": len(extracted_figures),
            "multi_page_diagrams": len([f for f in extracted_figures if f.get("is_multi_page")]),
            "figures": extracted_figures
        }
        with open(manifest_path, "w", encoding="utf-8") as mf:
            json.dump(summary_data, mf, indent=2)

        # Generate HTML Visual Report
        self.generate_svg_audit_report(summary_data)

        return summary_data

    def stitch_multi_page_svg(
        self,
        doc: Any,
        pages: List[int],
        output_filename: str,
        diagram_title: str
    ) -> Optional[Dict[str, Any]]:
        """
        Stitches multiple consecutive or related vector PDF pages into a single,
        unified panoramic SVG with aligned coordinate systems.
        """
        try:
            page_svgs = []
            widths = []
            heights = []

            for p_idx in pages:
                page = doc[p_idx]
                rect = page.rect
                widths.append(rect.width)
                heights.append(rect.height)
                svg_data = page.get_svg_image()
                page_svgs.append((p_idx + 1, rect.width, rect.height, svg_data))

            # Determine layout orientation:
            # If pages are wide (landscape), stitch vertically; if tall (portrait), stitch side-by-side (horizontally)
            avg_aspect = sum(w / h for w, h in zip(widths, heights)) / len(widths)
            is_horizontal = avg_aspect < 1.0  # Portrait pages look great stitched horizontally

            if is_horizontal:
                total_width = sum(widths)
                max_height = max(heights)
                stitched_xml = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {total_width:.2f} {max_height:.2f}" width="{total_width:.2f}" height="{max_height:.2f}">']
                stitched_xml.append(f'<defs><style>.stitched-bg {{ fill: #0f172a; }} .page-label {{ font-family: Inter, Arial; font-size: 14px; fill: #38bdf8; font-weight: bold; }}</style></defs>')
                stitched_xml.append(f'<rect width="{total_width:.2f}" height="{max_height:.2f}" class="stitched-bg"/>')

                cur_x = 0.0
                for p_num, w, h, s_data in page_svgs:
                    # Extract inner SVG body
                    inner = self._extract_svg_inner_content(s_data)
                    stitched_xml.append(f'<g transform="translate({cur_x:.2f}, 0)">')
                    stitched_xml.append(f'<text x="20" y="30" class="page-label">Part {pages.index(p_num-1)+1} (Page {p_num})</text>')
                    stitched_xml.append(inner)
                    stitched_xml.append('</g>')
                    cur_x += w
            else:
                total_height = sum(heights)
                max_width = max(widths)
                stitched_xml = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {max_width:.2f} {total_height:.2f}" width="{max_width:.2f}" height="{total_height:.2f}">']
                stitched_xml.append(f'<defs><style>.stitched-bg {{ fill: #0f172a; }} .page-label {{ font-family: Inter, Arial; font-size: 14px; fill: #38bdf8; font-weight: bold; }}</style></defs>')
                stitched_xml.append(f'<rect width="{max_width:.2f}" height="{total_height:.2f}" class="stitched-bg"/>')

                cur_y = 0.0
                for p_num, w, h, s_data in page_svgs:
                    inner = self._extract_svg_inner_content(s_data)
                    stitched_xml.append(f'<g transform="translate(0, {cur_y:.2f})">')
                    stitched_xml.append(f'<text x="20" y="{cur_y + 30:.2f}" class="page-label">Part {pages.index(p_num-1)+1} (Page {p_num})</text>')
                    stitched_xml.append(inner)
                    stitched_xml.append('</g>')
                    cur_y += h

            stitched_xml.append('</svg>')
            final_content = "\n".join(stitched_xml)

            out_path = os.path.join(self.figures_dir, output_filename)
            with open(out_path, "w", encoding="utf-8") as f_out:
                f_out.write(final_content)

            val_res = self.validate_svg_asset(out_path)
            self.logger.info(f"Successfully stitched multi-page SVG: {output_filename} ({len(pages)} pages) -> {val_res['status']}")

            return {
                "figure_id": f"PANORAMIC_{output_filename.upper().replace('.SVG', '')}",
                "category": "PANORAMIC",
                "title": f"Panoramic {diagram_title} (Stitched Pages: {', '.join(str(p+1) for p in pages)})",
                "page_number": pages[0] + 1,
                "is_multi_page": True,
                "source_pages": [p + 1 for p in pages],
                "svg_filename": output_filename,
                "svg_path": out_path,
                "relative_path": f"figures/{output_filename}",
                "validation": val_res
            }
        except Exception as e:
            self.logger.error(f"Failed to stitch multi-page SVG {output_filename}: {e}")
            return None

    def _extract_svg_inner_content(self, svg_str: str) -> str:
        """Extracts content between <svg ...> and </svg> tags."""
        start = svg_str.find('>')
        end = svg_str.rfind('</svg>')
        if start != -1 and end != -1:
            return svg_str[start+1:end].strip()
        return svg_str

    def validate_svg_asset(self, svg_path: str) -> Dict[str, Any]:
        """
        Performs rigorous evidence-based validation on an SVG asset:
        - XML parse validity
        - ViewBox / Dimension presence
        - Path, Line, Rect, and Text element counts
        - File size bounds
        """
        if not os.path.exists(svg_path):
            return {"status": "FAILED", "score": 0.0, "reason": "File missing"}

        file_size = os.path.getsize(svg_path)
        if file_size < 500:
            return {"status": "FAILED", "score": 10.0, "reason": f"File too small ({file_size} bytes)"}

        try:
            tree = ET.parse(svg_path)
            root = tree.getroot()

            # Read raw SVG text for namespace-agnostic entity counting
            with open(svg_path, "r", encoding="utf-8", errors="ignore") as f_raw:
                raw_svg = f_raw.read()

            path_count = len(re.findall(r'<path[\s>]', raw_svg, re.IGNORECASE))
            use_count = len(re.findall(r'<use[\s>]', raw_svg, re.IGNORECASE))
            line_count = len(re.findall(r'<line[\s>]', raw_svg, re.IGNORECASE))
            rect_count = len(re.findall(r'<rect[\s>]', raw_svg, re.IGNORECASE))
            text_count = len(re.findall(r'<text[\s>]', raw_svg, re.IGNORECASE))
            circle_count = len(re.findall(r'<circle[\s>]', raw_svg, re.IGNORECASE))
            g_count = len(re.findall(r'<g[\s>]', raw_svg, re.IGNORECASE))

            total_elements = path_count + use_count + line_count + rect_count + text_count + circle_count

            has_viewbox = "viewBox" in root.attrib or ("width" in root.attrib and "height" in root.attrib) or ("viewBox" in raw_svg)

            if total_elements < 15:
                status = "WARNING"
                score = 65.0
                evidence = f"Few vector elements ({total_elements}). Schematic may be minimal."
            else:
                status = "PASSED"
                score = 100.0
                evidence = f"Pristine vector schematic: {total_elements} vector elements ({path_count} paths, {use_count} symbol/glyphs, {line_count} lines, {rect_count} rects, {text_count} text tags). Infinite resolution vector SVG ({file_size/1024:.1f} KB)."

            return {
                "status": status,
                "score": score,
                "file_size_bytes": file_size,
                "path_count": path_count,
                "use_count": use_count,
                "line_count": line_count,
                "rect_count": rect_count,
                "text_count": text_count,
                "total_elements": total_elements,
                "has_viewbox": has_viewbox,
                "evidence": evidence
            }
        except ET.ParseError as e:
            return {
                "status": "FAILED",
                "score": 0.0,
                "reason": f"XML Parse Error: {e}",
                "evidence": "Invalid XML structure"
            }

    def generate_svg_audit_report(self, manifest_data: Dict[str, Any]) -> str:
        """Generates an evidence-based HTML audit report for all vector SVG figures."""
        figures = manifest_data.get("figures", [])
        report_path = os.path.join(self.output_root, "svg_validation_report.html")

        cards_html = []
        for fig in figures:
            v = fig.get("validation", {})
            status = v.get("status", "UNKNOWN")
            status_color = "#10b981" if status == "PASSED" else ("#f59e0b" if status == "WARNING" else "#ef4444")
            multi_badge = '<span style="background: #6366f1; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; margin-left: 8px;">Multi-Page Panoramic</span>' if fig.get("is_multi_page") else ''

            card = f"""
            <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 18px; margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; margin-bottom: 12px;">
                    <div>
                        <strong style="font-size: 16px; color: #f8fafc;">{fig.get('title')}</strong> {multi_badge}
                        <div style="color: #94a3b8; font-size: 12px; margin-top: 4px;">Source: Page {fig.get('page_number')} | File: <code>{fig.get('svg_filename')}</code></div>
                    </div>
                    <div>
                        <span style="background: {status_color}; color: #000; font-weight: bold; padding: 4px 12px; border-radius: 12px; font-size: 12px;">{status} ({v.get('score', 0):.0f}%)</span>
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 14px; font-size: 12px; color: #cbd5e1;">
                    <div style="background: rgba(15, 23, 42, 0.6); padding: 8px; border-radius: 6px;">Paths: <strong style="color: #38bdf8;">{v.get('path_count', 0)}</strong></div>
                    <div style="background: rgba(15, 23, 42, 0.6); padding: 8px; border-radius: 6px;">Lines: <strong style="color: #38bdf8;">{v.get('line_count', 0)}</strong></div>
                    <div style="background: rgba(15, 23, 42, 0.6); padding: 8px; border-radius: 6px;">Rects: <strong style="color: #38bdf8;">{v.get('rect_count', 0)}</strong></div>
                    <div style="background: rgba(15, 23, 42, 0.6); padding: 8px; border-radius: 6px;">Text Labels: <strong style="color: #38bdf8;">{v.get('text_count', 0)}</strong></div>
                </div>
                <div style="background: #020617; border-radius: 8px; padding: 12px; text-align: center; max-height: 400px; overflow: auto;">
                    <img src="{fig.get('relative_path')}" alt="{fig.get('title')}" style="max-width: 100%; height: auto; border-radius: 4px;" />
                </div>
                <div style="color: #94a3b8; font-size: 12px; margin-top: 8px;"><strong>Validation Evidence:</strong> {v.get('evidence', '')}</div>
            </div>
            """
            cards_html.append(card)

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Karpathy-Wiki Vector SVG Artwork Validation Report</title>
    <style>
        body {{
            background-color: #0b1120;
            color: #f1f5f9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 30px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            background: linear-gradient(135deg, #1e293b, #0f172a);
            border: 1px solid rgba(56, 189, 248, 0.3);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
        }}
        h1 {{ margin: 0 0 10px 0; font-size: 24px; color: #38bdf8; }}
        .badge {{
            display: inline-block;
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid #38bdf8;
            color: #38bdf8;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin-right: 8px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎨 Vector Artwork & Multi-Page SVG Validation Report</h1>
            <p style="color: #94a3b8; margin: 0 0 14px 0;">Rigorous evidence-based verification of extracted native vector schematics, clock trees, waveforms, and stitched panoramic figures.</p>
            <div>
                <span class="badge">Total Vector Figures: {len(figures)}</span>
                <span class="badge">Multi-Page Panoramic Diagrams: {manifest_data.get('multi_page_diagrams', 0)}</span>
                <span class="badge" style="background: rgba(16, 185, 129, 0.2); border-color: #10b981; color: #10b981;">Extraction Engine: PyMuPDF Native Vector Stream</span>
            </div>
        </div>

        <div>
            {''.join(cards_html) if cards_html else '<p style="color: #94a3b8;">No vector figures extracted yet. Run extraction on a valid Reference Manual.</p>'}
        </div>
    </div>
</body>
</html>
"""
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        self.logger.info(f"Generated Vector SVG Audit Report: {report_path}")
        return report_path
