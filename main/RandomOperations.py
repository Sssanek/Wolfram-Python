import random


def digit_try(n):
    flag = False
    try:
        n = float(n)
    except ValueError:
        flag = True
    return flag


def one_ravn(a, b):
    if a == 'Левая граница (a)' or b == 'Правая граница (b)':
        return 'Введите коэффициенты'
    if digit_try(a) or digit_try(b):
        return 'Коэффициенты должны быть цифрами'
    a, b = float(a), float(b)
    return str(random.uniform(a, b))


def one_norm(mu, sigma):
    if mu == 'Cреднее значение (mu)' or sigma == 'Стандартное отклонение (' \
                                                 'sigma)':
        return 'Введите коэффициенты'
    if digit_try(mu) or digit_try(sigma):
        return 'Коэффициенты должны быть цифрами'
    mu, sigma = float(mu), float(sigma)
    return str(random.normalvariate(mu, sigma))


def one_log(mu, sigma):
    if mu == 'Cреднее значение (mu)' or sigma == 'Стандартное отклонение (' \
                                                 'sigma)':
        return 'Введите коэффициенты'
    if digit_try(mu) or digit_try(sigma):
        return 'Коэффициенты должны быть цифрами'
    mu, sigma = float(mu), float(sigma)
    return str(random.normalvariate(mu, sigma))


def one_beta(alpha, beta):
    if alpha == 'alpha>0' or beta == 'beta>0':
        return 'Введите коэффициенты'
    if digit_try(alpha) or digit_try(beta):
        return 'Коэффициенты должны быть цифрами'
    alpha, beta = float(alpha), float(beta)
    if not (alpha > 0 and beta > 0):
        return 'Коэффициенты должны быть положительными'
    return str(random.betavariate(alpha, beta))


def one_exp(lamb):
    if lamb == 'λ=1/среднее желаемое':
        return 'Введите коэффициент'
    if digit_try(lamb):
        return 'Коэффициент должен быть цифрой'
    lamb = float(lamb)
    return str(random.expovariate(lamb))


def one_gauss(x, dx):
    if x == 'значение' or dx == 'стандартное отклонение':
        return 'Введите коэффициенты'
    if digit_try(x) or digit_try(dx):
        return 'Коэффициенты должны быть цифрами'
    x, dx = float(x), float(dx)
    return str(random.gauss(x, dx))
