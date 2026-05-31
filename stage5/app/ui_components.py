"""
ui_components.py
Reusable UI component helpers for PowerGym Pro.
Provides factory functions for styled widgets, popup dialogs,
and the data-grid (Treeview wrapper).
"""

import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk

# ── Colour palette ──────────────────────────────────────────────────────────
COLORS = {
    "bg_dark":       "#0F1117",
    "bg_card":       "#1A1D2E",
    "bg_input":      "#252840",
    "accent":        "#6C63FF",
    "accent_hover":  "#8B84FF",
    "accent_light":  "#A78BFA",
    "success":       "#10B981",
    "danger":        "#EF4444",
    "warning":       "#F59E0B",
    "text_primary":  "#F1F5F9",
    "text_secondary":"#94A3B8",
    "border":        "#334155",
    "sidebar":       "#13162B",
    "sidebar_hover": "#1E2140",
}

FONT_FAMILY = "Segoe UI"


# ── Widget factories ─────────────────────────────────────────────────────────

def make_label(parent, text, size=13, bold=False, color=None, **kwargs):
    color = color or COLORS["text_primary"]
    weight = "bold" if bold else "normal"
    return ctk.CTkLabel(
        parent, text=text,
        font=(FONT_FAMILY, size, weight),
        text_color=color,
        **kwargs
    )


def make_entry(parent, placeholder="", width=280, **kwargs):
    return ctk.CTkEntry(
        parent,
        placeholder_text=placeholder,
        width=width,
        height=36,
        font=(FONT_FAMILY, 12),
        fg_color=COLORS["bg_input"],
        border_color=COLORS["border"],
        text_color=COLORS["text_primary"],
        placeholder_text_color=COLORS["text_secondary"],
        **kwargs
    )


def make_button(parent, text, command, color=None, hover_color=None,
                width=160, height=38, **kwargs):
    color = color or COLORS["accent"]
    hover_color = hover_color or COLORS["accent_hover"]
    return ctk.CTkButton(
        parent, text=text, command=command,
        width=width, height=height,
        font=(FONT_FAMILY, 12, "bold"),
        fg_color=color,
        hover_color=hover_color,
        corner_radius=8,
        **kwargs
    )


def make_combo(parent, values, width=280, **kwargs):
    return ctk.CTkComboBox(
        parent,
        values=values,
        width=width,
        height=36,
        font=(FONT_FAMILY, 12),
        fg_color=COLORS["bg_input"],
        border_color=COLORS["border"],
        text_color=COLORS["text_primary"],
        button_color=COLORS["accent"],
        button_hover_color=COLORS["accent_hover"],
        dropdown_fg_color=COLORS["bg_card"],
        dropdown_text_color=COLORS["text_primary"],
        dropdown_hover_color=COLORS["accent"],
        **kwargs
    )


def make_card(parent, **kwargs):
    return ctk.CTkFrame(
        parent,
        fg_color=COLORS["bg_card"],
        corner_radius=12,
        border_width=1,
        border_color=COLORS["border"],
        **kwargs
    )


def make_separator(parent, orient="horizontal"):
    sep = ttk.Separator(parent, orient=orient)
    return sep


# ── Styled Treeview (data grid) ──────────────────────────────────────────────

def make_treeview(parent, columns, height=18):
    """
    Returns a fully styled (dark-theme) ttk.Treeview inside a frame
    with horizontal and vertical scrollbars.
    The caller receives the Treeview widget itself.
    """
    style = ttk.Style()
    style.theme_use("default")
    style.configure("PowerGym.Treeview",
                    background=COLORS["bg_card"],
                    foreground=COLORS["text_primary"],
                    rowheight=28,
                    fieldbackground=COLORS["bg_card"],
                    borderwidth=0,
                    font=(FONT_FAMILY, 11))
    style.configure("PowerGym.Treeview.Heading",
                    background=COLORS["bg_dark"],
                    foreground=COLORS["accent_light"],
                    font=(FONT_FAMILY, 11, "bold"),
                    relief="flat")
    style.map("PowerGym.Treeview",
              background=[("selected", COLORS["accent"])],
              foreground=[("selected", COLORS["text_primary"])])
    style.map("PowerGym.Treeview.Heading",
              background=[("active", COLORS["sidebar_hover"])])

    container = ctk.CTkFrame(parent, fg_color=COLORS["bg_card"], corner_radius=10)
    container.pack(fill="both", expand=True, padx=0, pady=0)

    vsb = ttk.Scrollbar(container, orient="vertical")
    hsb = ttk.Scrollbar(container, orient="horizontal")

    tree = ttk.Treeview(
        container,
        columns=columns,
        show="headings",
        height=height,
        style="PowerGym.Treeview",
        yscrollcommand=vsb.set,
        xscrollcommand=hsb.set,
    )
    vsb.configure(command=tree.yview)
    hsb.configure(command=tree.xview)

    for col in columns:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=max(90, len(col) * 10))

    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    tree.pack(fill="both", expand=True)

    # Alternating row colours
    tree.tag_configure("even", background="#1E2240")
    tree.tag_configure("odd",  background=COLORS["bg_card"])

    return tree


def populate_tree(tree, rows):
    """Clear and repopulate a Treeview with (rows) — list of tuples/lists."""
    tree.delete(*tree.get_children())
    for i, row in enumerate(rows):
        tag = "even" if i % 2 == 0 else "odd"
        tree.insert("", "end", values=[str(v) if v is not None else "" for v in row], tags=(tag,))


# ── Popup helpers ────────────────────────────────────────────────────────────

def show_info(title, message):
    messagebox.showinfo(title, message)


def show_error(title, message):
    messagebox.showerror(title, message)


def show_warning(title, message):
    messagebox.showwarning(title, message)


def ask_confirm(title, message):
    return messagebox.askyesno(title, message)


# ── Procedure result popup ───────────────────────────────────────────────────

def show_procedure_result(parent, title, lines):
    """
    Opens a top-level window showing procedure NOTICE output
    (list of strings) in a styled read-only text widget.
    """
    win = ctk.CTkToplevel(parent)
    win.title(title)
    win.geometry("640x420")
    win.grab_set()
    win.configure(fg_color=COLORS["bg_dark"])

    make_label(win, title, size=16, bold=True,
               color=COLORS["accent_light"]).pack(pady=(18, 6))

    text_frame = ctk.CTkFrame(win, fg_color=COLORS["bg_card"],
                               corner_radius=10)
    text_frame.pack(fill="both", expand=True, padx=20, pady=10)

    text = tk.Text(text_frame,
                   bg=COLORS["bg_card"],
                   fg=COLORS["text_primary"],
                   font=(FONT_FAMILY, 11),
                   relief="flat",
                   wrap="word",
                   state="normal",
                   bd=0,
                   padx=12, pady=8)
    text.pack(fill="both", expand=True)

    content = "\n".join(lines) if lines else "✅ הפרוצדורה הורצה בהצלחה (ללא פלט)."
    text.insert("end", content)
    text.configure(state="disabled")

    make_button(win, "סגור", win.destroy,
                width=120).pack(pady=14)
