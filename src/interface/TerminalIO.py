from src.blockchain.transaction import create_complete_transaction
from src.interface.IIO import IIO


class TerminalIO(IIO):
    def create_transaction(self):
        print("Create a transactions manually")

        prev_tx = input("Previous transaction hash")
        index = input("Transaction Index (The specific output referenced)")

        value = input("Value to transact")

        private_key = input("Please input private key for address.")
        public_key = input("Please input public key for address.")

        return create_complete_transaction(prev_tx, index, value, private_key, public_key)
