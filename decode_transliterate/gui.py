import tkinter as tk
from tkinter import ttk
from .processor import process_text

class App:

    def __init__(self, root):

        self.root = root
        root.title("Decode & Transliterate")

        self.input_var = tk.StringVar()

        ttk.Label(root, text="Input").grid(row=0,column=0)

        self.entry = ttk.Entry(root,width=60,textvariable=self.input_var)
        self.entry.grid(row=0,column=1)

        self.result = tk.Text(root,height=3,width=60)
        self.result.grid(row=1,column=1)

        ttk.Button(root,text="Copy",command=self.copy).grid(row=2,column=1)

        self.input_var.trace_add("write", self.update)

    def update(self,*_):

        text = self.input_var.get()

        try:
            result = process_text(text)

            self.result.delete("1.0", tk.END)
            self.result.insert(tk.END,result)

        except Exception as e:

            self.result.delete("1.0", tk.END)
            self.result.insert(tk.END,str(e))

    def copy(self):

        text = self.result.get("1.0", tk.END).strip()

        self.root.clipboard_clear()
        self.root.clipboard_append(text)