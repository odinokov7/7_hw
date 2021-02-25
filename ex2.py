from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method1(self):
        pass


class Coat:
    def __init__(self, pices, size):
        self.summ = float((size / 6.5 + 0.5) * pices)


class Suit:
    def __init__(self, pices, height):
        self.summ = float((2 * height + 0.3) * pices)


class Clothes(ABC):
    def __init__(self):
        self.list_of_summ = []
        self.summ_of_clothes = 0

    def add_coat(self, pices, size):
        self.list_of_summ.append(Coat(pices, size))

    def add_suit(self, pices, height):
        self.list_of_summ.append(Suit(pices, height))

    @property
    def general_sum(self):
        summ_of_clothes = self.summ_of_clothes
        for el in self.list_of_summ:
            summ_of_clothes += el.summ
        return f'Количество ткани необходимое для производства одежды -  {summ_of_clothes}'


a = Clothes()
a.add_suit(2, 1)
a.add_suit(2, 1)
a.add_coat(2, 13)
print(a.general_sum)
