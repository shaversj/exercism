def is_armstrong_number(number):
    power = len(str(number))
    values = [int(num) ** power for num in str(number)]

    return number == sum(values)
