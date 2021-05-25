from math import *


# функция sign(), нужная для выполнения расчетов
def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0


# функция, которая приводит все значения матрицы в численный тип
def int_matrix(mas):
    return list(map(float, mas))


# проверка значений, внесены ли числа
def digit_try(mas):
    flag = False
    for i, value in enumerate(mas):
        try:
            mas[i] = int(value)
        except ValueError:
            flag = True
    return flag


# функция для решения квадратного уравнения, позволяющее найти собственные числа матрицы
def count_sobstv_2(mas):
    d = (mas[0] + mas[3]) ** 2 - 4 * (mas[0] * mas[3] - mas[1] * mas[2])
    x1 = (mas[0] + mas[3] - d ** 0.5) / 2
    x2 = (mas[0] + mas[3] + d ** 0.5) / 2
    return round(x1, 2), round(x2, 2)


# решение кубического уравнения по тригонометрической формуле Виета для кубических уравнений
def count_sobstv_3(mas):
    a = -1
    b = mas[0] + mas[4] + mas[8]
    c = - (mas[0] * mas[4] + mas[0] * mas[8] + mas[4] * mas[8] -
           mas[5] * mas[7] - mas[1] * mas[3] - mas[2] * mas[6])
    d = mas[0] * mas[4] * mas[8] - mas[0] * mas[5] * mas[7] -\
        mas[1] * mas[3] * mas[8] + mas[1] * mas[5] * mas[6] +\
        mas[2] * mas[3] * mas[7] - mas[2] * mas[6] * mas[4]
    q = (a ** 2 - 3 * b) / 9
    r = (2 * a ** 3 - 9 * a * b + 27 * c) / 54
    s = q ** 3 - r ** 2
    x1, x2 = 'nan', 'nan'
    if s > 0:
        fi = 1 / 3 * acos(r / (q ** 3) ** 0.5)
        x1 = -2 * q ** 0.5 * cos(fi) - a / 3
        x2 = -2 * q ** 0.5 * cos(fi + 2 * pi / 3) - a / 3
        x3 = -2 * q ** 0.5 * cos(fi - 2 * pi / 3) - a / 3
    elif s < 0:
        if q > 0:
            fi = (1 / 3) * acosh(abs(r) / q ** (2/3))
            x1 = -2 * sgn(r) * q ** 0.5 * cosh(fi) - a / 3
        if q < 0:
            fi = 1 / 3 * acosh(1 + abs(r) / abs(q ** 3))
            x1 = -2 * sgn(r) * abs(q) ** 0.5 * cosh(fi) - a / 3
        if q == 0:
            x1 = -(c - a ** 3 / 27) ** 1/3 - a / 3
    elif s == 0:
        x1 = -2 * r ** (1 / 3) - a / 3
        x2 = r ** (1 / 3) - a / 3
    if x2 == 'nan':
        return x1, 'nan'
    else:
        return x1, x2

