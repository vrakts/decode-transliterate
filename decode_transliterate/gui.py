import tkinter as tk
from tkinter import ttk

from tkinterdnd2 import DND_TEXT

from .processor import process_text
from .clipboard import get_clipboard
from .transliterator import SUPPORTED_LANGS


class App:

    def __init__(self, root):

        self.root = root

        root.title("Decode & Transliterate")

        self.input_var = tk.StringVar()

        self.lang_var = tk.StringVar(value="ru")

        self.build_ui()

    def build_ui(self):

        frame = ttk.Frame(self.root, padding=10)
        frame.grid()

        ttk.Label(frame, text="Input").grid(row=0, column=0)

        self.entry = ttk.Entry(frame, width=60, textvariable=self.input_var)
        self.entry.grid(row=0, column=1)

        self.entry.drop_target_register(DND_TEXT)
        self.entry.dnd_bind("<<Drop>>", self.drop)

        ttk.Label(frame, text="Language").grid(row=1, column=0)

        lang_menu = ttk.Combobox(
            frame,
            values=list(SUPPORTED_LANGS.keys()),
            state="readonly"
        )

        lang_menu.set("Russian")

        lang_menu.grid(row=1, column=1)

        lang_menu.bind("<<ComboboxSelected>>", self.change_lang)

        ttk.Label(frame, text="Result").grid(row=2, column=0)

        self.result = tk.Text(frame, height=3, width=60)
        self.result.grid(row=2, column=1)

        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=3, column=1)

        ttk.Button(
            btn_frame,
            text="Paste Clipboard",
            command=self.paste_clipboard
        ).grid(row=0, column=0)

        ttk.Button(
            btn_frame,
            text="Copy Result",
            command=self.copy
        ).grid(row=0, column=1)

        self.input_var.trace_add("write", self.update)

    def change_lang(self, event):

        selected = event.widget.get()

        self.lang_var.set(SUPPORTED_LANGS[selected])

        self.update()

    def update(self, *_):

        text = self.input_var.get()

        lang = self.lang_var.get()

        result = process_text(text, lang)

        self.result.delete("1.0", tk.END)

        self.result.insert(tk.END, result)

    def paste_clipboard(self):

        text = get_clipboard(self.root)

        self.input_var.set(text)

    def copy(self):

        text = self.result.get("1.0", tk.END).strip()

        self.root.clipboard_clear()

        self.root.clipboard_append(text)

    def drop(self, event):

        self.input_var.set(event.data)