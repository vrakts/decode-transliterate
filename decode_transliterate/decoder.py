import html


def decode_html_entities(text: str) -> str:
    """
    Decode HTML entities into normal characters.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    try:
        return html.unescape(text)
    except Exception as e:
        raise RuntimeError(f"HTML decode failed: {e}")