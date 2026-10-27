"""
Main entry point for STM32 Karpathy-Wiki Generator application.
Supports both GUI and headless CLI execution modes with per-document isolated directory structures and raw storage.
"""

import sys
import os
import argparse

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.gui.app import StructuredWikiApp, KarpathyWikiApp
from src.core.checkpoint_manager import CheckpointManager
from src.core.logger import WikiLogger
from src.generators.wiki_generator import StructuredWikiGenerator, KarpathyWikiGenerator
from src.generators.cross_linker import CrossLinkerEngine
from src.parsers.docling_extractor import DoclingPDFExtractor
from src.parsers.register_parser import RegisterParser


def run_headless_cli(ref_pdf: str, output_dir: str, clean_first: bool = False) -> None:
    """Executes ingestion pipeline in headless CLI mode."""
    logger = WikiLogger(os.path.join(output_dir, "wiki", "log.md"))
    wiki_gen = StructuredWikiGenerator(output_root=output_dir, logger=logger)

    if clean_first:
        logger.info(f"Cleaning output directory: {output_dir}")
        wiki_gen.clean_output_directory()

    logger.info("Starting Headless Ingestion Pipeline...")

    chk_mgr = CheckpointManager(output_root=output_dir, logger=logger)
    linker = CrossLinkerEngine(output_root=output_dir, logger=logger)
    parser = RegisterParser(output_root=output_dir, logger=logger)
    extractor = DoclingPDFExtractor(logger=logger)

    wiki_gen.build_directory_structure()
    wiki_gen.create_schema_md()
    wiki_gen.populate_initial_markdown_pages()

    file_map = {"ref_manual": ref_pdf}
    wiki_gen.copy_raw_documents(file_map)

    raw_text = extractor.extract_pdf_with_streaming_progress(ref_pdf, max_pages=None)
    regs = parser.extract_registers_from_text(raw_text)

    linker.generate_register_index()
    linker.generate_backlinks_map()

    total_pages = extractor.get_pdf_page_count(ref_pdf)
    chk_mgr.update_file_status("ref_manual", "Reference Manual", ref_pdf, total_pages, total_pages)
    chk_mgr.mark_completed()
    print(f"\n[SUCCESS] Headless CLI Processing Complete. Output saved to: {output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description="STM32 Structured Wiki Generator")
    parser.add_argument("--cli", action="store_true", help="Run in headless CLI mode")
    parser.add_argument("--ref-manual", type=str, help="Path to Reference Manual PDF")
    parser.add_argument("--output-dir", type=str, default="artifacts/output/structured-wiki", help="Output directory path")
    parser.add_argument("--clean", action="store_true", help="Purge output directory before starting")

    args = parser.parse_args()

    if args.cli:
        if not args.ref_manual:
            print("[ERROR] Headless CLI mode requires --ref-manual <path_to_pdf>")
            sys.exit(1)
        run_headless_cli(args.ref_manual, args.output_dir, clean_first=args.clean)
    else:
        app = StructuredWikiApp()
        app.mainloop()


if __name__ == "__main__":
    main()
