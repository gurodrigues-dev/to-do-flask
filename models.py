import psycopg2

class User():
    def __init__(self, name, nickname, password, email):
        self.name = name
        self.nickname = nickname
        self.password = password
        self.email = email
