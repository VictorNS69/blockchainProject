# Social Network's Smart Contracts
This directory contains the truffle project with the Smart Contracts implemented

## Table of Contents
- [Requirements](#requirements)
- [Set up](#set-up)
- [Run the tests](#run-the-tests)
- [Deploy the Smart Contracts](#deploy-the-smart-contracts)

## Requirements
- Node (`sudo apt install node`)
- Truffle (`npm install -g truffle`)
- Install requirements with `npm install`

## Set up
To set up this project, you need to run your local Ethereum blockchain. You can do it easily with:
```bash
docker run --name ganache-cli -d -p 8545:8545 trufflesuite/ganache-cli:latest
```
## Run the tests
You can run all the unittest with the command
```bash
truffle test
```
**Notice**: When you run for the first time the test, maybe an error will appear 
(_ENOENT: no such file or directory, open 'build/contracts/SocialNetwork-address'_). If so, just create the file with 
`touch build/contracts/SocialNetwork-address` or just run the [deploy](#deploy-the-smart-contracts)

## Deploy the Smart Contracts
In order to deploy the Smart Contracts, you need to set up [ganache](#set-up) and run:
```bash
truffle deploy
```
