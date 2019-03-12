import json

from src.blockchain.blockchain import BlockChain
from src.blockchain.transaction import create_complete_transaction
from src.mining.blockminter import proof_of_work


def serialize_block_to_json(block):
    json_instance = {}

    """
    version = version
    prev_hash = prev_hash  # hash of previous block
    merkle_root = merkle_root  # @TODO: not sure if needed in prototype
    timestamp = timestamp
    difficulty_target = difficulty_target
    nonce = nonce
    """
    json_instance['block_header'] = {
        'version': block.version,
        'prev_hash': block.prev_hash,
        'merkle_root': block.merkle_root,
        'timestamp': block.timestamp,
        'difficulty_target': block.difficulty_target,
        'nonce': block.nonce,
    }

    json_instance['transactions'] = []

    for transaction in block.transactions:

        list_of_outputs = []
        for output in transaction.list_of_outputs:
            list_of_outputs.append(
                {'value': output.value,
                 'pubKey': output.scriptPubKey,
                 }
            )

        list_of_inputs = []
        for _input in transaction.list_of_inputs:
            list_of_inputs.append(
                {'txid': _input.txid,
                 'index': _input.index,
                 'scriptSig': _input.scriptSig
                 }
            )

        json_instance['transactions'].append({
            'list_of_inputs': list_of_inputs,
            'list_of_outputs': list_of_outputs,
            'version': transaction.version,
            'nonce': transaction.nonce
        }

        )

    return json.dumps(json_instance)


def convert_json_to_python(json_object):
    return json.loads(json_object)


if __name__ == '__main__':
    # @TODO: remove later!

    # Create blockchain
    block_chain = BlockChain()

    _public_key1 = "04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4"
    _private_key1 = '5KZgGoqV1XCxx25m6ZiPKnGzzZvAwiA9jDSV82rBYGfYSHJMHMc'
    _public_key2 = "04538998709970098768f77c151f402498bd1f58b7eb66e03d847810c18a8152b01590af445d06a47c7a506040fcd599f37978fe6d5e3ab2fdfdb6a86e88ea826e"
    _public_key3 = "04960caeb243844e44c906469195c2086e099a335684273c2eb61ef3c829e50f75ac57ecb31eec69e74db569501f3daab9c9cdaa27e95a6484249ce43b7f26454b"

    # First Block
    _prev_hash = block_chain.get_last_block().get_hash()
    _transactions = []

    block1 = proof_of_work(_prev_hash, _transactions, _public_key1)
    block_chain.add_new_block(block1)

    # Input
    prev_tx1 = block_chain.block_chain[1].transactions[0].__hash__()
    index1 = 0
    private_key1 = _private_key1

    #Multiple Output
    value1 = 5
    value2 = 5

    _inputs = [(prev_tx1, index1, private_key1)]
    _outputs = [(value1, _public_key2), (value2, _public_key3)]

    _transactions = [create_complete_transaction(_inputs, _outputs)]

    # Second Block
    _prev_hash = block_chain.get_last_block().get_hash()
    block2 = proof_of_work(_prev_hash, _transactions, _public_key1)
    block_chain.add_new_block(block2)

    a = serialize_block_to_json(block_chain.block_chain[-1])

    b = convert_json_to_python(a)

    print(a)

