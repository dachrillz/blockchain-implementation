# This file contains everything related to retrieving information from the blockchain
import pprint as pp

from src.blockchain import transaction


def retrieve_all_unspent_transactons(block_chain):
    # Calculate all outspent transactions and assign public addresses to them
    available_outputs = {}
    unvalid_outputs = {}  # Do we want this here?
    for block in block_chain:
        for transaction in block.transactions:
            for output in transaction.list_of_outputs:
                if output.validate():
                    if output.scriptPubKey in available_outputs:
                        available_outputs[output.scriptPubKey] += output.value
                    else:
                        available_outputs[output.scriptPubKey] = output.value
                else:
                    print("Found unvalid output - move this to log later")
                    print(output)


def pretty_print_blockchain(blockchain):
    for block in blockchain.block_chain:
        print(block.as_string())
        for transaction in block.transactions:
            print("\t" + transaction.as_string())
