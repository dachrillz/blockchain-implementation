from unittest import TestCase

from src.blockchain.transaction import *
from src.scriptmachine.scriptmachine import *


class TestTransaction(TestCase):
    def setUp(self):
        self.private_key = "5KZgGoqV1XCxx25m6ZiPKnGzzZvAwiA9jDSV82rBYGfYSHJMHMc"
        self.public_key = "04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4"
        self.bitcoin_address = "1HJvgcUKcbBqgd82iPKBqVm8RRY2yKdkVv"

        self.private_key_2 = "5JbqToF5EVeKerd6ankEZPshx2Q7cDo4fQesVLD9BATaWvyXkgD"
        self.public_key_2 = "04538998709970098768f77c151f402498bd1f58b7eb66e03d847810c18a8152b01590af445d06a47c7a506040fcd599f37978fe6d5e3ab2fdfdb6a86e88ea826e"
        self.bitcoin_address_2 = "15J9tU8oRTnGnettS6Y546iTEaTJ2eLKSo"

    def test_construct_transaction(self):
        pass

        # Construct output
        # pay_to_public_key_script(public_key)

        # Construct input

    def test_verify(self):
        pass

    def test_hash_transaction(self):
        script = create_locking_script(self.public_key)

        hash_locking_script(script)

        self.assertTrue(True)

    def test_unlocking_script_fails(self):
        the_script = create_unlocking_script("hej", self.public_key)

        script_machine = ScriptMachine()

        script_machine.set_code(the_script)

        script_machine.run()

        print("did the verification succeed?")
        print(script_machine.execution_successful)

        self.assertFalse(script_machine.execution_successful)

    def test_unlocking_script_succeeds(self):
        the_script = create_unlocking_script("hej", self.public_key)

        script_machine = ScriptMachine()

        script_machine.set_code(the_script)

        script_machine.run()

        print("did the verification succeed?")
        print(script_machine.execution_successful)

        self.assertTrue(script_machine.execution_successful)


class Transaction:
    """
    A Bitcoin transaction
    """

    def __init__(self, list_of_inputs, list_of_outputs):
        self.version = 1

        self.list_of_inputs = list_of_inputs

        self.list_of_outputs = list_of_outputs


class Input:

    def __init__(self, previous_tx, index, script_sig):
        self.previous_tx = previous_tx
        self.index = index
        self.scriptSig = script_sig


class Output:

    def __init__(self, value, script_pub_key):
        self.value = value
        self.scriptPubKey = script_pub_key
