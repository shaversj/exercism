FOOD = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}


class Allergies(object):
    def __init__(self, score):
        self.score = score
        self.matched_values = []
        self.name_of_allergies = []
        self.return_matching_food_values(score)
        self.get_name_from_score()

    def return_matching_food_values(self, value):
        sorted_food_scores = list(reversed(sorted(FOOD.values())))
        for num in sorted_food_scores:
            if value == 0:
                return None
            if value >= num:
                self.matched_values.append(num)
                new_value = value - num
                return self.return_matching_food_values(new_value)

    def get_name_from_score(self):
        for k, v in FOOD.items():
            for self.score in self.matched_values:
                if v == self.score:
                    self.name_of_allergies.append(k)

    def is_allergic_to(self, item):
        if item in self.name_of_allergies:
            return True
        else:
            return False

    @property
    def lst(self):
        return list(set(self.name_of_allergies))

