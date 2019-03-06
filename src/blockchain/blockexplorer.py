# This file contains everything related to retrieving information from the blockchain


def retrieve_all_unspent_transactions(block_chain):
    # @TODO: you should really write more tests for this function as it could be buggy as hell...
    available_outputs = {}
    for block in block_chain.block_chain:
        for transaction in block.transactions:
            _value = 0
            for _output in transaction.list_of_outputs:
                _value += _output.value

            for _input in transaction.list_of_inputs:
                # @TODO: handle key error here!
                del available_outputs[_input.txid]

            available_outputs[transaction.__hash__()] = _value
    return available_outputs

"""
def retrieve_all_unspent_transactons(block_chain):
    # Calculate all outspent transactions and assign public addresses to them
    available_outputs = {}
    spent_outputs = set()
    for block in block_chain.block_chain:
        for transaction in block.transactions:
            for output in transaction.list_of_outputs:
                if output.scriptPubKey in available_outputs:
                    available_outputs[output.scriptPubKey] += output.value
                else:
                    available_outputs[output.scriptPubKey] = output.value
"""




def pretty_print_blockchain(blockchain):
    for block in blockchain.block_chain:
        print(block.as_string())
        for transaction in block.transactions:
            print("\t" + transaction.as_string())


def pretty_print_unspent_transactions(map_of_unspent):
    for key in map_of_unspent:
        print(str(key) + ": " + str(map_of_unspent[key]))
