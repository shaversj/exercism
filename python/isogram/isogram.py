from collections import Counter


def is_isogram(string):
    string = string.lower()

    ignore_list = ["-", " "]

    IsogramCounter = Counter(char for char in string if char not in ignore_list)

    if len(string) == 0:
        return True
    else:
        for k, v in IsogramCounter.items():
            if v >= 2:
                return False
        return True
