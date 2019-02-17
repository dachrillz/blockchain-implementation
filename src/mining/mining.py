# This file contains the hash cash mining algorithm
from src.cryptography.cryptography import get_sha_256_from_str, get_sha_256_from_bytes
import os


def hash_cash(difficulty, state):
    """

    :param difficulty: Number of leading zeroes required
    :param state: A string representation of the state of the previous block
    :return: The string that solves the proof of work problem
    """

    guess = b'\0'
    state = state.encode()

    solution = get_sha_256_from_bytes(state + guess)

    while not problem_solved(difficulty, solution):
        solution = get_sha_256_from_bytes(state + guess)
        guess = os.urandom(32)

    print("found solution")

    check_solution(difficulty, solution, state)


def problem_solved(difficulty, solution):
    """
    Check if the string solution solves the hash cash problem, as defined by difficulty
    :param difficulty:
    :param solution:
    :return: true if solved
    """
    s = solution[:difficulty]
    return s == len(s) * b'\0'


def check_solution(difficulty, solution, state):
    print(difficulty)
    print(get_sha_256_from_bytes(state + solution))
