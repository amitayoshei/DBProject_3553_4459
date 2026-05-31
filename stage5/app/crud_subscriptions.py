"""
crud_subscriptions.py
Full CRUD screen for the subscription table.
Shows user full names via JOIN (no raw IDs).
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


class SubscriptionsScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self._user_map = {}
        self._build_ui()
        self._load_lookups()
        self.load_data()

    def _build_ui(self):
        make_label(self, "📄  ניהול מנויים (Subscriptions)", size=20, bold=True,
                   color=COLORS["accent_light"]).pack(anchor="w", padx=24, pady=(18, 4))
        make_label(self, "ניהול חוזי מנויים ותשלומים של מתאמנים",
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
        make_label(card, "📋  פרטי מנוי", size=14, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 8))

        make_label(card, "מתאמן *", size=11,
                   color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(6, 0))
        self._user_combo = make_combo(card, [], width=240)
        self._user_combo.pack(padx=16, pady=(2, 0))

        fields = [
            ("תאריך רכישה * (YYYY-MM-DD)", "purchase_date"),
            ("תאריך פקיעה * (YYYY-MM-DD)", "expiration_date"),
            ("עלות כוללת (₪) *", "total_cost"),
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

        # Stats panel
        stats_card = make_card(card)
        stats_card.pack(padx=16, pady=(14, 14), fill="x")
        make_label(stats_card, "📈 סטטיסטיקות מהירות", size=12, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=12, pady=(8, 4))
        self._stats_label = make_label(stats_card, "לחץ 'רענן' לעדכון",
                                        size=11, color=COLORS["text_secondary"])
        self._stats_label.pack(anchor="w", padx=12, pady=(0, 4))
        make_button(stats_card, "🔄 רענן סטטיסטיקות",
                    self._refresh_stats, width=200, height=30).pack(pady=(4, 10))

    def _build_grid(self, card):
        make_label(card, "📊  רשימת מנויים", size=14, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 8))
        cols = ("חוזה #", "מתאמן", "רכישה", "פקיעה", "עלות")
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
                SELECT s.contract_number,
                       cu.user_id || ' – ' || cu.first_name || ' ' || cu.last_name,
                       s.purchase_date,
                       s.expiration_date,
                       s.total_cost
                FROM public.subscription s
                JOIN public.core_user cu ON s.user_id = cu.user_id
                ORDER BY s.contract_number DESC
                LIMIT 300
                """
            )
            rows = cur.fetchall()
            conn.close()
            populate_tree(self._tree, rows)
        except Exception as e:
            show_error("שגיאת מסד נתונים", str(e))

    def _refresh_stats(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT COUNT(*) AS total,
                       ROUND(AVG(total_cost), 2) AS avg_cost,
                       SUM(total_cost) AS total_revenue
                FROM public.subscription
                WHERE expiration_date >= DATE '2024-01-01'
                """
            )
            row = cur.fetchone()
            conn.close()
            if row:
                self._stats_label.configure(
                    text=f"מנויים פעילים: {row[0]}  |  עלות ממוצעת: ₪{row[1]}  |  סה\"כ הכנסות: ₪{row[2]}"
                )
        except Exception as e:
            show_error("שגיאה", str(e))

    def _on_select(self, event):
        selected = self._tree.selection()
        if not selected:
            return
        vals = self._tree.item(selected[0], "values")
        self._pk_var.set(vals[0])
        self._pk_label.configure(text=f"עורך חוזה: #{vals[0]}")

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT user_id, purchase_date, expiration_date, total_cost FROM public.subscription WHERE contract_number=%s",
                (int(vals[0]),)
            )
            row = cur.fetchone()
            conn.close()
            if not row:
                return
            uid, pd, ed, cost = row
            for label, user_id in self._user_map.items():
                if user_id == uid:
                    self._user_combo.set(label)
                    break
            for key, val in zip(["purchase_date", "expiration_date", "total_cost"],
                                 [str(pd), str(ed), str(cost)]):
                self._entries[key].delete(0, "end")
                self._entries[key].insert(0, val)
        except Exception as e:
            show_error("שגיאה", str(e))

    def _clear_form(self):
        for e in self._entries.values():
            e.delete(0, "end")
        self._user_combo.set("")
        self._pk_var.set("")
        self._pk_label.configure(text="")

    def _insert(self):
        uid = self._user_map.get(self._user_combo.get())
        if uid is None:
            show_warning("שדה חסר", "בחר מתאמן.")
            return
        v = {k: e.get().strip() for k, e in self._entries.items()}
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO public.subscription
                    (contract_number, purchase_date, expiration_date, total_cost, user_id)
                VALUES (
                    (SELECT COALESCE(MAX(contract_number),0)+1 FROM public.subscription),
                    %s, %s, %s, %s
                )
                """,
                (v["purchase_date"], v["expiration_date"], v["total_cost"], uid)
            )
            conn.commit()
            conn.close()
            show_info("הצלחה", "המנוי נוסף!")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה", str(e))

    def _update(self):
        pk = self._pk_var.get()
        if not pk:
            show_warning("לא נבחרה רשומה", "בחר מנוי מהטבלה.")
            return
        uid = self._user_map.get(self._user_combo.get())
        if uid is None:
            show_warning("שדה חסר", "בחר מתאמן.")
            return
        v = {k: e.get().strip() for k, e in self._entries.items()}
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE public.subscription
                SET purchase_date=%s, expiration_date=%s, total_cost=%s, user_id=%s
                WHERE contract_number=%s
                """,
                (v["purchase_date"], v["expiration_date"], v["total_cost"], uid, int(pk))
            )
            conn.commit()
            conn.close()
            show_info("הצלחה", f"חוזה {pk} עודכן!")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה", str(e))

    def _delete(self):
        pk = self._pk_var.get()
        if not pk:
            show_warning("לא נבחרה רשומה", "בחר מנוי.")
            return
        if not ask_confirm("מחיקה", f"למחוק חוזה #{pk}?"):
            return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM public.subscription WHERE contract_number = %s", (int(pk),))
            conn.commit()
            conn.close()
            show_info("הצלחה", "נמחק.")
            self._clear_form()
            self.load_data()
        except Exception as e:
            show_error("שגיאה", str(e))
