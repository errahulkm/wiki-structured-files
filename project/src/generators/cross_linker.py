"""
Hyper-Accurate Cross-Linker and Backlinks Engine.
Generates register indexes and bidirectional markdown cross-reference maps.
"""

import os
import json
import re
from typing import Dict, List, Set, Tuple, Optional

from ..core.logger import WikiLogger


class CrossLinkerEngine:
    """Scans wiki markdown and register JSONs to construct bidirectional link topologies."""

    def __init__(self, output_root: str = "artifacts/output/structured-wiki",
                 logger: Optional[WikiLogger] = None) -> None:
        """Initializes cross linker with root output directory."""
        self.output_root = os.path.abspath(output_root)
        self.wiki_dir = self.output_root
        self.registers_dir = os.path.join(self.output_root, "registers_json")
        self.logger = logger or WikiLogger()

    def generate_register_index(self) -> str:
        """Generates master register index catalog."""
        target_file = os.path.join(self.output_root, "register_index.md")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        register_files = []
        if os.path.exists(self.registers_dir):
            for fname in sorted(os.listdir(self.registers_dir)):
                if fname.endswith(".json"):
                    full_path = os.path.join(self.registers_dir, fname)
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        reg_name = data.get("register_name", fname.replace(".json", ""))
                        offset = data.get("address_offset", "0x00")
                        peripheral = data.get("peripheral", "PERIPHERAL")
                        register_files.append((reg_name, fname, offset, peripheral))
                    except Exception:
                        reg_name = fname.replace(".json", "")
                        register_files.append((reg_name, fname, "0x00", "UNKNOWN"))

        lines = [
            "# Master Register JSON Catalog & Index\n",
            "This index lists all hardware register specifications isolated into JSON schema format.\n",
            "| Peripheral | Register Name | Address Offset | JSON Specification Link |",
            "| :--- | :--- | :--- | :--- |"
        ]

        for reg_name, fname, offset, peripheral in register_files:
            rel_link = f"registers_json/{fname}"
            lines.append(f"| {peripheral} | `{reg_name}` | `{offset}` | [{fname}]({rel_link}) |")

        content = "\n".join(lines) + "\n"
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)

        self.logger.info(f"Generated Master Register Index: {len(register_files)} register JSON files linked.")
        return target_file

    def generate_backlinks_map(self) -> str:
        """Scans all Markdown documents in output_root and builds backlinks.md."""
        backlinks_file = os.path.join(self.output_root, "backlinks.md")
        link_graph: Dict[str, List[str]] = {}

        # Scan all .md files
        for root, _, files in os.walk(self.output_root):
            for file in files:
                if file.endswith(".md") and file != "backlinks.md":
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.output_root)
                    
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            text = f.read()
                        
                        # Match markdown links: [text](target.md) or [text](target.json)
                        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)
                        for _, target in links:
                            clean_target = target.split("#")[0]
                            if clean_target not in link_graph:
                                link_graph[clean_target] = []
                            link_graph[clean_target].append(rel_path)
                    except Exception:
                        continue

        lines = [
            "# Structured Wiki Bidirectional Backlinks Map\n",
            "This document tracks incoming cross-references across all knowledge base nodes.\n"
        ]

        for target, sources in sorted(link_graph.items()):
            lines.append(f"### Target Node: `{target}`")
            for src in set(sources):
                lines.append(f"- Referenced by: [{src}]({src})")
            lines.append("")

        content = "\n".join(lines) + "\n"
        with open(backlinks_file, "w", encoding="utf-8") as f:
            f.write(content)

        self.logger.info("Generated Bidirectional Backlinks Map (backlinks.md).")
        return backlinks_file
