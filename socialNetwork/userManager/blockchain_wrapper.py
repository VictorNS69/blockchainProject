import json
from requests.exceptions import ConnectionError
from web3 import Web3, HTTPProvider


class BlockchainWrapper:
    def __init__(self):
        try:
            self.w3 = Web3(HTTPProvider("http://127.0.0.1:8545"))
            self.w3.eth.defaultAccount = self.w3.eth.accounts[0]
        except ConnectionError:
            raise ConnectionError("Connection error")
        try:
            with open("../blockchain/build/contracts/SocialNetwork-address", 'r', encoding='utf-8') as f:
                info_address = f.read()
        except IOError:
            raise IOError("Error reading contract address")
        contract_address = Web3.toChecksumAddress(info_address)
        try:
            with open("../blockchain/build/contracts/SocialNetwork.json", 'r', encoding='utf-8') as abi:
                info_json = json.load(abi)
        except IOError:
            raise IOError("Error reading contract ABI")
        contract_abi = info_json["abi"]
        self.socialNetwork_contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)

    def add_user(self, user_id):
        assert user_id >= 0
        try:
            tx_hash = self.socialNetwork_contract.functions.addUser(user_id).transact()
            return self.w3.eth.waitForTransactionReceipt(tx_hash)
        except ValueError:
            raise ValueError("User already exists")

