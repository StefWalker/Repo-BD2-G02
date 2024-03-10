import psycopg2


class Database:
    def __init__(
        self, database="db_name", host="db_host", user="db_user", password="db_pass", port="db_port"
    ):
        self.conn = psycopg2.connect(
            database=database, host=host, user=user, password=password, port=port
        )

    def get_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks;")
        data = cursor.fetchall()
        cursor.close()
        return data

    def create_task(self, task):
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO tasks (name, description, due_date, status, usuario_id) VALUES ('{task['name']}', '{task['description']}', '{task['due_date']}', '{task['status']}', '{task['usuario_id']}');"
        )
        self.conn.commit()
        cursor.close()
        return task

    def update_task(self, request_task):
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE tasks SET name = '{request_task['name']}', description = '{request_task['description']}', due_date = '{request_task['due_date']}', status = '{request_task['status']}', usuario_id = '{request_task['usuario_id']}' WHERE id = {request_task['id']};"
        )
        self.conn.commit()
        cursor.close()
        return request_task

    def delete_task(self, request_task_id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM tasks WHERE id = {request_task_id};")
        self.conn.commit()
        cursor.close()
        return request_task_id
    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def get_user(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios;")
        data = cursor.fetchall()
        cursor.close()
        return data

    def create_user(self, user):
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO usuarios (name, password) VALUES ('{user['name']}', '{user['password']}');"
        )
        self.conn.commit()
        cursor.close()
        return user

    def update_user(self, request_user):
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE usuarios SET name = '{request_user['name']}', password = '{request_user['password']}' WHERE user_id = {request_user['user_id']};"
        )
        self.conn.commit()
        cursor.close()
        return request_user

    def delete_user(self, request_user_id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM usuarios WHERE user_id = {request_user_id};")
        self.conn.commit()
        cursor.close()
        return request_user_id