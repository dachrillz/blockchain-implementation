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
        self.assertFalse(self.script_machine.execution_successful)

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

    ##############################################
    # Test Conditional Flow Control
    #############################################

    def test_op_nop(self):
        code = [OP_NOP]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_ver_success(self):
        code = [OP_2,OP_1,OP_0,OP_IF,OP_VER,OP_ENDIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_ver_fail(self):
        code = [OP_2,OP_1,OP_IF,OP_VER,OP_ENDIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertFalse(self.script_machine.execution_successful)

    def test_op_if_go(self):
        code = [OP_2,OP_1,OP_IF,OP_1,OP_ENDIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertequal(0x1, self.script_machine.pop())
        self.assertequal(0x2, self.script_machine.pop())

        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_if_go_by(self):
        code = [OP_2,OP_0,OP_IF,OP_1,OP_ENDIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertequal(0x2, self.script_machine.pop())

        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_notif_go(self):
        code = [OP_0,OP_NOTIF,OP_1,OP_ENDIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertequal(0x1, self.script_machine.pop())

        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_notif_go(self):
        code = [OP_1,OP_NOTIF,OP_1,OP_ENDIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_verif(self):
        code = [OP_VERIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertFalse(self.script_machine.execution_successful)

    def test_op_vernotif(self):
        code = [OP_VERNOTIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertFalse(self.script_machine.execution_successful)

    def test_op_else_go(self):
        code = [OP_1, OP_IF, OP_2, OP_ELSE, OP_3, OP_ENDIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)


    def test_op_else_go(self):
        code = [OP_0, OP_IF, OP_2, OP_ELSE, OP_3, OP_ENDIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_verify_success(self):
        code = [OP_1, OP_2, OP_VERIFY]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_verify_success(self):
        code = [OP_1, OP_2, OP_0, OP_VERIFY]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertFalse(self.script_machine.execution_successful)

    def test_op_return(self):
        code = [OP_1, OP_2, OP_RETURN]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertFalse(self.script_machine.execution_successful)

if __name__ == '__main__':
    unittest.main()
