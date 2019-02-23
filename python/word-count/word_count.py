from collections import Counter
import re


def word_count(phrase):

    phrase = phrase.lower()
    word = re.compile(r"(?<=')\w+(?=')|[a-z][^\t,._: !#$%&()*+-]+|\d")
    count_words = Counter(word.findall(phrase)).most_common()

    final_dict = {}

    for k, v in count_words:
        final_dict[k] = v

    return final_dict
