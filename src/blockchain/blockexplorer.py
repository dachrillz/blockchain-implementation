# This file contains everything related to retrieving information from the blockchain


def retrieve_all_unspent_transactions_from_transaction_hash(block_chain):
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


def retrieve_all_unspent_transactions_from_public_key(block_chain, public_key):
    ut = retrieve_all_unspent_transactions_from_transaction_hash(block_chain)

    _value = 0
    for block in block_chain.block_chain:
            for transaction in block.transactions:
                if (transaction.__hash__() in ut):
                    for o in transaction.list_of_outputs:
                        if o.scriptPubKey == public_key:
                            _value += o.value
    return _value


def pretty_print_blockchain(blockchain):
    for block in blockchain.block_chain:
        print(block.as_string())
        for transaction in block.transactions:
            print("\t" + transaction.as_string())


def pretty_print_unspent_transactions(map_of_unspent):
    for key in map_of_unspent:
        print(str(key) + ": " + str(map_of_unspent[key]))
