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

    # Проверка существования логина
    def checkUserLogin(self, login):
        if self.c.execute("select * from users where login like " + login):
            return True
        return False

    # Проверка существования пользователя
    def checkUser(self, login, password):
        users = self.c.execute("select * from users where login like " + login)
        for user in users:
            if password == user[2]:
                return (True, user[1])
        return (False, None)
