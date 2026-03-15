from .decoder import decode_html_entities
from .transliterator import transliterate_text


def process_text(text: str, lang: str) -> str:

    if not text:
        return ""

    decoded = decode_html_entities(text)

    result = transliterate_text(decoded, lang)

    return result