def hey(phrase):
    if len(phrase) == 0 or phrase.isspace():
        return "Fine. Be that way!"
    if phrase.isupper() and not phrase.endswith("?"):
        return "Whoa, chill out!"
    if phrase.isupper() and phrase.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if phrase.endswith("?") and not phrase.isupper():
        return "Sure."
    if phrase.strip().endswith("?"):
        return "Sure."
    else:
        return "Whatever."
