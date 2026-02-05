import string


def rotate(text: str, rotation: int) -> str:
    if not text.isalpha() and not text.isascii():
        raise ValueError()

    total_alphabets = len(string.ascii_lowercase)
    rotated_text = ""
    for character in text:
        offset = string.ascii_lowercase.find(character.lower())
        if offset == -1:
            raise ValueError()

        final_rotation = (offset + rotation) % total_alphabets

        if character.isupper():
            rotated_text += string.ascii_uppercase[final_rotation]
        else:
            rotated_text += string.ascii_lowercase[final_rotation]

    return rotated_text
