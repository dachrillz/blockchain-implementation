
from src.blockchain.blockchain import BlockChain
from src.blockchain.block import Block

# Create blockchain

block_chain = BlockChain()


# First Block
_version = 1
_prev_hash = block_chain.get_last_block().get_hash()
_merkle_root = None
_timestamp = "101010"
_difficulty_target = 1
_nonce = "10"
_transactions = []

block1 = Block(_version, _prev_hash, _merkle_root, _timestamp, _difficulty_target, _nonce, _transactions)
block_chain.add_new_block(block1)

# Second Block
_version = 1
_prev_hash = block_chain.get_last_block().get_hash()
_merkle_root = None
_timestamp = "101010"
_difficulty_target = 1
_nonce = "10"
_transactions = []

block2 = Block(_version, _prev_hash, _merkle_root, _timestamp, _difficulty_target, _nonce, _transactions)
block_chain.add_new_block(block2)

# Third Block
_version = 1
_prev_hash = block_chain.get_last_block().get_hash()
_merkle_root = None
_timestamp = "101010"
_difficulty_target = 1
_nonce = "10"
_transactions = []

block3 = Block(_version, _prev_hash, _merkle_root, _timestamp, _difficulty_target, _nonce, _transactions)
block_chain.add_new_block(block3)

# Fourth Block
_version = 1
_prev_hash = block_chain.get_last_block().get_hash()
_merkle_root = None
_timestamp = "101010"
_difficulty_target = 1
_nonce = "10"
_transactions = []

block4 = Block(_version, _prev_hash, _merkle_root, _timestamp, _difficulty_target, _nonce, _transactions)
block_chain.add_new_block(block4)


assert(block_chain.validate_block_chain(), "Dummy Chain is invalid!")
