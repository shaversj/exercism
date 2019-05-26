def verify(isbn):
    formatted_isbn = isbn.replace("-", "").replace("X", "10")

    if len(formatted_isbn) > 11 or len(formatted_isbn) < 10:
        return False
    if formatted_isbn.islower() or formatted_isbn.isupper():
        return False
    if "X" in isbn:
        return (
            int(formatted_isbn[0]) * 10
            + int(formatted_isbn[1]) * 9
            + int(formatted_isbn[2]) * 8
            + int(formatted_isbn[3]) * 7
            + int(formatted_isbn[4]) * 6
            + int(formatted_isbn[5]) * 5
            + int(formatted_isbn[6]) * 4
            + int(formatted_isbn[7]) * 3
            + int(formatted_isbn[8]) * 2
            + int(formatted_isbn[9:11]) * 1
        ) % 11 == 0
    if len(formatted_isbn) == 11:
        return False
    else:
        return (
            int(formatted_isbn[0]) * 10
            + int(formatted_isbn[1]) * 9
            + int(formatted_isbn[2]) * 8
            + int(formatted_isbn[3]) * 7
            + int(formatted_isbn[4]) * 6
            + int(formatted_isbn[5]) * 5
            + int(formatted_isbn[6]) * 4
            + int(formatted_isbn[7]) * 3
            + int(formatted_isbn[8]) * 2
            + int(formatted_isbn[9]) * 1
        ) % 11 == 0
