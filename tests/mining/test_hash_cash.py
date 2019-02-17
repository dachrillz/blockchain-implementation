from unittest import TestCase

from src.mining.mining import hash_cash


class TestHash_cash(TestCase):
    #@TODO: make this non random!
    def test_hash_cash(self):

        difficulty = 1
        state = "some state"
        hash_cash(difficulty, state)
