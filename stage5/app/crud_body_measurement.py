"""
crud_body_measurement.py
Full CRUD screen for the body_measurement table.
Uses JOINs to show user full names instead of raw user_id.
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


class BodyMeasurementScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self._user_map = {}
        self._build_ui()
        self._load_lookups()
        self.load_data()

    def _build_ui(self):
        make_label(self, "📏  מדידות גוף (Body Measurements)", size=20, bold=True,
                   color=COLORS["accent_light"]).pack(anchor="w", padx=24, pady=(18, 4))
        make_label(self, "מעקב גוף מלא – משקל, שומן, מסת שריר, BMI ועוד",
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
        make_label(card, "📋  פרטי מדידה", size=14, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 8))

        make_label(card, "מתאמן *", size=11,
                   color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(6, 0))
        self._user_combo = make_combo(card, [], width=240)
        self._user_combo.pack(padx=16, pady=(2, 0))

        fields = [
            ("תאריך מדידה * (YYYY-MM-DD)", "measurement_date"),
            ("משקל (ק\"ג) *", "weight_kg"),
            ("אחוז שומן *", "fat_percentage"),
            ("מסת שריר (ק\"ג) *", "muscle_mass_kg"),
            ("היקף מותן (ס\"מ) *", "waist_circumference_cm"),
            ("היקף כתפיים (ס\"מ) *", "shoulder_circumference_cm"),
            ("ציון BMI *", "bmi_score"),
            ("גובה (ס\"מ) *", "height_cm"),
        ]
        self._entries = {}
        for label, key in fields:
            make_label(card, label, size=11,
                       color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(4, 0))
            e = make_entry(card, placeholder=label, width=240)
            e.pack(padx=16, pady=(2, 0))
            self._entries[key] = e

        self._pk_var = tk.StringVar(value="")
        self._pk_label = make_label(card, "", size=10, color=COLORS["warning"])
        self._pk_label.pack(padx=16, pady=(4, 0))

        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(padx=16, pady=12, fill="x")
        make_button(btn_frame, "➕ הוסף", self._insert,
                    color=COLORS["success"], width=100).pack(side="left", padx=(0, 4))
        make_button(btn_frame, "💾 שמור", self._update,
                    color=COLORS["accent"], width=100).pack(side="left", padx=(0, 4))
        make_button(btn_frame, "🗑 מחק", self._delete,
                    color=COLORS["danger"], width=70).pack(side="left")
        make_button(btn_frame, "🔄", self._clear_form,
                    color=COLORS["bg_input"], width=50).pack(side="right")

    def _build_grid(self, card):
        make_label(card, "📊  היסטוריית מדידות", size=14, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 8))
        cols = ("ID", "מתאמן", "תאריך", "משקל", "שומן%", "שריר", "מותן", "כתפיים", "BMI", "גובה")
        self._tree = make_treeview(card, cols, height=22)
        self._tree.bind("<<TreeviewSelect>>", self._on_select)

    def _load_lookups(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT user_id, first_name || ' ' || last_name FROM public.core_user ORDER BY user_id LIMIT 500"
            )
            users = cur.fetchall()
            conn.close()
            self._user_map = {f"{uid} – {name}": uid for uid, name in users}
            self._user_combo.configure(values=list(self._user_map.keys()))
        except Exception as e:
            show_error("שגיאה", str(e))

    def load_data(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT bm.measurement_id,
                       cu.user_id || ' – ' || cu.first_name || ' ' || cu.last_name,
                       bm.measurement_date,
                       bm.weight_kg,
                       bm.fat_percentage,
                       bm.muscle_mass_kg,
                       bm.waist_circumference_cm,
                       bm.shoulder_circumference_cm,
                       bm.bmi_score,
                       bm.height_cm
                FROM public.body_measurement bm
                JOIN public.core_user cu ON bm.user_id = cu.user_id
                ORDER BY bm.measurement_id DESC
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
        self._pk_label.configure(text=f"עורך מדידה: ID = {vals[0]}")

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT user_id, measurement_date, weight_kg, fat_percentage,
                       muscle_mass_kg, waist_circumference_cm, shoulder_circumference_cm,
                       bmi_score, height_cm
                FROM public.body_measurement WHERE measurement_id = %s
                """,
                (int(vals[0]),)
            )
            row = cur.fetchone()
            conn.close()
            if not row:
                return
            uid = row[0]
            for label, user_id in self._user_map.items():
                if user_id == uid:
                    self._user_combo.set(label)
                    break

            field_keys = ["measurement_date", "weight_kg", "fat_percentage",
                          "muscle_mass_kg", "waist_circumference_cm",
                          "shoulder_circumference_cm", "bmi_score", "height_cm"]
            for key, val in zip(field_keys, row[1:]):
                e = self._entries[key]
                e.delete(0, "end")
                e.insert(0, str(val) if val is not None else "")
        except Exception as e:
            show_error("שגיאה", str(e))

    def _clear_form(self):
        for e in self._entries.values():
            e.delete(0, "end")
        self._user_combo.set("")
        self._pk_var.set("")
        self._pk_label.configure(text="")

    def _collect(self):
        uid = self._user_map.get(self._user_combo.get())
        v = {k: e.get().strip() for k, e in self._entries.items()}
        return uid, v

    def _insert(self):
        uid, v = self._collect()
        if uid is None:
            show_warning("שדה חסר", "בחר מתאמן.")
            return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO public.body_measurement
                    (measurement_id, measurement_date, weight_kg, fat_percentage,
                     muscle_mass_kg, waist_circumference_cm, shoulder_circumference_cm,
                     bmi_score, height_cm, user_id)
                VALUES (
                    (SELECT COALESCE(MAX(measurement_id),0)+1 FROM public.body_measurement),
                    %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
                """,
                (v["measurement_date"], v["weight_kg"], v["fat_percentage"],
                 v["muscle_mass_kg"], v["waist_circumference_cm"],
                 v["shoulder_circumference_cm"], v["bmi_score"], v["height_cm"], uid)
            )
            conn.commit()
            conn.close()
            show_info("הצלחה", "המדידה נוספה!")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה", str(e))

    def _update(self):
        pk = self._pk_var.get()
        if not pk:
            show_warning("לא נבחרה רשומה", "בחר מדידה מהטבלה.")
            return
        uid, v = self._collect()
        if uid is None:
            show_warning("שדה חסר", "בחר מתאמן.")
            return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE public.body_measurement
                SET measurement_date=%s, weight_kg=%s, fat_percentage=%s,
                    muscle_mass_kg=%s, waist_circumference_cm=%s,
                    shoulder_circumference_cm=%s, bmi_score=%s, height_cm=%s, user_id=%s
                WHERE measurement_id=%s
                """,
                (v["measurement_date"], v["weight_kg"], v["fat_percentage"],
                 v["muscle_mass_kg"], v["waist_circumference_cm"],
                 v["shoulder_circumference_cm"], v["bmi_score"], v["height_cm"],
                 uid, int(pk))
            )
            conn.commit()
            conn.close()
            show_info("הצלחה", f"מדידה {pk} עודכנה!")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה", str(e))

    def _delete(self):
        pk = self._pk_var.get()
        if not pk:
            show_warning("לא נבחרה רשומה", "בחר מדידה.")
            return
        if not ask_confirm("מחיקה", f"למחוק מדידה {pk}?"):
            return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM public.body_measurement WHERE measurement_id = %s", (int(pk),))
            conn.commit()
            conn.close()
            show_info("הצלחה", "נמחק.")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה", str(e))
