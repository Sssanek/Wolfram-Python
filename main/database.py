import sqlite3


# Класс для доступа к базе данных
class DB:
    # Создание и связь с базой данных
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
            (id integer primary key, login text, password text, bg_color text,
            size integer DEFAULT 1, activeColor text DEFAULT '#00ff00')
            ''')
        self.conn.commit()

    # Создать новый аккаунт
    def insertData(self, login, password):
        self.c.execute('''
            INSERT INTO users(login, password, bg_color)
            VALUES (?, ?, '#00ace6')
        ''', (login, password))
        self.conn.commit()

    # Проверка существования логина для регистрации
    def checkUserLogin(self, login):
        users = self.c.execute(
            '''SELECT * FROM users WHERE login=?''', (login,)
        )
        if users.fetchall():
            return True
        return False

    # Проверка логина и пароля
    def checkUser(self, login, password):
        users = self.c.execute(
            '''SELECT * FROM users WHERE login=?''', (login,)
        )
        for user in users.fetchall():
            if password == user[2]:
                return (True, user[1])
        return (False, None)

    # Получить цвет фона
    def bg_color(self, login):
        users = self.c.execute(
            '''SELECT * FROM users WHERE login=?''', (login,)
        )
        for user in users:
            return user[3]

    # Изменить цвет фона окна
    def bg_color_change(self, login, color):
        self.c.execute('''
            UPDATE users
            SET bg_color = ?
            WHERE login = login;''', (color,))
        self.conn.commit()

    # Получить размер окна
    def windowSize(self, login):
        users = self.c.execute(
            '''SELECT * FROM users WHERE login=?''', (login,)
        )
        for user in users:
            if user[4] == 0:
                return 0
            return 1

    # Изменить размер окна
    def changeSize(self, login, size):
        self.c.execute('''
            UPDATE users
            SET size = ?
            WHERE login = login;''', (size,))
        self.conn.commit()

    # Изменить цвет при наведнии на кнопку
    def active_color_change(self, login, color):
        self.c.execute('''
            UPDATE users
            SET activeColor = ?
            WHERE login = login;''', (color,))
        self.conn.commit()

    # Получить цвет при наведении на кнопку
    def activeColor(self, login):
        users = self.c.execute(
            '''SELECT * FROM users WHERE login=?''', (login,)
        )
        for user in users:
            return user[5]
