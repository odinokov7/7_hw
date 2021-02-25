class Cell:

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if self.count > other.count:
            result = self.count - other.count
            return result
        else:
            return f'{self.count} меньше или равно {other.count}'

    def __mul__(self, other):
        result = self.count * other.count
        return result

    def __truediv__(self, other):
        result = self.count / other.count
        result = int(result // 1)
        return result

    def make_order(self, row):
        out_string = '*' * self.count
        r = [out_string[i:i + row] for i in range(0, len(out_string), row)]
        r = r'\n'.join(r)
        return print(r)


a = Cell(46)
b = Cell(2)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
a.make_order(7)
b.make_order(5)
