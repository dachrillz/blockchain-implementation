# This is the main file used for running a full node/miner/client for the bitcoin prototype implementation


# @TODO: this one simply works locally for now but should connect to a network later to sync its state.
from src.blockchain.blockchain import BlockChain
from src.blockchain.blockexplorer import pretty_print_blockchain
from src.blockchain.mempool import MemPool
import src.blockchain.dummychain
from src.mining.blockminter import proof_of_work


from src.interface.TerminalIO import TerminalIO

if __name__ == "__main__":

    # Create the blockchain
    block_chain = BlockChain()

    mem_pool = MemPool()

    # Set the interface
    interface = TerminalIO()

    while True:
        # @TODO: all of these things should later be handled by different threads!

        latest_block = block_chain.get_last_block()
        prev_hash = latest_block.get_hash()
        difficulty = latest_block.difficulty_target

        #Add transactions to mempool
        transactions = interface.create_transaction()
        for item in transactions:
            mem_pool.add(item)

        # Get transactions from mempool, for now simply pick a couple of random transactions from it.
        transactions = []
        for item in mem_pool.mempool:
            transaction = mem_pool.mempool[item]
            transactions.append(mem_pool.get(transaction))


        print("solving proof of work")
        new_block = proof_of_work(prev_hash, difficulty, transactions)


        print("adding new block")
        block_chain.add_new_block(new_block)

        print("validating blockchain!")
        block_chain.validate_block_chain()

        #available_outputs = block_chain.unspent_transactions()

        print()
        print("The blockchain")
        print("Blockchain length " + str(len(block_chain.block_chain)))
        pretty_print_blockchain(block_chain)


