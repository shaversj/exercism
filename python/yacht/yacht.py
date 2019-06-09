# Score categories
# Change the values as you see fit
from collections import Counter

YACHT = ["YACHT", 50]
ONES = ["ONES", 1]
TWOS = ["TWOS", 2]
THREES = ["THREES", 3]
FOURS = ["FOURS", 4]
FIVES = ["FIVES", 5]
SIXES = ["SIXES", 6]
FULL_HOUSE = ["FULL_HOUSE"]
FOUR_OF_A_KIND = ["FOUR_OF_A_KIND"]
LITTLE_STRAIGHT = ["LITTLE_STRAIGHT", [1, 2, 3, 4, 5], 30]
BIG_STRAIGHT = ["BIG_STRAIGHT", [2, 3, 4, 5, 6], 30]
CHOICE = ["CHOICE"]


def score(dice, category):
    if category[0] == "YACHT":
        if len(set(dice)) == 1:
            return YACHT[1]
    if category[0] in ["ONES", "TWOS", "THREES", "FOURS", "FIVES", "SIXES"]:
        return dice.count(category[1]) * category[1]
    if category[0] == "FULL_HOUSE":
        count_of_dice_with_same_values = Counter(dice)
        if all(
            value == 3 or value == 2 for value in count_of_dice_with_same_values.values()
        ):
            return sum(dice)
    if category[0] == "FOUR_OF_A_KIND":
        count_of_dice_with_same_values = Counter(dice)
        for key, value in count_of_dice_with_same_values.items():
            if value >= 4:
                return key * 4

    if category[0] == "LITTLE_STRAIGHT":
        if sorted(dice) == LITTLE_STRAIGHT[1]:
            return category[2]

    if category[0] == "BIG_STRAIGHT":
        if sorted(dice) == BIG_STRAIGHT[1]:
            return category[2]

    if category[0] == "CHOICE":
        return sum(dice)

    return 0
