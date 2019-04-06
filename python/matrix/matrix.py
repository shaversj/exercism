class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_list = []
        for numbers in self.matrix_string.split("\n"):
            split_numbers = numbers.split()
            self.matrix_list.append(split_numbers)

    def row(self, index):
        index = index - 1
        return list(map(int, self.matrix_list[index]))

    def column(self, index):
        index = index - 1
        column_entries = [row[index] for row in self.matrix_list]
        return list(map(int, column_entries))
