from math import *

def digit_try(mas):
    flag = False
    for i, value in enumerate(mas):
        try:
            mas[i] = int(value)
        except ValueError:
            flag = True
    return flag


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0


def int_matrix(mas):
    return list(map(int, mas))


def count_sobstv_2(mas):
    d = (mas[0] + mas[3]) ** 2 - 4 * (mas[0] * mas[3] - mas[1] * mas[2])
    x1 = (mas[0] + mas[3] - d ** 0.5) / 2
    x2 = (mas[0] + mas[3] + d ** 0.5) / 2
    return round(x1, 2), round(x2, 2)


def count_sobstv_3(mas):
    a = -1
    b = mas[0] + mas[4] + mas[8]
    c = - (mas[0] * mas[4] + mas[0] * mas[8] + mas[4] * mas[8] - mas[5] * mas[7] - mas[1] * mas[3] - mas[2] * mas[6])
    d = mas[0] * mas[4] * mas[8] - mas[0] * mas[5] * mas[7] - mas[1] * mas[3] * mas[8] + mas[1] * mas[5] * mas[6] + mas[2] * mas[3] * mas[7] - mas[2] * mas[6] * mas[4]
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


def holetsky_operation(matrix, dim):
    if dim == '2 на 2':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if digit_try(matrix):
            return 'Введите цифры в поля'
        if matrix[1] != matrix[2]:
            return 'Матрица для разложения Холецкого\nдолжна быть симметричной'
        matrix = int_matrix(matrix)
        try:
            l11 = matrix[0] ** 0.5
            l21 = matrix[1] / l11
            l22 = (matrix[3] - matrix[1] ** 2 / matrix[0])
        except ValueError:
            return 'Матрица не положительна'
        l11 = complex(round(l11.real, 2), round(l11.imag, 2))
        l21 = complex(round(l21.real, 2), round(l21.imag, 2))
        l22 = complex(round(l22.real, 2), round(l22.imag, 2))
        return '|' + str(l11) + ' 0 ' + '| |' + str(l11) + ' ' + str(l21) + '|\n|' + str(l21) + ' ' + str(l22) + '| | 0 ' + str(l22) + '| '
    elif dim == '3 на 3':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if digit_try(matrix):
            return 'Введите цифры в поля'
        if matrix[3] != matrix[1] or matrix[6] != matrix[2] or matrix[7] != matrix[5]:
            return 'Матрица для разложения Холецкого\nдолжна быть ' \
                   'симметричной '
        try:
            matrix = int_matrix(matrix)
            l11 = matrix[0] ** 0.5
            l21 = matrix[1] / l11
            l31 = matrix[2] / l11
            l22 = (matrix[4] - matrix[1] ** 2 / matrix[0]) ** 0.5
            l32 = (matrix[5] - l21 * l31) / l22
            l33 = (matrix[8] - l31 ** 2 - l32 ** 2) ** 0.5
        except ValueError:
            return 'Матрица не положительна'
        l11 = complex(round(l11.real, 2), round(l11.imag, 2))
        l21 = complex(round(l21.real, 2), round(l21.imag, 2))
        l31 = complex(round(l31.real, 2), round(l31.imag, 2))
        l22 = complex(round(l22.real, 2), round(l22.imag, 2))
        l32 = complex(round(l32.real, 2), round(l32.imag, 2))
        l33 = complex(round(l33.real, 2), round(l33.imag, 2))
        return '|' + str(l11) + ' 0 ' + '0| |' + str(l11) + ' ' + str(l21) + ' ' + str(l31) + '|\n' + '|' + str(l21) + ' ' + str(l22) + ' 0| | 0 ' + str(l22) + ' ' + str(l32) + '|\n' + '|' + str(l31) + ' ' + str(l32) + ' ' + str(l33) + '| |0  0 ' + str(l33) + '|'


def determinant_operation(matrix, dim):
    if dim == '2 на 2':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if digit_try(matrix):
            return 'Введите цифры в поля'
        matrix = int_matrix(matrix)
        det = matrix[0] * matrix[3] - matrix[2] * matrix[1]
        return 'Детерминант матрицы: ' + str(det)
    elif dim == '3 на 3':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if digit_try(matrix):
            return 'Введите цифры в поля'
        matrix = int_matrix(matrix)
        det = matrix[0] * (matrix[4] * matrix[8] - matrix[5] * matrix[7]) - \
              matrix[1] * (matrix[3] * matrix[8] - matrix[5] * matrix[6]) + \
              matrix[2] * (matrix[3] * matrix[7] - matrix[6] * matrix[4])
        return 'Детерминант матрицы: ' + str(det)
    return 'Что-то пошло не так'


def obratn_operation(matrix, dim):
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
        matrix = [round(matrix[i] / det, 2) for i in range(4)]
        return 'Обратная матрица:\n' + '|' + str(matrix[0]) + ' ' + str(
            matrix[2]) + '|\n|' + str(matrix[1]) + ' ' + str(matrix[3]) + '|'
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
        matrix = [round(matrix[i] / det, 2) for i in range(9)]
        return 'Обратная матрица:\n' + '|' + str(matrix[0]) + ' ' + str(
            matrix[3]) + ' ' + str(matrix[6]) + '|\n|' + str(
            matrix[1]) + ' ' + str(matrix[4]) + ' ' + str(
            matrix[7]) + '|\n|' + str(matrix[2]) + ' ' + str(
            matrix[5]) + ' ' + str(matrix[8]) + '|'
    return 'Что-то пошло не так'

def sobstv_chisla_operation(matrix, dim):
    if dim == '2 на 2':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if digit_try(matrix):
            return 'Введите цифры в поля'
        matrix = int_matrix(matrix)
        if (matrix[0] + matrix[3]) ** 2 - 4 * (matrix[0] * matrix[3] - matrix[1] * matrix[2]) < 0:
            return 'У матрицы нет собственных чисел'
        x1, x2 = count_sobstv_2(matrix)
        return 'Собственные числа матрицы: ' + str(x1) + ' ' + str(x2)
    elif dim == '3 на 3':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if digit_try(matrix):
            return 'Введите цифры в поля'
        matrix = int_matrix(matrix)
        x1, x2 = count_sobstv_3(matrix)
        if x2 == 'nan':
            return 'Собственные числа матрицы: ' + str(round(x1, 2))
        else:
            return 'Собственные числа матрицы: ' + str(round(x1, 2)) + ' ' + str(round(x2, 2))
    return 'Что-то пошло не так'