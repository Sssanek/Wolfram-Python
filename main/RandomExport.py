import random
import pandas as pd
from tkinter import filedialog


def digit_try_int(n):
    flag = False
    try:
        n = float(n)
        if int(n) != float(n):
            flag = True
    except ValueError:
        flag = True
    return flag


def digit_try(n):
    flag = False
    try:
        n = float(n)
    except ValueError:
        flag = True
    return flag


def check(n, m):
    flag = True
    if n == 'n' or m == 'm':
        return flag, 'Введите все размерности'
    if digit_try_int(n) or digit_try_int(m):
        return flag, 'Размерности должны быть целыми числами'
    path = filedialog.asksaveasfilename(defaultextension='.csv')
    flag = False
    return flag, path


def export_ravn(n, m, a, b):
    if a == 'Левая граница (a)' or b == 'Правая граница (b)':
        return 'Введите коэффициенты'
    if digit_try(a) or digit_try(b):
        return 'Коэффициенты должны быть цифрами'
    a, b = float(a), float(b)
    flag, path = check(n, m)
    if flag:
        return path
    else:
        n, m = int(n), int(m)
        df = pd.DataFrame(
            data=[[random.uniform(a, b) for _ in range(m)] for _ in range(n)])
        df.to_csv(path, index=False, header=False)
        return 'Данные успешно выгружены в формате csv'


def export_norm(n, m, mu, sigma):
    if mu == 'Cреднее значение (mu)' or sigma == 'Стандартное отклонение (' \
                                                 'sigma)':
        return 'Введите коэффициенты'
    if digit_try(mu) or digit_try(sigma):
        return 'Коэффициенты должны быть цифрами'
    mu, sigma = float(mu), float(sigma)
    flag, path = check(n, m)
    if flag:
        return path
    else:
        n, m = int(n), int(m)
        mas = []
        for _ in range(m):
            q = []
            for _ in range(n):
                q.append(random.normalvariate(mu, sigma))
            mas.append(q)
        df = pd.DataFrame(data=mas)
        df.to_csv(path, index=False, header=False)
        return 'Данные успешно выгружены в формате csv'


def export_log(n, m, mu, sigma):
    if mu == 'Cреднее значение (mu)' or sigma == 'Стандартное отклонение (' \
                                                 'sigma)':
        return 'Введите коэффициенты'
    if digit_try(mu) or digit_try(sigma):
        return 'Коэффициенты должны быть цифрами'
    mu, sigma = float(mu), float(sigma)
    flag, path = check(n, m)
    if flag:
        return path
    else:
        n, m = int(n), int(m)

        mas = []
        for _ in range(m):
            q = []
            for _ in range(n):
                q.append(random.normalvariate(mu, sigma))
            mas.append(q)
        df = pd.DataFrame(data=mas)
        df.to_csv(path, index=False, header=False)
        return 'Данные успешно выгружены в формате csv'


def export_beta(n, m, alpha, beta):
    if alpha == 'alpha>0' or beta == 'beta>0':
        return 'Введите коэффициенты'
    if digit_try(alpha) or digit_try(beta):
        return 'Коэффициенты должны быть цифрами'
    alpha, beta = float(alpha), float(beta)
    if not (alpha > 0 and beta > 0):
        return 'Коэффициенты должны быть положительными'
    flag, path = check(n, m)
    if flag:
        return path
    else:
        n, m = int(n), int(m)
        mas = []
        for _ in range(m):
            q = []
            for _ in range(n):
                q.append(random.betavariate(alpha, beta))
            mas.append(q)
        df = pd.DataFrame(data=mas)
        df.to_csv(path, index=False, header=False)
        return 'Данные успешно выгружены в формате csv'


def export_exp(n, m, lamb):
    if lamb == 'λ=1/среднее желаемое':
        return 'Введите коэффициент'
    if digit_try(lamb):
        return 'Коэффициент должен быть цифрой'
    lamb = float(lamb)
    flag, path = check(n, m)
    if flag:
        return path
    else:
        n, m = int(n), int(m)
        mas = []
        for _ in range(m):
            q = []
            for _ in range(n):
                q.append(random.expovariate(lamb))
            mas.append(q)
        df = pd.DataFrame(data=mas)
        df.to_csv(path, index=False, header=False)
        return 'Данные успешно выгружены в формате csv'


def export_gauss(n, m, x, dx):
    if x == 'значение' or dx == 'стандартное отклонение':
        return 'Введите коэффициенты'
    if digit_try(x) or digit_try(dx):
        return 'Коэффициенты должны быть цифрами'
    x, dx = float(x), float(dx)
    flag, path = check(n, m)
    if flag:
        return path
    else:
        n, m = int(n), int(m)
        df = pd.DataFrame(
            data=[[random.gauss(x, dx) for _ in range(m)] for _ in range(n)])
        df.to_csv(path, index=False, header=False)
        return 'Данные успешно выгружены в формате csv'
