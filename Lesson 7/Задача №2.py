'''Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм.'''

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

class Coat(Clothes):
    @property
    def consumption(self):
        return f'Для пошива пальто необходимо: {self.param / 6.5 + 0.5 :.2f} метров ткани'


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма необходимо: {2 * self.param + 0.3 :.2f} метров ткани'

coat = Coat(500)
costume = Costume(100)
print(coat.consumption)
print(costume.consumption())
