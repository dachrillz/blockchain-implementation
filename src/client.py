# This is the main file used for running a full node/miner/client for the bitcoin prototype implementation


# @TODO: this one simply works locally for now but should connect to a network later to sync its state.
from src.blockchain.blockchain import BlockChain
from src.blockchain.blockexplorer import pretty_print_blockchain, pretty_print_unspent_transactions, \
    retrieve_all_unspent_transactions
from src.blockchain.mempool import MemPool
from src.blockchain.dummychain import get_dummy_chain
from src.mining.blockminter import proof_of_work

from src.interface.TerminalIO import TerminalIO


def run():
    # Create the blockchain
    block_chain = BlockChain()

    mem_pool = MemPool()

    # Set the interface
    interface = TerminalIO()
    public_key = '04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4'

    while True:
        # @TODO: all of these things should later be handled by different threads!

        latest_block = block_chain.get_last_block()
        prev_hash = latest_block.get_hash()
        difficulty = latest_block.difficulty_target

        # Add transactions to mempool
        transactions = interface.create_transaction()
        for item in transactions:
            mem_pool.add(item)

        # Get transactions from mempool, for now simply pick a couple of random transactions from it.
        transactions = []
        for item in mem_pool.mempool:
            transaction = mem_pool.mempool[item]
            transactions.append(mem_pool.get(transaction))

        print("solving proof of work")
        new_block = proof_of_work(prev_hash, difficulty, transactions, public_key)


        print("adding new block")
        block_chain.add_new_block(new_block)

        print("validating blockchain!")
        block_chain.validate_block_chain()

        print()
        print("The blockchain")
        print("Blockchain length " + str(len(block_chain.block_chain)))
        pretty_print_blockchain(block_chain)

def run_dummy():
    bc = get_dummy_chain()

    print("Blockchain")
    pretty_print_blockchain(bc)

    print("\nunspent transactions")
    un = retrieve_all_unspent_transactions(bc)

    pretty_print_unspent_transactions(un)


if __name__ == "__main__":
    #run()
    run_dummy()



