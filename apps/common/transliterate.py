from transliterate import translit


def latin_to_cyrillic(text):
    return translit(text, "ru", reversed=False)


def cyrillic_to_latin(text):
    return translit(text, "ru", reversed=True)
