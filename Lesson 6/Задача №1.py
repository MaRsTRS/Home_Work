# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).

from time import sleep # импортируем sleep для того, чтобы наш светофор мог вкл и выкл

class Traffic_Light:
    __color = ['Red', 'Yellow', 'Green'] # назначаем цвета и порядок для светофора
    def running (self):  # объявляем функцию running для запуска
        # создаем цикл работы светофора
        i = 0
        while i != 3:
            print(Traffic_Light.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            i += 1
t = Traffic_Light() # создаем экземпляр класса
t.running() # вызываем нашу функцию running для последовательности работы светофора

