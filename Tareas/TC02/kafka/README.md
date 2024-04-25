# Tarea corta 2

- Luis Felipe Calderón Pérez | 2021048663
- Dylan Stef Torres Walker | 2018135751
- Esteban Morales Ureña | 2018171928

# Commandos 

## Instalar las dependencias
``` bash
pip install confluent_kafka pymongo
```

## Levantar Docker

``` bash
docker-compose build
docker-compose up
```

## Se ejecuta el comando de Python y se inicia el Foro General
``` bash
consumerProducer.py
se ingresa el codigo: 612642713
```
Con este codigo se inicia el foro general el cual crea la db y la collecion
A su vez es lo que mantiene la persistencia de mensajes para foros que no tengan consumidores activos

## Se ejecuta otra instancia de Python en una nueva teminal
``` bash
consumerProducer.py
```
Apartir de este punto se puede navegar en el menu proporcionado con las opciones 1 y 2
La 1 permite crear nuevas entradas a su vez estos estaran disponibles para cualquiera que este escuchando 
La 2 se pone en modo consumidor esperando nuevos mensajes del foro que busco (ctrl+c) para terminar esta terminal

*Nota:
Por motivo de delay el primer consumidor no escucha los timestamps de mongo, la solucion se da con un ejecutar un segundo consumidor*

## Arquitectura

Es una arquitectura estandar de Kafka con un solo zookeeper sin replica y un broker, con n topics que se pueden generar de manera estandar
En cuanto a la arquitectura del cliente de python puede ser tanto consumidor como productor, pero cuando decide ser consumidor se debe crear una nueva terminar para lograr producir mensajes
A su vez se debe crear una primera instancia de foro general para tener la persistencia de datos enviados por Kafka

## Utilizacion de Kafka y MongoDB

Kafka se utiliza para la generacion de la instacia de produccion y del consumidor
Mongo se utiliza en el consumidor cuando recibe los mensajes del productor de Kafka
