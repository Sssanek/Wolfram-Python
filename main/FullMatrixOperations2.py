from math import *


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0


def int_matrix(mas):
    return list(map(int, mas))


def digit_try(mas):
    flag = False
    for i, value in enumerate(mas):
        try:
            mas[i] = int(value)
        except ValueError:
            flag = True
    return flag


def count_sobstv_2(mas):
    d = (mas[0] + mas[3]) ** 2 - 4 * (mas[0] * mas[3] - mas[1] * mas[2])
    x1 = (mas[0] + mas[3] - d ** 0.5) / 2
    x2 = (mas[0] + mas[3] + d ** 0.5) / 2
    return round(x1, 2), round(x2, 2)


def count_sobstv_3(mas):
    a = -1
    b = mas[0] + mas[4] + mas[8]
    c = - (mas[0] * mas[4] + mas[0] * mas[8] + mas[4] * mas[8] -
           mas[5] * mas[7] - mas[1] * mas[3] - mas[2] * mas[6])
    d = mas[0] * mas[4] * mas[8] - mas[0] * mas[5] * mas[7] - \
        mas[1] * mas[3] * mas[8] + mas[1] * mas[5] * mas[6] + \
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
            fi = (1 / 3) * acosh(abs(r) / q ** (2 / 3))
            x1 = -2 * sgn(r) * q ** 0.5 * cosh(fi) - a / 3
        if q < 0:
            fi = 1 / 3 * acosh(1 + abs(r) / abs(q ** 3))
            x1 = -2 * sgn(r) * abs(q) ** 0.5 * cosh(fi) - a / 3
        if q == 0:
            x1 = -(c - a ** 3 / 27) ** 1 / 3 - a / 3
    elif s == 0:
        x1 = -2 * r ** (1 / 3) - a / 3
        x2 = r ** (1 / 3) - a / 3
    if x2 == 'nan':
        return x1, 'nan'
    else:
        return x1, x2


def spectr_razl_operation(matrix, dim):
    if dim == '2 на 2':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if digit_try(matrix):
            return 'Введите цифры в поля'
        matrix = int_matrix(matrix)
        det = matrix[0] * matrix[3] - matrix[2] * matrix[1]
        if det == 0:
            return 'Обратную матрицу невозможно найти,\n' \
                   'так как детерминант матрицы равен нулю'
        if (matrix[0] + matrix[3]) ** 2 - 4 * (matrix[0] * matrix[3] -
                                               matrix[1] * matrix[2]) < 0:
            return 'У матрицы нет собственных чисел'
        matrix_priv = [round(matrix[i] / det, 2) for i in range(4)]
        x1, x2 = count_sobstv_2(matrix)
        flag = True
        A = matrix[0] - matrix[2] - x1
        B = matrix[1] - matrix[3] + x1
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
            x1 = x2
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
            return '|' + str(round(y1, 2)) + '| ' + '|' + str(x1) + ' 0| ' + \
                   '|' + str(matrix_priv[0]) + ' ' + str(matrix_priv[2]) + \
                   '|\n' + '|' + str(round(y2, 2)) + '| ' + '|0 ' \
                   + str(x1) + '| ' + '|' + str(matrix_priv[1]) + ' ' + \
                   str(matrix_priv[3]) + '|'
    elif dim == '3 на 3':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if digit_try(matrix):
            return 'Введите цифры в поля'
        matrix = int_matrix(matrix)
        det = matrix[0] * (matrix[4] * matrix[8] - matrix[5] * matrix[7]) \
            - matrix[1] * (matrix[3] * matrix[8] - matrix[5] * matrix[6]) \
            + matrix[2] * (matrix[3] * matrix[7] - matrix[6] * matrix[4])
        if det == 0:
            return 'Обратную матрицу невозможно найти,\n' \
                   'так как детерминант матрицы равен нулю'
        matrix_priv = [round(matrix[i] / det, 2) for i in range(9)]
        x1, x2 = count_sobstv_3(matrix)
        y1, y2, y3 = 0, 0, 0
        if x2 == 'nan':
            x2 = x1
        y1, y2, y3 = 0, 0, 0
        flag = True
        a = (matrix[0] - x1 + matrix[3] + matrix[6])
        b = (matrix[1] + matrix[4] - x1 + matrix[7])
        c = (matrix[2] + matrix[5] + matrix[8] - x1)
        if a == b == c == 0:
            y1, y2, y3 = 1, 1, 1
        if (a == 0 and b == 0) or (a == 0 and c == 0) or (
                c == 0 and b == 0):
            pass
        else:
            if a == 0:
                y1 = 1
                y2 = 1
                y3 = - b / c
                flag = False
            if b == 0:
                y2 = 1
                y1 = 1
                y3 = - a / c
                flag = False
            if c == 0:
                y3 = 1
                y1 = 1
                y2 = - a / b
                flag = False
            if y1 == y2 == y3 == 0:
                y1 = 1
                y2 = 1
                y3 = - (a + b) / c
                flag = False
            if flag:
                a = (matrix[0] - x2 + matrix[3] + matrix[6])
                b = (matrix[1] + matrix[4] - x2 + matrix[7])
                c = (matrix[2] + matrix[5] + matrix[8] - x2)
                if a == b == c == 0:
                    y1, y2, y3 = 1, 1, 1
                if (a == 0 and b == 0) or (a == 0 and c == 0) or (
                        c == 0 and b == 0):
                    pass
                else:
                    if a == 0:
                        y1 = 1
                        y2 = 1
                        y3 = - b / c
                        flag = False
                    if b == 0:
                        y2 = 1
                        y1 = 1
                        y3 = - a / c
                        flag = False
                    if c == 0:
                        y3 = 1
                        y1 = 1
                        y2 = - a / b
                        flag = False
                    if y1 == y2 == y3 == 0:
                        y1 = 1
                        y2 = 1
                        y3 = - (a + b) / c
                        flag = False
        if flag:
            return 'У матрицы нет спектрального разложения'
        else:
            x1 = round(x1, 2)
            return '|' + str(round(y1, 2)) + '| ' + '|' + str(x1) + \
                   '  0  0| ' + '|' + str(matrix[0]) + ' ' + str(
                matrix[3]) + ' ' + str(matrix[6]) + '|\n' + '|' + \
                str(round(y2, 2)) + '| ' + '|0 ' + str(x1) + \
                ' 0| ' + '|' + str(
                matrix[1]) + ' ' + str(matrix[4]) + ' ' + str(
                matrix[7]) + '|\n' + '|' + str(round(y3, 2)) + '| ' + \
                '|0  0 ' + str(x1) + '| ' + '|' + str(matrix[2]) + \
                ' ' + str(
                matrix[5]) + ' ' + str(matrix[8]) + '|'
    return 'Что-то пошло не так'