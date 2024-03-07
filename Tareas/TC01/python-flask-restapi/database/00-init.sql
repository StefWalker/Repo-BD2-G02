CREATE DATABASE tasksDB;

\c tasksDB;

CREATE TABLE usuarios (
  user_id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  correo TEXT NOT NULL
);

CREATE TABLE tasks (
  task_id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  due_date DATE NOT NULL,
  status BINARY NOT NULL,
  FOREIGN KEY (user_id) REFERENCES usuarios(user_id)
);