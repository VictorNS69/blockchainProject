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

addUserEvent_filter = socialNetwork_contract.events.sendMessageEvent.createFilter(fromBlock=0,
                                                                                  argument_filters={'_user1': 69})
# Todos los eventos
event_list = addUserEvent_filter.get_all_entries()
# Escucha de evento filtrando
for element in event_list:
    print(f"{element['args']['_user1']} said to {element['args']['_user2']}: {element['args']['_message']}")

# Selecciono la cuenta "from"
print(f"Account selected: {w3.eth.accounts[0]}")
w3.eth.defaultAccount = w3.eth.accounts[0]
# Añado un usuario
try:
    try:
        user_id = int(input("Identifier (positive number): "))
        assert user_id >= 0
    except ValueError:
        print("This isn't a valid number")
        exit(1)
    tx_hash = socialNetwork_contract.functions.addUser(user_id).transact()
    # print("The tx is:", tx_hash)
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    # print("The receipt is:", tx_receipt)
    print("User added successfully")
except ValueError:
    print(f"User already in the system")
    exit(1)

exit(0)
