# Программа возведение числа в степень вида x**y

def func_pow(x, y):
    return 1 / (x ** abs (y)) #возвращаем значение числа
    result = 1
    for i in range(abs(y)):
        result = result * x
    return 1  / result

x = int(input('Введите число x: '))
y = int(input('Введите число y: '))

result_pow = func_pow(x, y)
print('Ответ:', result_pow)

