FROM python:3.11

# Instala dependencias necesarias
RUN pip install confluent_kafka pymongo 

# Define el directorio de trabajo
WORKDIR /opt/app

# Copia todos los archivos del contexto de construcción a la imagen
COPY . .

# Configura las variables de entorno
ENV MONGO_URI='mongodb://root:example@MongoDB:27017'  
ENV BOOTSTRAP_HOST='localhost:9092'  
ENV DB_NAME='messageDB'  
ENV MONGO_COLLECTION='kafkaMensajes'  

# Ejecuta el consumidor-productor
#CMD ["python", "consumerProducer.py"]
#se debe crear un terminal por aparte 
