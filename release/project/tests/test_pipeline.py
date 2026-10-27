"""
Integration and Unit Tests for Structured Wiki Generator Pipeline.
Tests hardware detection, Structured virtual directory tree initialization, register model schemas, and clean directory utilities.
"""

import os
import shutil
import pytest

from src.core.hardware_detector import detect_hardware_device
from src.generators.wiki_generator import StructuredWikiGenerator, KarpathyWikiGenerator
from src.parsers.register_parser import RegisterParser
from src.models.register_model import RegisterModel, RegisterBitField


def test_hardware_detection():
    """Verifies PyTorch / CUDA hardware detection return schema."""
    hw = detect_hardware_device()
    assert "gpu_available" in hw
    assert "device_name" in hw
    assert "vram_gb" in hw
    assert isinstance(hw["gpu_available"], bool)


def test_structured_wiki_directory_generation(tmp_path):
    """Verifies creation of exact 5-layer Structured Virtual Directory layout."""
    out_dir = str(tmp_path / "structured_test_wiki")
    generator = StructuredWikiGenerator(output_root=out_dir)
    generator.build_directory_structure()
    generator.create_schema_md()
    generator.populate_initial_markdown_pages()

    # Verify virtual directory layout (7-Layer architecture)
    assert os.path.exists(os.path.join(out_dir, "index.md"))
    assert os.path.exists(os.path.join(out_dir, "SCHEMA.md"))
    assert os.path.isdir(os.path.join(out_dir, "memory"))
    assert os.path.isdir(os.path.join(out_dir, "system"))
    assert os.path.isdir(os.path.join(out_dir, "core"))
    assert os.path.isdir(os.path.join(out_dir, "peripherals"))
    assert os.path.isdir(os.path.join(out_dir, "security"))
    assert os.path.isdir(os.path.join(out_dir, "figures"))
    assert os.path.isdir(os.path.join(out_dir, "tables"))
    assert os.path.isdir(os.path.join(out_dir, "registers_json"))
    assert os.path.isdir(os.path.join(out_dir, "assets"))

    # Verify key template files
    assert os.path.exists(os.path.join(out_dir, "memory", "memory_map.md"))
    assert os.path.exists(os.path.join(out_dir, "system", "rcc.md"))
    assert os.path.exists(os.path.join(out_dir, "system", "pwr.md"))
    assert os.path.exists(os.path.join(out_dir, "core", "nvic.md"))
    assert os.path.exists(os.path.join(out_dir, "peripherals", "adc.md"))
    assert os.path.exists(os.path.join(out_dir, "peripherals", "usart.md"))
    assert os.path.exists(os.path.join(out_dir, "peripherals", "gpio.md"))
    assert os.path.exists(os.path.join(out_dir, "security", "trustzone.md"))
    assert os.path.exists(os.path.join(out_dir, "security", "hash.md"))
    assert os.path.exists(os.path.join(out_dir, "figures", "hash_block_diagram.md"))
    assert os.path.exists(os.path.join(out_dir, "tables", "hash_digest_modes_table.md"))


def test_register_parser_json_schema(tmp_path):
    """Verifies register parser output and JSON schema validity."""
    out_dir = str(tmp_path / "structured_test_wiki")
    parser = RegisterParser(output_root=out_dir)
    sample_text = """
    ADC Control register (ADC_CR)
    Address offset: 0x08
    Reset value: 0x20000000
    Bit 0 ADEN: ADC Enable control bit
    Bit 2 ADSTART: ADC Start regular conversion
    """
    regs = parser.extract_registers_from_text(sample_text)
    assert len(regs) >= 1
    
    # Check JSON files created in registers_json/
    reg_json_dir = os.path.join(out_dir, "registers_json")
    assert os.path.exists(reg_json_dir)
    assert os.path.exists(os.path.join(reg_json_dir, "ADC_CR.json"))


