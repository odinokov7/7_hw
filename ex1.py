a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
a1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class Matrix:
    iter = 0
    iter1 = 0
    iter2 = 0
    stroka = ''

    def __init__(self, list_of_lists):
        self.lists = list_of_lists

    def __str__(self):
        for self.iter in range(self.iter, len(self.lists)):
            self.stroka = self.stroka + str(self.lists[self.iter]) + '\n'
        return self.stroka

    def __add__(self, other):
        temp_list = self.lists.copy()
        if len(self.lists) > len(other.lists):
            for iter1 in range(len(other.lists)):
                for iter2 in range(len(other.lists[iter1])):
                    temp_list[iter1][iter2] = self.lists[iter1][iter2] + other.lists[iter1][iter2]
        else:
            for iter1 in range(len(self.lists)):
                for iter2 in range(len(self.lists[iter1])):
                    temp_list[iter1][iter2] = self.lists[iter1][iter2] + other.lists[iter1][iter2]
        for self.iter in range(self.iter, len(temp_list)):
            self.stroka = self.stroka + str(temp_list[self.iter]) + '\n'
        return self.stroka


c1 = Matrix(a)
c2 = Matrix(a1)
print((c1 + c2))
