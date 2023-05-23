# Программа, которая выводит слово с новой строки:

input_word = input('Введите слова, используя клавишу "пробел": ')
word_list = input_word.split(' ')
print('Введеные слова:', word_list)

for index, word_list_str in enumerate(word_list, start=1):
    print(index, word_list_str[:10])

