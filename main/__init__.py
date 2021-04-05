from tkinter import *
from tkinter import messagebox
from main.database import DB
from main.styledWidgets import EntryWithPlaceholder, HoverButton, App


# Окно авторизации
class Authentication(Frame):
    def __init__(self, parent, db):
        Frame.__init__(self)
        self.db = db
        self.parent = parent
        self.loggined = False
        self.user = None
        self.auth = Frame()
        self.label = Label(
            self.auth,
            text='Авторизация',
            font=("Courier", 44)
        )
        self.label['bg'] = '#00ace6'
        self.label.pack()
        self.Login = StringVar()
        self.Password = StringVar()
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
        self.submit = HoverButton(
            self.auth,
            text='Подтвердить',
            font=("Courier", 44),
            command=self.check,
            activebackground='#00ff00'
        )
        self.submit.pack(pady=(0, 15))
        self.reg = HoverButton(
            self.auth,
            text="Зарегистрироваться",
            font=("Courier", 26),
            command=self.register,
            activebackground='#00ff00'
        )
        self.reg.pack()
        for wid in self.parent.winfo_children():
            wid.configure(bg='#00ace6')
        self.auth.pack(pady=150)

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


# Окно регистрации
class Registr(Frame):
    def __init__(self, parent, db):
        self.parent = parent
        self.parent.geometry('1200x800')
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
        for wid in self.parent.winfo_children():
            wid.configure(bg='#00ace6')
        self.reg.pack(pady=150)

    # Добавление в базу данных и проверха возможности добавления
    def addToDb(self, login, password):
        if self.db.checkUserLogin(login):
            messagebox.showerror(
                "Регистрация",
                "Пользователь уже существует"
            )
            self.parent.attributes('-topmost', True)
            self.parent.update()
        else:
            self.db.insertData(login, password)
            messagebox.showinfo(
                "Регистрация",
                "Пользователь успешно зарегистрирован"
            )
            self.parent.destroy()


# Создание приложения
def create_app():
    db = DB()
    root = Tk()
    root.title('Авторизация')
    root.geometry("1200x800")
    root['bg'] = '#00ace6'
    app = Authentication(root, db)
    app.pack()
    root.mainloop()
