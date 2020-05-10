# Social Network
![Smart Contracts test](https://github.com/VictorNS69/blockchainProject/workflows/Smart%20Contracts%20tests/badge.svg)

**This is a work in progress**

## Table of Contents
- [Requirements](#requirements)
  - [socialNetwork (Django project)](#socialnetwork-django-project)
  - [blockchain (truffle project)](#blockchain-truffle-project)
- [Set up](#set-up)
  - [Database](#database)
  - [Virtual environment](#virtual-environment)
  - [Redis and celery](#redis-broker-and-celery-task-queue)
  - [Ganache](#ganache-cli-personal-blockchain-for-ethereum)
- [How to run the app](#how-to-run-the-app)
- [License](#license)
- [Contributors](#contributors)

## Requirements
- Docker and Docker-compose (`sudo apt install docker docker-compose`)
### socialNetwork (Django project)
- Python 3.6 (`sudo apt install python3.6`)
- Celery (`sudo apt install python-celery-common`)
- Requirements (inside socialNetwork directory with the [virtual environment](#virtual-environment) activated,
`pip install -r requirements.txt`)
### blockchain (truffle project)
- Node (`sudo apt install node`)
- Truffle (`npm install -g truffle`)
- Install requirements (inside blockchain directory `npm install`)

## Set up
### Database
First, we need a _postgres_ database. We can easy create one with this docker command.
```bash
# This creates the container, not the database
docker run --name socialNetwork_db -d -p 5432:5432 -e POSTGRES_PASSWORD="socialNetwork" postgres:9.6.17-alpine
```
Then we need to create the database inside the container.
```bash
docker exec -it socialNetwork_db createdb socialNetwork -U postgres
```
In addition, if we want to enter the terminal inside our postgres, we can do it with this command:
```bash
docker exec -it socialNetwork_db psql -U postgres
```
### Virtual environment
You need to create a python virtual environment. If you don't know how, follow this steps.
1. Install _virtualenv_ and _virtualenvwrapper_ following this 
[gist](https://gist.github.com/VictorNS69/25f82339708714628177a7e2bd566afc).
2. Create the environment with this command.
```bash
# This will create a virtual environment called "socialNetwork"
mkvirtualenv --python=/usr/bin/python3.6 socialNetwork
```
In order to **activate the environment** you just need to execute `workon socialNetwork`, and to deactivate it, just type
`deactivate`.

### Redis (Broker) and celery (Task queue)
In order to set up our redis, we just need to run this docker command:
```bash
docker run --name socialNetwork_redis -p 6379:6379  redis:6.0-alpine
```
At the moment, we have not dockerized celery, so we can start our celery running this command in a terminal 
(**don't kill this terminal**).
```bash
cd socialNetwork
celery worker -A socialNetwork --loglevel=info
```
### Ganache-cli (personal blockchain for Ethereum)
We can easily set up our local blockchain with this docker command:
```bash
docker run --name ganache-cli -d -p 8545:8545 trufflesuite/ganache-cli:latest
```

## How to run the app
**Before running this app, you need to install all requirements and do the set up.** 

If so, just follow this steps:
1. Be sure [ganache-cli](#ganache-cli-personal-blockchain-for-ethereum) docker is running.
1. Go into the [blockchain](/blockchain) directory and deploy the contracts with `truffle deploy`.
1. Be sure the [database](#database) is up.
1. Go to the [socialNetwork](/socialNetwork) directory and stay there.
1. Activate your [virtual environment](#virtual-environment).
1. Be sure [redis and celery](#redis-broker-and-celery-task-queue) are running.
1. Do the migrations if needed (`python manage.py makemigrations` and `python manage.py migrate`)
1. Flush the database `python manage.py flush` (this cleans the database, so there will be no conflicts with the 
Smart Contracts)
1. Finally, run the server with `python manage.py runserver` and go to http://127.0.0.1:8000.

## License
MIT License. See more [here](/LICENSE).

## Contributors
- [Víctor Nieves](https://github.com/VictorNS69)
- [Daniel Morgera](https://github.com/dmorgera)
