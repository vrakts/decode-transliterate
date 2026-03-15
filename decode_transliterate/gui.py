import tkinter as tk
from tkinter import ttk, messagebox

from tkinterdnd2 import DND_TEXT

from .processor import process_text
from .clipboard import get_clipboard, ClipboardWatcher
from .transliterator import SUPPORTED_LANGS


class App:

    def __init__(self, root):

        self.root = root

        root.title("Decode & Transliterate")

        self.input_var = tk.StringVar()

        self.lang_var = tk.StringVar(value="ru")

        self.build_ui()

        self.bind_shortcuts()

        self.clipboard_watcher = ClipboardWatcher(
            root,
            self.clipboard_changed
        )

    def build_ui(self):

        self.build_menu()

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

        ttk.Button(
            btn_frame,
            text="Clear",
            command=self.clear_fields
        ).grid(row=0, column=2)

        self.input_var.trace_add("write", self.update)

    def build_menu(self):

        menu = tk.Menu(self.root)

        help_menu = tk.Menu(menu, tearoff=0)

        help_menu.add_command(
            label="About",
            command=self.show_about
        )

        help_menu.add_separator()

        help_menu.add_command(
            label="Quit",
            command=self.root.quit
        )

        menu.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu)

    def bind_shortcuts(self):

        self.root.bind("<Escape>", lambda e: self.clear_fields())

        self.root.bind("<Control-q>", lambda e: self.root.quit())

    def show_about(self):

        messagebox.showinfo(
            "About",
            "Decode Transliterate\n\n"
            "Version: 1.2.0\n\n"
            "Features:\n"
            "• HTML entity decoding\n"
            "• Multi-language transliteration\n"
            "• Drag & drop text\n"
            "• Clipboard watcher\n"
            "• CLI support\n\n"
            "GUI usage:\n"
            "• Enter text in the input field\n"
            "• Select a language from the dropdown\n"
            "• See the transliterated result in the output field\n\n"
            "Command line usage:\n"
            "• Run with --cli \"text\" to process text directly from the command line\n"
        )

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

    def clipboard_changed(self, text):

        self.input_var.set(text)

    def copy(self):

        text = self.result.get("1.0", tk.END).strip()

        self.root.clipboard_clear()

        self.root.clipboard_append(text)

    def clear_fields(self):

        self.input_var.set("")

        self.result.delete("1.0", tk.END)

    def drop(self, event):

        self.input_var.set(event.data)