"""
@TODO: Everything in this file should be hard coded later!
"""
from src.blockchain.blockchain import BlockChain
from src.blockchain.block import Block
from src.blockchain.transaction import create_complete_transaction
from src.database.databaseinterface import TestDataBase

from src.mining.blockminter import proof_of_work

# @TODO: this transaction is not verified via the script machine yet!

# Create blockchain
block_chain = BlockChain()

_public_key1 = "04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4"
_private_key1 = '5KZgGoqV1XCxx25m6ZiPKnGzzZvAwiA9jDSV82rBYGfYSHJMHMc'
_public_key2 = "04538998709970098768f77c151f402498bd1f58b7eb66e03d847810c18a8152b01590af445d06a47c7a506040fcd599f37978fe6d5e3ab2fdfdb6a86e88ea826e"

# First Block
_prev_hash = block_chain.get_last_block().get_hash()
_transactions = []

block1 = proof_of_work(_prev_hash, _transactions, _public_key1)
block_chain.add_new_block(block1)

# Second Block, create a transaction
prev_tx = block_chain.get_last_block().transactions[0].__hash__()
index = 0
value = 10
_input = [(prev_tx, index, _private_key1)]
_output = [(value,_public_key1)]
_transactions =[create_complete_transaction(_input, _output)]

# construct the block
_prev_hash = block_chain.get_last_block().get_hash()
block2 = proof_of_work(_prev_hash, _transactions, _public_key1)
block_chain.add_new_block(block2)

# Third Block
_version = 1
_prev_hash = block_chain.get_last_block().get_hash()
_timestamp = "101010"
_difficulty_target = 1
_nonce = "10"
_transactions = []

block3 = proof_of_work(_prev_hash, _transactions, _public_key1)
block_chain.add_new_block(block3)

# Fourth Block
_prev_hash = block_chain.get_last_block().get_hash()
_transactions = []

block4 = proof_of_work(_prev_hash, _transactions, _public_key1)
block_chain.add_new_block(block4)


# Writes blockchain data to database! :D
a = TestDataBase(block_chain)



def get_dummy_chain():
    return block_chain


