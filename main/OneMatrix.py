from tkinter import *
from main.styledWidgets import HoverButton
from main.OneMatrixOperations import scalar_coord_operation
from main.OneMatrixOperations import scalar_angle_operation
from main.OneMatrixOperations import vector_cord_operation


class OneMatrix(Frame):
    def __init__(self, parent):
        # Объявление переменных
        self.parent = parent
        self.font30 = ("Courier", 30)
        self.font20 = ("Courier", 20)
        self.dimensions = 'three'

        # Основной фрейм
        self.mainPart = Frame(self.parent)

        # Кнопка возврата назад
        self.back = HoverButton(
            self.parent,
            font=("Courier", 18),
            text='Назад',
            activebackground='#00ff00',
            command=self.return_back
        )
        self.back.pack(anchor=NW, padx=20, pady=20)
        # информация из чего пользователь будет выбирать
        self.basis = Label(
            self.mainPart,
            text="Базис состоит из ",
            font=self.font20,
            bg='#00ace6'
        )
        self.vectors = Label(
            self.mainPart,
            text=" векторов",
            font=self.font20,
            bg='#00ace6'
        )
        self.cordinates = Label(
            self.mainPart,
            text="Координаты (i, j, k)",
            font=self.font20,
            bg='#00ace6'
        )
        self.angle = Label(
            self.mainPart,
            text="Угол в градусах",
            font=self.font20,
            bg='#00ace6'
        )
        self.absolute = Label(
            self.mainPart,
            text="Модуль",
            font=self.font20,
            bg='#00ace6'
        )
        # информация по 1 вектору
        self.first_vector = Label(
            self.mainPart,
            text="1-ый вектор: ",
            font=self.font20,
            bg='#00ace6'
        )
        self.first_cord1 = Entry(self.mainPart, font=self.font20)
        self.first_cord2 = Entry(self.mainPart, font=self.font20)
        self.first_cord3 = Entry(self.mainPart, font=self.font20)
        self.first_angle = Entry(self.mainPart, font=self.font20)
        self.first_absolute = Entry(self.mainPart, font=self.font20)
        # информация по 2 вектору
        self.second_vector = Label(
            self.mainPart,
            text="2-ой вектор: ",
            font=self.font20,
            bg='#00ace6'
        )
        self.second_cord1 = Entry(self.mainPart, font=self.font20)
        self.second_cord2 = Entry(self.mainPart, font=self.font20)
        self.second_cord3 = Entry(self.mainPart, font=self.font20)
        self.second_absolute = Entry(self.mainPart, font=self.font20)
        # расставляю 3 кнопки для подсчета нужной величины нужным способом
        self.scalar_coord = HoverButton(
            self.mainPart,
            font=("Courier", 24),
            text='Рассчитать скалярное произведение\nчерез координаты',
            activebackground='#cf34eb',
            command=lambda: self.scalar_coord_op()
        )
        self.scalar_angle = HoverButton(
            self.mainPart,
            font=("Courier", 24),
            text='Рассчитать скалярное произведение ' +
                 'через\nмодули векторов и угол между ними',
            activebackground='#cf34eb',
            command=lambda: self.scalar_angle_op()
        )
        self.vector_coord = HoverButton(
            self.mainPart,
            font=("Courier", 24),
            text='Рассчитать векторное произведение ' +
                 'через\nкоординаты векторов',
            activebackground='#cf34eb',
            command=lambda: self.vector_coord_op()
        )
        # вывод результата
        self.result = Label(
            self.mainPart,
            font=self.font30,
            text="Результат: ",
            bg='#00ace6'
        )
        self.final_result = Label(
            self.mainPart,
            font=self.font30,
            text="Здесь будет результат",
            bg="#34ebb4"
        )
        # реализую взаимоисключающий выбор размерности вектора
        self.dim = BooleanVar()
        self.dim.set(0)
        self.two = Radiobutton(
            self.mainPart,
            text='2',
            variable=self.dim,
            value=1,
            font=self.font20,
            bg='#00ace6',
            command=lambda: self.disable(self.first_cord3, self.second_cord3))
        self.three = Radiobutton(
            self.mainPart,
            text='3',
            variable=self.dim,
            value=0,
            font=self.font20,
            bg='#00ace6',
            command=lambda: self.undisable(
                self.first_cord3,
                self.second_cord3
            )
        )
        # ставлю основной фрейм, чтобы далее работать на нем
        self.mainPart.pack()
        # размещаю сетку элементов на фрейме
        self.basis.grid(row=0, column=1)
        self.two.grid(row=0, column=2)
        self.three.grid(row=0, column=3)
        self.vectors.grid(row=0, column=4)
        self.first_vector.grid(row=1, column=0)
        self.first_cord1.grid(row=1, column=1, ipadx=20)
        self.first_cord2.grid(row=1, column=2, ipadx=20)
        self.first_cord3.grid(row=1, column=3, ipadx=20)
        self.first_angle.grid(row=2, column=4, ipadx=20)
        self.first_absolute.grid(row=1, column=5, ipadx=20)
        self.second_vector.grid(row=2, column=0)
        self.second_cord1.grid(row=2, column=1, ipadx=20)
        self.second_cord2.grid(row=2, column=2, ipadx=20)
        self.second_cord3.grid(row=2, column=3, ipadx=20)
        self.second_absolute.grid(row=2, column=5, ipadx=20)
        self.cordinates.grid(row=3, column=1, columnspan=3)
        self.angle.grid(row=3, column=4)
        self.absolute.grid(row=3, column=5)
        self.scalar_coord.grid(row=4, column=0, columnspan=2, rowspan=2)
        self.scalar_angle.grid(row=4, column=2, columnspan=2, rowspan=2)
        self.vector_coord.grid(row=4, column=4, columnspan=2, rowspan=2)
        self.result.grid(row=6, column=0, columnspan=2, pady=10)
        self.final_result.grid(row=7, column=0, columnspan=2, pady=10)
        # Изменение парметров окна
        self.parent.resizable(width=False, height=False)
        self.parent.attributes('-fullscreen', True)
        # Изменение цвета приложения
        for wid in self.parent.winfo_children():
            wid.configure(bg='#00ace6')
        self.parent["bg"] = '#00ace6'
        self.back["bg"] = "#e0e0e0"

    # Возврат назад
    def return_back(self):
        self.parent.destroy()

    # блокировка поля при выборе двумерного вектора
    def disable(self, m, n):
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        self.dimensions = 'two'

    # разблокировка поля при выборе трехмерного вектора
    def undisable(self, m, n):
        m.config(state=NORMAL)
        n.config(state=NORMAL)
        self.dimensions = 'three'

    def scalar_coord_op(self):
        self.final_result['text'] = scalar_coord_operation(
            self.first_cord1.get(),
            self.first_cord2.get(),
            self.first_cord3.get(),
            self.second_cord1.get(),
            self.second_cord2.get(),
            self.second_cord3.get(),
            self.dimensions
        )

    def scalar_angle_op(self):
        self.final_result['text'] = scalar_angle_operation(
            self.first_absolute.get(),
            self.second_absolute.get(),
            self.first_angle.get()
        )

    def vector_coord_op(self):
        self.final_result['text'] = vector_cord_operation(
            self.first_cord1.get(),
            self.first_cord2.get(),
            self.first_cord3.get(),
            self.second_cord1.get(),
            self.second_cord2.get(),
            self.second_cord3.get(),
            self.dimensions
        )