# функция поиска собственных векторов матрицы
def sobstv_vectors_operation(matrix, dim):
    # ветка матрицы 2 на 2
    if dim == '2 на 2':
        # проверка и приведение данных
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if digit_try(matrix):
            return 'Введите цифры в поля'
        matrix = int_matrix(matrix)
        x1, x2 = count_sobstv_2(matrix)
        flag = True
        # в зависимости от решения квадратного уравнения и нахождения собственных чисел матрицы определяется решение
        # системы уравнений для того, чтобы сформулировать собственный вектор
        A = matrix[0] - matrix[2] - x1
        B = matrix[1] - matrix[3] + x1
        # значения вектора изначальна не определены
        y1, y2 = 'nan', 'nan'
        if (A == 0 and B != 0) or (A != 0 and B == 0):
            pass
        else:
            if A == 0 and B == 0:
                y1, y2 = 1, 1
                flag = False
            else:
                y1 = 1
                y2 = - A / B
                flag = False
        if flag:
            A = matrix[0] - matrix[2] - x2
            B = matrix[1] - matrix[3] + x2
            if (A == 0 and B != 0) or (A != 0 and B == 0):
                pass
            else:
                if A == 0 and B == 0:
                    y1, y2 = 1, 1
                    flag = False
                else:
                    y1 = 1
                    y2 = - A / B
                    flag = False
        if flag:
            return 'У матрицы нет собственных векторов'
        else:
            return 'собственный вектор матрицы:\n' +\
                   '(' + str(round(y1, 2)) + ',' + str(round(y2, 2)) + ') '
    # ветка 3 на 3
    elif dim == '3 на 3':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if digit_try(matrix):
            return 'Введите цифры в поля'
        matrix = int_matrix(matrix)
        x1, x2 = count_sobstv_3(matrix)
        # аналогично значения вектора (здесь уже трехмерного)
        u1, u2, u3 = 0, 0, 0
        # в зависимости от решений уравнения различные сценарии подсчета, вытекающие из решения системы путем
        # подстановки некторых переменных
        if x2 == 'nan':
            flag = True
            a = (matrix[0] - x1 + matrix[3] + matrix[6])
            b = (matrix[1] + matrix[4] - x1 + matrix[7])
            c = (matrix[2] + matrix[5] + matrix[8] - x1)
            if a == b == c == 0:
                return 'Собственный вектор матрицы:\n(1, 1, 1)'
            if a == 0 and b == 0:
                return 'У матрицы нет собственных векторов'
            if a == 0 and c == 0:
                return 'У матрицы нет собственных векторов'
            if c == 0 and b == 0:
                return 'У матрицы нет собственных векторов'
            if a == 0:
                y1 = 1
                y2 = 1
                y3 = - b / c
                return 'собственный вектор матрицы:\n' + '('\
                       + str(round(y1, 2)) + ',' + str(round(y2, 2)) +\
                       ',' + str(round(y3, 2)) + ')'
            if b == 0:
                y2 = 0
                y1 = 0
                y3 = - a / c
                return 'собственный вектор матрицы:\n' + '(' + str(
                    round(y1, 2)) + ',' + str(round(y2, 2)) + ',' + str(
                    round(y3, 2)) + ')'
            if c == 0:
                y3 = 1
                y1 = 1
                y2 = - a / b
                return 'собственный вектор матрицы:\n' + '(' + str(
                    round(y1, 2)) + ',' + str(round(y2, 2)) + ',' + str(
                    round(y3, 2)) + ')'
            y1 = 1
            y2 = 1
            y3 = - (a + b) / c
            return 'собственный вектор матрицы:\n' + '(' + str(
                round(y1, 2)) + ',' + str(round(y2, 2)) + ',' + str(
                round(y3, 2)) + ')'
        else:
            y1, y2, y3 = 0, 0, 0
            count = 0
            a = (matrix[0] - x1 + matrix[3] + matrix[6])
            b = (matrix[1] + matrix[4] - x1 + matrix[7])
            c = (matrix[2] + matrix[5] + matrix[8] - x1)
            if a == b == c == 0:
                y1, y2, y3 = 1, 1, 1
            if (a == 0 and b == 0) or (a == 0 and c == 0)\
                    or (c == 0 and b == 0):
                pass
            else:
                if a == 0:
                    y1 = 1
                    y2 = 1
                    y3 = - b / c
                    count += 1
                if b == 0:
                    y2 = 1
                    y1 = 1
                    y3 = - a / c
                    count += 1
                if c == 0:
                    y3 = 1
                    y1 = 1
                    y2 = - a / b
                    count += 1
                if y1 == y2 == y3 == 0:
                    y1 = 1
                    y2 = 1
                    y3 = - (a + b) / c
                    count += 1
                a = (matrix[0] - x2 + matrix[3] + matrix[6])
                b = (matrix[1] + matrix[4] - x2 + matrix[7])
                c = (matrix[2] + matrix[5] + matrix[8] - x2)
                if a == b == c == 0:
                    u1, u2, u3 = 1, 1, 1
                if (a == 0 and b == 0) or (a == 0 and c == 0) or (
                        c == 0 and b == 0):
                    pass
                else:
                    if a == 0:
                        u1 = 1
                        u2 = 1
                        u3 = - b / c
                        count += 1
                    if b == 0:
                        u2 = 1
                        u1 = 1
                        u3 = - a / c
                        count += 1
                    if c == 0:
                        u3 = 1
                        u1 = 1
                        u2 = - a / b
                        count += 1
                    if u1 == u2 == u3 == 0:
                        u1 = 1
                        u2 = 1
                        u3 = - (a + b) / c
                        count += 1
        # вывод результата
        if count == 0:
            return 'У матрицы нет собственных векторов'
        elif count == 1:
            if u1 == u2 == u3 == 0:
                return 'собственный вектор матрицы:\n' + '(' + str(
                    round(y1, 2)) + ',' + str(round(y2, 2)) + ',' + str(
                    round(y3, 2)) + ')'
            else:
                return 'собственный вектор матрицы:\n' + '(' + str(
                    round(u1, 2)) + ',' + str(round(u2, 2)) + ',' + str(
                    round(u3, 2)) + ')'
        elif count == 2:
            'собственные вектора матрицы:\n' + '(' + str(
                round(y1, 2)) + ',' + str(round(y2, 2)) + ',' + str(
                round(y3, 2)) + ')\n' + '(' + str(
                round(u1, 2)) + ',' + str(round(u2, 2)) + ',' + str(
                round(u3, 2)) + ')'
    return 'Что-то пошло не так'
