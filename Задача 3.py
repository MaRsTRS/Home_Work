# программа сложить числа по типу n+nn+nnn

user_number = int(input('Введите число: ')) # запрашиваем у пользователя чило

# Производим расчет:
second_number = user_number * 11
third_number = user_number * 111

user_number = int(user_number) + int(second_number) + int(third_number) # сумма трех переменных
# используем int для того, чтобы сложить и перевести из строки в числа

print('Ответ:', user_number) # отображаем полученный результат на дисплей