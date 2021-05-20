from math import *
import parser


def digit_try(n):
    flag = False
    try:
        n = float(n)
    except ValueError:
        flag = True
    return flag


def bisection_operation(a, b, epsilon, func):
    exp = e
    epsilon = epsilon.replace('^', '**')
    if a == '' or b == '':
        return 'Введите границы'
    if epsilon == '':
        return 'Введите точность'
    if func == '':
        return 'Введите уравнение'
    if digit_try(a) or digit_try(b):
        return 'Границы должны быть числами'
    a, b = float(a), float(b)
    if digit_try(epsilon):
        return 'Точность должна быть числом'
    epsilon = float(epsilon)
    if epsilon < 0:
        return 'Точность - положительная величина'
    if a == b:
        return 'Границы не должны совпадать'
    if a > b:
        return 'Левая граница должна быть меньше правой'
    x = (a + b) / 2
    func = func.split('=')[0]
    func = func.replace('^', '**')
    func = func.replace('e', 'exp')
    try:
        code = parser.expr(func).compile()
    except SyntaxError:
        return 'Не корректное выражение'
    try:
        eval(code)
    except TypeError:
        return 'Не корректное выражение'
    x = a
    fa = eval(code)
    x = b
    fb = eval(code)
    if fa * fb > 0:
        return 'F(a) и F(b) должны быть разного знака'
    for _ in range(100):
        c = (a + b) / 2
        x = c
        fc = eval(code)
        if abs(fc) <= epsilon:
            return str(c)
        if fa*fc > 0:
            a, fa = c, fc
        if fb*fc > 0:
            b, fb = c, fc
    return 'Не удалось решить'


def newton_operation(func, x0, epsilon):
    exp = e
    epsilon = epsilon.replace('^', '**')
    if x0 == '':
        return 'Введите начальное значение x0'
    if epsilon == '':
        return 'Введите точность'
    if func == '':
        return 'Введите уравнение'
    if digit_try(x0):
        return 'Начальное значение должно быть числом'
    x0 = float(x0)
    if digit_try(epsilon):
        return 'Точность должна быть числом'
    epsilon = float(epsilon)
    if epsilon < 0:
        return 'Точность - положительная величина'
    x = x0
    func = func.split('=')[0]
    func = func.replace('^', '**')
    func = func.replace('e', 'exp')
    try:
        code = parser.expr(func).compile()
    except SyntaxError:
        return 'Не корректное выражение'
    try:
        eval(code)
    except TypeError:
        return 'Не корректное выражение'
    fx = eval(code)
    dx = 1e-6
    for _ in range(100):
        if abs(fx) < epsilon:
            return str(x)
        x1 = x
        x = x + dx
        f1 = eval(code)
        x = x - 2 * dx
        f2 = eval(code)
        df = f1 - f2
        fpx = df / (2 * dx)
        x = x1
        if abs(fpx) < epsilon:
            return str(x)
        x = x - fx / fpx
        fx = eval(code)
    return 'Не удалось решить'
