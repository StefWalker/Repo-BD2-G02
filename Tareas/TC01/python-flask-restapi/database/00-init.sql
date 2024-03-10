CREATE DATABASE tareauno;

\c tareauno;

CREATE TABLE usuarios (
  user_id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  due_date DATE NOT NULL,
  status VARCHAR(255) NOT NULL,
  usuario_id INT NOT NULL
  );

