from django.test import TestCase
from .blockchain_wrapper import BlockchainWrapper
import json


class BlockchainWrapperTests(TestCase):

    def setUp(self):
        """Set up the wrapper"""
        self.wrapper = BlockchainWrapper()
        self.assertEqual("http://ganache:8545", self.wrapper.get_node_url())

    def test_get_address(self):
        """Get the contract address"""
        try:
            with open("../blockchain/build/contracts/SocialNetwork-address", 'r', encoding='utf-8') as f:
                info_address = f.read()
        except IOError:
            raise IOError("Error reading contract address")

        self.assertEqual(info_address, self.wrapper.get_contract_address())

    def test_get_abi(self):
        """Get the contract abi"""
        try:
            with open("../blockchain/build/contracts/SocialNetwork.json", 'r', encoding='utf-8') as abi:
                info_json = json.load(abi)
        except IOError:
            raise IOError("Error reading contract ABI")

        self.assertEqual(info_json["abi"], self.wrapper.get_contract_abi())

    def test_get_bytes(self):
        """Get user bytes for "user1" """
        self.assertEqual("0xa1c2b8080ed4b6f56211e0295659ef87dd454b0a884198c10384f230525d4ee8",
                         self.wrapper.get_user_bytes("user1"))


