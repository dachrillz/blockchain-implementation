##############################################################
### This file containts the script virtual stack machine.
##############################################################

from . import dispatch_map
from collections import deque

class Stack(deque):
    push = deque.append

    @property
    def top(self):
        if len(self) is 0:
            return 1
        return self[-1]

class ScriptMachine:
    def __init__(self, code=None):
        self.data_stack = Stack()
        self.alternative_stack = Stack()
        self.instruction_pointer = 0
        self.code = code
        self.dispatch_map = dispatch_map.dispatch_map
        self.execution_successful = False
        self.halted = False

    def set_code(self, code):
        self.code = code

    def pop(self):
        """
        Return element at stack pointer and
        move stack pointer back one step.
        """
        return self.data_stack.pop()

    def push(self, item):
        """
        Push an item onto the machine stack.
        """
        return self.data_stack.push(item)

    def peek(self):
        """
        Peek the item on top of the machine stack.
        """
        return self.data_stack.top

    def halt(self):
        self.instruction_pointer = len(self.code)
        self.execution_successful = False
        self.halted = True

    def run_single_statement(self):
            opcode = self.code[self.instruction_pointer]
            self.instruction_pointer += 1
            self.dispatch(opcode)

            if self.halted:
                return False

    def run(self):
        #reset
        self.execution_successful = False
        self.halted = False

        while self.instruction_pointer < len(self.code):
            print(self.data_stack)
            if self.halted:
                break
            self.run_single_statement()

        if not self.halted:
            if self.peek() is not 0:
                self.execution_successful = True


    def dispatch(self, op):
        if op in self.dispatch_map:
            self.dispatch_map[op](self) #python has higher order functions, meaning that we can evaluate them here.
        else:
            raise RuntimeError("The opcode: " + str(op) + " is not implemented!")

