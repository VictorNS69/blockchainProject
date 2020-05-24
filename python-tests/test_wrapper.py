import json
from requests.exceptions import ConnectionError
from web3 import Web3, HTTPProvider

NODE_URL = "http://127.0.0.1:8545"


class BlockchainWrapper:
    def __init__(self):
        try:
            self.__w3 = Web3(HTTPProvider(NODE_URL))
            self.__w3.eth.defaultAccount = self.__w3.eth.accounts[0]
        except ConnectionError:
            raise ConnectionError("Connection error")

        try:
            with open("../blockchain/build/contracts/SocialNetwork-address", 'r', encoding='utf-8') as f:
                info_address = f.read()
        except IOError:
            raise IOError("Error reading contract address")

        self.__contract_address = Web3.toChecksumAddress(info_address)
        try:
            with open("../blockchain/build/contracts/SocialNetwork.json", 'r', encoding='utf-8') as abi:
                info_json = json.load(abi)
        except IOError:
            raise IOError("Error reading contract ABI")

        self.__contract_abi = info_json["abi"]
        self.__socialNetwork_contract = self.__w3.eth.contract(address=self.__contract_address, abi=self.__contract_abi)

    def add_user(self, user_id):
        try:
            tx_hash = self.__socialNetwork_contract.functions.addUser(user_id).transact()
            self.__w3.eth.waitForTransactionReceipt(tx_hash)
            addUserEvent_filter = self.__socialNetwork_contract.events.addUserEvent.createFilter(fromBlock=0,
                                                                                  argument_filters={'_user': user_id})
            # Todos los eventos
            event_list = addUserEvent_filter.get_all_entries()
            # Escucha de evento filtrando
            for element in event_list:
                print(f"{element['args']['_user']}")
            return element['args']['_user']

        except ValueError:
            raise ValueError("User already exists in the SC")

    def get_contract_address(self):
        return self.__contract_address

    def get_contract_abi(self):
        return self.__contract_abi

    def get_user_bytes(self, username):
        tx_hash = self.__socialNetwork_contract.functions.getBytes(username).call()
        return '0x' + tx_hash.hex()

    @staticmethod
    def get_node_url():
        return NODE_URL

if __name__ == "__main__":
    print("--- Main ---")
    wrapper = BlockchainWrapper()
    print(f"Contract address: {wrapper.get_contract_address()}")
    papi = wrapper.get_user_bytes("papi")
    print(f"User {papi} length {len(papi)}")
    victor = wrapper.get_user_bytes("VictorNS69")
    print(f"User {victor} length {len(victor)}")
    rand = wrapper.get_user_bytes("qerqwerweqtroqwertusofndsmvncxcz,mvnxzvajhfdaoirfuqworuqwiofhasodhfnakjsvbakjsdvbnxzc,vbzxnvb122313")
    print(f"User {rand} length {len(rand)}")