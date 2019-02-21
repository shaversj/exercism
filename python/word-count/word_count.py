from collections import Counter
from string import punctuation


def word_count(phrase):
    table = str.maketrans(dict.fromkeys(punctuation))
    phrase_without_punctuation = phrase.translate(table)

    phrase_without_punctuation = phrase_without_punctuation.lower()

    phrase_no_whitespace_or_punc = phrase_without_punctuation.strip().split()

    count_words = Counter(phrase_no_whitespace_or_punc).most_common()
    final_dict = {}

    for k, v in count_words:
        final_dict[k] = v

    return final_dict


print(word_count("hey,my_spacebar_is_broken."))
# print(word_count("Joe can't tell between 'large' and large."))
# print(word_count("one,\ntwo,\nthree"))
