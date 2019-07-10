def find_anagrams(word, candidates):
    sorted_word = "".join(sorted(word.lower()))
    sorted_candidates = [
        "".join(sorted(candidate))
        for candidate in list(map(str.lower, candidates))
        if candidate != word.lower()
    ]

    matches = []
    for index, sorted_string in enumerate(sorted_candidates):
        if sorted_string == sorted_word:
            matches.append(candidates[index])

    return matches


def find_anagrams_old(word, candidates):
    from itertools import permutations

    lowered_word = word.lower()
    lowered_candidates = list(map(str.lower, candidates))
    possible_values = permutations(lowered_word)
    matches = []
    for value in possible_values:
        possible_word = "".join(value)
        if possible_word in [lowered_word, word]:
            continue
        if possible_word in lowered_candidates:
            candidate_index = lowered_candidates.index(possible_word)
            matches.append(candidates[candidate_index])

    return list(set(matches))
