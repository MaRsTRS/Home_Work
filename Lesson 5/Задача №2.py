'''Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке'''

my_file = open('Text(для задачи №2.txt', 'r')
my_text = my_file.readlines()

print('Общее количество строк:', len(my_text))

for i in range(len(my_text)):
    print(f'Строка № {i+1} - {len(my_text[i].split())} слово')
my_file.close()
