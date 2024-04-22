from pymongo import MongoClient
from bson.objectid import ObjectId


class Database:
    def __init__(self, mongo_uri):
        self.client = MongoClient(mongo_uri)
        self.db = self.client['messageDB']  # Puedes cambiar el nombre de la base de datos

    def get_tasks(self):
        tasks_collection = self.db['tasks']  # Nombre de la colección
        tasks = list(tasks_collection.find({}))
        return tasks

    def create_task(self, task):
        tasks_collection = self.db['tasks']
        inserted_id = tasks_collection.insert_one(task).inserted_id
        return str(inserted_id)  # Devuelve el ID del documento insertado

    def update_task(self, task_id, updated_task):
        tasks_collection = self.db['tasks']
        result = tasks_collection.update_one(
            {'_id': ObjectId(task_id)}, {"$set": updated_task}
        )
        return result.modified_count  # Devuelve el número de documentos modificados

    def delete_task(self, task_id):
        tasks_collection = self.db['tasks']
        result = tasks_collection.delete_one({'_id': ObjectId(task_id)})
        return result.deleted_count  # Devuelve el número de documentos eliminados

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def get_user(self):
        users_collection = self.db['users']
        users = list(users_collection.find({}))
        return users

    def create_user(self, user):
        users_collection = self.db['users']
        inserted_id = users_collection.insert_one(user).inserted_id
        return str(inserted_id)

    def update_user(self, user_id, updated_user):
        users_collection = self.db['users']
        result = users_collection.update_one(
            {'_id': ObjectId(user_id)}, {"$set": updated_user}
        )
        return result.modified_count

