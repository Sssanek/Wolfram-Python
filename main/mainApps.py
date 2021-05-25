from main.styledWidgets import HoverButton
from main.CalculatorSystemDigit import CalculatorSystemDigit
from main.TruthDiagram import TruthDiagram
from main.MatrixesCalculator import MatrixesCalculator
from main.Equations import Equations
from main.RandomGenerator import RandomGenerator
from main.Convers import Convers
from main.Calc import Calc
from main.settings import Settings
from tkinter import *


# Окно с приложениями
class App(Frame):
    def __init__(self, parent, db, user):
        # Объявление переменных
        self.parent = parent
        self.db = db
        self.width = 28
        self.height = 3
        self.user = user
        self.bg_color = self.db.bg_color(self.user)
        self.windowSize = self.db.windowSize(self.user)
        self.font = ("Courier", 30)
        self.activeColor = self.db.activeColor(self.user)

        # Создание структуры окна
        # Надпись
        self.label = Label(
            self.parent,
            text='Приложения',
            font=self.font
        )
        # Все кнопки
        self.Buttons = Frame()
        self.Equation = HoverButton(
            self.Buttons,
            text="Решение уравнений",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText='Решение нелинейных уравнений\n-методом деления '
                            'пополам\n-методом Ньютона',
            activebackground=self.activeColor,
            command=self.createEquations
        )
        self.MatrixCalculator = HoverButton(
            self.Buttons,
            text="Матричный калькулятор",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText='Различные операции с \nодной или двумя матрицами',
            activebackground=self.activeColor,
            command=self.createMatrixesCalculator
        )
        self.Calculator = HoverButton(
            self.Buttons,
            text="Арифметический калькулятор",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText='Приложение для арифметических вычислений',
            activebackground=self.activeColor,
            command=self.createCalc
        )
        self.RandomDigits = HoverButton(
            self.Buttons,
            text="Генератор случайных чисел",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText='Генератор рандомных чисел \nдля разных' +
                            'распределений',
            activebackground=self.activeColor,
            command=self.createRandom
        )
        self.CalculatorSystemDigit = HoverButton(
            self.Buttons,
            text="Калькулятор перевода СС",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText='Калькулятор для перевода чисел\
\n из любых систем счисления в любые другие',
            activebackground=self.activeColor,
            command=self.createCalculatorSystemDigit
        )
        self.CalculatorSystemUnits = HoverButton(
            self.Buttons,
            text="Калькулятор перевода единиц",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText='Калькулятор для перевода величин\
\n из одних систем единиц в другие',
            activebackground=self.activeColor,
            command=self.createConvers
        )
        self.TruthDiagram = HoverButton(
            self.Buttons,
            text="Построение таблиц истинности",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText='Приложение для построения таблиц\
\n истинности выражений',
            activebackground=self.activeColor,
            command=self.createTruthDiagram
        )
        self.configs = HoverButton(
            self.Buttons,
            text="Настройки приложения",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText="Настройки приложения",
            activebackground=self.activeColor,
            command=self.settings
        )
        # Раположение кнопок в сетку
        self.Equation.grid(row=0, column=0, padx=(50, 30), pady=10)
        self.MatrixCalculator.grid(row=0, column=1, padx=(30, 50), pady=10)
        self.Calculator.grid(row=1, column=0, padx=(50, 30), pady=10)
        self.RandomDigits.grid(row=1, column=1, padx=(30, 50), pady=10)
        self.CalculatorSystemDigit.grid(
            row=2,
            column=0,
            padx=(50, 30),
            pady=10
        )
        self.CalculatorSystemUnits.grid(
            row=2,
            column=1,
            padx=(30, 50),
            pady=10
        )
        self.TruthDiagram.grid(row=3, column=0, padx=(50, 30), pady=10)
        self.configs.grid(row=3, column=1, padx=(30, 50), pady=10)
        # Вывод на экран
        self.label.pack()
        self.Buttons.pack()
        # Изменение цвета
        self.parent['bg'] = self.bg_color
        for wid in self.parent.winfo_children():
            wid.configure(bg=self.bg_color)
        # Кнопка выхода
        self.exit = HoverButton(
            self.parent,
            font=("Courier", 20),
            text='Выход',
            activebackground=self.activeColor,
            command=self.close
        )
        self.exit.pack(anchor=NE, padx=20, pady=20)

        if self.windowSize:
            self.parent.attributes('-fullscreen', True)
        else:
            self.parent.wm_state('zoomed')

    # Кнопка выхода
    def close(self):
        self.parent.destroy()

    # Создание приложения для перевода систем счисления
    def createCalculatorSystemDigit(self):
        self.newApp = Toplevel(self.parent)
        self.app = CalculatorSystemDigit(self.newApp, self.db, self.user)

    # Создание приложения с таблицой истинности
    def createTruthDiagram(self):
        self.newApp = Toplevel(self.parent)
        self.app = TruthDiagram(self.newApp, self.db, self.user)

    # Матричный калькулятор
    def createMatrixesCalculator(self):
        self.newApp = Toplevel(self.parent)
        self.app = MatrixesCalculator(self.newApp, self.db, self.user)

    # Приложение для решениея уравнений
    def createEquations(self):
        self.newApp = Toplevel(self.parent)
        self.app = Equations(self.newApp, self.db, self.user)

    # Создание приложения для перевода единиц счисления
    def createConvers(self):
        self.newApp = Toplevel(self.parent)
        self.app = Convers(self.newApp, self.db, self.user)

    # Арифметический калькулятор
    def createCalc(self):
        self.newApp = Toplevel(self.parent)
        self.app = Calc(self.newApp, self.db, self.user)

    # Создание случайных чисел
    def createRandom(self):
        self.newApp = Toplevel(self.parent)
        self.app = RandomGenerator(self.newApp, self.db, self.user)

    # Приложение с настройками
    def settings(self):
        self.newApp = Toplevel(self.parent)
        self.app = Settings(self.newApp, self.db, self.user)
