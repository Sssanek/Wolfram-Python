from tkinter import *
from tkinter import ttk, messagebox
from main.styledWidgets import HoverButton, EntryWithPlaceholder
from math import *


class Calc(Frame):
    def __init__(self, parent, db):

        # Задание основных переменных
        self.parent = parent
        self.db = db

        # Кнопка возврата назад
        self.back = HoverButton(
            self.parent,
            font=("Courier", 18),
            text='Назад',
            activebackground='#00ff00',
            command=self.returnBack
        )
        self.back.pack(anchor=NW, padx=20, pady=20)

        # Настраиваем считывание нажатий клавиш
        self.parent.bind('<Key>', self.press_key)

        # Основной фрейм
        self.mainPart = Frame(self.parent)

        # Создаем поле ввода арифметического калькулятора
        self.calc = Entry(self.mainPart, justify=RIGHT,
                          font=('Comic Sans', 17), width=15)
        self.calc.insert(0, '0')
        self.calc['state'] = DISABLED
        self.calc.grid(row=0, column=0, columnspan=4, stick='we')

        # Создаем кнопки цифр арифметического калькулятора
        self.Button_1 = Button(self.mainPart, text='1', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit(1))
        self.Button_1.grid(row=1, column=0, stick='wens', padx=5, pady=5)
        self.Button_2 = Button(self.mainPart, text='2', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit(2))
        self.Button_2.grid(row=1, column=1, stick='wens', padx=5, pady=5)
        self.Button_3 = Button(self.mainPart, text='3', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit(3))
        self.Button_3.grid(row=1, column=2, stick='wens', padx=5, pady=5)
        self.Button_4 = Button(self.mainPart, text='4', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit(4))
        self.Button_4.grid(row=2, column=0, stick='wens', padx=5, pady=5)
        self.Button_5 = Button(self.mainPart, text='5', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit(5))
        self.Button_5.grid(row=2, column=1, stick='wens', padx=5, pady=5)
        self.Button_6 = Button(self.mainPart, text='6', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit(6))
        self.Button_6.grid(row=2, column=2, stick='wens', padx=5, pady=5)
        self.Button_7 = Button(self.mainPart, text='7', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit(7))
        self.Button_7.grid(row=3, column=0, stick='wens', padx=5, pady=5)
        self.Button_8 = Button(self.mainPart, text='8', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit(8))
        self.Button_8.grid(row=3, column=1, stick='wens', padx=5, pady=5)
        self.Button_9 = Button(self.mainPart, text='9', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit(9))
        self.Button_9.grid(row=3, column=2, stick='wens', padx=5, pady=5)
        self.Button_0 = Button(self.mainPart, text='0', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit(0))
        self.Button_0.grid(row=4, column=0, stick='wens', padx=5, pady=5)

        # Создаем кнопки операций арифметического калькулятора
        self.Button_plus = Button(self.mainPart, text='+', bd=5,
                                  font=('Comic Sans', 15), fg='red',
                                  command=lambda: self.add_operation('+'))
        self.Button_plus.grid(row=1, column=3, stick='wens', padx=5, pady=5)
        self.Button_minus = Button(self.mainPart, text='-', bd=5,
                                   font=('Comic Sans', 15), fg='red',
                                   command=lambda: self.add_operation('-')
                                   )
        self.Button_minus.grid(row=2, column=3, stick='wens', padx=5, pady=5)
        self.Button_mul = Button(self.mainPart, text='*', bd=5,
                                 font=('Comic Sans', 15), fg='red',
                                 command=lambda: self.add_operation('*'))
        self.Button_mul.grid(row=3, column=3, stick='wens', padx=5, pady=5)
        self.Button_div = Button(self.mainPart, text='/', bd=5,
                                 font=('Comic Sans', 15), fg='red',
                                 command=lambda: self.add_operation('/'))
        self.Button_div.grid(row=4, column=3, stick='wens', padx=5, pady=5)
        self.Button_equal = Button(self.mainPart, text='=', bd=5,
                                   font=('Comic Sans', 15), fg='red',
                                   command=lambda: self.calculate())
        self.Button_equal.grid(row=4, column=2, stick='wens', padx=5, pady=5)
        self.Button_C = Button(self.mainPart, text='C', bd=5,
                               font=('Comic Sans', 15), fg='red',
                               command=self.clear)
        self.Button_C.grid(row=4, column=1, stick='wens', padx=5, pady=5)
        self.Button_pi = Button(self.mainPart, text="\u03C0", bd=5,
                                font=('Comic Sans', 15),
                                command=lambda: self.add_digit('\u03C0'))
        self.Button_pi.grid(row=5, column=0, stick='wens', padx=5, pady=5)
        self.Button_e = Button(self.mainPart, text='e', bd=5,
                               font=('Comic Sans', 15),
                               command=lambda: self.add_digit('e'))
        self.Button_e.grid(row=5, column=1, stick='wens', padx=5, pady=5)

        self.Button_pow = Button(self.mainPart, text='^', bd=5,
                                 font=('Comic Sans', 15), fg='red',
                                 command=lambda: self.add_operation('^'))
        self.Button_pow.grid(row=1, column=4, stick='wens', padx=5, pady=5)
        self.Button_sqrt = Button(self.mainPart, text="\u221A", bd=5,
                                  font=('Comic Sans', 15), fg='red',
                                  command=lambda:
                                      self.add_complex_operation("\u221A"))
        self.Button_sqrt.grid(row=2, column=4, stick='wens', padx=5, pady=5)
        self.Button_fact = Button(self.mainPart, text="n!", bd=5,
                                  font=('Comic Sans', 15), fg='red',
                                  command=lambda:
                                      self.add_complex_operation('!'))
        self.Button_fact.grid(row=5, column=2, columnspan=2, stick='wens',
                              padx=5, pady=5)
        self.Button_log = Button(self.mainPart, text="log", bd=5,
                                 font=('Comic Sans', 15), fg='red',
                                 command=lambda:
                                     self.add_complex_operation("log"))
        self.Button_log.grid(row=4, column=4, stick='wens', padx=5, pady=5)
        self.Button_ln = Button(self.mainPart, text="ln", bd=5,
                                font=('Comic Sans', 15), fg='red',
                                command=lambda:
                                    self.add_complex_operation("ln"))
        self.Button_ln.grid(row=4, column=5, stick='wens', padx=5, pady=5)
        self.point_poss = True
        self.Button_point = Button(self.mainPart, text=".", bd=5,
                                   font=('Comic Sans', 15),
                                   fg='red', command=self.add_point)
        self.Button_point.grid(row=3, column=4, stick='wens', padx=5, pady=5)
        self.Button_backspace = Button(self.mainPart, text=chr(11176), bd=5,
                                       font=('Comic Sans', 9), fg='red',
                                       command=self.backspace)
        self.Button_backspace.grid(row=0, column=4, stick='wens', padx=5,
                                   pady=5)
        self.Button_lbra = Button(self.mainPart, text='(', bd=5,
                                  font=('Comic Sans', 15), fg='red',
                                  command=lambda: self.add_bracket('('))
        self.Button_lbra.grid(row=1, column=5, stick='wens', padx=5, pady=5)
        self.Button_rbra = Button(self.mainPart, text=')', bd=5,
                                  font=('Comic Sans', 15), fg='red',
                                  command=lambda: self.add_bracket(')'))
        self.Button_rbra.grid(row=3, column=5, stick='wens', padx=5, pady=5)
        self.leftBkt = 0

        # Создаем лейбл с отображением счётчика незакрытых скобок
        self.brackets = Label(self.mainPart, text=self.leftBkt)
        self.brackets.grid(row=2, column=5, stick='wens', padx=5, pady=5)

        # Создаем кнопку открытия раздела с тригонометрическими функциями
        self.Button_trygonom = Button(self.mainPart, text='Trygon', bd=5,
                                      font=('Comic Sans', 15),
                                      fg='red', command=self.active_try)
        self.Button_trygonom.grid(row=5, column=4, columnspan=2, stick='wens',
                                  padx=5, pady=5)

        # Задаём размеры кнопок на основном фрейме
        self.mainPart.grid_columnconfigure(0, minsize=90)
        self.mainPart.grid_columnconfigure(1, minsize=90)
        self.mainPart.grid_columnconfigure(2, minsize=90)
        self.mainPart.grid_columnconfigure(3, minsize=90)
        self.mainPart.grid_rowconfigure(0, minsize=40)
        self.mainPart.grid_rowconfigure(1, minsize=90)
        self.mainPart.grid_rowconfigure(2, minsize=90)
        self.mainPart.grid_rowconfigure(3, minsize=90)
        self.mainPart.grid_rowconfigure(4, minsize=90)
        self.mainPart.grid_rowconfigure(5, minsize=50)

        # Вывод поля и фрейма
        self.mainPart.pack()

        # Изменение парметров окна
        self.parent.resizable(width=False, height=False)
        self.parent.attributes('-fullscreen', True)

        # Изменение цвета приложения
        for wid in self.parent.winfo_children():
            wid.configure(bg='#00ace6')
        self.parent["bg"] = '#00ace6'
        self.back["bg"] = "#e0e0e0"

    # Возврат назад
    def returnBack(self):
        self.parent.destroy()

    # Добавление цифры или константы
    def add_digit(self, digit):
        global leftBkt
        value = self.calc.get()
        if (value[0] == '0') and (len(value) == 1):
            value = value[1:]
        if len(value) + 1 > 15:
            if value[14] == ')':
                self.leftBkt += 1
            elif value[14] == '(':
                self.leftBkt -= 1
            value = value[:-1]
        if len(value) >= 1:
            if value[-1].isdigit() and (digit == '\u03C0' or digit == 'e'):
                i = len(value) - 1
                while i > 0 and (value[i].isdigit() or value[i] == '.'):
                    i -= 1
                if i == 0 and (value[0].isdigit() or value[0] != '('):
                    i -= 1
                value = value[:i + 1]
            elif (value[-1] == '\u03C0') or (value[-1] == 'e'):
                value = value[:-1]
        if len(value) >= 2:
            if ((value[-1] == '0') and (value[-2] in '-+*/^')) or (
                    (value[-1] == '0') and (value[-2] == '(')):
                value = value[:-1]
            if value[-1] == ')':
                num = 0
                i = len(value) - 2
                while value[i] != '(' or num > 0:
                    if value[i] == ')':
                        num += 1
                    if value[i] == '(':
                        num -= 1
                    i -= 1
                value = value[:i]
        self.calc['state'] = NORMAL
        self.calc.delete(0, 'end')
        self.calc.insert(0, value + str(digit))
        self.calc['state'] = DISABLED
        self.brackets['text'] = self.leftBkt

    # Добавление арифметической операции
    def add_operation(self, operation):
        global point_poss, leftBkt
        self.point_poss = True
        value = self.calc.get()
        if value[-1] == '.':
            value = value[:-1]
        if len(value) + 1 > 15:
            if value[14] == ')':
                self.leftBkt += 1
            elif value[14] == '(':
                self.leftBkt -= 1
            value = value[:-1]
        if value[-1] in '-+*/^':
            value = value[:-1]
        elif (('+' in value) or ('-' in value) or ('*' in value) or (
                '/' in value) or ('^' in value)) and self.leftBkt == 0:
            self.calculate()
            value = self.calc.get()
        if (len(value) == 1) and (value[0] == '0') and (operation in '-()'):
            value = ''
        self.calc['state'] = NORMAL
        self.calc.delete(0, 'end')
        self.calc.insert(0, value + operation)
        self.calc['state'] = DISABLED

    # Добавление дробной точки
    def add_point(self):
        global point_poss
        value = self.calc.get()
        point = '.'
        if self.point_poss:
            if value[-1] in '-+*/^(':
                point = '0.'
            self.calc['state'] = NORMAL
            self.calc.delete(0, 'end')
            self.calc.insert(0, value + point)
            self.calc['state'] = DISABLED
            self.point_poss = False

    # Выполнение вычислений результата и его вывод
    def calculate(self):
        global point_poss, leftBkt
        self.point_poss = True
        value = self.calc.get()
        if value[-1] in '+-*/^':
            value = value + value[:-1]
        if '^' in value:
            if value[0] == '-' and not ('-' in value[1:]) and not (
                    '+' in value[1:]) and not ('*' in value[1:]) and not (
                    '/' in value[1:]):
                value = '(' + value[:value.find('^')] + ')' + value[
                                                              value.find(
                                                                  '^'):]
            value = value.replace('^', '**')
        if "\u221A" in value:
            value = value.replace("\u221A", 'sqrt')
        if '!' in value:
            value = value.replace('!', 'factorial')
        if '\u03C0' in value:
            value = value.replace('\u03C0', 'pi')
        if 'log' in value:
            value = value.replace('log', 'log10')
        if 'ln' in value:
            value = value.replace('ln', 'log')
        if 'cot' in value or 'tan' in value:
            i = 2
            while i <= len(value):
                if (((value[i - 2] == 't') and (value[i - 1] == 'a')) or (
                        (value[i - 1] == 'o') and (value[i] == 't'))) and (
                        value[i - 3] != 'a'):
                    j = i + 2
                    num = 0
                    while ((value[j] != ')') or (num > 0)) and (
                            j <= len(value)):
                        if value[j] == '(':
                            num += 1
                        if value[j] == ')':
                            num -= 1
                        j += 1
                    sin_value = str(eval('sin(' + value[i + 2:j] + ')'))
                    cos_value = str(eval('cos(' + value[i + 2:j] + ')'))
                    if len(str(sin_value)) >= 15:
                        sin_value = str('{:.7f}'.format(float(sin_value)))
                    if len(str(cos_value)) >= 15:
                        cos_value = str('{:.7f}'.format(float(cos_value)))
                    if (value[i - 2] == 't') and (value[i - 1] == 'a'):
                        value = value[:i - 2] + '(' + sin_value + '/' +\
                                    cos_value + ')' + value[j + 1:]
                    elif (value[i - 1] == 'o') and (value[i] == 't'):
                        value = value[:i - 2] + '(' + cos_value + '/' +\
                                sin_value + ')' + value[j + 1:]
                i += 1
        if 'acot' in value:
            while 'acot' in value:
                i = value.find('acot')
                j = i + 5
                num = 0
                while ((value[j] != ')') or (num > 0)) and (j <= len(value)):
                    if value[j] == '(':
                        num += 1
                    if value[j] == ')':
                        num -= 1
                    j += 1
                value = value[:i] + '(pi/2-atan' + value[
                                                   i + 4:j + 1] + ')' + value[
                                                                        j + 1:]
        self.calc['state'] = NORMAL
        self.calc.delete(0, 'end')
        try:
            if len(str(eval(value))) >= 15:
                answer = str('{:.7f}'.format(eval(value)))
            else:
                answer = str(eval(value))
            if len(answer) > 2:
                if (answer[-1] == '0') and (answer[-2] == '.'):
                    self.calc.insert(0, int(float(answer)))
                elif '.' in answer:
                    self.calc.insert(0, float(answer))
                else:
                    self.calc.insert(0, int(answer))
            else:
                self.calc.insert(0, int(float(answer)))
        except (NameError, SyntaxError, ValueError):
            messagebox.showerror('Ошибка', 'Неверный ввод')
            self.calc.insert(0, '0')
            self.parent.attributes('-topmost', True)
            self.parent.update()
            self.parent.attributes('-topmost', False)
            self.parent.update()
        except ZeroDivisionError:
            messagebox.showerror('Ошибка', 'На ноль делить нельзя')
            self.calc.insert(0, '0')
            self.parent.attributes('-topmost', True)
            self.parent.update()
            self.parent.attributes('-topmost', False)
            self.parent.update()
        self.calc['state'] = DISABLED
        self.leftBkt = 0
        self.brackets['text'] = self.leftBkt

    # Добавление скобок
    def add_bracket(self, bkt):
        global leftBkt
        value = self.calc.get()
        if len(value) + 1 > 15:
            if value[14] == ')':
                self.leftBkt += 1
            elif value[14] == '(':
                self.leftBkt -= 1
            value = value[:-1]
        if bkt == '(':
            self.leftBkt += 1
            if value[-1] in '+-*/^(':
                value = value + bkt
            elif value[-1].isdigit() or value[-1] == '.':
                c = len(value) - 1
                while c >= 0 and value[c] not in '+-*/^':
                    c -= 1
                value = value[:c + 1] + bkt + value[c + 1:]
            elif value[-1] == ')':
                num = 0
                i = len(value) - 2
                while value[i] != '(' or num > 0:
                    if value[i] == ')':
                        num += 1
                    if value[i] == '(':
                        num -= 1
                    i -= 1
                value = value[:i] + bkt
        else:
            if self.leftBkt > 0:
                value = value + bkt
                self.leftBkt -= 1
        self.calc['state'] = NORMAL
        self.calc.delete(0, 'end')
        self.calc.insert(0, value)
        self.calc['state'] = DISABLED
        self.brackets['text'] = self.leftBkt

    # Добавление сложной арифметической/тригонометрической операции
    def add_complex_operation(self, operation):
        global leftBkt
        value = self.calc.get()
        if value[-1] == '.':
            value = value[:-1]
        if value[-1] in '+-*/^':
            value = value[:-1]
        if value[-1] == ')':
            num = 0
            i = len(value) - 2
            while value[i] != '(' or num > 0:
                if value[i] == ')':
                    num += 1
                if value[i] == '(':
                    num -= 1
                i -= 1
            n = i
            while value[i - 1] in '\u221A!nstg':
                i -= 1
                while value[i] in '\u221A!sincoartlg' and i > 0:
                    i -= 1
            if n == i:
                value = value[:i] + operation + value[i:]
            else:
                value = value[:i] + operation + '(' + value[i:] + ')'
            self.calc['state'] = NORMAL
            self.calc.delete(0, 'end')
            self.calc.insert(0, value)
            self.calc['state'] = DISABLED
        else:
            if (value[0] == '-') and ('+' not in value) and (
                    '*' not in value) and ('/' not in value) and (
                    '^' not in value):
                value = operation + '(' + value + ')'
            else:
                i = len(value) - 1
                while (value[i].isdigit() or value[i] in '.e\u03C0') and (
                        i >= 0):
                    i -= 1
                value = value[:i + 1] + operation + '(' + value[i + 1:] + ')'
            self.calc['state'] = NORMAL
            self.calc.delete(0, 'end')
            self.calc.insert(0, value)
            self.calc['state'] = DISABLED
            if self.leftBkt == 0:
                self.calculate()

    # Открытие раздела с тригонометрическими функциями
    def active_try(self):
        self.Button_trygonom['bg'] = 'grey'

        # Создаём кнопки тригонометрических функций
        self.Button_sin = Button(self.mainPart, text="sin", bd=5,
                                 font=('Comic Sans', 15), fg='red',
                                 command=lambda:
                                     self.add_complex_operation('sin'))
        self.Button_sin.grid(row=1, column=6, stick='wens', padx=5, pady=5)

        self.Button_cos = Button(self.mainPart, text="cos", bd=5,
                                 font=('Comic Sans', 15), fg='red',
                                 command=lambda:
                                     self.add_complex_operation('cos'))
        self.Button_cos.grid(row=2, column=6, stick='wens', padx=5, pady=5)

        self.Button_tan = Button(self.mainPart, text="tan", bd=5,
                                 font=('Comic Sans', 15), fg='red',
                                 command=lambda:
                                     self.add_complex_operation('tan'))
        self.Button_tan.grid(row=3, column=6, stick='wens', padx=5, pady=5)

        self.Button_cot = Button(self.mainPart, text="cot", bd=5,
                                 font=('Comic Sans', 15), fg='red',
                                 command=lambda:
                                     self.add_complex_operation('cot'))
        self.Button_cot.grid(row=4, column=6, stick='wens', padx=5, pady=5)

        # Создаём кнопку смены тригонометрических функций
        self.Button_change = Button(self.mainPart, text="-1", bd=5,
                                    font=('Comic Sans', 9), fg='red',
                                    command=self.change_trygon)
        self.Button_change.grid(row=0, column=6, stick='wens', padx=5, pady=5)

    # Смена тригонометрических функций
    def change_trygon(self):

        # Создаём кнопки других тригонометрических функций
        self.Button_asin = Button(self.mainPart, text="asin", bd=5,
                                  font=('Comic Sans', 13), fg='red',
                                  command=lambda:
                                      self.add_complex_operation('asin'))
        self.Button_asin.grid(row=1, column=6, stick='wens', padx=5, pady=5)

        self.Button_asin = Button(self.mainPart, text="acos", bd=5,
                                  font=('Comic Sans', 13), fg='red',
                                  command=lambda:
                                      self.add_complex_operation('acos'))
        self.Button_asin.grid(row=2, column=6, stick='wens', padx=5, pady=5)

        self.Button_atan = Button(self.mainPart, text="atan", bd=5,
                                  font=('Comic Sans', 13), fg='red',
                                  command=lambda:
                                      self.add_complex_operation('atan'))
        self.Button_atan.grid(row=3, column=6, stick='wens', padx=5, pady=5)

        self.Button_acot = Button(self.mainPart, text="acot", bd=5,
                                  font=('Comic Sans', 13), fg='red',
                                  command=lambda:
                                      self.add_complex_operation('acot'))
        self.Button_acot.grid(row=4, column=6, stick='wens', padx=5, pady=5)

        # Создаём кнопку обратной смены тригонометрических функций
        self.Button_change2 = Button(self.mainPart, text="1", bd=5,
                                     font=('Comic Sans', 9), fg='red',
                                     command=self.active_try)
        self.Button_change2.grid(row=0, column=6, stick='wens', padx=5,
                                 pady=5)

    # Функция backspace (удаление последнего символа/функции)
    def backspace(self):
        global leftBkt, point_poss
        value = self.calc.get()
        if value[-1] in 'nstg':
            i = len(value) - 1
            while (value[i - 1] in 'sincoartlg') and (i > 0):
                value = value[:-1]
                i -= 1
        if value[-1] == '.':
            self.point_poss = True
        if value[-1] == '(':
            if self.leftBkt > 0:
                self.leftBkt -= 1
        if value[-1] == ')':
            self.leftBkt += 1
        self.brackets['text'] = self.leftBkt
        if len(value) > 1:
            value = value[:-1]
        else:
            value = '0'
        self.calc['state'] = NORMAL
        self.calc.delete(0, 'end')
        self.calc.insert(0, value)
        self.calc['state'] = DISABLED

    # Очистка поля ввода и удаление выражения
    def clear(self):
        global point_poss, leftBkt
        self.point_poss = True
        self.calc['state'] = NORMAL
        self.calc.delete(0, 'end')
        self.calc.insert(0, '0')
        self.calc['state'] = DISABLED
        self.leftBkt = 0
        self.brackets['text'] = self.leftBkt

    # Ввод с клавиатуры
    def press_key(self, event):
        print(event.char)
        if (event.char.isdigit()) or (event.char == 'e'):
            self.add_digit(event.char)
        elif (event.char in '+-*/^') and (event.char != ''):
            self.add_operation(event.char)
        elif event.char == '.':
            self.add_point()
        elif event.char == '(':
            self.add_bracket('(')
        elif event.char == ')':
            self.add_bracket(')')
        elif event.char == 'c':
            self.clear()
        elif event.char == '\r':
            self.calculate()
        elif event.char == '\x08':
            self.backspace()
