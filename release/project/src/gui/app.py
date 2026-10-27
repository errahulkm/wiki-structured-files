from ..parsers.wiki_auditor import KarpathyWikiAuditor

import subprocess

def get_gpu_telemetry_str(default_device_name: str) -> str:
    """Queries nvidia-smi for live GPU utilization and VRAM usage."""
    try:
        kwargs = {}
        if sys.platform == "win32":
            kwargs["creationflags"] = 0x08000000
        res = subprocess.check_output(
            ['nvidia-smi', '--query-gpu=name,utilization.gpu,memory.used,memory.total', '--format=csv,noheader,nounits'],
            encoding='utf-8', timeout=1.0, stderr=subprocess.DEVNULL, **kwargs
        ).strip()
        name, util, used_mb, total_mb = [x.strip() for x in res.split(',')]
        used_gb = float(used_mb) / 1024.0
        total_gb = float(total_mb) / 1024.0
        return f"🟢 GPU Accelerated: {name} | Load: {util}% | VRAM: {used_gb:.1f}/{total_gb:.1f} GB"
    except Exception:
        return f"🟢 GPU Accelerated: {default_device_name}"
"""
CustomTkinter Desktop GUI for STM32 Karpathy-Wiki Generator.
Focused exclusively on Reference Manual (RM0468) conversion into the Karpathy virtual directory tree.
"""

import json
import os
import sys
import threading
import time
from typing import Optional, Dict

import customtkinter as ctk
from tkinter import filedialog, messagebox

from .theme import THEME_CONFIG
from ..core.hardware_detector import detect_hardware_device
from ..core.checkpoint_manager import CheckpointManager
from ..core.logger import WikiLogger
from ..core.mcu_detector import detect_mcu_metadata, validate_reference_manual
from ..models.state_model import ProcessingStatus
from ..parsers.docling_extractor import DoclingPDFExtractor
from ..parsers.register_parser import RegisterParser
from ..generators.wiki_generator import KarpathyWikiGenerator
from ..generators.cross_linker import CrossLinkerEngine


