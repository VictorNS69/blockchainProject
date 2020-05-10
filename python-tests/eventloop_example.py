import json
import requests
from web3 import Web3, HTTPProvider

try:
    w3 = Web3(HTTPProvider("http://127.0.0.1:8545"))
    w3.eth.getBlockTransactionCount(0) # Sirve como "ping" para saber que la blockchain está levantada
except requests.exceptions.ConnectionError:
    print("Refused connection")
    exit(1)

with open("../blockchain/build/contracts/SocialNetwork-address", 'r', encoding='utf-8') as f:
    info_address = f.read()

print(f"Contract address: {info_address}")
contract_address = Web3.toChecksumAddress(info_address)

with open("../blockchain/build/contracts/SocialNetwork.json", 'r', encoding='utf-8') as abi:
    info_json = json.load(abi)
contract_abi = info_json["abi"]

socialNetwork_contract = w3.eth.contract(address=contract_address, abi=contract_abi)
event_filter = socialNetwork_contract.events.sendMessageEvent.createFilter(fromBlock=0, toBlock='latest', argument_filters={'_user2': 4})
while True:
    for event in event_filter.get_new_entries():
        print(event)

