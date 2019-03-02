from src.blockchain.transaction import create_complete_transaction
from src.interface.IIO import IIO


class TerminalIO(IIO):

    def create_transaction(self):
        print("Create a transactions manually")


        prev_tx = input("Previous transaction hash ")
        if prev_tx == "first":
            prev_tx = 0
            index = 0
            value = 10
            private_key = "5KZgGoqV1XCxx25m6ZiPKnGzzZvAwiA9jDSV82rBYGfYSHJMHMc"
            public_key = "04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4"
        elif prev_tx == "second":
            prev_tx = 0
            index = 0
            value = 10
            private_key = "5KZgGoqV1XCxx25m6ZiPKnGzzZvAwiA9jDSV82rBYGfYSHJMHMc"
            public_key = "04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4"
        else: #@TODO: remove later this is for testing only
            index = input("Transaction Index (The specific output referenced) ")
            value = input("Value to transact ")
            private_key = input("Please input private key for address. ")
            public_key = input("Please input public key for address. ")
        return [create_complete_transaction(prev_tx, index, value, private_key, public_key)]