def test_clean_output_directory_utility(tmp_path):
    """Verifies clean output directory purges files completely (including raw/) and supports skeleton rebuild."""
    out_dir = str(tmp_path / "structured_test_wiki")
    generator = StructuredWikiGenerator(output_root=out_dir)
    generator.build_directory_structure()

    # Create dummy artifact file and dummy raw file
    dummy_file = os.path.join(out_dir, "peripherals", "dummy.txt")
    with open(dummy_file, "w") as f:
        f.write("dummy text")
    raw_pdf = os.path.join(out_dir, "raw", "sample.pdf")
    with open(raw_pdf, "w") as f:
        f.write("sample pdf")
    assert os.path.exists(dummy_file)
    assert os.path.exists(raw_pdf)

    # 1. Clean directory with full complete purge (default: purge_raw=True, recreate_skeleton=False)
    generator.clean_output_directory(purge_raw=True, recreate_skeleton=False)
    assert not os.path.exists(dummy_file)
    assert not os.path.exists(raw_pdf)
    assert not os.path.exists(os.path.join(out_dir, "raw"))
    assert len(os.listdir(out_dir)) == 0  # Completely empty!

    # 2. Clean directory with recreate_skeleton=True
    generator.clean_output_directory(purge_raw=True, recreate_skeleton=True)
    assert os.path.exists(os.path.join(out_dir, "index.md"))
    assert os.path.exists(os.path.join(out_dir, "SCHEMA.md"))
    assert os.path.exists(os.path.join(out_dir, "peripherals"))
    assert not os.path.exists(dummy_file)
    assert not os.path.exists(raw_pdf)



def test_descending_bitfield_extraction(tmp_path):
    """Verifies descending bit range syntax (Bits 15:8) yields valid bit_offset and positive bit_width."""
    out_dir = str(tmp_path / "structured_test_wiki")
    parser = RegisterParser(output_root=out_dir)
    sample_text = """
    Bits 15:8 SQ1: 1st conversion in regular sequence
    Bits 4:0 L: Regular sequence length
    """
    fields = parser._extract_bitfields_from_text(sample_text)
    
    sq1_field = [f for f in fields if f.name == "SQ1"][0]
    assert sq1_field.bit_offset == 8
    assert sq1_field.bit_width == 8

    l_field = [f for f in fields if f.name == "L"][0]
    assert l_field.bit_offset == 0
    assert l_field.bit_width == 5


def test_knowledge_graph_visualizer(tmp_path):
    """Verifies KnowledgeGraphVisualizer extracts nodes and edges from Structured Wiki structure."""
    out_dir = str(tmp_path / "structured_test_wiki")
    generator = StructuredWikiGenerator(output_root=out_dir)
    generator.clean_output_directory()
    generator.populate_initial_markdown_pages()

    from src.visualizer.graph_visualizer import KnowledgeGraphVisualizer
    viz = KnowledgeGraphVisualizer(output_root=out_dir)
    nodes, edges, parse_elapsed = viz.build_graph_data()
    
    assert len(nodes) > 10
    assert len(edges) > 5
    assert parse_elapsed >= 0.0

    html_path = viz.generate_html_graph()
    assert os.path.exists(html_path)


def test_corpus_auditor_quality_score(tmp_path):
    """Verifies Independent StructuredWikiAuditor achieves >= 95% health score with zero broken links and valid schemas."""
    out_dir = str(tmp_path / "structured_test_wiki")
    generator = StructuredWikiGenerator(output_root=out_dir)
    generator.clean_output_directory()
    generator.populate_initial_markdown_pages()

    from src.parsers.wiki_auditor import StructuredWikiAuditor
    auditor = StructuredWikiAuditor(wiki_root=out_dir)
    audit_res = auditor.run_full_audit()

    assert audit_res["overall_health_score"] >= 95.0
    assert audit_res["registers"]["score"] >= 95.0
    assert audit_res["links"]["broken_links"] == 0
    assert os.path.exists(audit_res["report_path"])


