from collections import Counter

# There are a total of 5 books in the series. The books are numbered by 1, 2, 3, 4, 5.
# [3, 3] means that someone is buying two copies of three.
# [1, 2, 3] someone is buying book #1, book #2, and book #3.
COST_OF_BOOK = 800
TWO_DIF_BOOK_DISCOUNT = 0.05
THREE_DIF_BOOK_DISCOUNT = 0.10
FOUR_DIF_BOOK_DISCOUNT = 0.20
FIVE_DIF_BOOK_DISCOUNT = 0.25

GROUP_1 = 

def calculate_total(books):

    count_of_books = Counter(books)

    if len(count_of_books) < 1:
        return 0
    if len(count_of_books) == 1:
        return COST_OF_BOOK * count_of_books[books[0]]
    if len(count_of_books) == 2:
        discount = COST_OF_BOOK * len(count_of_books) * TWO_DIF_BOOK_DISCOUNT
        return (COST_OF_BOOK * len(count_of_books)) - discount
    if len(count_of_books) == 3:
        discount = COST_OF_BOOK * len(count_of_books) * THREE_DIF_BOOK_DISCOUNT
        return (COST_OF_BOOK * len(count_of_books)) - discount
    if len(count_of_books) == 4:
        discount = COST_OF_BOOK * len(count_of_books) * FOUR_DIF_BOOK_DISCOUNT
        return (COST_OF_BOOK * len(count_of_books)) - discount
    if len(count_of_books) == 5:
        discount = COST_OF_BOOK * len(count_of_books) * FIVE_DIF_BOOK_DISCOUNT
        return (COST_OF_BOOK * len(count_of_books)) - discount


#1, 2, 3 = 10% discount


#1, 2, 3, 4, 5 = 25% Discount