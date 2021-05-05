from tkinter import *
from main.styledWidgets import EntryWithPlaceholder, HoverButton
from tkinter import ttk
from main.FullMatrixOperations import determinant_operation


class TwoMatrix(Frame):
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

        self.matrix_part = Frame(self.parent)

        self.razmernost_label = Label(
            self.mainPart,
            font=self.font30,
            text='Размерность матрицы: ',
            bg='#00ace6'
        )

        self.mainPart.option_add("*TCombobox*Listbox*Font", self.font30)
        self.dimension = ttk.Combobox(self.mainPart,
                                      values=['2 на 2', '3 на 3'],
                                      font=self.font30,
                                      state="readonly")
        self.dimension.bind("<<ComboboxSelected>>", self.something)
        self.dimension.current(0)

        self.kinda_result = Label(
            self.mainPart,
            font=self.font20,
            text='Нихуя не произошло'
        )

        self.btn_for_something = Button(
            self.mainPart,
            font=self.font20,
            text='Инфа про матрицу',
            command=self.info
        )

        self.btn_deter = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Рассчитать определитель\nматрицы',
            activebackground='#cf34eb',
            command=self.determinant()
        )

        self.btn_obratn = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Рассчитать обратную\nматрицу',
            activebackground='#cf34eb'
        )

        self.btn_sobstv_chisla = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Рассчитать собственные\nчисла матрицы',
            activebackground='#cf34eb'
        )

        self.btn_sobstv_vectora = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Рассчитать собственные\nвектора матрицы',
            activebackground='#cf34eb'
        )

        self.btn_razl_hol = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Разложение\nХолецкого',
            activebackground='#cf34eb'
        )

        self.btn_razl_spectr = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Спектральное\nразложение',
            activebackground='#cf34eb'
        )

        # сетка виджетов
        self.razmernost_label.grid(row=0, column=0)
        self.dimension.grid(row=0, column=1, columnspan=2)
        self.btn_deter.grid(row=1, column=0, columnspan=2,
                            stick='WE', padx=5, pady=5)
        self.btn_obratn.grid(row=1, column=2, columnspan=2,
                             stick='WE', padx=5, pady=5)
        self.btn_sobstv_chisla.grid(row=1, column=4, columnspan=2,
                                    stick='WE', padx=5, pady=5)
        self.btn_sobstv_vectora.grid(row=2, column=0, columnspan=2,
                                     stick='WE', padx=5, pady=5)
        self.btn_razl_hol.grid(row=2, column=2, columnspan=2,
                               stick='WE', padx=5, pady=5)
        self.btn_razl_spectr.grid(row=2, column=4, columnspan=2,
                                  stick='WE', padx=5, pady=5)
        self.kinda_result.grid(row=3, column=0, columnspan=2)
        self.btn_for_something.grid(row=3, column=2)
        self.back.pack(anchor=NW, padx=20, pady=20)
        self.mainPart.pack()
        self.matrix_part.pack()

        self.my_matrix = []

        for y in range(2):
            for x in range(2):
                self.matrix = Entry(self.matrix_part, font=self.font30)
                self.matrix.grid(row=y, column=x, pady=10, padx=10)
                self.my_matrix.append(self.matrix)

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

    def something(self, event):
        a = 0
        self.matrix_part.destroy()
        self.my_matrix = []
        self.matrix_part = Frame(self.parent)
        self.matrix_part["bg"] = '#00ace6'
        self.matrix_part.pack()
        if self.dimension.get() == '2 на 2':
            a = 2
        if self.dimension.get() == '3 на 3':
            a = 3
        for y in range(a):
            for x in range(a):
                self.matrix = Entry(self.matrix_part, font=self.font30)
                self.matrix.grid(row=y, column=x, pady=10, padx=10)
                self.my_matrix.append(self.matrix)
        self.kinda_result['text'] = 'ЕБАТЬ ЧЕТА РАБОТАЕТ'

    def determinant(self):
        mas = []
        for i in self.my_matrix:
            mas.append(i.get())
        print(mas)
        self.kinda_result['text'] = determinant_operation(
            mas,
            self.dimension.get()
        )