class KarpathyWikiApp(ctk.CTk):
    """Main CustomTkinter GUI Application Window."""

    def __init__(self) -> None:
        super().__init__()

        self._settings_file = os.path.abspath("artifacts/gui_settings.json")

        self.title("⚡ STM32 Karpathy-Wiki Generator & Corpus Builder")
        self.geometry(f"{THEME_CONFIG['window_width']}x{THEME_CONFIG['window_height']}")
        self.minsize(1080, 720)

        # Application state tracking
        self.is_processing = False
        self.start_time = 0.0
        self.worker_thread: Optional[threading.Thread] = None
        self.current_file_name = ""
        self.live_tables = 0
        self.live_memory_maps = 0
        self.live_formulas = 0
        self.live_registers = 0

        # StringVars for dynamic label updates
        self.ref_manual_path = ctk.StringVar()
        self.output_dir_path = ctk.StringVar(value=os.path.abspath("artifacts/output/karpathy-wiki"))
        self.engine_mode = ctk.StringVar(value="Docling (ML/OCR)")
        self.browser_mode = ctk.StringVar(value="🖥 Native Desktop Window (Local Qt6 GPU)")
        self.status_ref = ctk.StringVar(value="[Pending ⏳]")
        self.pct_str = ctk.StringVar(value="0.0%")
        self.elapsed_str = ctk.StringVar(value="Elapsed Time: 00:00:00")
        self.eta_str = ctk.StringVar(value="ETA: --:--:--")
        self.speed_str = ctk.StringVar(value="Speed: 0.0 pages/sec")
        self.pages_count_str = ctk.StringVar(value="Pages: 0 / 0 (0 left)")
        self.memory_maps_str = ctk.StringVar(value="MemMaps: 0")
        self.formulas_str = ctk.StringVar(value="Registers: 0")
        self.tables_str = ctk.StringVar(value="Tables: 0")
        self.view_mode = ctk.StringVar(value="Console Log")

        # Hardware acceleration detection
        self.hw_info = detect_hardware_device()
        self.all_devices = [self.hw_info]
        self.selected_device_name = ctk.StringVar(value=self.hw_info["device_name"])

        # Detect initial MCU metadata
        self.mcu_info = detect_mcu_metadata()
        # Application logger
        self.logger = WikiLogger()

        self._build_ui()
        self._auto_detect_ref_manual()

        # Start live GUI timer loop
        self.after(500, self._timer_tick_loop)

    def _save_settings(self) -> None:
        """Persists user configuration (manual path, output dir, GPU target, viewer) across sessions."""
        try:
            os.makedirs(os.path.dirname(self._settings_file), exist_ok=True)
            data = {
                "ref_manual_path": self.ref_manual_path.get(),
                "output_dir_path": self.output_dir_path.get(),
                "engine_mode": self.engine_mode.get(),
                "browser_mode": self.browser_mode.get(),
                "selected_device_name": self.selected_device_name.get()
            }
            with open(self._settings_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            self.logger.error(f"Failed to save GUI settings: {e}")

    def _auto_detect_ref_manual(self) -> None:
        """Loads saved reference manual path or auto-detects dynamically across artifacts/st/."""
        # 1. Try saved settings first
        if os.path.exists(self._settings_file):
            try:
                with open(self._settings_file, "r", encoding="utf-8") as f:
                    cfg = json.load(f)
                saved_pdf = cfg.get("ref_manual_path")
                if saved_pdf and os.path.exists(saved_pdf):
                    self.ref_manual_path.set(saved_pdf)
                    if cfg.get("output_dir_path"):
                        self.output_dir_path.set(cfg["output_dir_path"])
                    if cfg.get("engine_mode"):
                        self.engine_mode.set(cfg["engine_mode"])
                    if cfg.get("browser_mode"):
                        self.browser_mode.set(cfg["browser_mode"])
                    self._update_detected_mcu_ui(saved_pdf, auto_adjust_output=False)
                    if hasattr(self, 'entry_rm') and self.entry_rm:
                        self.entry_rm.xview_moveto(1.0)
                    if hasattr(self, 'out_entry') and self.out_entry:
                        self.out_entry.xview_moveto(1.0)
                    return
            except Exception as e:
                self.logger.error(f"Error loading gui_settings.json: {e}")

        # 2. Dynamic multi-MCU detection across artifacts/st/
        st_root = os.path.abspath("artifacts/st")
        found_candidates = []
        if os.path.exists(st_root):
            for root, _, files in os.walk(st_root):
                for fname in files:
                    if fname.lower().endswith(".pdf") and "rm" in fname.lower():
                        full_p = os.path.join(root, fname)
                        mtime = os.path.getmtime(full_p)
                        found_candidates.append((mtime, full_p))
        
        if found_candidates:
            # Pick most recently modified manual PDF (e.g. STM32U3 rm0487)
            found_candidates.sort(key=lambda x: x[0], reverse=True)
            best_pdf = found_candidates[0][1]
            self.ref_manual_path.set(best_pdf)
            self._update_detected_mcu_ui(best_pdf, auto_adjust_output=True)
            self._save_settings()
            if hasattr(self, 'entry_rm') and self.entry_rm:
                self.entry_rm.xview_moveto(1.0)
            if hasattr(self, 'out_entry') and self.out_entry:
                self.out_entry.xview_moveto(1.0)

    def _update_detected_mcu_ui(self, source_hint: str, auto_adjust_output: bool = True) -> None:
        """Dynamically updates window title, header badges, input labels and output folder for the selected MCU."""
        mcu_info = detect_mcu_metadata(source_hint=source_hint)
        self.mcu_info = mcu_info

        if hasattr(self, 'title_label') and self.title_label:
            self.title_label.configure(text=f"⚡ {mcu_info['mcu_family']} Karpathy-Wiki Generator ({mcu_info['rm_number']} Engine)")
        if hasattr(self, 'lbl_rm') and self.lbl_rm:
            self.lbl_rm.configure(text=f"Reference Manual ({mcu_info['rm_number']}):")

        if auto_adjust_output:
            target_sub = mcu_info['target_device'] if mcu_info['target_device'] != "STM32 Microcontroller" else mcu_info['mcu_family']
            new_out = os.path.abspath(f"artifacts/output/{target_sub}")
            self.output_dir_path.set(new_out)

        if hasattr(self, 'status_label') and self.status_label:
            self.status_label.configure(text=f"Status: Ready to Ingest {mcu_info['display_title']}.")
        self.log_msg(f"🎯 Target MCU Detected: {mcu_info['display_title']} -> Output Directory: {self.output_dir_path.get()}")

    def _build_ui(self) -> None:
        """Constructs the application frame layout."""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Header Frame
        header_frame = ctk.CTkFrame(self, corner_radius=10)
        header_frame.grid(row=0, column=0, padx=20, pady=(15, 5), sticky="ew")
        header_frame.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            header_frame,
            text=f"⚡ {self.mcu_info['mcu_family']} Karpathy-Wiki Generator ({self.mcu_info['rm_number']} Engine)",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=15, pady=(8, 2), sticky="w")

        # Hardware Badge (GPU vs CPU)
        gpu_badge_color = "#00e676" if self.hw_info["gpu_available"] else "#ffab00"
        gpu_badge_text = f"🟢 GPU Accelerated: {self.hw_info['device_name']}" if self.hw_info["gpu_available"] else "🟡 Hardware: CPU Fallback Mode"
        
        self.gpu_label = ctk.CTkLabel(
            header_frame,
            text=gpu_badge_text,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=gpu_badge_color
        )
        self.gpu_label.grid(row=1, column=0, padx=15, pady=(0, 8), sticky="w")

        theme_switch = ctk.CTkSwitch(
            header_frame,
            text="Dark Mode",
            command=self._toggle_theme
        )
        theme_switch.select()
        theme_switch.grid(row=0, column=1, rowspan=2, padx=15, pady=10, sticky="e")

        # Input & Output Configuration Frame (Clean 3-column layout)
        inputs_frame = ctk.CTkFrame(self, corner_radius=10)
        inputs_frame.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
        inputs_frame.grid_columnconfigure(1, weight=1)

        # Row 0: Reference Manual Row
        self.lbl_rm = ctk.CTkLabel(inputs_frame, text=f"Reference Manual ({self.mcu_info['rm_number']}):", font=ctk.CTkFont(size=12, weight="bold"))
        self.lbl_rm.grid(row=0, column=0, padx=(16, 8), pady=8, sticky="w")

        rm_box_frame = ctk.CTkFrame(inputs_frame, fg_color="transparent")
        rm_box_frame.grid(row=0, column=1, padx=4, pady=8, sticky="ew")

        self.entry_rm = ctk.CTkEntry(
            rm_box_frame,
            textvariable=self.ref_manual_path,
            placeholder_text="Select Reference Manual PDF (e.g. RM0487 / RM0468)...",
            font=ctk.CTkFont(family="Consolas" if os.name == 'nt' else "Monospace", size=11)
        )
        self.entry_rm.pack(side="left", fill="x", expand=True, padx=(0, 8))

        status_lbl = ctk.CTkLabel(rm_box_frame, textvariable=self.status_ref, font=ctk.CTkFont(size=11, weight="bold"), text_color="#00e5ff")
        status_lbl.pack(side="right", padx=(0, 4))

        btn_rm = ctk.CTkButton(inputs_frame, text="Browse", width=80, command=self._browse_ref_manual)
        btn_rm.grid(row=0, column=2, padx=(8, 16), pady=8, sticky="e")

        # Row 1: Output Directory Row
        out_lbl = ctk.CTkLabel(inputs_frame, text="Output Wiki Directory:", font=ctk.CTkFont(size=12, weight="bold"))
        out_lbl.grid(row=1, column=0, padx=(16, 8), pady=8, sticky="w")

        self.out_entry = ctk.CTkEntry(
            inputs_frame,
            textvariable=self.output_dir_path,
            placeholder_text="Output Wiki Directory...",
            font=ctk.CTkFont(family="Consolas" if os.name == 'nt' else "Monospace", size=11)
        )
        self.out_entry.grid(row=1, column=1, padx=4, pady=8, sticky="ew")

        out_btn = ctk.CTkButton(inputs_frame, text="Browse", width=80, command=self._browse_output_dir)
        out_btn.grid(row=1, column=2, padx=(8, 16), pady=8, sticky="e")

        # Row 2: Parsing Engine & Graph Target GPU Options Row
        eng_lbl = ctk.CTkLabel(inputs_frame, text="Parsing Engine Mode:", font=ctk.CTkFont(size=12, weight="bold"))
        eng_lbl.grid(row=2, column=0, padx=(16, 8), pady=8, sticky="w")

        row2_frame = ctk.CTkFrame(inputs_frame, fg_color="transparent")
        row2_frame.grid(row=2, column=1, columnspan=2, padx=4, pady=8, sticky="ew")

        def _on_engine_changed(choice: str) -> None:
            self.engine_mode.set(choice)
            self._save_settings()

        eng_selector = ctk.CTkOptionMenu(
            row2_frame,
            values=["Docling (ML/OCR)", "OCR / Hybrid Table Engine"],
            variable=self.engine_mode,
            command=_on_engine_changed,
            width=180
        )
        eng_selector.pack(side="left", padx=(0, 20))

        gpu_lbl = ctk.CTkLabel(row2_frame, text="Graph Target GPU:", font=ctk.CTkFont(size=12, weight="bold"))
        gpu_lbl.pack(side="left", padx=(0, 8))

        def _on_gpu_changed(choice: str) -> None:
            self.selected_device_name.set(choice)
            self._save_settings()
            self.log_msg(f"⚡ Target Hardware Acceleration set to: {choice}")

        dev_names = [d["device_name"] for d in self.all_devices] if hasattr(self, 'all_devices') else ["Auto GPU Selection"]
        self.gpu_option_menu = ctk.CTkOptionMenu(
            row2_frame,
            values=dev_names if dev_names else ["Auto GPU Selection"],
            variable=self.selected_device_name,
            command=_on_gpu_changed,
            width=280
        )
        self.gpu_option_menu.pack(side="left", padx=(0, 8))

        self.btn_detect_gpu = ctk.CTkButton(
            row2_frame,
            text="🔄 Detect GPUs",
            width=100,
            fg_color="#0284c7",
            hover_color="#0369a1",
            font=ctk.CTkFont(size=11, weight="bold"),
            command=self._detect_gpus_manual
        )
        self.btn_detect_gpu.pack(side="left")

        # Row 3: Graph Viewer Target Row
        browser_lbl = ctk.CTkLabel(inputs_frame, text="Graph Viewer Target:", font=ctk.CTkFont(size=12, weight="bold"))
        browser_lbl.grid(row=3, column=0, padx=(16, 8), pady=8, sticky="w")

        def _on_browser_changed(choice: str) -> None:
            self.browser_mode.set(choice)
            self._save_settings()
            self.log_msg(f"Target Viewer set to: {choice}")

        browser_selector = ctk.CTkOptionMenu(
            inputs_frame,
            values=[
                "🖥 Native Desktop Window (Local Qt6 GPU)",
                "🌐 Google Chrome Browser",
                "🦊 Mozilla Firefox Browser",
                "⚙️ Auto / System Default Browser"
            ],
            variable=self.browser_mode,
            command=_on_browser_changed,
            width=360,
            fg_color="#0284c7",
            button_color="#0369a1",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        browser_selector.grid(row=3, column=1, padx=4, pady=8, sticky="w")

        # Controls & Telemetry Dashboard Frame
        ctrl_frame = ctk.CTkFrame(self, corner_radius=10)
        ctrl_frame.grid(row=2, column=0, padx=20, pady=5, sticky="ew")
        ctrl_frame.grid_columnconfigure(0, weight=1)

        btn_container = ctk.CTkFrame(ctrl_frame, fg_color="transparent")
        btn_container.grid(row=0, column=0, padx=10, pady=6, sticky="ew")

        self.start_btn = ctk.CTkButton(
            btn_container,
            text="🚀 Start Ingestion",
            fg_color="#16a34a",
            hover_color="#15803d",
            font=ctk.CTkFont(weight="bold"),
            command=self._start_pipeline
        )
        self.start_btn.pack(side="left", padx=6)

        self.pause_btn = ctk.CTkButton(
            btn_container,
            text="⏸ Pause / Flush",
            fg_color="#d97706",
            hover_color="#b45309",
            state="disabled",
            command=self._pause_pipeline
        )
        self.pause_btn.pack(side="left", padx=6)

        self.resume_btn = ctk.CTkButton(
            btn_container,
            text="🔄 Resume Warm Boot",
            fg_color="#0284c7",
            hover_color="#0369a1",
            command=self._resume_pipeline
        )
        self.resume_btn.pack(side="left", padx=6)

        self.clean_btn = ctk.CTkButton(
            btn_container,
            text="🧹 Clean Output Directory",
            fg_color="#dc2626",
            hover_color="#991b1b",
            font=ctk.CTkFont(weight="bold"),
            command=self._clean_output_directory
        )
        self.clean_btn.pack(side="left", padx=6)

        self.open_dir_btn = ctk.CTkButton(
            btn_container,
            text="📁 Open Output Directory",
            fg_color="#8b5cf6",
            hover_color="#7c3aed",
            font=ctk.CTkFont(weight="bold"),
            command=self._open_output_directory
        )
        self.open_dir_btn.pack(side="left", padx=6)

        self.graph_btn = ctk.CTkButton(
            btn_container,
            text="❇ Multi-View Graph",
            fg_color="#06b6d4",
            hover_color="#0891b2",
            font=ctk.CTkFont(weight="bold"),
            command=self._open_graph_view
        )
        self.graph_btn.pack(side="left", padx=6)

        self.audit_btn = ctk.CTkButton(
            btn_container,
            text="🔍 Audit Wiki Corpus",
            fg_color="#059669",
            hover_color="#047857",
            font=ctk.CTkFont(weight="bold"),
            command=self._on_run_audit_clicked
        )
        self.audit_btn.pack(side="left", padx=6)

        # Telemetry Labels Row
        telemetry_frame = ctk.CTkFrame(ctrl_frame, fg_color="#1a1d24", corner_radius=6)
        telemetry_frame.grid(row=1, column=0, padx=10, pady=4, sticky="ew")
        telemetry_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        ctk.CTkLabel(telemetry_frame, textvariable=self.pct_str, font=ctk.CTkFont(size=14, weight="bold"), text_color="#00e5ff").grid(row=0, column=0, padx=8, pady=4)
        ctk.CTkLabel(telemetry_frame, textvariable=self.pages_count_str, font=ctk.CTkFont(size=11, weight="bold"), text_color="#00e676").grid(row=0, column=1, padx=8, pady=4)
        ctk.CTkLabel(telemetry_frame, textvariable=self.elapsed_str, font=ctk.CTkFont(size=11)).grid(row=0, column=2, padx=8, pady=4)
        ctk.CTkLabel(telemetry_frame, textvariable=self.eta_str, font=ctk.CTkFont(size=11)).grid(row=0, column=3, padx=8, pady=4)
        ctk.CTkLabel(telemetry_frame, textvariable=self.speed_str, font=ctk.CTkFont(size=11)).grid(row=0, column=4, padx=8, pady=4)

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(ctrl_frame)
        self.progress_bar.set(0.0)
        self.progress_bar.grid(row=2, column=0, padx=15, pady=(2, 6), sticky="ew")

        self.status_label = ctk.CTkLabel(ctrl_frame, text="Status: Ready to Ingest RM0468 Reference Manual.", font=ctk.CTkFont(size=12))
        self.status_label.grid(row=3, column=0, padx=15, pady=(0, 6), sticky="w")

        # Bottom Frame: View Switcher (Console Log vs Processing Detailed View)
        view_frame = ctk.CTkFrame(self, corner_radius=10)
        view_frame.grid(row=3, column=0, padx=20, pady=(5, 15), sticky="nsew")
        view_frame.grid_columnconfigure(0, weight=1)
        view_frame.grid_rowconfigure(1, weight=1)

        view_header = ctk.CTkFrame(view_frame, fg_color="transparent")
        view_header.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(view_header, text="View Mode:", font=ctk.CTkFont(size=12, weight="bold")).pack(side="left", padx=5)

        segmented_btn = ctk.CTkSegmentedButton(
            view_header,
            values=["Console Log", "Processing Detailed View"],
            variable=self.view_mode,
            command=self._switch_view_mode
        )
        segmented_btn.pack(side="left", padx=10)

        # Console Text Box
        self.console_text = ctk.CTkTextbox(view_frame, font=ctk.CTkFont(family="Courier", size=11))
        self.console_text.grid(row=1, column=0, padx=10, pady=6, sticky="nsew")

        # Detailed Processing View Frame
        self.detailed_view_frame = ctk.CTkFrame(view_frame, fg_color="transparent")
        self.detail_textbox = ctk.CTkTextbox(self.detailed_view_frame, font=ctk.CTkFont(family="Courier", size=11))
        self.detail_textbox.pack(fill="both", expand=True, padx=10, pady=6)

        self.log_msg("System ready. Hardware GPU acceleration checked.")
        self.update_detailed_view("System initialized. Click 'Start Ingestion' to process RM0468.")

    def _timer_tick_loop(self) -> None:
        """Main thread loop running every 500ms to update live elapsed time, ETA, and GPU telemetry."""
        try:
            if not self.winfo_exists():
                return
        except Exception:
            return

        try:
            if self.is_processing and self.start_time > 0:
                elapsed_sec = max(1.0, time.time() - self.start_time)
                mins, secs = divmod(int(elapsed_sec), 60)
                hours, mins = divmod(mins, 60)
                self.elapsed_str.set(f"Elapsed Time: {hours:02d}:{mins:02d}:{secs:02d}")
                
                # Compute live continuous ETA across all percentages
                try:
                    curr_pct_val = float(self.pct_str.get().replace("%", "").strip())
                    if 0.1 <= curr_pct_val < 100.0:
                        speed_pct = curr_pct_val / elapsed_sec
                        rem_pct = max(0.0, 100.0 - curr_pct_val)
                        eta_s = int(rem_pct / speed_pct) if speed_pct > 0 else 0
                        e_m, e_s = divmod(eta_s, 60)
                        e_h, e_m = divmod(e_m, 60)
                        self.eta_str.set(f"ETA: {e_h:02d}:{e_m:02d}:{e_s:02d}")
                    elif curr_pct_val >= 100.0:
                        self.eta_str.set("ETA: 00:00:00")
                except Exception:
                    pass

                if self.view_mode.get() == "Processing Detailed View":
                    self.update_detailed_view()

            self.after(500, self._timer_tick_loop)
        except Exception:
            pass

    def update_detailed_view(self, extra_info: str = "") -> None:
        """Updates the Processing Detailed View text box with live extraction stats."""
        gpu_name = self.hw_info["device_name"]
        gpu_status = "CUDA Active" if self.hw_info["gpu_available"] else "CPU Fallback"
        
        details = f"""================================================================================
            LIVE KARPATHY-WIKI DETAILED TELEMETRY VIEW (RM0468 ENGINE)
================================================================================
[HARDWARE ENGINE]
- Device Acceleration: {gpu_name} ({gpu_status})
- VRAM Allocated     : {self.hw_info['vram_gb']} GB

[KARPATHY VIRTUAL DIRECTORY TREE]
- Master Dashboard   : index.md (Map of Content)
- Raw PDF Storage    : raw/RM0468_Reference_Manual.pdf
- Memory Architecture: memory/memory_map.md
- System Infrastructure: system/ (bus_matrix.md, rcc.md, pwr.md, syscfg.md)
- Core & Interrupts  : core/ (nvic.md, systick.md)
- Peripherals        : peripherals/ (gpio.md, usart.md, i2c.md, spi.md, timers.md, adc.md, dac.md, dma.md, fmc.md, octospi.md, fdcan.md, eth.md, usb.md)
- Security Domain    : security/ (trustzone.md, cryp.md, rng.md)
- Register JSON Map  : registers_json/
- Assets / Diagrams  : assets/

[LIVE EXTRACTION COUNTERS]
- Current Active File: {self.current_file_name or 'None'}
- Pages Converted    : {self.pages_count_str.get()}
- Tables Extracted   : {self.live_tables}
- Memory Maps Found  : {self.live_memory_maps}
- Formulas Parsed    : {self.live_formulas}
- Register JSONs     : {self.live_registers}

[PERFORMANCE & TIMING]
- Task Completion     : {self.pct_str.get()}
- Time Elapsed         : {self.elapsed_str.get()}
- Time Remaining (ETA) : {self.eta_str.get()}
- Processing Speed     : {self.speed_str.get()}

[STATUS STAGE DETAILS]
{extra_info}
================================================================================
"""
        self.detail_textbox.delete("1.0", "end")
        self.detail_textbox.insert("end", details)

    def _switch_view_mode(self, value: str) -> None:
        """Switches between Console Log and Processing Detailed View."""
        if value == "Console Log":
            self.detailed_view_frame.grid_forget()
            self.console_text.grid(row=1, column=0, padx=10, pady=6, sticky="nsew")
        else:
            self.console_text.grid_forget()
            self.detailed_view_frame.grid(row=1, column=0, padx=10, pady=6, sticky="nsew")
            self.update_detailed_view("Viewing live processing pipeline stats.")

    def log_msg(self, msg: str) -> None:
        """Appends log text to GUI console."""
        timestamp = time.strftime("%H:%M:%S")
        self.console_text.insert("end", f"[{timestamp}] {msg}\n")
        self.console_text.see("end")

    def _toggle_theme(self) -> None:
        """Toggles appearance mode between Light and Dark."""
        current = ctk.get_appearance_mode()
        new_mode = "Light" if current == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)

    def _browse_ref_manual(self) -> None:
        init_dir = os.path.dirname(self.ref_manual_path.get()) if self.ref_manual_path.get() and os.path.exists(os.path.dirname(self.ref_manual_path.get())) else os.path.abspath("artifacts/st")
        path = filedialog.askopenfilename(initialdir=init_dir, filetypes=[("PDF Documents", "*.pdf")])
        if path:
            is_rm, val_msg, resolved_rm = validate_reference_manual(path)
            if not is_rm:
                if resolved_rm and os.path.exists(resolved_rm):
                    messagebox.showwarning(
                        "Auto-Switching to Reference Manual",
                        f"The selected file is not a Reference Manual:\n{os.path.basename(path)}\n\n"
                        f"{val_msg}\n\n"
                        f"The tool has automatically switched to the authentic Reference Manual:\n{os.path.basename(resolved_rm)}"
                    )
                    path = resolved_rm
                else:
                    messagebox.showerror(
                        "Document Rejected",
                        f"{val_msg}\n\nPlease select an authentic Reference Manual (RMxxxx PDF)."
                    )
                    self.log_msg(f"❌ Document Rejected: {val_msg}")
                    return

            self.ref_manual_path.set(path)
            self._update_detected_mcu_ui(path, auto_adjust_output=True)
            self._save_settings()
            if hasattr(self, 'entry_rm') and self.entry_rm:
                self.entry_rm.xview_moveto(1.0)
            if hasattr(self, 'out_entry') and self.out_entry:
                self.out_entry.xview_moveto(1.0)

    def _browse_output_dir(self) -> None:
        init_dir = self.output_dir_path.get() if self.output_dir_path.get() and os.path.exists(self.output_dir_path.get()) else os.path.abspath("artifacts/output")
        path = filedialog.askdirectory(initialdir=init_dir)
        if path:
            self.output_dir_path.set(path)
            self._save_settings()
            if hasattr(self, 'out_entry') and self.out_entry:
                self.out_entry.xview_moveto(1.0)

    def _clean_output_directory(self) -> None:
        """Purges output directory files with user choice of Complete Wipe (empty) or Skeleton Reset."""
        out_root = self.output_dir_path.get()
        if not out_root:
            return

        dialog = ctk.CTkToplevel(self)
        dialog.title("🧹 Clean Output Directory")
        dialog.geometry("560x320")
        dialog.transient(self)
        dialog.grab_set()
        dialog.focus_force()

        lbl_icon = ctk.CTkLabel(dialog, text="🧹", font=ctk.CTkFont(size=36))
        lbl_icon.pack(pady=(15, 5))

        lbl_title = ctk.CTkLabel(
            dialog,
            text="Clean & Purge Output Directory",
            font=ctk.CTkFont(size=15, weight="bold")
        )
        lbl_title.pack(pady=(0, 5))

        lbl_path = ctk.CTkLabel(
            dialog,
            text=f"Target: {out_root}",
            font=ctk.CTkFont(size=12, family="Courier"),
            text_color="#38bdf8",
            wraplength=520
        )
        lbl_path.pack(pady=(0, 10), padx=20)

        lbl_desc = ctk.CTkLabel(
            dialog,
            text="Choose your desired cleaning mode below:\n(All old PDFs in raw/ and stale artifacts will be permanently purged)",
            font=ctk.CTkFont(size=12),
            text_color="#94a3b8"
        )
        lbl_desc.pack(pady=(0, 15))

        btn_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        btn_frame.pack(fill="x", padx=20, pady=(5, 15))

        def _execute_clean(recreate_skeleton: bool):
            dialog.grab_release()
            dialog.destroy()

            def _clean_worker():
                t0 = time.time()
                try:
                    gen = KarpathyWikiGenerator(output_root=out_root)
                    gen.clean_output_directory(purge_raw=True, recreate_skeleton=recreate_skeleton)
                    elapsed = time.time() - t0
                    remaining = os.listdir(out_root) if os.path.exists(out_root) else []

                    def _ui_reset():
                        # Reset UI states & telemetry
                        self.progress_bar.set(0.0)
                        self.pct_str.set("0.0%")
                        self.elapsed_str.set("Elapsed Time: 00:00:00")
                        self.eta_str.set("ETA: --:--:--")
                        self.speed_str.set("Speed: 0.0 pages/sec")
                        self.pages_count_str.set("Pages: 0 / 0 (0 left)")
                        self.live_tables = 0
                        self.live_memory_maps = 0
                        self.live_formulas = 0
                        self.live_registers = 0
                        self.current_file_name = ""
                        
                        self.is_processing = False
                        self.start_btn.configure(state="normal")
                        self.pause_btn.configure(state="disabled")
                        self.status_ref.set("[Pending ⏳]")
                        
                        if recreate_skeleton:
                            mode_desc = f"reset to clean 7-layer skeleton ({len(remaining)} items)"
                            status_msg = f"Output directory reset to skeleton in {elapsed:.3f}s. Ready for fresh ingestion."
                        else:
                            mode_desc = f"completely emptied ({len(remaining)} items left)"
                            status_msg = f"Output directory completely wiped in {elapsed:.3f}s. Ready for fresh ingestion."

                        self.status_label.configure(text=f"Status: {status_msg}")
                        self.log_msg(f"🧹 Cleaned output directory ({mode_desc}) in {elapsed:.3f}s: {out_root}")
                        self.update_detailed_view(f"Output directory {mode_desc}.")
                        messagebox.showinfo(
                            "Directory Cleaned",
                            f"Output directory successfully {mode_desc} in {elapsed:.3f}s:\n{out_root}"
                        )

                    self.after(0, _ui_reset)
                except Exception as e:
                    err = str(e)
                    self.after(0, lambda m=err: messagebox.showerror("Clean Error", f"Could not clean output directory: {m}"))

            threading.Thread(target=_clean_worker, daemon=True).start()

        btn_wipe = ctk.CTkButton(
            btn_frame,
            text="🗑️ Complete Wipe (100% Empty)",
            fg_color="#ef4444",
            hover_color="#dc2626",
            font=ctk.CTkFont(weight="bold"),
            command=lambda: _execute_clean(recreate_skeleton=False)
        )
        btn_wipe.pack(side="left", padx=5, expand=True, fill="x")

        btn_reset = ctk.CTkButton(
            btn_frame,
            text="🔄 Reset Skeleton Template",
            fg_color="#3b82f6",
            hover_color="#2563eb",
            font=ctk.CTkFont(weight="bold"),
            command=lambda: _execute_clean(recreate_skeleton=True)
        )
        btn_reset.pack(side="left", padx=5, expand=True, fill="x")

        btn_cancel = ctk.CTkButton(
            btn_frame,
            text="Cancel",
            fg_color="#4b5563",
            hover_color="#374151",
            width=80,
            command=lambda: (dialog.grab_release(), dialog.destroy())
        )
        btn_cancel.pack(side="left", padx=5)


    def _open_output_directory(self) -> None:
        """Opens the output directory in system file manager (e.g. Nautilus/xdg-open on Linux)."""
        out_dir = self.output_dir_path.get()
        if not out_dir or not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
        try:
            if sys.platform == "win32":
                os.startfile(out_dir)
            elif sys.platform == "darwin":
                import subprocess
                subprocess.Popen(["open", out_dir])
            else:
                import subprocess
                subprocess.Popen(["xdg-open", out_dir])
            self.log_msg(f"📂 Opened output directory: {out_dir}")
        except Exception as e:
            messagebox.showerror("Error Opening Directory", f"Could not open output directory: {e}")

    def _detect_gpus_manual(self) -> None:
        """Scans hardware devices dynamically and updates GPU selector dropdown menu."""
        from ..core.hardware_detector import detect_all_hardware_devices
        from ..core.gpu_runtime import detect_system_gpu_architecture
        self.all_devices = detect_all_hardware_devices()
        dev_names = [d["name"] for d in self.all_devices]
        if hasattr(self, 'gpu_option_menu'):
            self.gpu_option_menu.configure(values=dev_names)
            if dev_names:
                self.selected_device_name.set(dev_names[0])
        arch_info = detect_system_gpu_architecture()
        dev_summary = "\n".join([f"• {d['name']}" for d in self.all_devices])
        self.log_msg(f"🔄 Hardware GPU Re-detected: Found {len(self.all_devices)} accelerators | Architecture: {arch_info['switcher_tool']}")
        messagebox.showinfo(
            "GPU Re-detection & Self-Healing Diagnostics",
            f"Hardware acceleration re-detected successfully:\n\n{dev_summary}\n\n"
            f"• System Architecture: {arch_info['architecture']}\n"
            f"• Display Server: {arch_info['display_server'].upper()}\n"
            f"• GPU Switcher: {arch_info['switcher_tool']}\n"
            f"• Adaptive Self-Healing: Active (Tier 1-3 Multi-Tier Fallback)"
        )

    def _open_graph_view(self) -> None:
        """Generates and opens interactive Obsidian-style knowledge graph in selected Web Browser with target GPU hardware offloading."""
        out_dir = self.output_dir_path.get()
        if not out_dir or not os.path.exists(out_dir):
            messagebox.showwarning("Graph View", "Output directory does not exist yet. Please run ingestion first.")
            return
        try:
            from ..visualizer.graph_visualizer import KnowledgeGraphVisualizer
            from ..core.logger import WikiLogger
            viz = KnowledgeGraphVisualizer(output_root=out_dir, logger=WikiLogger())
            gpu_choice = self.selected_device_name.get()
            target_choice = self.browser_mode.get()
            html_path = viz.open_graph_in_browser(gpu_preference=gpu_choice, browser_preference=target_choice)
            self.log_msg(f"🕸 Launched Knowledge Graph Visualizer [{target_choice} | GPU: {gpu_choice}] -> {html_path}")
        except Exception as e:
            messagebox.showerror("Graph Error", f"Could not launch Knowledge Graph: {e}")

    def _start_pipeline(self) -> None:
        """Triggers worker thread to run ingestion pipeline after validating Reference Manual authenticity."""
        ref_path = self.ref_manual_path.get()
        if not ref_path:
            messagebox.showerror("Missing File", "Please select the Reference Manual PDF file.")
            return

        is_rm, val_msg, resolved_rm = validate_reference_manual(ref_path)
        if not is_rm:
            if resolved_rm and os.path.exists(resolved_rm):
                messagebox.showwarning(
                    "Auto-Switching to Reference Manual",
                    f"{val_msg}\n\nAuto-switching to authentic Reference Manual:\n{os.path.basename(resolved_rm)}"
                )
                ref_path = resolved_rm
                self.ref_manual_path.set(resolved_rm)
                self._update_detected_mcu_ui(resolved_rm, auto_adjust_output=True)
            else:
                messagebox.showerror(
                    "Document Rejected",
                    f"{val_msg}\n\nPlease select an authentic Reference Manual (RMxxxx PDF)."
                )
                self.log_msg(f"❌ Document Ingestion Aborted: {val_msg}")
                return

        mcu_info = detect_mcu_metadata(source_hint=ref_path, wiki_root=self.output_dir_path.get())
        self.is_processing = True
        self.start_time = time.time()
        self.start_btn.configure(state="disabled")
        self.pause_btn.configure(state="normal")
        self.progress_bar.set(0.01)
        self.pct_str.set("1.0%")
        self.status_label.configure(text=f"Status: Starting {mcu_info['display_title']} Karpathy-Wiki conversion...")

        self.worker_thread = threading.Thread(target=self._run_ingestion_worker, daemon=True)
        self.worker_thread.start()

    def _pause_pipeline(self) -> None:
        """Pauses processing thread cleanly."""
        self.is_processing = False
        self.log_msg("Pause signal sent. Flushing state to memory/state.json...")
        self.status_label.configure(text="Status: Pausing and flushing state...")

    def _resume_pipeline(self) -> None:
        """Triggers warm boot resume."""
        self.log_msg("Warm boot resume triggered.")
        self._start_pipeline()

    def _run_ingestion_worker(self) -> None:
        """Background worker executing document ingestion into Karpathy Wiki layout with instant telemetry."""
        out_root = self.output_dir_path.get()
        ref_pdf = self.ref_manual_path.get()
        mcu_info = detect_mcu_metadata(source_hint=ref_pdf, wiki_root=out_root)

        try:
            logger = WikiLogger(os.path.join(out_root, "log.md"))
            chk_mgr = CheckpointManager(output_root=out_root, logger=logger)
            wiki_gen = KarpathyWikiGenerator(output_root=out_root, logger=logger)
            linker = CrossLinkerEngine(output_root=out_root, logger=logger)
            parser = RegisterParser(output_root=out_root, logger=logger)

            def step_progress_callback(pct: float, stage_msg: str, curr_p: int = 0, tot_p: int = 3357) -> None:
                if not self.is_processing:
                    return
                self.pct_str.set(f"{pct:.1f}%")
                self.progress_bar.set(max(0.01, pct / 100.0))
                
                if curr_p > 0:
                    left_p = max(0, tot_p - curr_p)
                    elapsed = max(1.0, time.time() - self.start_time)
                    speed = curr_p / elapsed
                    self.pages_count_str.set(f"Pages: {curr_p} / {tot_p} ({left_p} left)")
                    self.speed_str.set(f"Speed: {speed:.1f} p/s")

                self.status_ref.set(f"[Processing 🔄 {pct:.1f}%]")
                self.status_label.configure(text=f"Status: {stage_msg}")
                self.log_msg(stage_msg)

            # Immediate startup telemetry signal
            step_progress_callback(1.0, f"🚀 Initializing {mcu_info['display_title']} Karpathy-Wiki Ingestion Engine...")

            # 1. Build exact Karpathy virtual directory layout
            wiki_gen.build_directory_structure()
            wiki_gen.create_schema_md()
            step_progress_callback(2.0, "📂 Created Karpathy virtual directory structure...")

            # 2. Copy source Reference Manual PDF into raw/
            file_map = {"ref_manual": ref_pdf}
            self.log_msg(f"Copying raw {mcu_info['rm_number']} Reference Manual into raw/ directory...")
            wiki_gen.copy_raw_documents(file_map)

            # 3. Dynamic Chapter & Architectural DNA Ingestion
            step_progress_callback(5.0, f"🧬 Extracting Architectural DNA for {mcu_info['display_title']}...")
            wiki_gen.populate_initial_markdown_pages(ref_pdf_path=ref_pdf, progress_callback=step_progress_callback)

            # Lazy initialize ML extractor after initial fast markdown generation
            step_progress_callback(90.0, f"⚡ Initializing {self.engine_mode.get()} parsing models...")
            extractor = DoclingPDFExtractor(logger=logger, engine_mode=self.engine_mode.get(), target_device=self.selected_device_name.get())

            fname = os.path.basename(ref_pdf)
            self.current_file_name = fname
            self.log_msg(f"Processing {mcu_info['display_title']}: {fname}")
            self.status_ref.set("[Processing 🔄 0%]")

            total_pages = extractor.get_pdf_page_count(ref_pdf)

            def page_progress_callback(curr_p: int, tot_p: int, stage_desc: str,
                                       tables: int, mem_maps: int, formulas: int) -> None:
                """Streaming callback executed for every single extracted page."""
                if not self.is_processing:
                    return

                self.live_tables = tables
                self.live_memory_maps = mem_maps
                self.live_formulas = formulas

                left_pages = tot_p - curr_p
                overall_pct = (curr_p / tot_p) * 100.0

                elapsed = max(1.0, time.time() - self.start_time)
                speed = curr_p / elapsed
                eta_sec = int(left_pages / speed) if speed > 0 else 0
                eta_m, eta_s = divmod(eta_sec, 60)
                eta_h, eta_m = divmod(eta_m, 60)

                self.pct_str.set(f"{overall_pct:.1f}%")
                self.progress_bar.set(overall_pct / 100.0)
                self.pages_count_str.set(f"Pages: {curr_p} / {tot_p} ({left_pages} left)")
                self.speed_str.set(f"Speed: {speed:.1f} p/s")
                self.eta_str.set(f"ETA: {eta_h:02d}:{eta_m:02d}:{eta_s:02d}")
                
                self.status_ref.set(f"[Processing 🔄 {overall_pct:.1f}%]")
                status_text = f"Status: [{fname} Page {curr_p}/{tot_p}] Tables: {tables} | Memory Maps: {mem_maps} | Formulas: {formulas}"
                self.status_label.configure(text=status_text)

            # Process all pages of reference manual
            raw_text = extractor.extract_pdf_with_streaming_progress(
                ref_pdf,
                max_pages=None,
                progress_callback=page_progress_callback
            )

            # Extract hardware register definitions into registers_json/
            self.log_msg("Parsing 32-Bit Hardware Registers into registers_json/...")
            regs = parser.extract_registers_from_text(raw_text)
            self.live_registers += len(regs)

            self.status_ref.set("[Completed ✅ 100%]")
            chk_mgr.update_file_status("ref_manual", "Reference Manual", ref_pdf, total_pages, total_pages, ProcessingStatus.COMPLETED)

            # Generate cross links and index
            self.log_msg("Generating Cross-Links and Register Indices...")
            linker.generate_register_index()
            linker.generate_backlinks_map()
            chk_mgr.mark_completed()

            self.pct_str.set("100.0%")
            self.progress_bar.set(1.0)
            self.eta_str.set("ETA: 00:00:00")
            self.speed_str.set("Speed: Finished")
            
            self.status_label.configure(text=f"Status: {mcu_info['display_title']} Karpathy-Wiki Generation Complete! (Finished in {chk_mgr.format_elapsed_str()})")
            self.log_msg(f"🎉 {mcu_info['display_title']} Karpathy-Wiki Built Successfully!")
            self.update_detailed_view("ALL PIPELINE STAGES PASSED 100% SUCCESS.")

            messagebox.showinfo("Success", f"{mcu_info['display_title']} Karpathy-Wiki generated successfully in {chk_mgr.format_elapsed_str()} at:\n{out_root}")

        except Exception as err:
            self.log_msg(f"ERROR: Processing failed: {err}")
            self.status_label.configure(text=f"Status: Error - {err}")
            messagebox.showerror("Execution Error", f"Processing failed: {err}")
        finally:
            self.is_processing = False
            self.start_btn.configure(state="normal")
            self.pause_btn.configure(state="disabled")




    def _show_custom_info_modal(self, title: str, message: str) -> None:
        """Displays a sleek CustomTkinter modal popup that closes cleanly on OK click."""
        dialog = ctk.CTkToplevel(self)
        dialog.title(title)
        dialog.geometry("520x240")
        dialog.transient(self)
        dialog.grab_set()
        dialog.focus_force()

        lbl_icon = ctk.CTkLabel(dialog, text="🎉", font=ctk.CTkFont(size=36))
        lbl_icon.pack(pady=(15, 5))

        lbl_msg = ctk.CTkLabel(dialog, text=message, font=ctk.CTkFont(size=13, weight="bold"), wraplength=480)
        lbl_msg.pack(pady=10, padx=20)

        def _on_ok():
            dialog.grab_release()
            dialog.destroy()

        btn_ok = ctk.CTkButton(dialog, text="OK", width=120, font=ctk.CTkFont(weight="bold"), command=_on_ok)
        btn_ok.pack(pady=15)

    def _start_gpu_telemetry_thread(self) -> None:
        """Launches background thread to continuously poll GPU load and VRAM without blocking UI."""
        def _gpu_worker():
            import subprocess, time
            kwargs = {}
            if sys.platform == "win32":
                kwargs["creationflags"] = 0x08000000
            while True:
                try:
                    res = subprocess.check_output(
                        ['nvidia-smi', '--query-gpu=name,utilization.gpu,memory.used,memory.total', '--format=csv,noheader,nounits'],
                        encoding='utf-8', timeout=1.5, stderr=subprocess.DEVNULL, **kwargs
                    ).strip()
                    name, util, used_mb, total_mb = [x.strip() for x in res.split(',')]
                    used_gb = float(used_mb) / 1024.0
                    total_gb = float(total_mb) / 1024.0
                    msg = f"🟢 GPU Accelerated: {name} | Load: {util}% | VRAM: {used_gb:.2f}/{total_gb:.2f} GB"
                    if hasattr(self, 'gpu_label'):
                        self.after(0, lambda m=msg: self.gpu_label.configure(text=m))
                except Exception:
                    pass
                time.sleep(1.0)

        t = threading.Thread(target=_gpu_worker, daemon=True)
        t.start()

    def _on_run_audit_clicked(self) -> None:
        """Runs independent KarpathyWikiAuditor in background thread and launches HTML report."""
        if self.is_processing:
            self._show_modal_message("Audit Notice", "Please pause or complete ingestion before running the independent Auditor.")
            return

        def _worker():
            self.is_processing = True
            self.log_msg("🔍 Starting Independent Karpathy-Wiki Corpus Audit...")
            try:
                auditor = KarpathyWikiAuditor(
                    wiki_root=self.output_dir_path.get(),
                    logger=self.logger
                )
                
                def _audit_cb(pct, msg):
                    self.pct_str.set(f"{pct:.1f}%")
                    self.progress_bar.set(pct / 100.0)
                    self.status_label.configure(text=f"Status: {msg}")
                    self.log_msg(msg)

                res = auditor.run_full_audit(progress_callback=_audit_cb)
                score = res["overall_health_score"]
                report_path = res["report_path"]

                self.pct_str.set("100.0%")
                self.progress_bar.set(1.0)
                self.status_label.configure(text=f"Status: Audit Complete ({score}% Overall Health Score)")
                
                # Auto-open HTML report in browser
                auditor.open_report_in_browser()

                s_val = score
                r_path = report_path
                self.after(0, lambda s=s_val, p=r_path: messagebox.showinfo(
                    "Audit Complete 🔍",
                    f"Karpathy-Wiki Corpus Audit Complete!\n\n"
                    f"Overall Health Score: {s}%\n"
                    f"Report File: {p}\n\n"
                    f"HTML report opened in default web browser."
                ))
            except Exception as e:
                err_msg = str(e)
                self.log_msg(f"Audit Error: {err_msg}")
                self.after(0, lambda m=err_msg: messagebox.showerror("Audit Error", f"Failed to complete audit: {m}"))
            finally:
                self.is_processing = False

        threading.Thread(target=_worker, daemon=True).start()


def main() -> None:
    app = KarpathyWikiApp()
    app.mainloop()


if __name__ == "__main__":
    main()
