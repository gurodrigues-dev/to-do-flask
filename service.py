from genericpath import exists
import utils
import models
import repository
from main import get_jwt_identity

def save_user(user: models.User):
    save, err = repository.save_user(user)
    return save, err

def verify_identity(nickname, current_user):
    if current_user != nickname:
        return False, f"Autorização necessária"
    return True, None

def delete_user(nickname):
    remove, err = repository.remove_user(nickname)
    return remove, err

def get_user(nickname):
    exists, value = repository.get_user(nickname)
    return exists, value

def criptografar_password(password):
    return utils.criptografar_password(password)

def update_user(nickname, data):
    if 'password' in data:
        new_password = criptografar_password(data['password'])
        data['password'] = new_password
        
    update, err = repository.update_user(nickname, data)
    return update, err

def verify_user(user):
    login, err = repository.verify_user(user)
    return login, err


def save_task(Task: models.Tasks):
    save, err = repository.save_task(Task)
    return save, err

def delete_task(titulo, nickname):
    remove, err = repository.remove_task(titulo, nickname)
    return remove, err

def get_task(titulo, nickname):
    exist, value = repository.get_task(titulo, nickname)
    return exist, value

def get_tasks(nickname):
    exist, value = repository.get_tasks(nickname)
    return exist, value

def update_task(nickname, titulo, data):
    update, err = repository.update_task(nickname, titulo, data)
    return update, err

