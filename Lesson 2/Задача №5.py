# Программа рейтинг

my_list = [7, 5, 3, 3, 2]
print('Рейтинг:', my_list)
number = int(input('Введите число: '))

if number <= my_list[-1]:
    print(f'{number} <= {my_list[-1]}')
    my_list.append(number)

else:
    for i in range(len(my_list)):
        input('')
        print(f'i = {i}, my_list [i] = {my_list[i]}')
        if number > my_list[i]:
            print(f'{number} > {my_list[i]}')
            my_list.insert(i, number)
            break
print('Новый рейтинг:', my_list)
