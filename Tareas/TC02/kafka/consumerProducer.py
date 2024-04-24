from datetime import datetime, timezone
import json
#import pymongo
from pymongo import MongoClient
from confluent_kafka import Consumer, Producer, KafkaError, KafkaException
#import os


MONGO_URI = "mongodb://root:example@MongoDB:27017"
MONGO_DB = "messageDB"
MONGO_COLLECTION = "kafkaMensajes"
BOOTSTRAP_HOST =  "localhost:9092"
canales_suscritos = []  # Lista de canales suscritos
mensajes_pendientes = []  # Lista de mensajes pendientes

print(MONGO_URI)


def conectar_mongo():
    try:
        client = MongoClient('localhost', 27017, username='root', password='example') #pasarlo a variables de entorno
        db = client[MONGO_DB]
        coleccion = db[MONGO_COLLECTION]
        return coleccion
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")
        return None

# Conexión a Kafka

# Configuration for Kafka Producer
producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'mi-productor-app',
}

# Crea el Producer sin errores
producer = Producer(producer_config)

# Produce a message with manual serialization
def produce_message(topic, key, value):
    producer.produce(topic, key=key.encode('utf-8'), value=value.encode('utf-8'))
    producer.flush()  # Para asegurarse de que los mensajes se envíen

# Configuration for Kafka Consumer
def configurar_consumidor(tema):
    config = {
        'bootstrap.servers': 'localhost:9092',  # Cambia a tu servidor Kafka
        'group.id': 'my-group',
        'auto.offset.reset': 'earliest',  # Comenzar desde el inicio si es un nuevo grupo
    }
    consumer = Consumer(config)
    consumer.subscribe([tema])
    return consumer

def guardar_mensaje_mongo(mensaje):
    # Guardar el mensaje en la colección de MongoDB
    coleccion = conectar_mongo()
    documento = {
        "mensaje": mensaje,
        "timestamp": datetime.now(timezone.utc),  # Para agregar un tiempo a cada mensaje
    }
    coleccion.insert_one(documento)
    

def mostrar_mensajes_almacenados():
    coleccion = conectar_mongo()
    mensajes = coleccion.find({})
    for mensaje in mensajes:
        print(f"Mensaje almacenado: {mensaje}")

def mostrar_mensajes_pendientes():
    if mensajes_pendientes:
        for mensaje in mensajes_pendientes:
            print(f"Mensaje recibido del canal '{mensaje['canal']}': {mensaje['mensaje']}")
        mensajes_pendientes.clear()  # Limpiar la lista de mensajes pendientes
    else:
        print("No hay mensajes pendientes.")

"""def crear_topic(topic):
    try:
        producer.create_topics(topic, partitions=1, factorOfReplication=1)
        print(f"tema '{topic}' creado correctamente.")
    except Exception as e:
        print(f"Error al crear el tema '{topic}': {e}")"""

def enviar_mensaje(topic, mensaje):
    try:
        producer.produce(topic, value=mensaje)
        guardar_mensaje_mongo(mensaje)
        print(f"Mensaje enviado correctamente al tema '{topic}': {mensaje}")
    except Exception as e:
        print(f"Error al enviar mensaje al tema '{topic}': {e}")

def consumidor(tema):
    consumer = configurar_consumidor(tema)
    mensajes_pendientes = []

    while True:
        try:
            message = consumer.poll(timeout=1.0)

            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print("Error en el mensaje:", message.error())
                    continue

            key = message.key()
            value = message.value()

            if isinstance(value, bytes):
                value = value.decode('utf-8')

            mensaje_json = json.loads(value)
            guardar_mensaje_mongo(mensaje_json)
            mensajes_pendientes.append(mensaje_json)

        except KafkaException as ke:
            print("KafkaException:", ke)
        
        except json.JSONDecodeError:
            print("Error al decodificar el mensaje")
        
        except Exception as e:
            print("Error en el consumidor:", str(e))
"""
def suscribirse_canal(canal):
    if canal not in canales_suscritos:
        # Verificar si el topic existe
        if not producer.topics_exist([canal]):
            crear_topic(canal)

        canales_suscritos.append(canal)
        consumer.subscribe(canales_suscritos)
        print(f"Suscrito al canal '{canal}'.")
        """
"""
def desuscribirse_canal(canal):
    if canal in canales_suscritos:
        canales_suscritos.remove(canal)
        consumer.subscribe(canales_suscritos)
        print(f"Desuscrito del canal '{canal}'.")
        """

def main():
    print(
            "\nMenú Principal:\n",
            "1. Suscribirse a un canal\n",
            "2. Enviar mensaje\n",
            "3. Desuscribirse de un canal\n",
            "4. Consumir mensajes\n",
            "5. Ver mensajes pendientes\n",
            "6. Ver mensajes almacenados\n",
            "7. Salir",
        )

    while True:
        seleccion = int(input("Digite el numero de una opción: "))
        encontrar_topics()
        if seleccion == 1:
            nombre_tema = input("Ingrese el nombre del tema a suscribirse: ")
            #crear_topic(nombre_tema)
        elif seleccion == 2:
            tema = input("Ingrese el tema de destino: ")
            mensaje = input("Ingrese el mensaje a enviar: ")
            enviar_mensaje(tema, mensaje)
        elif seleccion==3:
            nombre_tema = input("Ingrese el nombre del tema a desuscribirse: ")
            #desuscribirse_canal(nombre_tema)
        elif seleccion == 4:
            tema = input("Ingrese el tema a consumir: ")
            consumidor(tema)
        elif seleccion == 5:
            mostrar_mensajes_pendientes()
        elif seleccion == 6:
            mostrar_mensajes_almacenados()
        else:
            break
main()