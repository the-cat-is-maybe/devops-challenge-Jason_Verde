FROM mongo:latest

RUN mkdir -p /data/import; mkdir -p /docker-entrypoint-initdb.d/

COPY data/restaurant.json /data/import/restaurant.json
COPY data/mongo-init* /docker-entrypoint-initdb.d/
