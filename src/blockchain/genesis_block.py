import datetime

from src.blockchain.block import Block

#@TODO: reformat this file!
version = 1
prev_hash = b"Let's go!" #genesis hash
merkle_root = None #@TODO: what is genesis merkle root?
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #@TODO: make a module for this
difficulty_target = 0
nonce = 0
genesis_block = Block(version, prev_hash, merkle_root, timestamp, difficulty_target, nonce, transactions=[])


def get_genesis():
    return genesis_block
