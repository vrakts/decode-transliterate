from transliterate import translit

def transliterate_to_latin(text: str) -> str:
    try:
        return translit(text, 'ru', reversed=True)
    except Exception as e:
        raise ValueError(f"Transliteration failed: {e}")