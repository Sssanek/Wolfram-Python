from math import cos, pi


def digit_try(mas):
    flag = False
    for i, value in enumerate(mas):
        try:
            mas[i] = int(value)
        except ValueError:
            flag = True
    return flag


def scalar_coord_operation(x1, y1, z1, x2, y2, z2, check):
    if check == 'two':
        if x1 == '' or x2 == '' or y1 == '' or y2 == '':
            return 'введите числа в пустые поля'
        if digit_try([x1, y1, x2, y2]):
            return 'введите числа'
        return str(int(x1) * int(x2) + int(y1) * int(y2))
    elif check == 'three':
        if any([x1 == '', x2 == '', y1 == '', y2 == '', z1 == '', z2 == '']):
            return 'введите числа в пустые поля'
        if digit_try([x1, y1, x2, y2, z1, z2]):
            return 'введите числа'
        return str(int(x1) * int(x2) + int(y1) * int(y2) + int(z1) * int(z2))


def scalar_angle_operation(m1, m2, angle):
    if m1 == '' or m2 == '' or angle == '':
        return 'введите числа в пустые поля'
    if digit_try([m1, m2, angle]):
        return 'введите числа'
    if int(m1) < 0 or int(m2) < 0:
        return 'Модуль это положительная величина'
    return str(round(
        (cos(float(angle) * pi / 180) * float(m1) * float(m2)), 2)
    )


def vector_cord_operation(x1, y1, z1, x2, y2, z2, check):
    if check == 'two':
        if x1 == '' or x2 == '' or y1 == '' or y2 == '':
            return 'введите числа в пустые поля'
        if digit_try([x1, y1, x2, y2]):
            return 'введите числа'
        return str(int(x1) * int(y2) - int(y1) * int(x2)) + ' * k'
    elif check == 'three':
        if any([x1 == '', x2 == '', y1 == '', y2 == '', z1 == '', z2 == '']):
            return 'введите числа в пустые поля'
        if digit_try([x1, y1, x2, y2, z1, z2]):
            return 'введите числа'
        i = int(y1) * int(z2) - int(z1) * int(y2)
        j = int(x1) * int(z2) - int(x2) * int(z1)
        k = int(x1) * int(y2) - int(x2) * int(y1)
        return 'i*(' + str(i) + ') + j*(' + str(j) + ') + k*(' + str(k) +\
               ')\n' + '('+str(i) + ',' + str(j) + ',' + str(k) + ')'