def test_document_classification_and_rejection(tmp_path):
    """Verifies document classifier correctly accepts RMs and rejects Datasheets, Errata, and Programming Manuals."""
    from src.core.mcu_detector import classify_st_document, validate_reference_manual

    # Test RM classification
    rm_dummy = str(tmp_path / "rm0440-stm32g4-reference-manual.pdf")
    with open(rm_dummy, "w") as f:
        f.write("%PDF-1.4 dummy RM content")
    c_rm = classify_st_document(rm_dummy)
    assert c_rm["is_reference_manual"] is True
    assert c_rm["doc_type"] == "REFERENCE_MANUAL"

    # Test Datasheet classification
    ds_dummy = str(tmp_path / "stm32g474ve-datasheet.pdf")
    with open(ds_dummy, "w") as f:
        f.write("%PDF-1.4 dummy DS content")
    c_ds = classify_st_document(ds_dummy)
    assert c_ds["is_reference_manual"] is False
    assert c_ds["doc_type"] == "DATASHEET"

    # Test Errata Sheet classification
    es_dummy = str(tmp_path / "es0491-errata-sheet.pdf")
    with open(es_dummy, "w") as f:
        f.write("%PDF-1.4 dummy ES content")
    c_es = classify_st_document(es_dummy)
    assert c_es["is_reference_manual"] is False
    assert c_es["doc_type"] == "ERRATA_SHEET"

    # Test Programming Manual classification
    pm_dummy = str(tmp_path / "pm0253-programming-manual.pdf")
    with open(pm_dummy, "w") as f:
        f.write("%PDF-1.4 dummy PM content")
    c_pm = classify_st_document(pm_dummy)
    assert c_pm["is_reference_manual"] is False
    assert c_pm["doc_type"] == "PROGRAMMING_MANUAL"

    # Test validate_reference_manual auto-resolution of sibling RM
    is_valid, msg, resolved = validate_reference_manual(ds_dummy)
    assert is_valid is False
    assert resolved == rm_dummy  # Found sibling RM!

    # Test rejection when isolated without sibling RM
    iso_dir = tmp_path / "isolated"
    iso_dir.mkdir()
    iso_ds = str(iso_dir / "isolated-datasheet.pdf")
    with open(iso_ds, "w") as f:
        f.write("%PDF-1.4 dummy DS")
    is_valid_iso, msg_iso, resolved_iso = validate_reference_manual(iso_ds)
    assert is_valid_iso is False
    assert resolved_iso is None  # Completely rejected!


