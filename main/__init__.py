from tkinter import *
from main.database import DB
from main.mainApps import App
from main.Registration import Registr
from main.styledWidgets import EntryWithPlaceholder, HoverButton


# Окно авторизации
class Authentication(Frame):
    def __init__(self, parent, db):
        Frame.__init__(self)
        # Создание основных переменных
        self.db = db
        self.parent = parent
        self.loggined = False
        self.user = None
        # Создание основного фрейма
        self.auth = Frame()
        # Название
        self.label = Label(
            self.auth,
            text='Авторизация',
            font=("Courier", 44)
        )
        self.label.pack()
        # Логин и пароль
        self.Login = StringVar()
        self.Password = StringVar()
        # Поле ввода для логина и пароля
        self.login = EntryWithPlaceholder(
            self.auth,
            'Логин',
            textvariable=self.Login,
            font=("Courier", 44)
        )
        self.login.pack()
        self.password = EntryWithPlaceholder(
            self.auth,
            'Пароль',
            hideChar=True,
            textvariable=self.Password,
            font=("Courier", 44)
        )
        self.password.pack(pady=15)
        # Кнопка подтверждения
        self.submit = HoverButton(
            self.auth,
            text='Подтвердить',
            font=("Courier", 44),
            command=self.check,
            activebackground='#00ff00'
        )
        self.submit.pack(pady=(0, 15))
        # Кнопка для регистрации
        self.reg = HoverButton(
            self.auth,
            text="Зарегистрироваться",
            font=("Courier", 26),
            command=self.register,
            activebackground='#00ff00'
        )
        self.reg.pack()
        # Изменение цвета
        self.label['bg'] = '#00ace6'
        for wid in self.parent.winfo_children():
            wid.configure(bg='#00ace6')
        self.exit = HoverButton(
            self.parent,
            font=("Courier", 20),
            text='Выход',
            activebackground='#00ff00',
            command=self.close
        )
        self.exit.pack(anchor=NW, padx=20, pady=20)
        self.auth.pack(pady=110)

    def close(self):
        self.parent.destroy()

    # Проверка введенного логина и пароля
    def check(self):
        self.loggined, self.User = self.db.checkUser(
            self.Login.get(),
            self.Password.get()
        )
        if self.loggined:
            self.parent.destroy()
            self.parent = Tk()
            self.app = App(self.parent, self.db)
            self.parent.resizable(width=False, height=False)
            self.parent.attributes('-fullscreen', True)
            self.parent.mainloop()
        else:
            messagebox.showerror(
                "Авторизация",
                "Неверный логин или пароль"
            )

    # Создание окна регистрации
    def register(self):
        self.newWindow = Toplevel(self.parent)
        self.app = Registr(self.newWindow, self.db)


# Создание приложения
def create_app():
    # Создание и вызов базы данных
    db = DB()
    # Главное окно
    root = Tk()
    # Изменение параметров окна
    root.title('Авторизация')
    root['bg'] = '#00ace6'
    root.resizable(width=False, height=False)
    root.attributes('-fullscreen', True)
    # root.wm_state('zoomed')
    # Вызов приложения
    app = Authentication(root, db)
    app.pack()
    root.mainloop()
