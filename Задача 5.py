# Программа вычисления выручки издержек и прибыли фирмы

revenue = float(input('Введите выручку: '))
cost = float(input('Введите издержку: '))
profitability = 0

if revenue > cost:
    profitability = revenue - cost
    print('Фирма отработала в прибыль:', profitability)
    employees = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы в рассчете на каждого сотрудника: {(profitability/employees):.2f}')
elif revenue == cost:
    print('Выручка равна издержке')
else:
    print('Фирма отработала в убыток', profitability)

