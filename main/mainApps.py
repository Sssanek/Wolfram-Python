from main.styledWidgets import HoverButton
from main.CalculatorSystemDigit import CalculatorSystemDigit
from main.TruthDiagram import TruthDiagram
from main.MatrixesCalculator import MatrixesCalculator
from main.Equations import Equations
from main.RandomGenerator import RandomGenerator
from main.Convers import Convers
from main.Calc import Calc
from tkinter import *


# Окно с приложениями
class App(Frame):
    def __init__(self, parent, db):
        # Объявление переменных
        self.parent = parent
        self.db = db
        self.width = 28
        self.height = 3
        self.font = ("Courier", 30)

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
            activebackground='#00ff00',
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
            activebackground='#00ff00',
            command=self.createMatrixesCalculator
        )
        self.Calculator = HoverButton(
            self.Buttons,
            text="Арифметический калькулятор",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText='Арифметический калькулятор',
            activebackground='#00ff00',
            command=self.createCalc
        )
        self.RandomDigits = HoverButton(
            self.Buttons,
            text="Генератор случайных чисел",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText='Генератор рандомных числен\nдля разных' +
                            'распределений',
            activebackground='#00ff00',
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
            activebackground='#00ff00',
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
            activebackground='#00ff00',
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
            activebackground='#00ff00',
            command=self.createTruthDiagram
        )
        self.configs = HoverButton(
            self.Buttons,
            text="Настройки приложения",
            font=self.font,
            width=self.width,
            height=self.height,
            description=True,
            descriptionText="Потом сделаю",
            activebackground='#00ff00'
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
        self.parent['bg'] = '#00ace6'
        for wid in self.parent.winfo_children():
            wid.configure(bg='#00ace6')
        # Кнопка выхода
        self.exit = HoverButton(
            self.parent,
            font=("Courier", 20),
            text='Выход',
            activebackground='#00ff00',
            command=self.close
        )
        self.exit.pack(anchor=NE, padx=20, pady=20)

    # Кнопка выхода
    def close(self):
        self.parent.destroy()

    # Создание приложения для перевода систем счисления
    def createCalculatorSystemDigit(self):
        self.newApp = Toplevel(self.parent)
        self.app = CalculatorSystemDigit(self.newApp, self.db)

    def createTruthDiagram(self):
        self.newApp = Toplevel(self.parent)
        self.app = TruthDiagram(self.newApp, self.db)

    def createMatrixesCalculator(self):
        self.newApp = Toplevel(self.parent)
        self.app = MatrixesCalculator(self.newApp)

    def createEquations(self):
        self.newApp = Toplevel(self.parent)
        self.app = Equations(self.newApp)

    def createConvers(self):
        self.newApp = Toplevel(self.parent)
        self.app = Convers(self.newApp, self.db)
        
    def createCalc(self):
        self.newApp = Toplevel(self.parent)
        self.app = Calc(self.newApp, self.db)

    def createRandom(self):
        self.newApp = Toplevel(self.parent)
        self.app = RandomGenerator(self.newApp)
