from src.scriptmachine.constants import *
from src.scriptmachine.scriptmachine import ScriptMachine

a = ScriptMachine()

code = [OP_1, OP_IF, OP_2, OP_ELSE, OP_3, OP_ENDIF]

a.set_code(code)
print(a.code)
a.run()



print(a.data_stack)

