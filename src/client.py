# This is the main file used for running a full node/miner/client for the bitcoin prototype implementation


# @TODO: this one simply works locally for now but should connect to a network later to sync its state.
from src.blockchain.blockchain import BlockChain
from src.blockchain.blockexplorer import retrieve_all_unspent_transactons
from src.blockchain.genesis_block import get_genesis
from src.mining.blockminter import proof_of_work
from collections import deque


from src.interface.TerminalIO import TerminalIO

if __name__ == "__main__":

    #Create the blockchain
    block_chain = BlockChain()

    #Set the interface
    interface = TerminalIO()

    while True:
        # @TODO: change later, but for now simply create a chain of blocks

        latest_block = block_chain.get_last_block()
        prev_hash = latest_block.get_hash()
        difficulty = latest_block.difficulty_target

        #Get transactions from mempool
        transactions = interface.create_transaction()

        solution, new_block = proof_of_work(prev_hash, difficulty, transactions)

        # @TODO: calculate integrity of blockchain here
        block_chain.add_new_block(new_block)

        block_chain.validate_block_chain()

        #available_outputs = block_chain.unspent_transactions()

        print()
        print("The blockchain")
        print("Blockchain length " + str(len(block_chain.block_chain)))
        for item in block_chain.block_chain:
            print(item.as_string())


