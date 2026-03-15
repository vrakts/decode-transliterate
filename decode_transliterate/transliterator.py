from transliterate import translit


SUPPORTED_LANGS = {
    "Russian": "ru",
    "Ukrainian": "uk",
    "Greek": "el",
    "Armenian": "hy"
}


def transliterate_text(text: str, lang_code: str) -> str:
    """
    Transliterate text to Latin characters.
    """

    if not text:
        return ""

    try:
        return translit(text, lang_code, reversed=True)
    except Exception:
        return text