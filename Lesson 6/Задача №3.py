'''Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход)'''

class Worker:

    def __init__(self, name, surname, position, salary, prize):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'salary': str(salary), 'prize': str(prize)} # в реале можно поставить int(), чтобы отобразить цифры


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income['salary'] + self.income['prize']

p = Position('Имя (работника)', 'Фамилия (работника)', 'idL - 792389340', 'Оклад', ' + ' 'Премия')
print(p.get_full_name())
print(p.get_total_income())

