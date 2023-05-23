# Программа, возвращающая сумму наибольших двух аргументов

def func_x (a, b, c):
    if a <= b and a <= c:
        return b + c
    elif b < c:
        return a + c
    else:
        return a + b

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число с: '))

sum_x = func_x(a, b, c)
print('Ответ:', sum_x)
