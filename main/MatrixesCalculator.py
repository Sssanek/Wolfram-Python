from tkinter import *
from main.styledWidgets import EntryWithPlaceholder, HoverButton
from main.OneMatrix import OneMatrix
from main.TwoMatrix import TwoMatrix


class MatrixesCalculator(Frame):
    def __init__(self, parent):
        # Объявление переменных
        self.parent = parent
        self.font30 = ("Courier", 30)
        self.font20 = ("Courier", 20)

        # Основной фрейм
        self.mainPart = Frame(self.parent)
        # Кнопка возврата назад
        self.back = HoverButton(
            self.parent,
            font=("Courier", 18),
            text='Назад',
            activebackground='#00ff00',
            command=self.returnBack
        )
        self.back.pack(anchor=NW, padx=20, pady=20)

        # Кнопка для выбора окна для 1 матрицы
        self.one = HoverButton(
            self.mainPart,
            font=("Courier", 26),
            text='Операции с векторами',
            activebackground='#00ff00',
            command=self.createOneMatrix
        )
        self.one.pack(expand=1, padx=20, pady=20)

        # Кнопка для выбора окна для 2 матриц
        self.two = HoverButton(
            self.mainPart,
            font=("Courier", 26),
            text='Операции над матрицей',
            activebackground='#00ff00',
            command=self.createTwoMatrix
        )
        self.two.pack(expand=1, padx=20, pady=20)

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


    def createOneMatrix(self):
        self.newApp = Toplevel(self.parent)
        self.app = OneMatrix(self.newApp)


    def createTwoMatrix(self):
        self.newApp = Toplevel(self.parent)
        self.app = TwoMatrix(self.newApp)

