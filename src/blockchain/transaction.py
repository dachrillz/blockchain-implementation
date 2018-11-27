from src.scriptmachine.constants import *
from src.scriptmachine.cryptography import get_hash_160_from_str, get_sha_256_from_str


class Transaction:
    """
    A Bitcoin transaction
    """

    def __init__(self, list_of_inputs, list_of_outputs):
        self.version = 1

        self.list_of_inputs = list_of_inputs

        self.list_of_outputs = list_of_outputs


class Input:

    def __init__(self, txid, index, script_sig):
        self.txid = txid
        self.index = index
        self.scriptSig = script_sig


class Output:

    def __init__(self, value, script_pub_key):
        self.value = value
        self.scriptPubKey = script_pub_key


def verify_script(output_transaction, input_transaction):
    pass


def create_locking_script(public_key):
    hashed_public_key_as_str = get_hash_160_from_str(public_key)

    script = [OP_DUP,
              OP_HASH160,
              OP_DATA,
              hashed_public_key_as_str,
              OP_EQUALVERIFY,
              OP_CHECKSIG
              ]

    return script


def hash_locking_script(script):
    """
    :param script:
    :return:

    Note here, in the real bitcoin transacitons are serialized.
    Here I simply take the script in its' Python form and hash the string of that.

    @TODO: Do we need to sign the whole transaction or just the script?
    """

    serialized = ''.join(str(x) for x in script)

    res = get_sha_256_from_str(serialized)
    res = get_sha_256_from_str(str(res))

    return res


def sign_locking_script(private_key, script):



def create_unlocking_script(signature_of_locking_script, public_key):
    script = [OP_DATA,
              signature_of_locking_script,
              OP_DATA,
              public_key]

    script_tail = create_locking_script(public_key)

    script += script_tail

    return script