def test_vector_artwork_extractor_and_validation(tmp_path):
    """Verifies VectorArtworkExtractor validates SVG schemas, path counts, and builds audit reports."""
    from src.parsers.vector_extractor import VectorArtworkExtractor

    out_dir = str(tmp_path / "svg_test_wiki")
    extractor = VectorArtworkExtractor(output_root=out_dir)

    # 1. Test SVG Validation on a mock vector schematic
    valid_svg = out_dir + "/figures/mock_clock_tree.svg"
    os.makedirs(os.path.dirname(valid_svg), exist_ok=True)
    with open(valid_svg, "w", encoding="utf-8") as f:
        paths = "\n".join([f'<path d="M {i} {i} L {i+10} {i+10}" stroke="#38bdf8"/>' for i in range(30)])
        f.write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
            <rect width="800" height="600" fill="#0f172a"/>
            <text x="20" y="30" fill="#ffffff">Mock Clock Tree Architecture</text>
            {paths}
        </svg>''')

    val_res = extractor.validate_svg_asset(valid_svg)
    assert val_res["status"] == "PASSED"
    assert val_res["score"] == 100.0
    assert val_res["path_count"] >= 30
    assert val_res["has_viewbox"] is True

    # 2. Test Audit Report Generation
    manifest = {
        "total_extracted": 1,
        "multi_page_diagrams": 0,
        "figures": [{
            "figure_id": "MOCK_CLOCK_TREE",
            "title": "Clock Tree Architecture",
            "page_number": 93,
            "is_multi_page": False,
            "svg_filename": "mock_clock_tree.svg",
            "relative_path": "figures/mock_clock_tree.svg",
            "validation": val_res
        }]
    }
    report_path = extractor.generate_svg_audit_report(manifest)
    assert os.path.exists(report_path)
    with open(report_path, "r", encoding="utf-8") as f_rep:
        assert "Vector Artwork" in f_rep.read()


def test_parameterized_multi_block_registers_and_plausibility(tmp_path):
    """Verifies that RegisterParser handles parameterized ST registers (e.g., SAI_xCR1) and rejects spurious tokens."""
    out_dir = str(tmp_path / "sai_test_wiki")
    parser = RegisterParser(output_root=out_dir)

    # 1. Multi-block parameterized register text
    sample_text = """
    # 29.17 SAI registers
    29.17.1 SAI x configuration register 1 (SAI_xCR1) where x is A or B
    Address offset: Block A: 0x004
    Address offset: Block B: 0x024
    Reset value: 0x00000000
    Bit 0 MODE[1:0]: Audio block mode
    Bit 2 NODIV: No divider
    Bit 16 MCKDIV[3:0]: Master clock divider

    29.17.2 SAI x status register (SAI_xSR) where x is A or B
    Address offset: Block A: 0x018
    Address offset: Block B: 0x038
    Reset value: 0x00000008
    Bit 0 OVRUDR: Overrun / underrun
    Bit 1 MUTEDET: Mute detection
    """
    regs = parser.extract_peripheral_registers(sample_text, "sai", "Serial Audio Interface (SAI)")
    reg_names = [r.register_name for r in regs]
    
    assert "SAI_ACR1" in reg_names
    assert "SAI_BCR1" in reg_names
    assert "SAI_ASR" in reg_names
    assert "SAI_BSR" in reg_names

    acr1 = next(r for r in regs if r.register_name == "SAI_ACR1")
    assert int(acr1.address_offset, 16) == 0x004
    assert len(acr1.bit_fields) >= 3

    bcr1 = next(r for r in regs if r.register_name == "SAI_BCR1")
    assert int(bcr1.address_offset, 16) == 0x024

    # 2. Test Plausibility Rejection
    # Should reject bare peripheral and bare instances
    assert parser._is_plausible_register_name("SAI", "SAI") is False
    assert parser._is_plausible_register_name("ADC", "ADC") is False
    assert parser._is_plausible_register_name("ADC1", "ADC") is False
    assert parser._is_plausible_register_name("GPIOA", "GPIO") is False
    # Should reject trailing/leading underscores
    assert parser._is_plausible_register_name("SAI_", "SAI") is False
    assert parser._is_plausible_register_name("GPIO_", "GPIO") is False
    # Should reject page numbers and hex literals
    assert parser._is_plausible_register_name("1413OTG_HS_GRXSTSP", "OTG_HS") is False
    assert parser._is_plausible_register_name("0XB0", "PERIPH") is False
    assert parser._is_plausible_register_name("17XX", "PERIPH") is False
    # Should reject clock/signal lines
    assert parser._is_plausible_register_name("SAI_CK_X", "SAI") is False
    assert parser._is_plausible_register_name("SAI_CK", "SAI") is False
    # Should reject stopwords
    assert parser._is_plausible_register_name("CONTINUED", "PERIPH") is False
    assert parser._is_plausible_register_name("COUNTER", "PERIPH") is False
    assert parser._is_plausible_register_name("OUTPUT", "PERIPH") is False

    # 3. Legitimate registers must pass
    assert parser._is_plausible_register_name("SAI_ACR1", "SAI") is True
    assert parser._is_plausible_register_name("SAI_BDR", "SAI") is True
    assert parser._is_plausible_register_name("RCC_CR", "RCC") is True
    assert parser._is_plausible_register_name("TIM_CR1", "TIMERS") is True

