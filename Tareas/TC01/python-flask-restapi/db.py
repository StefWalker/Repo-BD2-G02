import psycopg2


class Database:
    def __init__(
        self, database="db_name", host="db_host", user="db_user", password="db_pass", port="db_port"
    ):
        self.conn = psycopg2.connect(
            database=database, host=host, user=user, password=password, port=port
        )

    def get_tasks(self, token):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks;")
        data = cursor.fetchall()
        cursor.close()
        return data

    def create_task(self, task, token):
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO tasks (title, description) VALUES ('{task['title']}', '{task['description']}');"
        )
        self.conn.commit()
        cursor.close()
        return task

    def update_task(self, request_task, token):
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE tasks SET title = '{request_task['title']}', description = '{request_task['description']}' WHERE id = {request_task['id']};"
        )
        self.conn.commit()
        cursor.close()
        return request_task

    def delete_task(self, request_task_id, token):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM tasks WHERE id = {request_task_id};")
        self.conn.commit()
        cursor.close()
        return request_task_id

    def verify_user(self, user_token):
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT COUNT(*) FROM usuarios WHERE token ='{user_token}';"
        )
        data = cursor.fetchall()
        cursor.close()
        return data
    
    #//////////////////////////////////////////////////////
    """""
    def get_user(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios;")
        data = cursor.fetchall()
        cursor.close()
        return data

    def create_user(self, user):
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO usuarios (name, correo) VALUES ('{user['name']}', '{user['correo']}');"
        )
        self.conn.commit()
        cursor.close()
        return user

    def update_user(self, request_user):
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE usuarios SET name = '{request_user['name']}', description = '{request_user['description']}' WHERE id = {request_user['id']};"
        )
        self.conn.commit()
        cursor.close()
        return request_user

    def delete_user(self, request_user_id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM usuarios WHERE id = {request_user_id};")
        self.conn.commit()
        cursor.close()
        return request_user_id
    """
