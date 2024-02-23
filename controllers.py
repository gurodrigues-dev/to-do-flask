from http import server
import models
import repository
import utils
import service
from flask import Flask, request, jsonify
from main import jwt, create_access_token, get_jwt_identity

def create_user():
    
    password = service.criptografar_password(request.json.get('password'))

    user = models.User(
        request.json.get('name'),
        request.json.get('nickname'),
        password,
        request.json.get('email')
    )

    save, err = service.save_user(user)

    if not save:
        return jsonify({
            "message": "Erro ao criar usuário",
            "error": str(err)
        }), 502

    return jsonify({

        "message": "Usuário criado com sucesso",
    }), 201

def delete_user(nickname):
    current_user = get_jwt_identity()
    user, error = service.verify_identity(nickname, current_user)
    if not user:
        return jsonify({
            "message": "Unauthorized",
            "error": str(error)
            }), 401

    remove, err = service.delete_user(nickname)

    if not remove:
        return jsonify({
            "message": "erro ao deletar usuário",
            "error": str(err)
        }), 502

    return jsonify({
        "message": "usuário deletado com sucesso",
    }), 201

def get_user(nickname):

    exists, value = service.get_user(nickname)
    
    if not exists:
        return jsonify({
            "message": "Usuário não encontrado",
        }), 404

    elif exists:
        return jsonify({
            "message": "Usuário encontrado",
            "user": value
        }), 200
    
    return jsonify({
        "message": "erro ao encontrar usuário",
        "error": value
    }), 502

def update_user(nickname):
    current_user = get_jwt_identity()
    user, error = service.verify_identity(nickname, current_user)
    if not user:
        return jsonify({
            "message": "Unauthorized",
            "error": str(error)
            }), 401

    data = request.json

    update, err = service.update_user(nickname, data)

    if not update:
        return jsonify({
            "message": "erro ao atualizar usuário",
            "error": str(err)
        }), 502

    return jsonify({
        "message": "usuário atualizado com sucesso",
    }), 201


def login():

    password = service.criptografar_password(request.json.get('password'))

    user = models.User(
        None,
        request.json.get('nickname'),
        password,
        None
        )
    
    login, err = service.verify_user(user)

    if not login:
        return jsonify({
            "message": "erro no nickname ou senha",
            "error": str(err)
        }), 502
    
    access_token = create_access_token(identity=user.nickname)
    
    return jsonify({
        "message": "usuário encontrado",
        "token": access_token
    }), 200

def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
