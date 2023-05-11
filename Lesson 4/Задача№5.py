'''Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка'''


from functools import reduce # # используем reduce для сведения последовательностей к единственному значению

def func_tools (first_element, second_element):
    return first_element * second_element

my_list = [i for i in range(100, 1000, 2)] # диапазон от 100 до 1000 с шагом 2

result = reduce(func_tools, my_list)
print(result)



