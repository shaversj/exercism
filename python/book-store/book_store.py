from collections import Counter

book_dict = {1: [], 2: [], 3: [], 4: [], 5: []}
book_dict2 = {1: [], 2: [], 3: [], 4: []}


def calculate_total(books):

    books_counter = Counter(books)
    num_of_unique_titles = [value != 0 for key, value in books_counter.items()].count(
        True
    )
    print("first num of unique titles =", num_of_unique_titles)
    print("first counter", books_counter)
    if len(books) == 0:
        return 0

    while len(list(books_counter.elements())) != 0:
        num_of_unique_titles = [value != 0 for key, value in books_counter.items()].count(
            True
        )

        # if len(books_counter.keys()) == 1:
        if num_of_unique_titles == 1:
            for k, v in books_counter.items():
                if v != 0:
                    book_dict[1].append(1)
                    books_counter[k] -= 1
        # if len(books_counter.keys()) == 2:
        if num_of_unique_titles == 2:
            print("two")
            for k, v in list(books_counter.items())[:2]:
                if v != 0:
                    book_dict[2].append(1)
                    books_counter[k] -= 1

        # if len(books_counter.keys()) == 3:
        if num_of_unique_titles == 3:
            print("three")
            for k, v in list(books_counter.items())[:3]:
                if v != 0:
                    book_dict[3].append(1)
                    books_counter[k] -= 1

        # if len(books_counter.keys()) == 4:
        if num_of_unique_titles == 4:
            print("four")
            for k, v in list(books_counter.items())[:4]:
                if v != 0:
                    book_dict[4].append(1)
                    books_counter[k] -= 1

        # if len(books_counter.keys()) >= 5:
        if num_of_unique_titles >= 5:
            print("five")
            for k, v in list(books_counter.items())[:5]:
                if v != 0:
                    book_dict[5].append(1)
                    books_counter[k] -= 1

    print("last num of unique titles = ", num_of_unique_titles)
    print("last counter", books_counter)
    print("last dict", book_dict)
    return final_calcs()


def final_calcs():

    book_1 = sum(book_dict[1]) * 800
    book_2 = sum(book_dict[2]) * 760
    book_3 = sum(book_dict[3]) * 720
    book_4 = sum(book_dict[4]) * 640
    book_5 = sum(book_dict[5]) * 600

    books = book_1 + book_2 + book_3 + book_4 + book_5

    return books


def calculate_total_2(books):
    books_counter = Counter(books)
    num_of_unique_titles = [value != 0 for key, value in books_counter.items()].count(
        True
    )
    print("first num of unique titles =", num_of_unique_titles)
    print("first counter", books_counter)
    if len(books) == 0:
        return 0

    count = 0
    while len(list(books_counter.elements())) != 0:
        num_of_unique_titles = [value != 0 for key, value in books_counter.items()].count(
            True
        )

        # if len(books_counter.keys()) == 1:
        if num_of_unique_titles == 1:
            print("one")
            for k, v in books_counter.items():
                if v != 0:
                    book_dict[1].append(1)
                    books_counter[k] -= 1
        # if len(books_counter.keys()) == 2:
        if num_of_unique_titles == 2:
            print("two")
            for k, v in list(books_counter.items())[:2]:
                if v != 0:
                    book_dict[2].append(1)
                    books_counter[k] -= 1

        # if len(books_counter.keys()) == 3:
        if num_of_unique_titles == 3:
            print("three")
            for k, v in list(books_counter.items())[:3]:
                if v != 0:
                    book_dict[3].append(1)
                    books_counter[k] -= 1

        # if len(books_counter.keys()) == 4:
        if num_of_unique_titles >= 4:
            print("four")
            for k, v in list(books_counter.items()):
                if v != 0:
                    book_dict[4].append(1)
                    books_counter[k] -= 1
        count += 1
        print(f"{count} iteration: {books_counter}")

    print("last num of unique titles = ", num_of_unique_titles)
    print("last counter", books_counter)
    print("last dict", book_dict)

    return final_calcs()


def final_cals_v2():
    book_1 = sum(book_dict2[1]) * 800
    book_2 = sum(book_dict2[2]) * 760
    book_3 = sum(book_dict2[3]) * 720
    book_4 = sum(book_dict2[4]) * 640

    books = book_1 + book_2 + book_3 + book_4

    return books


print(calculate_total_2([1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]))
# print(calculate_total([1, 1, 2, 3, 4, 4, 5, 5]))
# print(calculate_total([1, 1, 2, 2, 3, 3, 4, 4, 5]))
# print(calculate_total([1, 1, 2, 2, 3, 3, 4, 4, 5]))
# print(calculate_total([2, 2]))
# print(calculate_total([1, 2]))
# print(calculate_total([1, 2, 3, 4, 5]))
# One copy of any of the five books costs $8.

# If, however, you buy two different books, you get a 5%
# discount on those two books.

# If you buy 3 different books, you get a 10% discount.

# If you buy 4 different books, you get a 20% discount.

# If you buy all 5, you get a 25% discount.
