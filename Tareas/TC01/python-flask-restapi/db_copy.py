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

    def update_task(self, request_task):
        cursor = self.conn.cursor()
        query = "UPDATE tasks SET name = %s, description = %s WHERE id = %s;"
        values = (request_task["name"], request_task["description"], request_task["id"])
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        return request_task

    def delete_task(self, request_task_id):
        cursor = self.conn.cursor()
        query = "DELETE FROM tasks WHERE id = %s;"
        values = (request_task_id,)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        return request_task_id

    def create_task(self, task):
        cursor = self.conn.cursor()
        query = "INSERT INTO tasks (name, description) VALUES (%s, %s);"
        values = (task["name"], task["description"])
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        return task

    def create_task(self, task):
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO tasks (name, description) VALUES ('{task['name']}', '{task['description']}');"
        )
        self.conn.commit()
        cursor.close()
        return task

    def update_task(self, request_task):
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE tasks SET name = '{request_task['name']}', description = '{request_task['description']}' WHERE id = {request_task['id']};"
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
