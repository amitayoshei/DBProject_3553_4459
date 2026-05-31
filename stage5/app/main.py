"""
main.py
PowerGym Pro – Main application entry point.
Builds the root window, sidebar navigation, and content area.
Run with:  python main.py  (from inside stage5/app/)
"""

import sys
import os

# Ensure this directory is on the path for relative imports
sys.path.insert(0, os.path.dirname(__file__))

import customtkinter as ctk
import tkinter as tk
from ui_components import COLORS, FONT_FAMILY, make_label

# ── Screens (imported lazily to keep startup fast) ───────────────────────────
from dashboard import DashboardScreen
from crud_users import UsersScreen
from crud_workout_log import WorkoutLogScreen
from crud_lockers import LockersScreen
from crud_body_measurement import BodyMeasurementScreen
from crud_subscriptions import SubscriptionsScreen
from advanced_operations import AdvancedOperationsScreen


# ── Configure CustomTkinter global theme ─────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PowerGymApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🏋️ PowerGym Pro – מערכת ניהול מכון כושר")
        self.geometry("1400x820")
        self.minsize(1100, 680)
        self.configure(fg_color=COLORS["bg_dark"])

        # Screen registry: key → (constructor, title, icon)
        self._screen_registry = {
            "dashboard":        (DashboardScreen,         "דשבורד ראשי",           "🏠"),
            "users":            (UsersScreen,              "ניהול מתאמנים",         "👤"),
            "workout_log":      (WorkoutLogScreen,         "יומן אימונים",           "🏋️"),
            "lockers":          (LockersScreen,            "ניהול לוקרים",          "🔐"),
            "body_measurement": (BodyMeasurementScreen,    "מדידות גוף",            "📏"),
            "subscriptions":    (SubscriptionsScreen,      "מנויים",                "📄"),
            "advanced":         (AdvancedOperationsScreen, "פעולות מתקדמות",        "⚡"),
        }
        self._active_screen = None
        self._sidebar_buttons = {}

        self._build_layout()
        self._navigate("dashboard")

    # ── Layout ───────────────────────────────────────────────────────────────

    def _build_layout(self):
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Sidebar
        sidebar = ctk.CTkFrame(self, width=220, fg_color=COLORS["sidebar"],
                                corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)
        self._build_sidebar(sidebar)

        # Content area
        self._content = ctk.CTkFrame(self, fg_color=COLORS["bg_dark"],
                                      corner_radius=0)
        self._content.grid(row=0, column=1, sticky="nsew")
        self._content.rowconfigure(0, weight=1)
        self._content.columnconfigure(0, weight=1)

    def _build_sidebar(self, sidebar):
        # Logo
        logo_frame = ctk.CTkFrame(sidebar, fg_color=COLORS["bg_dark"],
                                   corner_radius=12)
        logo_frame.pack(fill="x", padx=12, pady=(16, 8))
        make_label(logo_frame, "💪", size=30).pack(pady=(10, 0))
        make_label(logo_frame, "PowerGym Pro", size=14, bold=True,
                   color=COLORS["accent_light"]).pack(pady=(2, 4))
        make_label(logo_frame, "מערכת ניהול מכון כושר", size=9,
                   color=COLORS["text_secondary"]).pack(pady=(0, 10))

        # Separator
        sep = ctk.CTkFrame(sidebar, height=1, fg_color=COLORS["border"])
        sep.pack(fill="x", padx=12, pady=(0, 12))

        # Nav buttons
        nav_items = [
            ("dashboard",        "🏠  דשבורד ראשי"),
            ("users",            "👤  מתאמנים"),
            ("workout_log",      "🏋️  יומן אימונים"),
            ("lockers",          "🔐  לוקרים"),
            ("body_measurement", "📏  מדידות גוף"),
            ("subscriptions",    "📄  מנויים"),
            ("advanced",         "⚡  פעולות מתקדמות"),
        ]

        for key, label in nav_items:
            btn = ctk.CTkButton(
                sidebar,
                text=label,
                command=lambda k=key: self._navigate(k),
                width=196, height=44,
                corner_radius=8,
                fg_color="transparent",
                hover_color=COLORS["sidebar_hover"],
                text_color=COLORS["text_secondary"],
                font=(FONT_FAMILY, 12),
                anchor="w",
            )
            btn.pack(padx=12, pady=2)
            self._sidebar_buttons[key] = btn

        # Bottom info
        info_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        info_frame.pack(side="bottom", fill="x", padx=12, pady=16)
        sep2 = ctk.CTkFrame(info_frame, height=1, fg_color=COLORS["border"])
        sep2.pack(fill="x", pady=(0, 8))
        make_label(info_frame, "Supabase PostgreSQL", size=9,
                   color=COLORS["text_secondary"]).pack()
        make_label(info_frame, "Phase 5 – Academic Project", size=9,
                   color=COLORS["text_secondary"]).pack(pady=(2, 0))

    # ── Navigation ────────────────────────────────────────────────────────────

    def _navigate(self, screen_key: str):
        if screen_key not in self._screen_registry:
            return

        # Highlight active sidebar button
        for key, btn in self._sidebar_buttons.items():
            if key == screen_key:
                btn.configure(
                    fg_color=COLORS["accent"],
                    text_color=COLORS["text_primary"],
                    font=(FONT_FAMILY, 12, "bold"),
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=COLORS["text_secondary"],
                    font=(FONT_FAMILY, 12),
                )

        # Destroy previous screen
        for widget in self._content.winfo_children():
            widget.destroy()

        # Instantiate new screen
        ScreenClass, title, icon = self._screen_registry[screen_key]

        if screen_key == "dashboard":
            screen = ScreenClass(self._content, navigate_callback=self._navigate)
        else:
            screen = ScreenClass(self._content)

        screen.grid(row=0, column=0, sticky="nsew")
        self._active_screen = screen
        self.title(f"🏋️ PowerGym Pro – {icon} {title}")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = PowerGymApp()
    app.mainloop()
