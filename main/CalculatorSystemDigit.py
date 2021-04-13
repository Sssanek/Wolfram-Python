from tkinter import *
from main.styledWidgets import EntryWithPlaceholder, HoverButton


# Приложение для перевода чисел между система счисления
class CalculatorSystemDigit(Frame):
    def __init__(self, parent, db):
        # Объявление переменных
        self.parent = parent
        self.db = db
        self.font30 = ("Courier", 30)
        self.font20 = ("Courier", 20)

        # Основной фрейм
        self.mainPart = Frame(self.parent)
        # Переменные для ввода данных
        self.inputSystem = StringVar()
        self.inputValue = StringVar()
        self.outputSystem = StringVar()

        # Кнопка возврата назад
        self.back = HoverButton(
            self.parent,
            font=("Courier", 18),
            text='Назад',
            activebackground='#00ff00',
            command=self.returnBack
        )
        self.back.pack(anchor=NW, padx=20, pady=20)

        # Поле информации
        self.inputInformation = Label(
            self.mainPart,
            text="Число для перевода и его \n система счисления",
            font=self.font30
        )
        self.inputInformation["bg"] = '#00ace6'

        # Поле ответа
        self.outputInformation = Label(
            self.mainPart,
            text="Результат перевода",
            font=self.font30
        )
        self.outputInformation["bg"] = '#00ace6'

        # Место для ответа
        self.result = Label(
            self.mainPart,
            text='Здесь будет результат',
            font=self.font30
        )
        self.result["bg"] = '#00ace6'

        # Ввод исходной системы счисления
        self.inputNumeralSystem = EntryWithPlaceholder(
            self.mainPart,
            'Система счисления исходного числа (2-36)',
            textvariable=self.inputSystem,
            font=self.font20,
            width=40
        )

        # Ввод исходного числа
        self.inputNumber = EntryWithPlaceholder(
            self.mainPart,
            'Исходное число',
            textvariable=self.inputValue,
            font=self.font20,
            width=40
        )

        # Ввод выходной системы счисления
        self.outputNumeralSystem = EntryWithPlaceholder(
            self.mainPart,
            'Система счисления выходного числа (2-36)',
            textvariable=self.outputSystem,
            font=self.font20,
            width=40
        )

        # Кнопка для перевода
        self.submit = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Перевести',
            activebackground='#00ff00',
            command=self.translate
        )

        # Растановка виджетов на экране
        self.inputInformation.grid(
            row=0,
            column=0,
            padx=(0, 120),
            pady=(100, 0)
        )
        self.outputInformation.grid(row=0, column=1, pady=(100, 0))
        self.inputNumeralSystem.grid(
            row=1,
            column=0,
            ipady=20,
            padx=(0, 120),
            pady=(20, 30)
        )
        self.outputNumeralSystem.grid(
            row=3,
            column=0,
            ipady=20,
            padx=(0, 120),
            pady=30
        )
        self.submit.grid(row=4, column=0, padx=(0, 100))
        self.inputNumber.grid(row=2, column=0, ipady=20, padx=(0, 120))
        self.result.grid(row=1, column=1, rowspan=3)
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

    # Перевод в другую систему счисления
    def translate(self):
        # Проверка валидности входной системы счисления
        if self.checkSystem(self.inputSystem.get(), self.result, 'исходной'):
            from_base = int(self.inputSystem.get())
        else:
            return
        num = self.inputValue.get()
        # Проверка валдиности исходного числа
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if any([True for i in num if i not in alphabet]):
            self.result['text'] = 'Введите корректное число'
        elif any([True for i in num if alphabet.index(i) >= from_base]):
            self.result['text'] = 'Введите корректное число'
        # Проверка валидности выходной системы счисления
        if self.checkSystem(self.outputSystem.get(), self.result, 'выходной'):
            to_base = int(self.outputSystem.get())
        else:
            return
        # Перевод к десятичному числу
        n = int(num, from_base) if isinstance(num, str) else num
        # Перевод в новую систему счисления
        res = ""
        while n > 0:
            n, m = divmod(n, to_base)
            res += alphabet[m]
        # Запись результата
        s = ''
        res = res[::-1]
        for i in range(len(res)):
            if i % 30 == 0:
                s += '\n'
            s += res[i]
        self.result['text'] = s

    # Метод для проверки валидности числа
    def checkSystem(self, systemToCheck, label, errorText):
        s = 'Введите число\nот 2 до 36 в {}\nсистеме счисления'.format(
            errorText
        )
        # Если не число, то запись ошибку и вернуть ошибку
        if not systemToCheck.isdigit():
            label['text'] = s
            return False
        # Проверка что число от 2 до 36
        if int(systemToCheck) > 36 or int(systemToCheck) < 2:
            label['text'] = s
            return False
        # Если переводится в число и оно от 2 до 36
        return True
