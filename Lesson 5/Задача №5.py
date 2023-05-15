'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

my_file = open ('file.txt', 'w', encoding='utf-8')
line = input('Введите число: ')
my_file.write(line)
my_file.close()

my_file_sum = open('summ_list.txt', 'r', encoding='utf-8')
list_sum = my_file_sum.read()

print('Сумма:', sum(map(int, list_sum.split())))
my_file_sum.close()