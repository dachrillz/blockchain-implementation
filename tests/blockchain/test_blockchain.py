from unittest import TestCase

from src.blockchain.blockchain import BlockChain
from src.mining.blockminter import proof_of_work


class TestBlockChain(TestCase):

    def test_validate_blockchain(self):
        bc = BlockChain()

        genesis_block = bc.get_last_block()

        block1 = proof_of_work(prev_hash=genesis_block.get_hash(), transactions=[],public_key="")
        block2 = proof_of_work(prev_hash=block1.get_hash(), transactions=[],public_key="")

        bc.add_new_block(block1)
        bc.add_new_block(block2)

        self.assertTrue(bc.validate_block_chain())

    def test_invalid_blockchain(self):
        bc = BlockChain()

        genesis_block = bc.get_last_block()

        block1 = proof_of_work(prev_hash=genesis_block.get_hash(), transactions=[],public_key="")
        block2 = proof_of_work(prev_hash="invalid hash", transactions=[],public_key="")

        bc.add_new_block(block1)
        bc.add_new_block(block2)

        self.assertFalse(bc.validate_block_chain())
