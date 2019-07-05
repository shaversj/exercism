def decode(string):
    decoded_string = ""
    for index, (char_1, char_2) in enumerate(zip(string, string[1:])):
        if index == 0 and char_1.isalpha():
            decoded_string += char_1
        if char_1.isdigit() and char_2.isdigit():
            continue
        if char_1.isdigit() and char_2.isalpha() and string[index - 1].isdigit():
            num = int(string[index - 1] + char_1)
            decoded_string += num * char_2
        if char_1.isdigit() and not string[index - 1].isdigit():
            decoded_string += int(char_1) * char_2
        if char_1.isalpha() and char_2.isalpha or char_1 == " ":
            decoded_string += char_2
        elif char_2.isalpha() and not char_1.isdigit():
            decoded_string += char_2

    return "".join([char for char in decoded_string if not char.isdigit()])


def encode(string):
    bag = []
    encoded_string = ""

    if string == "":
        return encoded_string

    for index, char in enumerate(string):
        if index == 0:
            bag.append(char)
        else:
            if char in bag:
                bag.append(char)
            else:
                if bag.count(bag[0]) == 1:
                    encoded_string += bag[0]
                    bag.clear()
                    bag.append(char)
                else:
                    encoded_string += str(bag.count(bag[0])) + bag[0]
                    bag.clear()
                    bag.append(char)
    else:
        if bag.count(bag[0]) == 1:
            encoded_string += bag[0]
        else:
            encoded_string += str(bag.count(bag[0])) + bag[0]

    return encoded_string
