# blockchainProject
![Smart Contracts tests](https://github.com/VictorNS69/blockchainProject/workflows/Smart%20Contracts%20tests/badge.svg)

## work in progress

crear container postgres
```bash
docker run --name socialNetwork_DB -e POSTGRES_PASSWORD="socialNetwork" -d postgres:9.6.17-alpine
```
crear base de datos dentro del container
```bash
docker exec -it socialNetwork_DB createdb socialNetwork -U postgres
```
Acceder al terminal de postgres
```bash
docker exec -it socialNetwork_DB psql -U postgres
```