# blockchainProject
![Smart Contracts tests](https://github.com/VictorNS69/blockchainProject/workflows/Smart%20Contracts%20tests/badge.svg)

## work in progress

crear container postgres
```bash
docker run --name socialNetwork_db -d -p 5432:5432 -e POSTGRES_PASSWORD="socialNetwork" postgres:9.6.17-alpine
```
crear base de datos dentro del container
```bash
docker exec -it socialNetwork_db createdb socialNetwork -U postgres
```
Acceder al terminal de postgres
```bash
docker exec -it socialNetwork_db psql -U postgres
```

## Requisitos
para el proyecto de django
- python3.6
- install requirements.txt
- docker (y ejecutar las consultas para la base de datos)
- postgresql

para el proyecto blockchain
- node
- mpm install -g truffle
- npm install truffle-assertions (desde dentro de blockchain)
- docker (para ganache)

```bash
docker run --name ganache-cli -d -p 8545:8545 trufflesuite/ganache-cli:latest
```
docker run --name socialNetwork_redis -p 6379:6379  redis:6.0-alpine


install celery sudo apt install python-celery-common

celery worker -A socialNetwork --loglevel=info


