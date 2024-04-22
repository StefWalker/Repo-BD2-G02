import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from app_service import AppService

# Conexión a MongoDB
MONGO_URI = os.getenv("MONGO_URI")
API_PORT= os.getenv("ApiPort")
API_HOST= os.getenv("DB_HOST")
client = MongoClient(MONGO_URI)

# Nombre de la base de datos
DB_NAME = "mydatabase"
db = client[DB_NAME]

appService = AppService(db)

app = Flask(__name__)

@app.route("/api/messages", methods=["POST"])
def create_message():
    # Obtener los datos del request
    request_data = request.get_json()

    # Insertar los datos en la colección de MongoDB
    db.messages.insert_one(request_data)

    return jsonify({"status": "success", "message": "Message created"}), 201

@app.route("/api/messages", methods=["GET"])
def get_messages():
    # Obtener todos los mensajes de la colección
    messages = list(db.messages.find({}))

    # Convertir objetos BSON a JSON
    for message in messages:
        message["_id"] = str(message["_id"])  # Convertir ObjectId a string

    return jsonify(messages)

if __name__ == "__main__":
    app.run(host=API_HOST, port=API_PORT, debug=True)
