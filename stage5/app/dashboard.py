"""
dashboard.py
Main dashboard / landing screen for PowerGym Pro.
Shows KPI stats and a welcome panel.
"""

import tkinter as tk
import customtkinter as ctk
from ui_components import (
    COLORS, FONT_FAMILY,
    make_label, make_button, make_card,
    show_error
)
from db_connection import get_connection


class DashboardScreen(ctk.CTkFrame):
    def __init__(self, parent, navigate_callback):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self._navigate = navigate_callback
        self._build_ui()
        self._load_stats()

    def _build_ui(self):
        # ── Hero header ──────────────────────────────────────────────────────
        hero = ctk.CTkFrame(self, fg_color=COLORS["sidebar"], corner_radius=16)
        hero.pack(fill="x", padx=24, pady=(20, 16))

        make_label(hero, "🏋️‍♂️  PowerGym Pro", size=28, bold=True,
                   color=COLORS["accent_light"]).pack(anchor="w", padx=24, pady=(18, 4))
        make_label(hero, "מערכת מתקדמת לניהול מתאמנים, מדדי גוף ותוכניות אימון",
                   size=13, color=COLORS["text_secondary"]).pack(anchor="w", padx=24, pady=(0, 18))

        # Badge row
        badge_row = ctk.CTkFrame(hero, fg_color="transparent")
        badge_row.pack(anchor="w", padx=24, pady=(0, 18))
        for text, color in [
            ("🐘 PostgreSQL", "#4169E1"),
            ("🌿 Supabase", "#3ECF8E"),
            ("🐍 Python 3", "#3776AB"),
            ("🖥️ CustomTkinter", "#6C63FF"),
        ]:
            b = ctk.CTkLabel(badge_row, text=text,
                              fg_color=color, corner_radius=12,
                              padx=10, pady=4,
                              font=(FONT_FAMILY, 11, "bold"),
                              text_color=COLORS["text_primary"])
            b.pack(side="left", padx=(0, 8))

        # ── KPI row ─────────────────────────────────────────────────────────
        kpi_row = ctk.CTkFrame(self, fg_color="transparent")
        kpi_row.pack(fill="x", padx=24, pady=(0, 16))
        for i in range(4):
            kpi_row.columnconfigure(i, weight=1)

        self._kpi_labels = []
        kpi_configs = [
            ("👥", "מתאמנים", "0", COLORS["accent"]),
            ("📋", "יומני אימון", "0", COLORS["success"]),
            ("🔐", "לוקרים", "0", COLORS["warning"]),
            ("📄", "מנויים פעילים", "0", "#EC4899"),
        ]
        for col, (icon, title, val, color) in enumerate(kpi_configs):
            card = make_card(kpi_row)
            card.grid(row=0, column=col, padx=6, pady=0, sticky="ew")
            make_label(card, icon, size=24).pack(pady=(14, 2))
            make_label(card, title, size=11,
                       color=COLORS["text_secondary"]).pack()
            lbl = make_label(card, val, size=26, bold=True, color=color)
            lbl.pack(pady=(2, 14))
            self._kpi_labels.append(lbl)

        # ── Quick-nav grid ───────────────────────────────────────────────────
        make_label(self, "🚀  ניווט מהיר", size=15, bold=True,
                   color=COLORS["text_primary"]).pack(anchor="w", padx=24, pady=(6, 8))

        nav_grid = ctk.CTkFrame(self, fg_color="transparent")
        nav_grid.pack(fill="x", padx=24, pady=(0, 16))
        for i in range(4):
            nav_grid.columnconfigure(i, weight=1)

        nav_items = [
            ("👤 ניהול מתאמנים", "users", COLORS["accent"]),
            ("🏋️ יומן אימונים", "workout_log", "#8B5CF6"),
            ("🔐 ניהול לוקרים", "lockers", COLORS["warning"]),
            ("📏 מדידות גוף", "body_measurement", COLORS["success"]),
            ("📄 מנויים", "subscriptions", "#EC4899"),
            ("⚡ פעולות מתקדמות", "advanced", "#F97316"),
        ]
        for idx, (label, screen_key, color) in enumerate(nav_items):
            col = idx % 4
            row = idx // 4
            btn = ctk.CTkButton(
                nav_grid, text=label,
                command=lambda k=screen_key: self._navigate(k),
                height=72, corner_radius=12,
                font=(FONT_FAMILY, 13, "bold"),
                fg_color=color, hover_color=COLORS["accent_hover"]
            )
            btn.grid(row=row, column=col, padx=6, pady=6, sticky="ew")

        # ── Recent workout log preview ────────────────────────────────────────
        make_label(self, "📈  אימונים אחרונים", size=15, bold=True,
                   color=COLORS["text_primary"]).pack(anchor="w", padx=24, pady=(4, 8))

        from ui_components import make_treeview, populate_tree
        preview_card = make_card(self)
        preview_card.pack(fill="both", expand=True, padx=24, pady=(0, 20))
        cols = ("מתאמן", "תוכנית", "תאריך", "דקות", "קלוריות", "דירוג")
        self._preview_tree = make_treeview(preview_card, cols, height=7)
        self._preview_tree_ref = (preview_card, cols)

    def _load_stats(self):
        try:
            conn = get_connection()
            cur = conn.cursor()

            # KPI counts
            cur.execute("SELECT COUNT(*) FROM public.core_user")
            users = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM public.workout_log")
            logs = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM public.locker WHERE user_id IS NOT NULL")
            lockers = cur.fetchone()[0]

            cur.execute(
                "SELECT COUNT(*) FROM public.subscription WHERE expiration_date >= DATE '2024-01-01'"
            )
            subs = cur.fetchone()[0]

            for lbl, val in zip(self._kpi_labels, [users, logs, lockers, subs]):
                lbl.configure(text=f"{val:,}")

            # Recent workouts
            cur.execute(
                """
                SELECT cu.first_name || ' ' || cu.last_name,
                       tp.program_name,
                       wl.log_date,
                       wl.duration_minutes,
                       wl.total_calories_burned,
                       wl.trainee_feedback_rating
                FROM public.workout_log wl
                JOIN public.core_user cu ON wl.user_id = cu.user_id
                JOIN public.training_program tp ON wl.program_id = tp.program_id
                ORDER BY wl.log_date DESC, wl.log_id DESC
                LIMIT 20
                """
            )
            rows = cur.fetchall()
            conn.close()

            from ui_components import populate_tree
            populate_tree(self._preview_tree, rows)

        except Exception as e:
            show_error("שגיאת חיבור", f"לא ניתן לטעון נתונים:\n{str(e)}")
