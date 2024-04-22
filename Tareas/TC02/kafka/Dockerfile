FROM python:3.11

ENV DB_HOST='localhost'
ENV DB_PORT=8081
ENV DB_NAME='messageDB'
ENV ApiPort=5000
ENV MONGO_URI='mongodb://root:example@mongo:27017'


WORKDIR /opt/app

COPY . .

RUN pip install poetry
RUN poetry install

VOLUME /data_store
EXPOSE 5000

# Command "python3 -m flask run --host=0.0.0.0"
CMD ["poetry", "run", "python3", "-m", "flask", "run", "--host=0.0.0.0"]

