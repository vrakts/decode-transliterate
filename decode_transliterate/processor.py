from .decoder import decode_html_entities
from .transliterator import transliterate_to_latin

def process_text(text: str) -> str:

    if not text:
        return ""

    decoded = decode_html_entities(text)
    transliterated = transliterate_to_latin(decoded)

    return transliterated