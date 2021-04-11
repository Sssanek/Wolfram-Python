from tkinter import *
from main.database import DB
from main.mainApps import Authentication


# Создание приложения
def create_app():
    # Создание и вызов базы данных
    db = DB()
    # Главное окно
    root = Tk()
    # Изменение параметров окна
    root.title('Авторизация')
    root.geometry("1200x800")
    root['bg'] = '#00ace6'
    root.resizable(width=False, height=False)
    root.attributes('-fullscreen', True)
    # root.wm_state('zoomed')
    # Вызов приложения
    app = Authentication(root, db)
    app.pack()
    root.mainloop()
