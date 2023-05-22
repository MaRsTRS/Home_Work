'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.'''



class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[-1, 20], [36, 40], [51, -1]])
new_m = Matrix([[32, 2], [1, 3], [0, 87]])
print(m.__add__(new_m))

m = Matrix([[-1, 0, 31], [-1, 4, 4], [0, 60, -1]])
new_m = Matrix([[4, 5, 1], [3, 0, 2], [-1, 4, -7]])
print(m.__add__(new_m))

m = Matrix([[-1, 5, 5, 1], [10, 0, 5, 0]])
new_m = Matrix([[4, 0, 3, 2], [-2, 3, 2, 1]])
print(m.__add__(new_m))