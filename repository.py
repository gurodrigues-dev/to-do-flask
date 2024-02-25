import models
import utils
import psycopg2

def save_user(User: models.User):
    try:
        conn = utils.connect_database()
        cursor = conn.cursor()

        query = """SELECT * FROM users WHERE nickname = %s"""
        cursor.execute(query, (User.nickname, ))
        result = cursor.fetchone()

        if result is not None:
            return False, f"Nickname '{User.nickname}' já está em uso"

        query = """INSERT INTO users (name, nickname, password, email) VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (User.name, User.nickname, User.password, User.email))
        conn.commit()
        conn.close()

        return True, None

    except psycopg2.errors.UniqueViolation as err:
        return False, f"Nickname '{User.nickname}' já está em uso"

    except Exception as err:
        return False, err


def remove_user(nickname):

    try:
        conn = utils.connect_database()
        cursor = conn.cursor()
        query = """DELETE FROM users WHERE nickname = %s"""
        cursor.execute(query, (nickname, ))
        conn.commit()
        conn.close()

        return True, None
    
    except Exception as err:
        return False, err

def get_user(nickname):

    try:
        conn = utils.connect_database()
        cursor = conn.cursor()
        query = """SELECT * FROM users WHERE nickname = %s"""
        cursor.execute(query, (nickname, ))
        user = cursor.fetchone()
        
        conn.close()

        if user:
            return True, user
        else:
            return False, "Usuário não encontrado"
    
    except Exception as err:
        return False, err
    
def update_user(nickname, data):
    try:
        conn = utils.connect_database()
        cursor = conn.cursor()

        if 'nickname' in data and data['nickname'] != nickname:
            query = """SELECT * FROM users WHERE nickname = %s"""
            cursor.execute(query, (data['nickname'],))
            result = cursor.fetchone()

            if result is not None:
                return False, f"Nickname '{data['nickname']}' já está em uso"

        
        update_fields = ", ".join([f"{key} = %s" for key in data.keys()])
        query = f"""UPDATE users SET {update_fields} WHERE nickname = %s"""

        
        values = list(data.values())
        values.append(nickname)

        
        cursor.execute(query, tuple(values))
        conn.commit()
        conn.close()

        return True, None
    
    except Exception as err:
        return False, err

def verify_user(User: models.User):

    try:
        conn = utils.connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE nickname = %s AND password = %s", (User.nickname, User.password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user == None:
            return False, "usuario nao encontrado no banco de dados"
        
        return True, None

    except Exception as err:
        return False, err


def save_task(Task: models.Tasks):
    try:
        conn = utils.connect_database()
        cursor = conn.cursor()

        query = """INSERT INTO tasks (titulo, descricao, status, nickname) VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (Task.titulo, Task.descricao, Task.status, Task.nickname))
        conn.commit()
        conn.close()

        return True, None

    except Exception as err:
        return False, err

def remove_task(titulo, nickname):

    try:

        exist, err = get_task(titulo, nickname)
        if not exist:
            return False, "Task não encontrada"

        conn = utils.connect_database()
        cursor = conn.cursor()
        query = """DELETE FROM tasks WHERE titulo = %s AND nickname = %s"""
        cursor.execute(query, (titulo, nickname))
        conn.commit()
        conn.close()

        return True, None
    
    except Exception as err:
        return False, err

def get_task(titulo, nickname):

    try:
        conn = utils.connect_database()
        cursor = conn.cursor()
        query = """SELECT * FROM tasks WHERE titulo = %s AND nickname = %s"""
        cursor.execute(query, (titulo, nickname))
        task = cursor.fetchone()

        conn.close()
        
        if task:
            return True, task
        else:
            return False, "Task não encontrada"

    except Exception as err:
        return False, err

def get_tasks(nickname):

    try:
        conn = utils.connect_database()
        cursor = conn.cursor()
        query = """SELECT * FROM tasks WHERE nickname = %s"""
        cursor.execute(query, (nickname, ))
        task = cursor.fetchall()

        conn.close()
        
        if task:
            return True, task
        else:
            return False, "Tasks não encontradas"

    except Exception as err:
        return False, err

def update_task(nickname, titulo, data):
    try:
        conn = utils.connect_database()
        cursor = conn.cursor()

        exist, err = get_task(titulo, nickname)
        if not exist:
            return False, "Task não encontrada"

        update_fields = ", ".join([f"{key} = %s" for key in data.keys()])
        query = f"""UPDATE tasks SET {update_fields} WHERE nickname = %s AND titulo = %s"""

        
        values = list(data.values())
        values.append(nickname)
        values.append(titulo)

        
        cursor.execute(query, tuple(values))
        conn.commit()
        conn.close()

        return True, None
    
    except Exception as err:
        return False, err

            