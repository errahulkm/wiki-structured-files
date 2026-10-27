"""
UI Theme and Aesthetics Configuration.
Defines color palettes, typography, and dark/light tokens for CustomTkinter.
"""

from typing import Dict, Any

THEME_CONFIG: Dict[str, Any] = {
    "app_name": "STM32 Karpathy-Wiki Generator",
    "window_width": 1200,
    "window_height": 820,
    "min_width": 1050,
    "min_height": 700,
    "fonts": {
        "title": ("Inter", 20, "bold"),
        "section": ("Inter", 14, "bold"),
        "body": ("Inter", 12),
        "console": ("Roboto Mono", 11)
    },
    "colors": {
        "dark": {
            "bg": "#121417",
            "card_bg": "#1e2229",
            "accent": "#00e5ff",
            "accent_hover": "#00b2cc",
            "text": "#f0f4f8",
            "subtext": "#94a3b8",
            "success": "#00e676",
            "warning": "#ffab00",
            "error": "#ff5252"
        },
        "light": {
            "bg": "#f8fafc",
            "card_bg": "#ffffff",
            "accent": "#0284c7",
            "accent_hover": "#0369a1",
            "text": "#0f172a",
            "subtext": "#64748b",
            "success": "#16a34a",
            "warning": "#d97706",
            "error": "#dc2626"
        }
    }
}
