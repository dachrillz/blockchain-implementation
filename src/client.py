#This is the main file used for running a full node/miner/client for the bitcoin prototype implementation


#@TODO: this one simply works locally for now but should connect to a network later to sync its state.
from src.blockchain.block import Block
from src.blockchain.genesis_block import get_genesis
from collections import deque
import datetime

if __name__ == "__main__":
    #Create genesisblock
    genesis_block = get_genesis()

    block_chain = deque()
    block_chain.append(genesis_block)


    while True:
        #@TODO: change later, but for now simply create a chain of blocks

        #Get latest block, calculate hash and append to chain
        latest_block = block_chain[-1]


        prev_hash = latest_block.get_hash()
        version = 1 #@TODO: move to some config file
        merkle_root = None #@TODO: generalise
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #@TODO: make a module for this

        difficulty_target = 1.0 #@TODO: this has to be requested / calculated later
        nonce = 1 #@TODO: how to calculate nonce?

        transactions = [] #@TODO: append collected transactions requests here!


        new_block = Block(version, prev_hash, merkle_root, timestamp, difficulty_target, nonce, transactions)


        #@TODO: calculate integrity of blockchain here
        block_chain.append(new_block)

        print(latest_block.as_string())
        input()




