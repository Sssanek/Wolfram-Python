from tkinter import *
from main.styledWidgets import HoverButton
from tkinter import colorchooser


class Settings(Frame):
    def __init__(self, parent, db, user):
        # Задание основных переменных
        self.parent = parent
        self.db = db
        self.user = user
        self.bg_color = self.db.bg_color(self.user)
        self.font = ('Courier', 25)
        self.activeColor = self.db.activeColor(self.user)
        self.windowSize = self.db.windowSize(self.user)

        # Основной фрейм
        self.mainPart = Frame(self.parent)

        # Надпись выбора цвета фона
        self.bgColorPickLabel = Label(
            self.mainPart,
            text='Цвет фона',
            font=self.font,
            bg=self.bg_color
        )

        # Выбор цвета фона
        self.bgColorPick = HoverButton(
            self.mainPart,
            font=self.font,
            text='Выбрать цвет',
            activebackground=self.activeColor,
            command=self.chooseColor
        )

        # Надпись вида окна
        self.sizeLabel = Label(
            self.mainPart,
            text='Вид окна',
            font=self.font,
            bg=self.bg_color
        )

        # Фрейм для видов окна
        self.sizeChoose = Frame(self.mainPart)
        # Переменная
        self.size = IntVar()
        if self.windowSize:
            self.size.set(1)
        else:
            self.size.set(0)
        # Варианты
        self.inWindow = Radiobutton(
            self.sizeChoose,
            text="В окне на весь экран",
            font=self.font,
            variable=self.size,
            value=0,
            bg=self.bg_color
        )
        self.fullSize = Radiobutton(
            self.sizeChoose,
            text="Полный экран",
            font=self.font,
            variable=self.size,
            value=1,
            bg=self.bg_color
        )

        # Кнопка для изменения цвета
        self.changeSize = HoverButton(
            self.mainPart,
            font=self.font,
            text='Изменить размер',
            activebackground=self.activeColor,
            command=self.change
        )

        # Надпись цвета при навидении на кнопку
        self.activeColorLabel = Label(
            self.mainPart,
            text='Цвет при наведение\nна кнопку',
            font=self.font,
            bg=self.bg_color
        )

        # Выбор цвета при наведении на кнопку
        self.activeColorPick = HoverButton(
            self.mainPart,
            font=self.font,
            text='Выбрать цвет',
            activebackground=self.activeColor,
            command=self.chooseActiveColor
        )

        # Кнопка возврата назад
        self.back = HoverButton(
            self.parent,
            font=("Courier", 18),
            text='Назад',
            activebackground=self.activeColor,
            command=self.returnBack
        )

        # Вывод кнопки назад
        self.back.pack(anchor=NW, padx=20, pady=20)

        # Выбор видов окна
        self.fullSize.pack()
        self.inWindow.pack()
        # Основная часть
        self.mainPart.pack()

        # Растановка всех элементов
        self.bgColorPickLabel.grid(row=0, column=0, padx=100)
        self.bgColorPick.grid(row=0, column=1)
        self.sizeLabel.grid(row=1, column=0, padx=100)
        self.sizeChoose.grid(row=1, column=1)
        self.changeSize.grid(row=1, column=2)
        self.activeColorLabel.grid(row=2, column=0, padx=100)
        self.activeColorPick.grid(row=2, column=1)

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
        self.sizeChoose['bg'] = self.bg_color
        self.back["bg"] = "#e0e0e0"

    # Возврат назад
    def returnBack(self):
        self.parent.destroy()

    # Выбор цвета
    def chooseColor(self):
        color_code = colorchooser.askcolor(title="Choose color")
        self.parent.attributes('-topmost', True)
        self.parent.update()
        self.parent.attributes('-topmost', False)
        self.parent.update()
        self.db.bg_color_change(self.user, color_code[1])

    # Измнить размер окна
    def change(self):
        self.db.changeSize(self.user, int(self.size.get()))

    # Изменить цвет при навдении на кнопку
    def chooseActiveColor(self):
        color_code = colorchooser.askcolor(title="Choose color")
        self.parent.attributes('-topmost', True)
        self.parent.update()
        self.parent.attributes('-topmost', False)
        self.parent.update()
        self.db.active_color_change(self.user, color_code[1])
