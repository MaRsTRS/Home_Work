
my_file = open('List_L5(для задачи №3).txt', 'r', encoding='utf-8')

list_work = my_file.readlines()

summary = 0
names = []

for user_line in list_work:
    user_line_split = user_line.split()
    summary += float(user_line_split[1])
    if float(user_line_split[1]) < 20000.00:
        names.append(user_line_split[0])
my_file.close()

print('Имя:', ', ' .join(names))
print('Средняя зарплата:', summary/len(list_work))
