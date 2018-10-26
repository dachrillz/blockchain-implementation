import unittest

from src.scriptmachine.scriptmachine import ScriptMachine
from src.scriptmachine.constants import *


class TestBasicStackOperations(unittest.TestCase):

    def setUp(self):
        self.script_machine = ScriptMachine()

    def test_can_push_false_to_stack(self):
        code = [0x00]
        self.script_machine.set_code(code)

        self.script_machine.run()

        self.assertEqual(0, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_simple_add_and_equal(self):
        code = [OP_2, OP_3, OP_ADD, OP_5, OP_NUMEQUAL]

        self.script_machine.set_code(code)

        self.script_machine.run()

        self.assertEqual(0x01, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_push_all_small_numbers_onto_stack(self):
        code = [OP_2,OP_3,OP_4,OP_5,OP_6,OP_7,OP_8,OP_9,OP_10,OP_11,OP_12,OP_13,OP_14,OP_15,OP_16]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x10, self.script_machine.pop())
        self.assertEqual(0x0f, self.script_machine.pop())
        self.assertEqual(0x0e, self.script_machine.pop())
        self.assertEqual(0x0d, self.script_machine.pop())
        self.assertEqual(0x0c, self.script_machine.pop())
        self.assertEqual(0x0b, self.script_machine.pop())
        self.assertEqual(0x0a, self.script_machine.pop())
        self.assertEqual(0x09, self.script_machine.pop())
        self.assertEqual(0x08, self.script_machine.pop())
        self.assertEqual(0x07, self.script_machine.pop())
        self.assertEqual(0x06, self.script_machine.pop())
        self.assertEqual(0x05, self.script_machine.pop())
        self.assertEqual(0x04, self.script_machine.pop())
        self.assertEqual(0x03, self.script_machine.pop())
        self.assertEqual(0x02, self.script_machine.pop())

        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_negative_push(self):
        code = [OP_1NEGATE]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(-0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

if __name__ == '__main__':
    unittest.main()
