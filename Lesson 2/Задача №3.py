# Программа расчитывающая какому месяцу года относится тот или иной сезон:

seasons = {'winter': [12, 1 , 2], 'spring' : [3, 4, 5],
           'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
month = int(input('Введите число месяца: '))

if month in seasons['winter']:
    print('Это Зима')
if month in seasons['spring']:
    print('Это Весна')
if month in seasons['summer']:
    print('Это Лето')
if month in seasons['autumn']:
    print('Это Осень')

#if month != seasons:
    #print('Вы ввели неправильный диапазон месяца')
