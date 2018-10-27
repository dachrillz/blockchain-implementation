from src.scriptmachine.constants import *
from src.scriptmachine.scriptmachine import ScriptMachine

a = ScriptMachine()

code = [OP_1, OP_2, OP_3, OP_5, OP_2, OP_ROT, OP_4, OP_10]

a.set_code(code)
print(a.code)
a.run()



print(a.data_stack)

