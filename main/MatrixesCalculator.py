from tkinter import *
from main.styledWidgets import EntryWithPlaceholder, HoverButton
from main.OneMatrix import OneMatrix
from main.TwoMatrix import TwoMatrix


class MatrixesCalculator(Frame):
    def __init__(self, parent, db, user):
        # Объявление переменных
        self.parent = parent
        self.db = db
        self.user = user
        self.font30 = ("Courier", 30)
        self.font20 = ("Courier", 20)
        self.push_color = self.db.activeColor(self.user)
        self.bg_color = self.db.bg_color(self.user)
        self.windowSize = self.db.windowSize(self.user)
        # Основной фрейм
        self.mainPart = Frame(self.parent)
        # Кнопка возврата назад
        self.back = HoverButton(
            self.parent,
            font=("Courier", 18),
            text='Назад',
            activebackground=self.push_color,
            command=self.returnBack
        )
        self.back.pack(anchor=NW, padx=20, pady=20)

        # Кнопка для выбора окна для 1 матрицы
        self.one = HoverButton(
            self.mainPart,
            font=("Courier", 26),
            text='Операции с векторами',
            activebackground=self.push_color,
            command=self.createOneMatrix
        )
        self.one.pack(expand=1, padx=20, pady=20)

        # Кнопка для выбора окна для 2 матриц
        self.two = HoverButton(
            self.mainPart,
            font=("Courier", 26),
            text='Операции над матрицей',
            activebackground=self.push_color,
            command=self.createTwoMatrix
        )
        self.two.pack(expand=1, padx=20, pady=20)

        self.mainPart.pack()
        # Изменение парметров окна
        self.parent.resizable(width=False, height=False)
        if self.windowSize:
            self.parent.attributes('-fullscreen', True)
        else:
            self.parent.wm_state('zoomed')

        # Изменение цвета приложения
        for wid in self.parent.winfo_children():
            wid.configure(bg=self.bg_color)
        self.parent["bg"] = self.bg_color
        self.back["bg"] = "#e0e0e0"

    # Возврат назад
    def returnBack(self):
        self.parent.destroy()

    # функция, которая создает окно приложения с операциями над векторами
    def createOneMatrix(self):
        self.newApp = Toplevel(self.parent)
        self.app = OneMatrix(self.newApp, self.db, self.user)

    # функция, которая создает окно приложения с операциями над матрицами
    def createTwoMatrix(self):
        self.newApp = Toplevel(self.parent)
        self.app = TwoMatrix(self.newApp, self.db, self.user)
