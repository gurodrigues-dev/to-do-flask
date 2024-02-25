import controllers
from main import app, jwt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import jsonify

@app.route("/api/v1/user", methods=["POST"])
def create_user():
    return controllers.create_user()

@app.route("/api/v1/user/<nickname>", methods=["DELETE"])
@jwt_required()
def delete_user(nickname):
    return controllers.delete_user(nickname)

@app.route("/api/v1/user/<nickname>", methods=["GET"])
def get_user(nickname):
    return controllers.get_user(nickname)

@app.route("/api/v1/user/<nickname>", methods=["PUT"])
@jwt_required()
def update_user(nickname):
    return controllers.update_user(nickname)

@app.route("/api/v1/login", methods=["POST"])
def login():
    return controllers.login()

@app.route("/api/v1/task/<nickname>", methods=['POST'])
@jwt_required()
def create_task(nickname):
    return controllers.create_task(nickname)

@app.route("/api/v1/task/<nickname>/<titulo>", methods=["DELETE"])
@jwt_required()
def delete_task(nickname, titulo):
    return controllers.delete_task(nickname, titulo)

@app.route("/api/v1/task/<nickname>/<titulo>", methods=["GET"])
def get_task(nickname, titulo):
    return controllers.get_task(nickname, titulo)

@app.route("/api/v1/task/<nickname>", methods=["GET"])
def get_tasks(nickname):
    return controllers.get_tasks(nickname)

@app.route("/api/v1/task/<nickname>/<titulo>", methods=["PUT"])
@jwt_required()
def update_task(nickname, titulo):
    return controllers.update_task(nickname, titulo)

@app.route("/api/v1/jwt", methods=["GET"])
@jwt_required()
def protected():
    return controllers.protected()

if __name__ == '__main__':
    app.run(debug=True, port=5000)