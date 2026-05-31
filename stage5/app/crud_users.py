"""
crud_users.py
Full CRUD screen for the core_user table.
Implements the two-step update process and parameterized queries.
"""

import tkinter as tk
import customtkinter as ctk
from ui_components import (
    COLORS, FONT_FAMILY,
    make_label, make_entry, make_button, make_card,
    make_treeview, populate_tree,
    show_info, show_error, show_warning, ask_confirm
)
from db_connection import get_connection


class UsersScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self._build_ui()
        self.load_data()

    # ── Layout ───────────────────────────────────────────────────────────────

    def _build_ui(self):
        # Title
        make_label(self, "👤  ניהול מתאמנים (Users)", size=20, bold=True,
                   color=COLORS["accent_light"]).pack(anchor="w", padx=24, pady=(18, 4))
        make_label(self, "הוספה, עריכה, מחיקה ועיון ברשומות מתאמנים במערכת",
                   size=12, color=COLORS["text_secondary"]).pack(anchor="w", padx=24, pady=(0, 14))

        # ── Top: form + grid ────────────────────────────────────────────────
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=0)
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=3)
        content.rowconfigure(0, weight=1)

        # Form card
        form_card = make_card(content)
        form_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=0)
        self._build_form(form_card)

        # Grid card
        grid_card = make_card(content)
        grid_card.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=0)
        self._build_grid(grid_card)

    def _build_form(self, card):
        make_label(card, "📋  פרטי מתאמן", size=14, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 8))

        fields = [
            ("שם פרטי *", "first_name"),
            ("שם משפחה *", "last_name"),
            ("טלפון *", "phone_number"),
            ("אימייל *", "email"),
            ("תאריך הצטרפות * (YYYY-MM-DD)", "join_date"),
        ]
        self._entries = {}
        for label, key in fields:
            make_label(card, label, size=11, color=COLORS["text_secondary"]).pack(
                anchor="w", padx=16, pady=(6, 0))
            e = make_entry(card, placeholder=label, width=240)
            e.pack(padx=16, pady=(2, 0))
            self._entries[key] = e

        # Hidden PK label (shown only in edit mode)
        self._pk_var = tk.StringVar(value="")
        self._pk_label = make_label(card, "", size=10,
                                    color=COLORS["warning"])
        self._pk_label.pack(padx=16, pady=(6, 0))

        # Buttons
        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(padx=16, pady=14, fill="x")

        make_button(btn_frame, "➕ הוסף", self._insert,
                    color=COLORS["success"], width=110).pack(side="left", padx=(0, 6))
        make_button(btn_frame, "💾 שמור עדכון", self._update,
                    color=COLORS["accent"], width=110).pack(side="left", padx=(0, 6))
        make_button(btn_frame, "🗑 מחק", self._delete,
                    color=COLORS["danger"], width=80).pack(side="left")
        make_button(btn_frame, "🔄 נקה", self._clear_form,
                    color=COLORS["bg_input"], width=80).pack(side="right")

        # Search
        make_label(card, "🔍 חיפוש לפי שם:", size=11,
                   color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(10, 0))
        self._search_var = tk.StringVar()
        self._search_var.trace("w", lambda *_: self.load_data())
        search = ctk.CTkEntry(card, textvariable=self._search_var,
                               placeholder_text="חפש שם...",
                               width=240, height=34,
                               fg_color=COLORS["bg_input"],
                               border_color=COLORS["border"],
                               text_color=COLORS["text_primary"])
        search.pack(padx=16, pady=(2, 14))

    def _build_grid(self, card):
        make_label(card, "📊  רשימת מתאמנים", size=14, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 8))

        cols = ("ID", "שם פרטי", "שם משפחה", "טלפון", "אימייל", "תאריך הצטרפות")
        self._tree = make_treeview(card, cols, height=22)
        self._tree.bind("<<TreeviewSelect>>", self._on_select)

    # ── Data operations ───────────────────────────────────────────────────────

    def load_data(self):
        search = self._search_var.get().strip() if hasattr(self, "_search_var") else ""
        try:
            conn = get_connection()
            cur = conn.cursor()
            if search:
                cur.execute(
                    """
                    SELECT user_id, first_name, last_name, phone_number, email, join_date
                    FROM public.core_user
                    WHERE first_name ILIKE %s OR last_name ILIKE %s
                    ORDER BY user_id
                    LIMIT 200
                    """,
                    (f"%{search}%", f"%{search}%")
                )
            else:
                cur.execute(
                    """
                    SELECT user_id, first_name, last_name, phone_number, email, join_date
                    FROM public.core_user
                    ORDER BY user_id
                    LIMIT 200
                    """
                )
            rows = cur.fetchall()
            conn.close()
            populate_tree(self._tree, rows)
        except Exception as e:
            show_error("שגיאת מסד נתונים", str(e))

    def _on_select(self, event):
        """Two-step update: selecting a row populates the form."""
        selected = self._tree.selection()
        if not selected:
            return
        values = self._tree.item(selected[0], "values")
        # values: (ID, first_name, last_name, phone, email, join_date)
        self._pk_var.set(values[0])
        self._pk_label.configure(text=f"עורך רשומה: ID = {values[0]}")
        keys = ["first_name", "last_name", "phone_number", "email", "join_date"]
        for key, val in zip(keys, values[1:]):
            e = self._entries[key]
            e.delete(0, "end")
            e.insert(0, val)

    def _get_form_values(self):
        return {k: e.get().strip() for k, e in self._entries.items()}

    def _clear_form(self):
        for e in self._entries.values():
            e.delete(0, "end")
        self._pk_var.set("")
        self._pk_label.configure(text="")

    def _insert(self):
        v = self._get_form_values()
        if not all([v["first_name"], v["last_name"], v["phone_number"],
                    v["email"], v["join_date"]]):
            show_warning("שדות חסרים", "נא למלא את כל השדות המסומנים ב-*")
            return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO public.core_user
                    (user_id, first_name, last_name, phone_number, email, join_date)
                VALUES (
                    (SELECT COALESCE(MAX(user_id), 0) + 1 FROM public.core_user),
                    %s, %s, %s, %s, %s
                )
                """,
                (v["first_name"], v["last_name"], v["phone_number"],
                 v["email"], v["join_date"])
            )
            conn.commit()
            conn.close()
            show_info("הצלחה", "המתאמן נוסף בהצלחה!")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה בהכנסת נתונים", str(e))

    def _update(self):
        pk = self._pk_var.get()
        if not pk:
            show_warning("לא נבחרה רשומה",
                         "בחר תחילה רשומה מהטבלה, ולאחר מכן ערוך ולחץ 'שמור עדכון'.")
            return
        v = self._get_form_values()
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE public.core_user
                SET first_name=%s, last_name=%s, phone_number=%s,
                    email=%s, join_date=%s
                WHERE user_id=%s
                """,
                (v["first_name"], v["last_name"], v["phone_number"],
                 v["email"], v["join_date"], int(pk))
            )
            conn.commit()
            conn.close()
            show_info("הצלחה", f"רשומה {pk} עודכנה בהצלחה!")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה בעדכון", str(e))

    def _delete(self):
        pk = self._pk_var.get()
        if not pk:
            show_warning("לא נבחרה רשומה", "בחר תחילה רשומה מהטבלה.")
            return
        if not ask_confirm("אישור מחיקה",
                           f"האם אתה בטוח שברצונך למחוק מתאמן ID {pk}?\n"
                           "שים לב: מחיקה תסיר גם נתונים קשורים (אם אין מגבלות FK)."):
            return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM public.core_user WHERE user_id = %s", (int(pk),))
            conn.commit()
            conn.close()
            show_info("הצלחה", f"מתאמן {pk} נמחק.")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה במחיקה", str(e))
