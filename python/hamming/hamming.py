def distance_old(strand_a, strand_b):
    different = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("The length of strands do not match.")
    for index, char in enumerate(strand_a):
        if char != strand_b[index]:
            different += 1

    return different


def distance(strand_a, strand_b):
    different = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands do not match")
    for char_a, char_b in zip(strand_a, strand_b):
        if char_a != char_b:
            different += 1

    return different
