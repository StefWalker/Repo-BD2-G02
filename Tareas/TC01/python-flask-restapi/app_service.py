import json
from flask_jwt_extended import get_jwt_identity, jwt_required

from db import Database

class AppService:

    def __init__(self, database: Database):
        self.database = database

    def get_tasks(self):
        data = self.database.get_tasks()
        return data

    def create_task(self, task):
        self.database.create_task(task)
        return task

    def update_task(self, request_task):
        self.database.update_task(request_task)
        return request_task

    def delete_task(self, request_task_id):
        self.database.delete_task(request_task_id)
        return request_task_id

    def get_user(self):
        current_user = get_jwt_identity()
        data = self.database.get_user(current_user)
        return data
    
    def create_user(self, user):
        self.database.create_user(user)
        return user

    def update_user(self, request_user):
        current_user = get_jwt_identity()

        if current_user == request_user['username']:
            self.database.update_user(request_user)
            return request_user
        else:
            return {'message': 'No tienes permiso para actualizar este usuario'}, 403

    def delete_user(self, request_user_id):
        current_user = get_jwt_identity()

        if current_user == request_user_id:
            self.database.delete_user(request_user_id)
            return {'message': 'Usuario eliminado exitosamente'}
        else:
            return {'message': 'No tienes permiso para eliminar este usuario'}, 403