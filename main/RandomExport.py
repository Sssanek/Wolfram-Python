import random
import pandas as pd
from tkinter import filedialog


# проверка, является введенная строка целым числом
def digit_try_int(n):
    flag = False
    try:
        n = float(n)
        if int(n) != float(n):
            flag = True
    except ValueError:
        flag = True
    return flag


# проверка, является введенная строка числом
def digit_try(n):
    flag = False
    try:
        n = float(n)
    except ValueError:
        flag = True
    return flag


# общая для всех функций вывода часть для проверки наличия размерности матрицы вывода
def check(n, m):
    flag = True
    if n == 'n' or m == 'm':
        return flag, 'Введите все размерности'
    if digit_try_int(n) or digit_try_int(m):
        return flag, 'Размерности должны быть целыми числами'
    # открываем диалоговое окно и просим выбрать место и дать название файлу экспорта
    path = filedialog.asksaveasfilename(defaultextension='.csv')
    flag = False
    return flag, path


# функции экспорта рандомных чисел из приведенных распределений
def export_ravn(n, m, a, b):
    # проверка значений на наличие и корректность
    if a == 'Левая граница (a)' or b == 'Правая граница (b)':
        return 'Введите коэффициенты'
    if digit_try(a) or digit_try(b):
        return 'Коэффициенты должны быть цифрами'
    a, b = float(a), float(b)
    # путь сохранения файла
    flag, path = check(n, m)
    if flag:
        return path
    else:
        # формулирую матрицу из списков питона, затем конвертирую их в дата фрейм, который по итогу экспортирую
        n, m = int(n), int(m)
        df = pd.DataFrame(
            data=[[random.uniform(a, b) for _ in range(m)] for _ in range(n)])
        df.to_csv(path, index=False, header=False)
        return 'Данные успешно выгружены в формате csv'


def export_norm(n, m, mu, sigma):
    # проверка значений на наличие и корректность
    if mu == 'Cреднее значение (mu)' or sigma == 'Стандартное отклонение (' \
                                                 'sigma)':
        return 'Введите коэффициенты'
    if digit_try(mu) or digit_try(sigma):
        return 'Коэффициенты должны быть цифрами'
    mu, sigma = float(mu), float(sigma)
    # путь сохранения файла
    flag, path = check(n, m)
    if flag:
        return path
    else:
        # формулирую матрицу из списков питона, затем конвертирую их в дата фрейм, который по итогу экспортирую
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
    # проверка значений на наличие и корректность
    if mu == 'Cреднее значение (mu)' or sigma == 'Стандартное отклонение (' \
                                                 'sigma)':
        return 'Введите коэффициенты'
    if digit_try(mu) or digit_try(sigma):
        return 'Коэффициенты должны быть цифрами'
    mu, sigma = float(mu), float(sigma)
    # путь сохранения файла
    flag, path = check(n, m)
    if flag:
        return path
    else:
        # формулирую матрицу из списков питона, затем конвертирую их в дата фрейм, который по итогу экспортирую
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
    # проверка значений на наличие и корректность
    if alpha == 'alpha>0' or beta == 'beta>0':
        return 'Введите коэффициенты'
    if digit_try(alpha) or digit_try(beta):
        return 'Коэффициенты должны быть цифрами'
    alpha, beta = float(alpha), float(beta)
    if not (alpha > 0 and beta > 0):
        return 'Коэффициенты должны быть положительными'
    # путь сохранения файла
    flag, path = check(n, m)
    if flag:
        return path
    else:
        # формулирую матрицу из списков питона, затем конвертирую их в дата фрейм, который по итогу экспортирую
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
    # проверка значений на наличие и корректность
    if lamb == 'λ=1/среднее желаемое':
        return 'Введите коэффициент'
    if digit_try(lamb):
        return 'Коэффициент должен быть цифрой'
    lamb = float(lamb)
    # путь сохранения файла
    flag, path = check(n, m)
    if flag:
        return path
    else:
        # формулирую матрицу из списков питона, затем конвертирую их в дата фрейм, который по итогу экспортирую
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
    # проверка значений на наличие и корректность
    if x == 'значение' or dx == 'стандартное отклонение':
        return 'Введите коэффициенты'
    if digit_try(x) or digit_try(dx):
        return 'Коэффициенты должны быть цифрами'
    x, dx = float(x), float(dx)
    # путь сохранения файла
    flag, path = check(n, m)
    if flag:
        return path
    else:
        # формулирую матрицу из списков питона, затем конвертирую их в дата фрейм, который по итогу экспортирую
        n, m = int(n), int(m)
        df = pd.DataFrame(
            data=[[random.gauss(x, dx) for _ in range(m)] for _ in range(n)])
        df.to_csv(path, index=False, header=False)
        return 'Данные успешно выгружены в формате csv'
