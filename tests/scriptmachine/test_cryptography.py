import unittest

import src.scriptmachine.cryptography

from src.scriptmachine.scriptmachine import ScriptMachine


class TestCryptography(unittest.TestCase):

    def setUp(self):
        self.script_machine = ScriptMachine()


    def test_remove_later(self):
        self.assertEqual(1, 2)

