from main.styledWidgets import EntryWithPlaceholder, HoverButton
from tkinter import messagebox
from tkinter import *


# Окно регистрации
class Registr(Frame):
    def __init__(self, parent, db):
        self.parent = parent
        self.parent.title("Регистрация")
        self.db = db
        self.reg = Frame(self.parent)
        self.label = Label(
            self.reg,
            text='Регистрация',
            font=("Courier", 44)
        )
        self.label.pack()
        self.label['bg'] = '#00ace6'
        self.Login = StringVar()
        self.Password = StringVar()
        self.login = EntryWithPlaceholder(
            self.reg,
            'Логин',
            font=("Courier", 44),
            textvariable=self.Login
        )
        self.login.pack()
        self.password = EntryWithPlaceholder(
            self.reg,
            'Пароль',
            font=("Courier", 44),
            hideChar=True,
            textvariable=self.Password,
        )
        self.password.pack(pady=15)
        self.submit = HoverButton(
            self.reg,
            text='Подтвердить',
            font=("Courier", 44),
            command=lambda: self.addToDb(
                self.login.get(),
                self.password.get()
            ),
            activebackground='#00ff00'
        )
        self.submit.pack()
        self.parent['bg'] = '#00ace6'
        self.parent.resizable(width=False, height=False)
        self.parent.attributes('-fullscreen', True)
        for wid in self.parent.winfo_children():
            wid.configure(bg='#00ace6')
        self.reg.pack(pady=150)

    # Добавление в базу данных и проверха возможности добавления
    def addToDb(self, login, password):
        # Проверка что такого пользователя не существует
        if self.db.checkUserLogin(login):
            messagebox.showerror(
                "Регистрация",
                "Пользователь уже существует"
            )
            self.parent.attributes('-topmost', True)
            self.parent.update()
        else:
            # Создание записи
            self.parent.attributes('-topmost', True)
            self.parent.update()
            self.parent.destroy()
            self.db.insertData(login, password)
            messagebox.showinfo(
                "Регистрация",
                "Пользователь успешно зарегистрирован",
            )
