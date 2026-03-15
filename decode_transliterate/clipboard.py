def get_clipboard(root):

    try:
        return root.clipboard_get()
    except Exception:
        return ""