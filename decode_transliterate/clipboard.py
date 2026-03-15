def get_clipboard(root):

    try:
        return root.clipboard_get()
    except Exception:
        return ""


class ClipboardWatcher:

    def __init__(self, root, callback):

        self.root = root
        self.callback = callback

        self.last_text = ""

        self.poll()

    def poll(self):

        try:
            current = self.root.clipboard_get()
        except Exception:
            current = ""

        if current != self.last_text:

            self.last_text = current

            if current.strip():
                self.callback(current)

        self.root.after(800, self.poll)