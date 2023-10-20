# Python API for Delta Tables

A simple FastAPI example of three endpoints to create, read and append data to a delta table.

Note: This example uses Azurite Emulator as Storage Account.

## Stand up the services

```bash
docker-compose up -d --build
```

## Create the container

1. Using Microsoft Azure Storage Explorer connect to Storage Accounts / Emulator.
1. Create a container: sandbox 

## Create a delta table

```bash
curl -X POST http://127.0.0.1:8000/create \
   -H 'Content-Type: application/json' \
   -d '{ "x": 1, "y": 1 }'
```

## Append to delta table

```bash
curl -X POST http://127.0.0.1:8000/append \
   -H 'Content-Type: application/json' \
   -d '{ "x": 2, "y": 2 }'
```

## Read delta table

```bash
curl http://127.0.0.1:8000/read
```

