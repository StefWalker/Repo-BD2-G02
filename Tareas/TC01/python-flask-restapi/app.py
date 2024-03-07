import json
import os

from app_service import AppService
from db import Database
from flask import Flask, request

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


db = Database(database=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)

app = Flask(__name__)
appService = AppService(db)


@app.route("/")
def home():
    return "App Works!!! juan"


@app.route("/api/tasks")
def tasks():
    # Obtener el JSON para validar usuario
    request_data = request.get_json()
    
    return appService.get_tasks(request_data)


@app.route("/api/tasks", methods=["POST"])
def create_task():
    # Obtener el JSON para validar usuario
    request_data = request.get_json()
    return appService.create_task(request_data)


@app.route("/api/tasks", methods=["PUT"])
def update_task():
    # Obtener el JSON para validar usuario
    request_data = request.get_json()
    return appService.update_task(request_data)


@app.route("/api/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    # Obtener el JSON para validar usuario
    request_data = request.get_json()
    return appService.delete_task(request_data ,str(id))

#/////////////////////////////////////////////////////////////////////
"""
@app.route("/api/user")
def user():
    return appService.get_user()


@app.route("/api/user", methods=["POST"])
def create_user():
    request_data = request.get_json()
    user = request_data
    return appService.create_user(user)


@app.route("/api/user", methods=["PUT"])
def update_user():
    request_data = request.get_json()
    return appService.update_user(request_data)


@app.route("/api/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    return appService.delete_user(str(id))
"""