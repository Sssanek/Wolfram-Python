import sqlite3


# Класс для доступа к базе данных
class DB:
    # Создание и связь с базой данных
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
            (id integer primary key, login text, password text)
            ''')
        self.conn.commit()

    # Создать новый аккаунт
    def insertData(self, login, password):
        self.c.execute('''
            INSERT INTO users(login, password) VALUES (?, ?)
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
