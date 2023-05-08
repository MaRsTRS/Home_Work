# Программа, которая запрашивет два числа и делит между собой

def func_x(a, b): # указывем функцию
    try:
        c = a / b
        return c
    except ZeroDivisionError: # используем данную функуцию, чтобы предотвратить деление на ноль
        print('Ошибка: на ноль делить нельзя!')
    except TypeError:
        print('Неправильные данные')

a = int(input('Введите число: '))
b = int(input('Введите число: '))
result = func_x(a, b)

print('Ответ: ', result)



