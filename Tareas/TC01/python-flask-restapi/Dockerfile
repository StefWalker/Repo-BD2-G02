FROM python:3.11

ENV DB_HOST='localhost'
ENV DB_PORT=5432
ENV DB_NAME='flask_restapi'
ENV DB_USER='flask_restapi'
ENV DB_PASSWORD='flask_restapi_pass'


WORKDIR /opt/app

COPY . .

RUN pip install poetry
RUN poetry install

RUN poetry add flask-bcrypt flask-jwt-extended

VOLUME /data_store
EXPOSE 5000

# Command "python3 -m flask run --host=0.0.0.0"
CMD ["poetry", "run", "python3", "-m", "flask", "run", "--host=0.0.0.0"]

RUN poetry run python -m venv .venv