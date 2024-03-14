# Investigacion Despliegue de Aplicaciones con Docker y PostgreSQL

El objetivo de esta tarea es familiarizar a los estudiantes con las prácticas de contenedorización y orquestación de aplicaciones mediante el uso de Docker y Docker Compose. Los estudiantes aprenderán a desplegar
una aplicación REST API en conjunto con una base de datos PostgreSQL, enfocándose en la automatización,
la reproducibilidad y la escalabilidad.

[Link del Api](http://127.0.0.1:5000/api/tasks)

# Orquestación con Docker Compose

Construye la imagen de docker, contenedor y volumenes necesarios para la ejecucion
``` bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```
En caso de que un fallo con reejecutar el codigo se soluciona
``` bash example-bad
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

## Ejecuta un shell dentro del contenedor

Los se encuentran en este link donde encontrada un archivo tipo json para importar en Postman
[Archivo postman de EndPoints](https://github.com/StefWalker/Repo-BD2-G02/blob/main/Tareas/TC01/TC01-Endpoints.postman_collection.json)

## Autenticacion JWT

Ejecutando el request tipo POST "http://localhost:5002/api/user"

Con body de estructura "{
    "username":"Erick",
    "password":"Log1n_P@55"
}"

Se obtiene el "access_token", el cual se consume en los demas request como Beader Token.
