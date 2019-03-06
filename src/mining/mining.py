# This file contains the hash cash mining algorithm
import os


def hash_cash(block):
    """

    :param block: You know what kind of block this is!
    :return: The string that solves the proof of work problem
    """

    guess = b'\0'

    while not proof_of_work_solved(block):
        block.nonce = guess
        guess = os.urandom(32)
    return guess


def proof_of_work_solved(block):
    solution = block.get_hash().encode()
    difficulty = block.difficulty_target
    return len(str(solution)) <= 78 - difficulty # Since I represent the hash with an integer, 78 is the length of a sha256 as integer.


