import datetime

from src.blockchain.block import Block
from src.blockchain.transaction import Output, Transaction
from src.mining.mining import hash_cash

# @TODO: higly temporary, move to other file really soon!
_public_key = "04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4"
_coinbase_amount = 10


def mint_block(prev_hash, transactions, solution):
    version = 1  # @TODO: move to some config file
    merkle_root = None  # @TODO: generalise
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # @TODO: make a module for this

    # Add coinbase transaction to queried transactions.
    transactions = [Transaction([], [Output(_coinbase_amount, _public_key)])] + transactions

    difficulty_target = 1  # @TODO: this has to be requested / calculated later
    nonce = solution

    return Block(version, prev_hash, merkle_root, timestamp, difficulty_target, nonce, transactions)


def proof_of_work(prev_hash, difficulty, transactions):

    solution = 0 # Dummy solution
    block = mint_block(prev_hash, transactions, solution)
    hash_cash(block)
    return block
