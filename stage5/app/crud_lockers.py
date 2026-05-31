"""
crud_lockers.py
Full CRUD screen for the locker table.
Displays user names via JOIN; supports NULL (unoccupied) lockers.
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


class LockersScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self._user_map = {}
        self._build_ui()
        self._load_lookups()
        self.load_data()

    def _build_ui(self):
        make_label(self, "🔐  ניהול לוקרים (Lockers)", size=20, bold=True,
                   color=COLORS["accent_light"]).pack(anchor="w", padx=24, pady=(18, 4))
        make_label(self, "הקצאה, עריכה ומחיקה של לוקרים – כולל תצוגת שמות מתאמנים",
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
        make_label(card, "📋  פרטי לוקר", size=14, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 8))

        make_label(card, "אזור מיקום *", size=11,
                   color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(6, 0))
        self._entry_zone = make_entry(card, placeholder="לדוגמה: Men's Locker Room", width=240)
        self._entry_zone.pack(padx=16, pady=(2, 0))

        make_label(card, "תאריך סיום השכרה (YYYY-MM-DD)", size=11,
                   color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(6, 0))
        self._entry_end = make_entry(card, placeholder="השאר ריק ללוקר פנוי", width=240)
        self._entry_end.pack(padx=16, pady=(2, 0))

        make_label(card, "מתאמן מוקצה (השאר ריק = פנוי)", size=11,
                   color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(6, 0))
        self._user_combo = make_combo(card, ["— פנוי —"], width=240)
        self._user_combo.pack(padx=16, pady=(2, 0))

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
        make_label(card, "📊  רשימת לוקרים", size=14, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 8))
        cols = ("Locker ID", "אזור", "סיום השכרה", "מתאמן מוקצה")
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
            values = ["— פנוי —"] + list(self._user_map.keys())
            self._user_combo.configure(values=values)
        except Exception as e:
            show_error("שגיאה בטעינת משתמשים", str(e))

    def load_data(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT l.locker_id,
                       l.location_zone,
                       COALESCE(l.rental_end_date::TEXT, 'פנוי'),
                       COALESCE(cu.user_id::TEXT || ' – ' || cu.first_name || ' ' || cu.last_name, '— פנוי —')
                FROM public.locker l
                LEFT JOIN public.core_user cu ON l.user_id = cu.user_id
                ORDER BY l.locker_id
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
        self._pk_label.configure(text=f"עורך לוקר: ID = {vals[0]}")

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT location_zone, rental_end_date, user_id FROM public.locker WHERE locker_id = %s",
                (int(vals[0]),)
            )
            row = cur.fetchone()
            conn.close()
            if not row:
                return
            zone, end_date, uid = row

            self._entry_zone.delete(0, "end")
            self._entry_zone.insert(0, zone or "")
            self._entry_end.delete(0, "end")
            self._entry_end.insert(0, str(end_date) if end_date else "")

            if uid is None:
                self._user_combo.set("— פנוי —")
            else:
                for label, user_id in self._user_map.items():
                    if user_id == uid:
                        self._user_combo.set(label)
                        break
        except Exception as e:
            show_error("שגיאה", str(e))

    def _clear_form(self):
        self._entry_zone.delete(0, "end")
        self._entry_end.delete(0, "end")
        self._user_combo.set("— פנוי —")
        self._pk_var.set("")
        self._pk_label.configure(text="")

    def _get_user_id(self):
        label = self._user_combo.get()
        if label == "— פנוי —" or label == "":
            return None
        return self._user_map.get(label)

    def _insert(self):
        zone = self._entry_zone.get().strip()
        end_date = self._entry_end.get().strip() or None
        uid = self._get_user_id()
        if not zone:
            show_warning("שדה חסר", "נא להזין אזור מיקום.")
            return
        if (uid is None) != (end_date is None):
            show_warning("אילוץ לוקר",
                         "לוקר תפוס דורש גם מתאמן וגם תאריך סיום השכרה.\n"
                         "לוקר פנוי – השאר שניהם ריקים.")
            return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO public.locker (locker_id, location_zone, rental_end_date, user_id)
                VALUES (
                    (SELECT COALESCE(MAX(locker_id), 0) + 1 FROM public.locker),
                    %s, %s, %s
                )
                """,
                (zone, end_date, uid)
            )
            conn.commit()
            conn.close()
            show_info("הצלחה", "הלוקר נוסף בהצלחה!")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה בהכנסה", str(e))

    def _update(self):
        pk = self._pk_var.get()
        if not pk:
            show_warning("לא נבחרה רשומה", "בחר לוקר מהטבלה תחילה.")
            return
        zone = self._entry_zone.get().strip()
        end_date = self._entry_end.get().strip() or None
        uid = self._get_user_id()
        if (uid is None) != (end_date is None):
            show_warning("אילוץ", "לוקר תפוס – חייב מתאמן + תאריך. פנוי – שניהם ריקים.")
            return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE public.locker
                SET location_zone=%s, rental_end_date=%s, user_id=%s
                WHERE locker_id=%s
                """,
                (zone, end_date, uid, int(pk))
            )
            conn.commit()
            conn.close()
            show_info("הצלחה", f"לוקר {pk} עודכן!")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה בעדכון", str(e))

    def _delete(self):
        pk = self._pk_var.get()
        if not pk:
            show_warning("לא נבחרה רשומה", "בחר לוקר מהטבלה.")
            return
        if not ask_confirm("מחיקה", f"למחוק לוקר {pk}?"):
            return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM public.locker WHERE locker_id = %s", (int(pk),))
            conn.commit()
            conn.close()
            show_info("הצלחה", "הלוקר נמחק.")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה במחיקה", str(e))
