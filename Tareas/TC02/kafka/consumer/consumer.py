import pymongo
from confluent_kafka import Consumer

# Conexión a MongoDB
client = pymongo.MongoClient("localhost:27017")
db = client["my-database"]
collection = db["my-collection"]

# Conexión a Kafka
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest',
})

consumer.subscribe(topics=['my-topic'])

try:
    while True:
        message = consumer.poll(timeout=1.0)
        if message is None:
            continue
        else:
            value = message.value().decode('utf-8')
            print(f"Mensaje recibido: {value}")

            # Almacenar el mensaje en MongoDB
            collection.insert_one({"value": value})
except KeyboardInterrupt:
    pass

finally:
    consumer.close()
