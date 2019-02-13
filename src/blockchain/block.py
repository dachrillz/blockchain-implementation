#This file contains a class that represents a block in the blockchain

from src.cryptography.cryptography import get_sha_256_from_str

class Block:
    def __init__(self, version, prev_hash, merkle_root, timestamp, difficulty_target, nonce, transactions):
        self.version = version
        self.prev_hash = prev_hash #hash of previous block
        self.merkle_root = merkle_root #@TODO: not sure if needed in prototype
        self.timestamp = timestamp
        self.difficulty_target = difficulty_target
        self.nonce = nonce

        self.transactions = transactions


    def get_hash(self):
        string_to_be_hashed = str(self.version)
        string_to_be_hashed += str(int.from_bytes(self.prev_hash, byteorder="little"))
        string_to_be_hashed += str(self.merkle_root)
        string_to_be_hashed += self.timestamp
        string_to_be_hashed += str(self.difficulty_target)
        string_to_be_hashed += str(self.nonce)
        for item in self.transactions:
            string_to_be_hashed += item.as_string()
        ret = get_sha_256_from_str(string_to_be_hashed)
        return ret

    def as_string(self):
        """
        @TODO: expand later
        :return:
        """

        string_to_return = ""

        string_to_return += "version: " + str(self.version)
        string_to_return += " prev_hash: " + str(int.from_bytes(self.prev_hash, byteorder="little"))
        string_to_return += " timestamp: " + self.timestamp
        string_to_return += " difficulty: " + str(self.difficulty_target)
        string_to_return += " Transactions: "
        for item in self.transactions:
            string_to_return += item.as_string()
        return string_to_return


