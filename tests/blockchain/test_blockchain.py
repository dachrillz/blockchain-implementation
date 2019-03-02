from unittest import TestCase

from src.blockchain.blockchain import BlockChain
from src.mining.blockminter import mint_block


class TestBlockChain(TestCase):

    def test_validate_blockchain(self):
        bc = BlockChain()

        genesis_block = bc.get_last_block()

        block1 = mint_block(genesis_block.get_hash(), [])

        block2 = mint_block(block1.get_hash(), [])

        bc.add_new_block(block1)
        bc.add_new_block(block2)

        self.assertTrue(bc.validate_block_chain())

    def test_invalid_blockchain(self):
        bc = BlockChain()

        genesis_block = bc.get_last_block()

        block1 = mint_block(genesis_block.get_hash(), [])

        block2 = mint_block("I am an invalid hash", [])

        bc.add_new_block(block1)
        bc.add_new_block(block2)

        self.assertFalse(bc.validate_block_chain())
