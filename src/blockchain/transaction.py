from src.cryptography.signature import create_signature
from src.scriptmachine.constants import *

from src.cryptography.cryptography import get_hash_160_from_str, get_sha_256_from_str, get_sha_256_from_bytes

_version = 1


def create_complete_transaction(prev_tx, index, value, private_key, public_key):
    '''
    @TODO: Currently only handles single input/output change this later!

    :param prev_tx: Reference
    :param index:
    :param value:
    :param private_key:
    :param public_key:
    :return:
    '''
    locking_script = create_locking_script(public_key)
    signature = sign_hashed_locking_script(private_key, hash_locking_script(locking_script))

    #@TODO: change these names to something better
    _input = [Input(prev_tx, index, signature)]
    _output = [Output(value, public_key)]

    return Transaction(_input, _output)


class Transaction:
    """
    A Bitcoin transaction
    """

    def __init__(self, list_of_inputs, list_of_outputs):
        self.version = _version

        self.list_of_inputs = list_of_inputs

        self.list_of_outputs = list_of_outputs

    def as_string(self):
        return "Transaction: version: " + str(self.version) + " inputs: " + str(self.list_of_inputs) + " outputs: " + str(
            self.list_of_outputs)

    def __hash__(self):

        string_to_hash = str(self.version)

        for item in self.list_of_inputs:
            string_to_hash += item.txid + item.index + item.scriptSig

        for item in self.list_of_outputs:
            string_to_hash += str(item.value) + str(item.scriptPubKey)

        return get_sha_256_from_bytes(get_sha_256_from_bytes(string_to_hash.encode()))


class Input:

    def __init__(self, txid, index, script_sig):
        """
        :param txid: A reference (double sha256 as string) to the transaction
        :param index: Points to which output in the referenced transactoin
        :param script_sig: #signature for the unlocking script to prove ownership
        """
        self.txid = txid
        self.index = index
        self.scriptSig = script_sig


class Output:

    def __init__(self, value, script_pub_key):
        """
        :param value: The amount to be transacted
        :param script_pub_key: The address to be transacted to
        """
        self.value = value
        self.scriptPubKey = script_pub_key


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

    @TODO: Change this to the whole transaction later !
    """

    serialized = ''.join(str(x) for x in script).encode()

    res = get_sha_256_from_bytes(get_sha_256_from_bytes(serialized))
    return str(int.from_bytes(res, byteorder='big'))


def sign_hashed_locking_script(private_key, hashed_locking_script):
    # @TODO: Change this to the whole transaction later !
    signature = create_signature(private_key, hashed_locking_script)
    return signature


def create_unlocking_script(signature_of_locking_script, public_key):
    script = [OP_DATA,
              signature_of_locking_script,
              OP_DATA,
              public_key]

    script_tail = create_locking_script(public_key)

    script += script_tail

    return script
