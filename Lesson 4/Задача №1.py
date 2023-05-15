# Скрипт расчета заработной платы сотрудника

from sys import argv # импортируем argv для дальнейшей работы

name, hours, salary, prize = argv # распаковываем предаваемые аргументы

print(float(hours) * float(salary) + float(prize))

#далее необходимо в терминале запустить наш скрипт например: python.exe .Lesson 4/Задача №1.py (здесь укажем наши значения)
