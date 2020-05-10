import json
from requests.exceptions import ConnectionError
from web3 import Web3, HTTPProvider


NODE_URL = "http://127.0.0.1:8545"

class BlockchainWrapper:
    def __init__(self):
        try:
            self._w3 = Web3(HTTPProvider(NODE_URL))
            self._w3.eth.defaultAccount = self._w3.eth.accounts[0]
        except ConnectionError:
            raise ConnectionError("Connection error")

        try:
            with open("../blockchain/build/contracts/SocialNetwork-address", 'r', encoding='utf-8') as f:
                info_address = f.read()
        except IOError:
            raise IOError("Error reading contract address")

        self._contract_address = Web3.toChecksumAddress(info_address)
        try:
            with open("../blockchain/build/contracts/SocialNetwork.json", 'r', encoding='utf-8') as abi:
                info_json = json.load(abi)
        except IOError:
            raise IOError("Error reading contract ABI")

        self._contract_abi = info_json["abi"]
        self._socialNetwork_contract = self._w3.eth.contract(address=self._contract_address, abi=self._contract_abi)

    def add_user(self, user_id):
        assert user_id >= 0
        try:
            tx_hash = self._socialNetwork_contract.functions.addUser(user_id).transact()
            return self._w3.eth.waitForTransactionReceipt(tx_hash)
        except ValueError:
            raise ValueError("User already exists in the SC")

    def get_contract_address(self):
        return self._contract_address

    def get_contract_abi(self):
        return self._contract_abi

    @staticmethod
    def get_node_url():
        return NODE_URL
