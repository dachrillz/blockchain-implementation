import datetime

from src.blockchain.block import Block
from src.blockchain.transaction import Output, Transaction
from src.mining.mining import hash_cash

# @TODO: higly temporary, move to other file really soon!
_coinbase_amount = 10


def mint_block(prev_hash, transactions, solution, public_key):
    version = 1  # @TODO: move to some config file
    merkle_root = None  # @TODO: generalise
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # @TODO: make a module for this

    # Add coinbase transaction to queried transactions.
    transactions = [Transaction([], [Output(_coinbase_amount, public_key)])] + transactions

    difficulty_target = 1  # @TODO: this has to be requested / calculated later
    nonce = solution

    return Block(version, prev_hash, merkle_root, timestamp, difficulty_target, nonce, transactions)


def proof_of_work(prev_hash, transactions, public_key):

    solution = 0 # Dummy solution
    block = mint_block(prev_hash, transactions, solution, public_key)
    hash_cash(block)
    return block
