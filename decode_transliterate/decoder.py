import html

def decode_html_entities(text: str) -> str:
    try:
        return html.unescape(text)
    except Exception as e:
        raise ValueError(f"HTML decode failed: {e}")