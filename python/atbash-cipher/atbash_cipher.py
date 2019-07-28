import string


def encode(plain_text):
    lowered_plain_text = plain_text.lower()
    intab = string.ascii_lowercase
    outtab = string.ascii_lowercase[::-1]

    translated_string = lowered_plain_text.translate(
        str.maketrans(intab, outtab, string.punctuation)
    ).replace(" ", "")

    return group_translation(translated_string).rstrip()


def decode(ciphered_text):
    stripped_ciphered_text = ciphered_text.replace(" ", "")
    intab = string.ascii_lowercase[::-1]
    outtab = string.ascii_lowercase

    decoded_string = stripped_ciphered_text.translate(
        str.maketrans(intab, outtab, string.punctuation)
    )

    return decoded_string


def group_translation(s):

    grouped_translation = ""
    for num in range(0, len(s), 5):
        grouped_translation += s[num : num + 5] + " "

    return grouped_translation
