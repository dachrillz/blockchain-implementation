# This is the main file used for running a full node/miner/client for the bitcoin prototype implementation


# @TODO: this one simply works locally for now but should connect to a network later to sync its state.
from src.blockchain.genesis_block import get_genesis
from src.mining.blockminter import proof_of_work
from collections import deque


from src.interface.TerminalIO import TerminalIO

if __name__ == "__main__":
    # Create genesis block
    genesis_block = get_genesis()

    block_chain = deque()
    block_chain.append(genesis_block)

    #Set the interface
    interface = TerminalIO()

    while True:
        # @TODO: change later, but for now simply create a chain of blocks

        # Get latest block, calculate hash and append to chain
        latest_block = block_chain[-1]

        prev_hash = latest_block.get_hash()
        difficulty = latest_block.difficulty_target

        #Get transactions from mempool
        transactions = interface.create_transaction()

        solution, new_block = proof_of_work(prev_hash, difficulty, transactions)

        # @TODO: calculate integrity of blockchain here
        block_chain.append(new_block)


        #Calculate all outspent transactions and assign public addresses to them
        #@TODO: break out this function!
        available_outputs = {}
        for block in block_chain:
            for transaction in block.transactions:
                for output in transaction.list_of_outputs:
                    if output.scriptPubKey in available_outputs:
                        available_outputs[output.scriptPubKey] += output.value
                    else:
                        available_outputs[output.scriptPubKey] = output.value

        print()
        print("The blockchain")
        print("Blockchain length " + str(len(block_chain)))
        for item in block_chain:
            print(item.as_string())


        print()
        print("All available outputs!")
        print(available_outputs)

