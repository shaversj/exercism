import string

LOWER_CASE = string.ascii_lowercase * 2
UPPER_CASE = string.ascii_uppercase * 2


def rotate(text, key):
    cipher_text = []

    for char in text:
        if not char.isalpha():
            cipher_text.append(char)
        if char in LOWER_CASE:
            char_index = LOWER_CASE.index(char)

            new_char = LOWER_CASE[char_index + key]
            cipher_text.append(new_char)
        if char in UPPER_CASE:
            char_index = UPPER_CASE.index(char)
            new_char = UPPER_CASE[char_index + key]
            cipher_text.append(new_char)

    return "".join(cipher_text)
