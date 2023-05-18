'''Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.'''

class Road:

# объявляем функцию и переменную экземпляра принадлежащую объекту
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.heigth = 5

# объявляем функцию и расчет для массы асфальта
    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.heigth / 1000
        print(f'Рассчет: необходимо {round(asphalt_mass)} тонн асфальта') # round необходим для округления до целого числа

r = Road(5000, 20) # создаем экземпляр класса
r.asphalt_mass() # вызываем функцию рассчета массы асфальта


