# This file contains the block chain class
from collections import deque

from src.blockchain.difficulty_calculator import calculate_difficulty
from src.blockchain.genesis_block import get_genesis
from src.mining.mining import proof_of_work_solved


class BlockChain:
    def __init__(self):

        self.block_chain = deque()
        # Create genesis block
        genesis_block = get_genesis()
        self.block_chain.append(genesis_block)

        self.reference_to_transactions = {}
        self.unspent_transactions = {}

    def get_last_block(self):
        # Get latest block, calculate hash and append to chain
        return self.block_chain[-1]

    def validate_block_chain(self):
        previous_hash = self.block_chain[0].get_hash()
        k = 0
        for block in self.block_chain:
            if k is not 0:
                if not proof_of_work_solved(block):
                    return False
                if block.prev_hash != previous_hash:
                    return False
            else:
                k = 1
            previous_hash = block.get_hash()
        return True

    def add_new_block(self, new_block):
        # Add a reference to each transaction in dictionary so that they can be easily referenced.
        for transaction in new_block.transactions:
            self._add_reference_to_transactions(transaction.__hash__(), transaction)

        self.block_chain.append(new_block)

    def get_unspent_transactions(self):
        raise NotImplementedError
        # return self.unspent_transactions

    def _add_reference_to_transactions(self, tx, transaction):
        '''
        @TODO:
        Note, how sure am I that the tx hash is gonna be unique?
        It is unlikely that there would be a collision, but it is possible
        There should be some way to handle this!
        :param tx:
        :param input_class:
        :return:
        '''

        self.reference_to_transactions[tx] = transaction
