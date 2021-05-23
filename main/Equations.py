from tkinter import *
from main.styledWidgets import EntryWithPlaceholder, HoverButton
from main.EquationsOperations import bisection_operation, newton_operation


class Equations(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.font30 = ("Courier", 30)
        self.font20 = ("Courier", 20)
        self.push_color = '#cf34eb'
        self.bg_color = '#00ace6'

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
        # ставлю основной фрейм, чтобы далее работать на нем
        self.mainPart.pack()

        self.info = Label(
            self.mainPart,
            text="Введите уравнение вида f(x) = 0",
            font=self.font30,
            bg=self.bg_color
        )

        # Поле для ввода выражения
        self.inputField = EntryWithPlaceholder(
            self.mainPart,
            'Уравнение',
            font=('Courier', 40),
            width=30
        )
        self.first = Entry(
            self.mainPart,
            font=self.font20,
        )
        self.second = Entry(
            self.mainPart,
            font=self.font20,
        )
        self.accuracy = Entry(
            self.mainPart,
            font=self.font20,
        )
        self.start = Entry(
            self.mainPart,
            font=self.font20,
        )
        self.lfirst = Label(
            self.mainPart,
            text='Левая\nграница (a)',
            font=self.font20,
            bg=self.bg_color
        )
        self.lsecond = Label(
            self.mainPart,
            text='Правая\nграница (b)',
            font=self.font20,
            bg=self.bg_color
        )
        self.laccuracy = Label(
            self.mainPart,
            text='Точность ε',
            font=self.font20,
            bg=self.bg_color
        )
        self.lstart = Label(
            self.mainPart,
            text='Начальная\nточка x0',
            font=self.font20,
            bg=self.bg_color
        )
        self.bisection = HoverButton(
            self.mainPart,
            font=("Courier", 24),
            text='Решить методом\nделения пополам',
            activebackground=self.push_color,
            command=self.bisection_op
        )
        self.newton = HoverButton(
            self.mainPart,
            font=("Courier", 24),
            text='Решить методом\nНьютона',
            activebackground=self.push_color,
            command=self.newton_op
        )
        self.result = Label(
            self.mainPart,
            font=self.font30,
            text='Решения уравнения:',
            bg=self.bg_color
        )
        # расположение виджетов на фрейме
        self.info.grid(row=0, column=0, columnspan=3)
        self.inputField.grid(row=1, column=0, columnspan=4)
        self.first.grid(row=2, column=0, pady=10, padx=10)
        self.second.grid(row=2, column=1, pady=10, padx=10)
        self.accuracy.grid(row=2, column=2, pady=10, padx=10)
        self.start.grid(row=2, column=3, pady=10, padx=10)
        self.lfirst.grid(row=3, column=0, pady=10, padx=10)
        self.lsecond.grid(row=3, column=1, pady=10, padx=10)
        self.laccuracy.grid(row=3, column=2, pady=10, padx=10)
        self.lstart.grid(row=3, column=3, pady=10, padx=10)
        self.bisection.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        self.newton.grid(row=4, column=2, columnspan=2, pady=10, padx=10)
        self.result.grid(row=5, column=0, columnspan=3, pady=10, padx=10)
        # Изменение парметров окна
        self.parent.resizable(width=False, height=False)
        self.parent.attributes('-fullscreen', True)
        # Изменение цвета приложения
        for wid in self.parent.winfo_children():
            wid.configure(bg=self.bg_color)
        self.parent["bg"] = self.bg_color
        self.back["bg"] = "#e0e0e0"

    # Возврат назад
    def returnBack(self):
        self.parent.destroy()

    def bisection_op(self):
        self.result['text'] = 'Подсчет результата...'
        self.result['text'] = bisection_operation(
            self.first.get(),
            self.second.get(),
            self.accuracy.get(),
            self.inputField.get()
        )

    def newton_op(self):
        self.result['text'] = 'Подсчет результата...'
        self.result['text'] = newton_operation(
            self.inputField.get(),
            self.start.get(),
            self.accuracy.get()
        )
