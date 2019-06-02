import string


def is_pangram(sentence):
    sentence = sentence.lower()
    letters = string.ascii_lowercase

    letters_in_sentence = [char for char in sentence if char in letters]

    if set(letters_in_sentence) == set(letters):
        return True
    else:
        return False
