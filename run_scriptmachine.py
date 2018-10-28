from src.scriptmachine.constants import *
from src.scriptmachine.scriptmachine import ScriptMachine

a = ScriptMachine()

code = [OP_4, OP_8, OP_4, OP_WITHIN]

a.set_code(code)
print(a.code)
a.run()



print(a.data_stack)

