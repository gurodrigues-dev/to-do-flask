import psycopg2

class User():
    def __init__(self, name, nickname, password, email):
        self.name = name
        self.nickname = nickname
        self.password = password
        self.email = email

class Tasks():
    def __init__(self, titulo, descricao, status, nickname):    
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.nickname = nickname