"""
crud_workout_log.py
Full CRUD screen for the workout_log table.
Displays user names and program names via JOINs (no raw IDs in UI).
Implements two-step update process.
"""

import tkinter as tk
import customtkinter as ctk
from ui_components import (
    COLORS, FONT_FAMILY,
    make_label, make_entry, make_button, make_card, make_combo,
    make_treeview, populate_tree,
    show_info, show_error, show_warning, ask_confirm
)
from db_connection import get_connection


class WorkoutLogScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self._user_map = {}     # display_label -> user_id
        self._program_map = {}  # display_label -> program_id
        self._build_ui()
        self._load_lookups()
        self.load_data()

    # ── Layout ───────────────────────────────────────────────────────────────

    def _build_ui(self):
        make_label(self, "🏋️  יומן אימונים (Workout Log)", size=20, bold=True,
                   color=COLORS["accent_light"]).pack(anchor="w", padx=24, pady=(18, 4))
        make_label(self, "ניהול רישומי אימון – CRUD מלא עם JOINs לשמות מתאמנים ותוכניות",
                   size=12, color=COLORS["text_secondary"]).pack(anchor="w", padx=24, pady=(0, 14))

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=0)
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=3)
        content.rowconfigure(0, weight=1)

        form_card = make_card(content)
        form_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self._build_form(form_card)

        grid_card = make_card(content)
        grid_card.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        self._build_grid(grid_card)

    def _build_form(self, card):
        make_label(card, "📋  פרטי יומן אימון", size=14, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 8))

        # User dropdown
        make_label(card, "מתאמן *", size=11,
                   color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(6, 0))
        self._user_combo = make_combo(card, [], width=240)
        self._user_combo.pack(padx=16, pady=(2, 0))

        # Program dropdown
        make_label(card, "תוכנית אימון *", size=11,
                   color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(6, 0))
        self._prog_combo = make_combo(card, [], width=240)
        self._prog_combo.pack(padx=16, pady=(2, 0))

        # Numeric/text entries
        fields = [
            ("תאריך אימון * (YYYY-MM-DD)", "log_date"),
            ("משך (דקות) *", "duration_minutes"),
            ("קלוריות שנשרפו *", "total_calories_burned"),
            ("ממוצע דופק *", "average_heart_rate"),
            ("דירוג מתאמן (1-10) *", "trainee_feedback_rating"),
            ("הערות מאמן", "coach_notes"),
        ]
        self._entries = {}
        for label, key in fields:
            make_label(card, label, size=11,
                       color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(6, 0))
            e = make_entry(card, placeholder=label, width=240)
            e.pack(padx=16, pady=(2, 0))
            self._entries[key] = e

        self._pk_var = tk.StringVar(value="")
        self._pk_label = make_label(card, "", size=10, color=COLORS["warning"])
        self._pk_label.pack(padx=16, pady=(6, 0))

        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(padx=16, pady=14, fill="x")
        make_button(btn_frame, "➕ הוסף", self._insert,
                    color=COLORS["success"], width=100).pack(side="left", padx=(0, 4))
        make_button(btn_frame, "💾 שמור", self._update,
                    color=COLORS["accent"], width=100).pack(side="left", padx=(0, 4))
        make_button(btn_frame, "🗑 מחק", self._delete,
                    color=COLORS["danger"], width=70).pack(side="left")
        make_button(btn_frame, "🔄", self._clear_form,
                    color=COLORS["bg_input"], width=50).pack(side="right")

    def _build_grid(self, card):
        make_label(card, "📊  רשימת אימונים", size=14, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 8))

        cols = ("Log ID", "מתאמן", "תוכנית", "תאריך", "דקות",
                "קלוריות", "דופק", "דירוג", "הערות")
        self._tree = make_treeview(card, cols, height=22)
        self._tree.bind("<<TreeviewSelect>>", self._on_select)

    # ── Lookups ────────────────────────────────────────────────────────────

    def _load_lookups(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT user_id, first_name || ' ' || last_name FROM public.core_user ORDER BY user_id LIMIT 500"
            )
            users = cur.fetchall()
            self._user_map = {f"{uid} – {name}": uid for uid, name in users}

            cur.execute(
                "SELECT program_id, program_name FROM public.training_program ORDER BY program_id LIMIT 500"
            )
            progs = cur.fetchall()
            self._program_map = {f"{pid} – {pname}": pid for pid, pname in progs}
            conn.close()

            self._user_combo.configure(values=list(self._user_map.keys()))
            self._prog_combo.configure(values=list(self._program_map.keys()))
        except Exception as e:
            show_error("שגיאת טעינת נתוני עזר", str(e))

    # ── Data operations ───────────────────────────────────────────────────────

    def load_data(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT wl.log_id,
                       cu.user_id || ' – ' || cu.first_name || ' ' || cu.last_name,
                       tp.program_id || ' – ' || tp.program_name,
                       wl.log_date,
                       wl.duration_minutes,
                       wl.total_calories_burned,
                       wl.average_heart_rate,
                       wl.trainee_feedback_rating,
                       wl.coach_notes
                FROM public.workout_log wl
                JOIN public.core_user cu ON wl.user_id = cu.user_id
                JOIN public.training_program tp ON wl.program_id = tp.program_id
                ORDER BY wl.log_id DESC
                LIMIT 300
                """
            )
            rows = cur.fetchall()
            conn.close()
            populate_tree(self._tree, rows)
        except Exception as e:
            show_error("שגיאת מסד נתונים", str(e))

    def _on_select(self, event):
        selected = self._tree.selection()
        if not selected:
            return
        vals = self._tree.item(selected[0], "values")
        self._pk_var.set(vals[0])
        self._pk_label.configure(text=f"עורך רשומה: Log ID = {vals[0]}")

        # Fetch raw record to set combos correctly
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT wl.user_id, wl.program_id, wl.log_date,
                       wl.duration_minutes, wl.total_calories_burned,
                       wl.average_heart_rate, wl.trainee_feedback_rating,
                       wl.coach_notes
                FROM public.workout_log wl
                WHERE wl.log_id = %s
                """,
                (int(vals[0]),)
            )
            row = cur.fetchone()
            conn.close()
            if not row:
                return
            uid, pid, log_date, dur, cal, hr, rating, notes = row

            # Set user combo
            for label, user_id in self._user_map.items():
                if user_id == uid:
                    self._user_combo.set(label)
                    break

            # Set program combo
            for label, prog_id in self._program_map.items():
                if prog_id == pid:
                    self._prog_combo.set(label)
                    break

            text_vals = [str(log_date), str(dur), str(cal),
                         str(hr), str(rating), str(notes or "")]
            for key, val in zip(
                ["log_date", "duration_minutes", "total_calories_burned",
                 "average_heart_rate", "trainee_feedback_rating", "coach_notes"],
                text_vals
            ):
                e = self._entries[key]
                e.delete(0, "end")
                e.insert(0, val)
        except Exception as e:
            show_error("שגיאה בטעינת רשומה", str(e))

    def _get_ids(self):
        user_label = self._user_combo.get()
        prog_label = self._prog_combo.get()
        uid = self._user_map.get(user_label)
        pid = self._program_map.get(prog_label)
        return uid, pid

    def _clear_form(self):
        for e in self._entries.values():
            e.delete(0, "end")
        self._pk_var.set("")
        self._pk_label.configure(text="")
        self._user_combo.set("")
        self._prog_combo.set("")

    def _insert(self):
        uid, pid = self._get_ids()
        if uid is None or pid is None:
            show_warning("שדות חסרים", "בחר מתאמן ותוכנית אימון.")
            return
        v = {k: e.get().strip() for k, e in self._entries.items()}
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO public.workout_log
                    (log_id, log_date, duration_minutes, total_calories_burned,
                     average_heart_rate, trainee_feedback_rating, coach_notes,
                     program_id, user_id)
                VALUES (
                    (SELECT COALESCE(MAX(log_id), 0) + 1 FROM public.workout_log),
                    %s, %s, %s, %s, %s, %s, %s, %s
                )
                """,
                (v["log_date"], v["duration_minutes"], v["total_calories_burned"],
                 v["average_heart_rate"], v["trainee_feedback_rating"],
                 v["coach_notes"] or "", pid, uid)
            )
            conn.commit()
            conn.close()
            show_info("הצלחה", "יומן האימון נוסף בהצלחה!")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה בהכנסה", str(e))

    def _update(self):
        pk = self._pk_var.get()
        if not pk:
            show_warning("לא נבחרה רשומה", "בחר רשומה מהטבלה תחילה.")
            return
        uid, pid = self._get_ids()
        if uid is None or pid is None:
            show_warning("שדות חסרים", "בחר מתאמן ותוכנית.")
            return
        v = {k: e.get().strip() for k, e in self._entries.items()}
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE public.workout_log
                SET log_date=%s, duration_minutes=%s, total_calories_burned=%s,
                    average_heart_rate=%s, trainee_feedback_rating=%s,
                    coach_notes=%s, program_id=%s, user_id=%s
                WHERE log_id=%s
                """,
                (v["log_date"], v["duration_minutes"], v["total_calories_burned"],
                 v["average_heart_rate"], v["trainee_feedback_rating"],
                 v["coach_notes"] or "", pid, uid, int(pk))
            )
            conn.commit()
            conn.close()
            show_info("הצלחה", f"Log {pk} עודכן!")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה בעדכון", str(e))

    def _delete(self):
        pk = self._pk_var.get()
        if not pk:
            show_warning("לא נבחרה רשומה", "בחר רשומה מהטבלה.")
            return
        if not ask_confirm("מחיקה", f"למחוק Log ID {pk}?"):
            return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM public.workout_log WHERE log_id = %s", (int(pk),))
            conn.commit()
            conn.close()
            show_info("הצלחה", "הרשומה נמחקה.")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה במחיקה", str(e))
