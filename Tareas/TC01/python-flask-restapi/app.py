import json
import os
import re
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_bcrypt import Bcrypt

from app_service import AppService
from db import Database

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

db = Database(database=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = 'mysecretkey'  
jwt = JWTManager(app)
appService = AppService(db)

@app.route("/")
@jwt_required()  
def home():
    return "App Works!!!"

@app.route("/api/tasks")
@jwt_required()  
def tasks():
    return appService.get_tasks()

@app.route("/api/tasks", methods=["POST"])
@jwt_required()  
def create_task():
    request_data = request.get_json()
    task = request_data
    return appService.create_task(task)

@app.route("/api/tasks", methods=["PUT"])
@jwt_required()  
def update_task():
    request_data = request.get_json()
    return appService.update_task(request_data)

@app.route("/api/tasks/<int:id>", methods=["DELETE"])
@jwt_required()  
def delete_task(id):
    return appService.delete_task(str(id))

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route("/api/user")
@jwt_required()  
def user():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route("/api/user", methods=["POST"])
def create_user():
    request_data = request.get_json()
    username = request_data.get('username')
    password = request_data.get('password')
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    access_token = create_access_token(identity=username)

    return jsonify({'message': 'Usuario registrado exitosamente', 'access_token': access_token}), 201


@app.route("/api/user", methods=["PUT"])
@jwt_required()  
def update_user():
    current_user = get_jwt_identity()
    request_data = request.get_json()

    if current_user == request_data.get('username'):
        return appService.update_user(request_data)
    else:
        return {'message': 'No tienes permiso para actualizar este usuario'}, 403

@app.route("/api/user/<int:id>", methods=["DELETE"])
@jwt_required() 
def delete_user(id):
    current_user = get_jwt_identity()

    
    if current_user == str(id):
        return appService.delete_user(str(id))
    else:
        return {'message': 'No tienes permiso para eliminar este usuario'}, 403

if __name__ == "__main__":
    app.run(debug=True)
