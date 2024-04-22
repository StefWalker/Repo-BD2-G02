#!/bin/bash

# Crear dos topics en Kafka
kafka-topics.sh \
  --create \
  --topic topic1 \
  --partitions 1 \
  --replication-factor 1 \
  --if-not-exists \
  --bootstrap-server kafka:9092

kafka-topics.sh \
  --create \
  --topic topic2 \
  --partitions 1 \
  --replication-factor 1 \
  --if-not-exists \
  --bootstrap-server kafka:9092
