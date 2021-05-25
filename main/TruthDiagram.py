from tkinter import *
from main.styledWidgets import HoverButton, EntryWithPlaceholder


# Фрейм с приложением для создания таблицы истинности
class TruthDiagram(Frame):
    def __init__(self, parent, db, user):
        # Задание основных переменных
        self.parent = parent
        self.db = db
        self.user = user
        self.bg_color = self.db.bg_color(self.user)
        self.activeColor = self.db.activeColor(self.user)
        self.windowSize = self.db.windowSize(self.user)
        # Поле и скролл для таблицы
        self.text = Text(self.parent, wrap="none")
        self.vsb = Scrollbar(
            self.parent,
            orient="vertical",
            command=self.text.yview
        )
        # Кнопка возврата назад
        self.back = HoverButton(
            self.parent,
            font=("Courier", 18),
            text='Назад',
            activebackground=self.activeColor,
            command=self.returnBack
        )
        self.back.pack(anchor=NW, padx=20, pady=20)
        # Основной фрейм
        self.mainPart = Frame(self.parent)
        # Переменная с логическим выражением
        self.inputInformation = StringVar()
        # Поле для ввода выражения
        self.inputField = EntryWithPlaceholder(
            self.mainPart,
            'Логическое выражение',
            textvariable=self.inputInformation,
            font=('Courier', 40),
            width=30
        )
        # Кнопка для построения таблицы истинности
        self.submit = HoverButton(
            self.mainPart,
            font=('Courier', 30),
            text='Построить',
            activebackground=self.activeColor,
            command=self.buildTable
        )
        # Вывод поля и фрейма
        self.inputField.grid(row=0, column=0, columnspan=3, padx=25)
        self.submit.grid(row=0, column=4)
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

    # Создание таблицы истинности
    def buildTable(self):
        # Попытка выполнить программу
        try:
            # Получение всех переменных из выражения
            variables = set()
            s = ''
            line = self.inputInformation.get()
            for i in line:
                if i == '+' or i == '*' or i == '!':
                    if s:
                        variables.add(s)
                        s = ''
                elif i == '(' or i == ')':
                    if s:
                        variables.add(s)
                        s = ''
                else:
                    s += i
            if s != 'Логическое выражение' and s:
                variables.add(s)
            variables = sorted(list(variables))
            # Текстовое поле со скроллом
            self.createText()
            # Вывод переменных
            for i in variables:
                label = Label(
                    self.parent,
                    text="%s \t" % i,
                    font=("Courier", 20),
                    borderwidth=2,
                    relief="groove"
                )
                self.text.window_create("end", window=label)
            label = Label(
                self.parent,
                text="Res \t",
                font=("Courier", 20),
                borderwidth=2,
                relief="groove"
            )
            self.text.window_create("end", window=label)
            self.text.insert("end", "\n")
            # Заполнение таблицы
            for i in range(2**len(variables)):
                t = 2**(len(variables) - 1)
                val = []
                s = line
                # Заполнение таблицы 1 и 0
                while t > 0:
                    if (i // t) % 2 == 0:
                        label = Label(
                            self.parent,
                            text="0\t",
                            font=("Courier", 20),
                            borderwidth=2,
                            relief="groove"
                        )
                        val.append(0)
                    else:
                        label = Label(
                            self.parent,
                            text="1\t",
                            font=("Courier", 20),
                            borderwidth=2,
                            relief="groove"
                        )
                        val.append(1)
                    self.text.window_create("end", window=label)
                    t //= 2
                # Вычисление значения каждой строки
                s = line
                # Замена цифр на булевы функции
                for i in range(len(variables)):
                    if val[i]:
                        s = s.replace(variables[i], 'True')
                    else:
                        s = s.replace(variables[i], 'False')
                # Вычисление значений в скобках
                while '(' in s:
                    a = s.index('(')
                    b = s.index(')')
                    t = eval(s[a:b + 1])
                    if t:
                        s = s.replace(s[a:b + 1], 'True')
                    else:
                        s = s.replace(s[a:b + 1], 'False')
                # Замена обратных булевых функций
                s = s.replace('!True', 'False')
                s = s.replace('!False', 'True')
                # Выполнение строчки и вывод результата
                if eval(s):
                    label = Label(
                        self.parent,
                        text="1\t",
                        font=("Courier", 20),
                        borderwidth=2,
                        relief="groove"
                    )
                else:
                    label = Label(
                        self.parent,
                        text="0\t",
                        font=("Courier", 20),
                        borderwidth=2,
                        relief="groove"
                    )
                # Вывод строчки
                self.text.window_create("end", window=label)
                # Перенос строки
                self.text.insert("end", "\n")
            self.text.configure(state="disabled")
        # В случае ошибки
        except Exception:
            # Текстовое поле со скроллом
            self.createText()
            label = Label(
                self.parent,
                text='Введите корректное выражение',
                font=("Courier", 20)
            )
            self.text.window_create("end", window=label)

    # Метод для создания поля для таблицы
    def createText(self):
        self.text.destroy()
        self.vsb.destroy()
        self.text = Text(self.parent, wrap="none")
        self.vsb = Scrollbar(
            self.parent,
            orient="vertical",
            command=self.text.yview
        )
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(fill="both", expand=True)
