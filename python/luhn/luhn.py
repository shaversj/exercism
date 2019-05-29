class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def is_valid(self):
        if len(self.card_num) <= 1:
            return False
        if not self.card_num.isdigit():
            return False

        numbers_to_double = [int(num) for num in self.card_num[-2::-2]]
        other_numbers = [int(num) for num in self.card_num[-1::-2]]

        list_of_numbers_to_sum = []

        for num in numbers_to_double:
            doubled_num = num * 2
            if doubled_num > 9:
                final_num = doubled_num - 9
                list_of_numbers_to_sum.append(final_num)
            else:
                list_of_numbers_to_sum.append(doubled_num)

        list_of_numbers_to_sum.extend(other_numbers)
        sum_of_numbers = sum(list_of_numbers_to_sum)

        if sum_of_numbers % 10 == 0:
            return True
        else:
            return False
