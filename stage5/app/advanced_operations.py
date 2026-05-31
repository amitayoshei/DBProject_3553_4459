"""
advanced_operations.py
Advanced Operations screen integrating:
  - 2 complex SELECT queries from Phase B (README שלב ב')
  - 2 stored functions  from Phase D: fn_user_workout_stats, fn_trainee_progress_cursor
  - 2 stored procedures from Phase D: proc_award_achieved_goals, proc_extend_expiring_lockers
"""

import tkinter as tk
import customtkinter as ctk
from ui_components import (
    COLORS, FONT_FAMILY,
    make_label, make_entry, make_button, make_card, make_combo,
    make_treeview, populate_tree,
    show_info, show_error, show_warning, show_procedure_result
)
from db_connection import get_connection


class AdvancedOperationsScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self._build_ui()

    def _build_ui(self):
        make_label(self, "⚡  פעולות מתקדמות", size=20, bold=True,
                   color=COLORS["accent_light"]).pack(anchor="w", padx=24, pady=(18, 4))
        make_label(self,
                   "שאילתות מורכבות מ-שלב ב' | פונקציות מ-שלב ד' | פרוצדורות מ-שלב ד'",
                   size=12, color=COLORS["text_secondary"]).pack(anchor="w", padx=24, pady=(0, 14))

        # Scrollable container
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=20, pady=0)

        # ── Section 1: Complex Queries (Phase B) ─────────────────────────────
        self._section_header(scroll, "🔍  שאילתות מורכבות (Phase B)")

        q1_card = make_card(scroll)
        q1_card.pack(fill="x", pady=(0, 14))
        self._build_query1_panel(q1_card)

        q2_card = make_card(scroll)
        q2_card.pack(fill="x", pady=(0, 14))
        self._build_query2_panel(q2_card)

        # ── Section 2: Functions (Phase D) ────────────────────────────────────
        self._section_header(scroll, "🔢  פונקציות מאוחסנות (Phase D)")

        fn_row = ctk.CTkFrame(scroll, fg_color="transparent")
        fn_row.pack(fill="x", pady=(0, 14))
        fn_row.columnconfigure(0, weight=1)
        fn_row.columnconfigure(1, weight=1)

        fn1_card = make_card(fn_row)
        fn1_card.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        self._build_fn1_panel(fn1_card)

        fn2_card = make_card(fn_row)
        fn2_card.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        self._build_fn2_panel(fn2_card)

        # ── Section 3: Procedures (Phase D) ──────────────────────────────────
        self._section_header(scroll, "🧠  פרוצדורות מאוחסנות (Phase D)")

        proc_row = ctk.CTkFrame(scroll, fg_color="transparent")
        proc_row.pack(fill="x", pady=(0, 30))
        proc_row.columnconfigure(0, weight=1)
        proc_row.columnconfigure(1, weight=1)

        p1_card = make_card(proc_row)
        p1_card.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        self._build_proc1_panel(p1_card)

        p2_card = make_card(proc_row)
        p2_card.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        self._build_proc2_panel(p2_card)

    # ── Shared helper ─────────────────────────────────────────────────────────

    def _section_header(self, parent, text):
        """Renders a prominent section divider label."""
        wrapper = ctk.CTkFrame(parent, fg_color=COLORS["bg_input"], corner_radius=10)
        wrapper.pack(fill="x", pady=(8, 10))
        make_label(wrapper, text, size=16, bold=True,
                   color=COLORS["accent"]).pack(anchor="w", padx=14, pady=8)

    def _info_box(self, card, lines):
        """Renders a dark info-box with bullet metadata lines."""
        box = ctk.CTkFrame(card, fg_color=COLORS["bg_input"], corner_radius=8)
        box.pack(fill="x", padx=16, pady=(0, 12))
        for line in lines:
            make_label(box, line, size=10,
                       color=COLORS["text_secondary"]).pack(anchor="w", padx=10, pady=(4, 0))
        ctk.CTkFrame(box, height=4, fg_color="transparent").pack()  # bottom spacer

    # ══════════════════════════════════════════════════════════════════════════
    # SECTION 1 — Complex Queries (Phase B)
    # ══════════════════════════════════════════════════════════════════════════

    # ── Query 1: Monthly workout summary ─────────────────────────────────────

    def _build_query1_panel(self, card):
        make_label(card, "📊  שאילתה 1: סיכום שריפת קלוריות ודופק לפי חודשים",
                   size=14, bold=True, color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 2))
        make_label(card,
                   "אנליזה חודשית – כמות אימונים, סך קלוריות וממוצע דופק. "
                   "משתמש ב-GROUP BY ופונקציות צבירה (COUNT, SUM, AVG).",
                   size=11, color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(0, 6))

        row = ctk.CTkFrame(card, fg_color="transparent")
        row.pack(fill="x", padx=16, pady=(0, 4))
        make_label(row, "שנה:", size=11, color=COLORS["text_secondary"]).pack(side="left", padx=(0, 6))
        self._q1_year = make_entry(row, placeholder="2026", width=100)
        self._q1_year.pack(side="left", padx=(0, 10))
        self._q1_year.insert(0, "2026")
        make_button(row, "▶ הרץ שאילתה", self._run_query1, width=160, height=32).pack(side="left")

        cols = ("חודש", "כמות אימונים", "סך קלוריות", "ממוצע דופק", "ממוצע דירוג")
        self._q1_tree = make_treeview(card, cols, height=8)

    def _run_query1(self):
        year = self._q1_year.get().strip() or "2026"
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT
                    TO_CHAR(log_date, 'YYYY-MM') AS month,
                    COUNT(*) AS workout_count,
                    SUM(total_calories_burned) AS total_calories,
                    ROUND(AVG(average_heart_rate), 1) AS avg_heart_rate,
                    ROUND(AVG(trainee_feedback_rating), 2) AS avg_rating
                FROM public.workout_log
                WHERE EXTRACT(YEAR FROM log_date) = %s
                GROUP BY TO_CHAR(log_date, 'YYYY-MM')
                ORDER BY month
                """,
                (int(year),)
            )
            rows = cur.fetchall()
            conn.close()
            populate_tree(self._q1_tree, rows)
            if not rows:
                show_info("אין נתונים", f"לא נמצאו אימונים בשנת {year}.")
        except Exception as e:
            show_error("שגיאה", str(e))

    # ── Query 2: Legal risk / expired declarations ────────────────────────────

    def _build_query2_panel(self, card):
        make_label(card, "⚠️  שאילתה 2: חשיפה לתביעות – מתאמנים עם הצהרת בריאות שפגה",
                   size=14, bold=True, color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 2))
        make_label(card,
                   "איתור מתאמנים עם לוקר פעיל אך הצהרת בריאות פגת תוקף. "
                   "JOIN משולש: core_user ⟷ locker ⟷ health_declaration. "
                   "מציג 'ימים בסיכון'.",
                   size=11, color=COLORS["text_secondary"]).pack(anchor="w", padx=16, pady=(0, 6))

        make_button(card, "▶ הרץ שאילתה", self._run_query2,
                    width=180, height=32).pack(anchor="w", padx=16, pady=(0, 8))

        cols = ("שם מלא", "Locker ID", "תאריך סיום לוקר", "תאריך פקיעת הצהרה", "ימים בסיכון")
        self._q2_tree = make_treeview(card, cols, height=8)

    def _run_query2(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT
                    cu.first_name || ' ' || cu.last_name AS full_name,
                    l.locker_id,
                    l.rental_end_date,
                    hd.expiry_date,
                    (DATE '2024-01-01' - hd.expiry_date) AS days_at_risk
                FROM public.core_user cu
                JOIN public.locker l ON cu.user_id = l.user_id
                JOIN public.health_declaration hd ON cu.user_id = hd.user_id
                WHERE l.rental_end_date IS NOT NULL
                  AND hd.expiry_date < DATE '2024-01-01'
                ORDER BY days_at_risk DESC
                LIMIT 100
                """
            )
            rows = cur.fetchall()
            conn.close()
            populate_tree(self._q2_tree, rows)
            if not rows:
                show_info("תוצאה", "לא נמצאו מתאמנים בסיכון – כל הצהרות הבריאות בתוקף! ✅")
        except Exception as e:
            show_error("שגיאה", str(e))

    # ══════════════════════════════════════════════════════════════════════════
    # SECTION 2 — Functions (Phase D)
    # ══════════════════════════════════════════════════════════════════════════

    # ── Function 1: fn_user_workout_stats ─────────────────────────────────────

    def _build_fn1_panel(self, card):
        make_label(card, "📈  fn_user_workout_stats(user_id)",
                   size=14, bold=True, color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 4))
        make_label(card,
                   "מחשבת ומחזירה שורת סיכום מלאה עם כל סטטיסטיקות האימון "
                   "של מתאמן: מספר אימונים, דקות, קלוריות, דופק ממוצע, "
                   "דירוג ממוצע, ציון הדירוג הטוב ביותר ותאריך האחרון.",
                   size=11, color=COLORS["text_secondary"],
                   wraplength=340).pack(anchor="w", padx=16, pady=(0, 10))

        self._info_box(card, [
            "📌 פרמטר: user_id (מספר שלם)",
            "📌 RETURNS TABLE – 7 עמודות",
            "📌 שימוש ב: COUNT, SUM, AVG, MAX (Implicit Cursor)",
        ])

        # user_id input row
        input_row = ctk.CTkFrame(card, fg_color="transparent")
        input_row.pack(fill="x", padx=16, pady=(0, 8))
        make_label(input_row, "User ID:", size=11,
                   color=COLORS["text_secondary"]).pack(side="left", padx=(0, 6))
        self._fn1_user_id = make_entry(input_row, placeholder="1", width=80)
        self._fn1_user_id.pack(side="left", padx=(0, 10))
        self._fn1_user_id.insert(0, "1")
        make_button(input_row, "▶ הרץ פונקציה", self._run_fn1,
                    width=160, height=32, color=COLORS["accent"]).pack(side="left")

        cols = ("אימונים", "דקות כולל", "קלוריות כולל",
                "ממוצע דופק", "ממוצע דירוג", "דירוג מקסימלי", "אימון אחרון")
        self._fn1_tree = make_treeview(card, cols, height=4)

    def _run_fn1(self):
        raw = self._fn1_user_id.get().strip()
        if not raw.isdigit():
            show_warning("קלט שגוי", "יש להזין מספר User ID תקין.")
            return
        user_id = int(raw)
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM public.fn_user_workout_stats(%s)",
                (user_id,)
            )
            rows = cur.fetchall()
            conn.close()
            populate_tree(self._fn1_tree, rows)
            if not rows:
                show_info("אין נתונים", f"לא נמצאו אימונים עבור user_id = {user_id}.")
        except Exception as e:
            show_error("שגיאה בהרצת פונקציה", str(e))

    # ── Function 2: fn_trainee_progress_cursor ────────────────────────────────

    def _build_fn2_panel(self, card):
        make_label(card, "📉  fn_trainee_progress_cursor(user_id)",
                   size=14, bold=True, color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 4))
        make_label(card,
                   "מחזירה Ref Cursor עם היסטוריית מדידות גוף של מתאמן, "
                   "כולל חישוב הפרש משקל בין מדידות עוקבות (LAG Window Function). "
                   "מדפיסה NOTICE למדידות מעל 100 ק\"ג.",
                   size=11, color=COLORS["text_secondary"],
                   wraplength=340).pack(anchor="w", padx=16, pady=(0, 10))

        self._info_box(card, [
            "📌 פרמטר: user_id (מספר שלם)",
            "📌 RETURNS refcursor (Explicit Cursor + LAG)",
            "📌 הפונקציה נקראת בתוך BEGIN/COMMIT block",
        ])

        # user_id input row
        input_row = ctk.CTkFrame(card, fg_color="transparent")
        input_row.pack(fill="x", padx=16, pady=(0, 8))
        make_label(input_row, "User ID:", size=11,
                   color=COLORS["text_secondary"]).pack(side="left", padx=(0, 6))
        self._fn2_user_id = make_entry(input_row, placeholder="1", width=80)
        self._fn2_user_id.pack(side="left", padx=(0, 10))
        self._fn2_user_id.insert(0, "1")
        make_button(input_row, "▶ הרץ פונקציה", self._run_fn2,
                    width=160, height=32, color=COLORS["accent"]).pack(side="left")

        cols = ("תאריך", "משקל", "שומן%", "מסת שריר", "BMI",
                "היקף מותניים", "משקל קודם", "שינוי משקל")
        self._fn2_tree = make_treeview(card, cols, height=4)

    def _run_fn2(self):
        raw = self._fn2_user_id.get().strip()
        if not raw.isdigit():
            show_warning("קלט שגוי", "יש להזין מספר User ID תקין.")
            return
        user_id = int(raw)
        try:
            conn = get_connection()
            conn.autocommit = False
            cur = conn.cursor()
            # fn_trainee_progress_cursor returns a refcursor – must be called inside a transaction
            cur.execute("SELECT public.fn_trainee_progress_cursor(%s)", (user_id,))
            cursor_name = cur.fetchone()[0]
            # Fetch all rows from the returned refcursor
            cur.execute(f'FETCH ALL FROM "{cursor_name}"')
            rows = cur.fetchall()
            notices = [str(n) for n in conn.notices]
            conn.commit()
            conn.close()
            populate_tree(self._fn2_tree, rows)
            if notices:
                show_procedure_result(
                    self,
                    "📢 הודעות NOTICE מהפונקציה",
                    notices
                )
            if not rows:
                show_info("אין נתונים",
                          f"לא נמצאו מדידות גוף עבור user_id = {user_id}.")
        except Exception as e:
            show_error("שגיאה בהרצת פונקציה", str(e))

    # ══════════════════════════════════════════════════════════════════════════
    # SECTION 3 — Procedures (Phase D)
    # ══════════════════════════════════════════════════════════════════════════

    # ── Procedure 1: proc_award_achieved_goals ────────────────────────────────

    def _build_proc1_panel(self, card):
        make_label(card, "🏆  proc_award_achieved_goals()",
                   size=14, bold=True, color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 4))
        make_label(card,
                   "סורקת את כל היעדים שלא הושגו ובודקת האם "
                   "המדידה האחרונה של המתאמן עומדת ביעדי המשקל ואחוז השומן. "
                   "מעדכנת is_achieved=1 עבור יעדים שהושגו.",
                   size=11, color=COLORS["text_secondary"],
                   wraplength=340).pack(anchor="w", padx=16, pady=(0, 12))

        self._info_box(card, [
            "📌 פרמטרים: ללא (NO ARGS)",
            "📌 DML: UPDATE על trainee_goal",
            "📌 אלמנטים: Implicit Cursor, Record, Exception Handling",
        ])

        make_button(card, "▶ הרץ פרוצדורה",
                    self._run_proc_award, width=200, height=38,
                    color=COLORS["success"]).pack(padx=16, pady=(0, 14))

    def _run_proc_award(self):
        try:
            conn = get_connection()
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute("CALL public.proc_award_achieved_goals()")
            notices = [str(n) for n in conn.notices]
            conn.close()
            show_procedure_result(
                self,
                "🏆 תוצאת proc_award_achieved_goals",
                notices if notices else ["✅ הפרוצדורה הושלמה ללא שגיאות."]
            )
        except Exception as e:
            show_error("שגיאה בהרצת פרוצדורה", str(e))

    # ── Procedure 2: proc_extend_expiring_lockers ─────────────────────────────

    def _build_proc2_panel(self, card):
        make_label(card, "🔐  proc_extend_expiring_lockers()",
                   size=14, bold=True, color=COLORS["accent"]).pack(anchor="w", padx=16, pady=(14, 4))
        make_label(card,
                   "סורקת לוקרים שתוקפם יפוג בטווח של 90 יום "
                   "ומאריכה אותם אוטומטית לפי לוח זמנים: "
                   "<30 ימים → +365 ימים, <60 → +180, אחרת → +90.",
                   size=11, color=COLORS["text_secondary"],
                   wraplength=340).pack(anchor="w", padx=16, pady=(0, 12))

        self._info_box(card, [
            "📌 פרמטרים: ללא (NO ARGS)",
            "📌 DML: UPDATE על locker",
            "📌 אלמנטים: Explicit Cursor, Loop, Branching, Record",
        ])

        make_button(card, "▶ הרץ פרוצדורה",
                    self._run_proc_lockers, width=200, height=38,
                    color=COLORS["success"]).pack(padx=16, pady=(0, 14))

    def _run_proc_lockers(self):
        try:
            conn = get_connection()
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute("CALL public.proc_extend_expiring_lockers()")
            notices = [str(n) for n in conn.notices]
            conn.close()
            show_procedure_result(
                self,
                "🔐 תוצאת proc_extend_expiring_lockers",
                notices if notices else ["✅ הפרוצדורה הושלמה ללא שגיאות."]
            )
        except Exception as e:
            show_error("שגיאה בהרצת פרוצדורה", str(e))
