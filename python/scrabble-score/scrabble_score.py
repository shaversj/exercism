SCRABBLE_KEY = {
    1: ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"],
    2: ["d", "g"],
    3: ["b", "c", "m", "p"],
    4: ["f", "h", "v", "w", "y"],
    5: ["k"],
    8: ["j", "x"],
    10: ["q", "z"],
}


def score(word):
    lowerd_word = word.lower()
    scrabble_score = 0
    for key, value in SCRABBLE_KEY.items():
        for char in lowerd_word:
            if char in value:
                scrabble_score += int(key)

    return scrabble_score

