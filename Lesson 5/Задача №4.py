'''Создать (не программно) текстовый файл со следующим содержимым:
необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

replace_dict_list = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

file_list = open('Text_List4.txt', 'r', encoding='utf-8')
new_file_list = open('New_Text_List4.txt', 'w', encoding='utf-8')

for line in file_list:
    line = line.split(' - ')
    line[0] = replace_dict_list[line[0]]
    line = ' - ' .join(line)
    new_file_list.write(line)

file_list.close()
new_file_list.close()

