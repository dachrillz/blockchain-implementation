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

        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())

        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_if_go_by(self):
        code = [OP_2,OP_0,OP_IF,OP_1,OP_ENDIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x2, self.script_machine.pop())

        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_notif_go(self):
        code = [OP_0,OP_NOTIF,OP_1,OP_ENDIF]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x1, self.script_machine.pop())

        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_notif_go_by(self):
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


    def test_op_else_go_2(self):
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

    def test_op_verify_fail(self):
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

    def test_op_toaltstack(self):
        code = [OP_0, OP_TOALTSTACK, OP_0, OP_1]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x0, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_fromaltstack(self):
        code = [OP_0, OP_TOALTSTACK, OP_0, OP_FROMALTSTACK, OP_1]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x0, self.script_machine.pop())
        self.assertEqual(0x0, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_2drop(self):
        code = [OP_1, OP_2, OP_2DROP, OP_3]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)
    def test_op_2dup(self):
        code = [OP_1, OP_2, OP_2DUP, OP_3]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op3dup(self):
        code = [OP_1, OP_2, OP_3, OP_3DUP, OP_3]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_2over(self):
        code = [OP_1, OP_2, OP_3, OP_4, OP_2OVER, OP_3]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x4, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_2rot(self):
        code = [OP_1, OP_2, OP_3, OP_4, OP_5, OP_6, OP_2ROT, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x6, self.script_machine.pop())
        self.assertEqual(0x5, self.script_machine.pop())
        self.assertEqual(0x4, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_2swap(self):
        code = [OP_1, OP_2, OP_3, OP_4, OP_2SWAP, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x4, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))
        self.assertTrue(self.script_machine.execution_successful)

    def test_op_ifdup_succ(self):
        code = [OP_1, OP_IFDUP, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_ifdup_fail(self):
        code = [OP_0, OP_IFDUP, OP_10]
        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x0, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_depth(self):
        code = [OP_1, OP_2, OP_DEPTH, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_drop(self):
        code = [OP_1, OP_2, OP_DROP, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_dup(self):
        code = [OP_1, OP_2, OP_DUP, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_nip(self):
        code = [OP_1, OP_2, OP_NIP, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()

        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_over(self):
        code = [OP_1, OP_2, OP_OVER, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()
        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_pick(self):
        code = [OP_1, OP_2, OP_3, OP_5, OP_2, OP_PICK, OP_4, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()
        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x4, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x5, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_roll(self):
        code = [OP_1, OP_2, OP_3, OP_5, OP_2, OP_ROLL, OP_4, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()
        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x4, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x5, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_rot(self):
        code = [OP_1, OP_2, OP_3, OP_10, OP_5, OP_2, OP_ROT, OP_4, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()
        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x4, self.script_machine.pop())
        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x5, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_rot_2(self):
        code = [OP_1, OP_2, OP_3, OP_5, OP_2, OP_ROT, OP_4, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()
        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x4, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x5, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_swap(self):
        code = [OP_1, OP_2, OP_3, OP_5, OP_2, OP_SWAP, OP_4, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()
        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x4, self.script_machine.pop())
        self.assertEqual(0x5, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

    def test_op_tuck(self):
        code = [OP_1, OP_2, OP_3, OP_5, OP_2, OP_TUCK, OP_4, OP_10]

        self.script_machine.set_code(code)
        self.script_machine.run()
        self.assertEqual(10, self.script_machine.pop())
        self.assertEqual(0x4, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x5, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x3, self.script_machine.pop())
        self.assertEqual(0x2, self.script_machine.pop())
        self.assertEqual(0x1, self.script_machine.pop())
        self.assertEqual(0, len(self.script_machine.data_stack))

if __name__ == '__main__':
    unittest.main()
