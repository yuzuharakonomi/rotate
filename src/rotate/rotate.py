import string


def rotate(text: str, rotation: int) -> str:
    if not text.isalpha() or not text.isascii():
        raise ValueError()

    normalized_rotation = rotation % 26
    translation_table = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[normalized_rotation:]
        + string.ascii_lowercase[:normalized_rotation]
        + string.ascii_uppercase[normalized_rotation:]
        + string.ascii_uppercase[:normalized_rotation],
    )
    return text.translate(translation_table)
