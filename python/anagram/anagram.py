from itertools import permutations


def find_anagrams(word, candidates):
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
