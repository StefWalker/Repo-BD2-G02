import json

from db import Database


class AppService:

    def __init__(self, database: Database):
        self.database = database

    def get_tasks(self, token):
        data = self.database.get_tasks(token)
        return data

    def create_task(self, task, token):
        self.database.create_task(task, token)
        return task

    def update_task(self, request_task, token):
        self.database.update_task(request_task, token)
        return request_task

    def delete_task(self, request_task_id, token):
        self.database.delete_task(request_task_id, token)
        return request_task_id
    #//////////////////////////////////////////////////////////////
    """
    def get_user(self):
        data = self.database.get_user()
        return data

    def create_user(self, user):
        self.database.create_user(user)
        return user

    def update_user(self, request_user):
        self.database.update_user(request_user)
        return request_user

    def delete_user(self, request_user_id):
        self.database.delete_user(request_user_id)
        return request_user_id
    """
    