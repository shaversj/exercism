import re


def abbreviate(words):
    pattern = re.compile(r"(?<!')\b[a-zA-Z]{1}|(?<=_)[a-zA-Z]{1}")

    return "".join(pattern.findall(words)).upper()
