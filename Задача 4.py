# Программа по расчету наибольшего введенного пользователем числа

user_number = int(input('Введите любое целое число: '))

max_number = user_number % 10 # Операция деление по модулю

# Вычисление наибольшей цифры:
while user_number > 0:
    if user_number % 10 > max_number:
        max_number = user_number % 10
    user_number = user_number // 10
print('Наибольшая цифра в числе:', max_number)