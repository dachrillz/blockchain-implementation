#This map contains a reference for each opcode corresponding python function.

from .constants import *

import copy

#################################################
# Stack Operations
##################################################

def op_1_negate(this):
    '''
    Push value -1 onto stack
    '''
    this.push(-0x1)

def op_reserved():
    raise NotImplementedError

#Push data
def op_pushdata1():
    raise NotImplementedError
def op_pushdata2():
    raise NotImplementedError
def op_pushdata4():
    raise NotImplementedError

#################################################
# Push small numbers onto stack.
##################################################

def op_push_0(this):
    this.push(0x0)

def op_push_1(this):
    this.push(0x1)

def op_push_2(this):
    this.push(0x2)

def op_push_3(this):
    this.push(0x3)

def op_push_4(this):
    this.push(0x4)

def op_push_5(this):
    this.push(0x5)

def op_push_6(this):
    this.push(0x6)

def op_push_7(this):
    this.push(0x7)

def op_push_8(this):
    this.push(0x8)

def op_push_9(this):
    this.push(0x9)

def op_push_10(this):
    this.push(0xa)

def op_push_11(this):
    this.push(0xb)

def op_push_12(this):
    this.push(0xc)

def op_push_13(this):
    this.push(0xd)

def op_push_14(this):
    this.push(0xe)

def op_push_15(this):
    this.push(0xf)

def op_push_16(this):
    this.push(0x10)

#################################################
# Conditional Flow Control
##################################################

def op_nop(this):
    pass

def op_ver(this):
    this.halt()

def op_if(this):
    #Execute statements following if top os stack is not 0

    if this.pop() is not 0:
        while this.code[this.instruction_pointer] is not OP_ENDIF:
            if this.code[this.instruction_pointer] is OP_ELSE:
                while this.code[this.instruction_pointer] is not OP_ENDIF:
                    this.instruction_pointer += 1
                else:
                    return 

            if this.run_single_statement() is False:
                return

        if this.code[this.instruction_pointer] is OP_ELSE:
            while this.code[this.instruction_pointer] is not OP_ENDIF:
                    this.instruction_pointer += 1
    else:
        while this.code[this.instruction_pointer] is not OP_ENDIF:
            if this.code[this.instruction_pointer] is OP_ELSE:
                if op_else(this) is False:
                    return
            else:
                this.instruction_pointer += 1

def op_notif(this):
    #Execute statements following if top os stack is 0

    if this.pop() is 0:
        while this.code[this.instruction_pointer] is not OP_ENDIF:
            if this.run_single_statement() is False:
                return
    else:
        while this.code[this.instruction_pointer] is not OP_ENDIF:
            if this.code[this.instruction_pointer] is OP_ELSE:
                if op_else(this) is False:
                    return
            else:
                this.instruction_pointer += 1

def op_verif(this):
    this.halt()

def op_vernotif(this):
    this.halt()

def op_else(this):
    while this.code[this.instruction_pointer] is not OP_ENDIF:
        if this.run_single_statement() is False:
            return False

def op_endif(this):
    """
    Simply pass this one.
    """
    pass

def op_verify(this):
    if this.pop() is 0:
        this.halt()

def op_return(this):
    this.halt()

#################################################
# Stack Operations
##################################################

def op_toaltstack(this):
    this.alternative_stack.push(this.pop())
def op_fromaltstack(this):
    this.push(this.alternative_stack.pop())
def op_2drop(this):
    this.pop()
    this.pop()
def op_2dup(this):
    a,b = this.data_stack[-2], this.data_stack[-1]
    this.push(a)
    this.push(b)

def op3dup(this):
    a,b,c = this.data_stack[-1], this.data_stack[-2], this.data_stack[-3]
    this.push(c)
    this.push(b)
    this.push(a)

def op_2over(this):
    a,b = this.data_stack[-3], this.data_stack[-4]
    this.push(b)
    this.push(a)

def op_2rot(this):
    a,b = this.data_stack[-6], this.data_stack[-5]
    del this.data_stack[0] #it feels unnecessary to do this twice
    del this.data_stack[0] #but the deque wont allow me to delete with slices
    this.push(a)
    this.push(b)

def op_2swap(this):
    a,b = this.pop(), this.pop()
    c,d = this.pop(), this.pop()
    this.push(b)
    this.push(a)
    this.push(d)
    this.push(c)

def op_ifdup(this):
    if this.peek() is not 0:
        this.push(this.peek())

def op_depth(this):
    this.push(len(this.data_stack))

def op_drop(this):
    this.pop()

def op_dup(this):
    this.push(this.peek())

def op_nip(this):
    del this.data_stack[-2]

def op_over(this):
    this.push(this.data_stack[-2])

def op_pick(this):
    this.push(this.data_stack[this.pop()])

def op_roll(this):
    a = this.pop()
    this.push(this.data_stack[a])
    del this.data_stack[a]

def op_rot(this):
    a = this.data_stack[-3]
    del this.data_stack[-3]
    this.push(a)

def op_swap(this):
    """
    To me this conflicts between the description and how other online tools work.
    Implemented like the other script machines I tested against.
    """
    a = this.data_stack[-2]
    del this.data_stack[-2]
    this.push(a)

def op_tuck(this):
    a = this.pop()
    b = this.pop()
    this.push(a)
    this.push(b)
    this.push(a)

#################################################
# Arithmetic operations
##################################################

def op_1add(this):
    raise NotImplementedError

def op_1sub(this):
    raise NotImplementedError
def op_negate(this):
    raise NotImplementedError

def op_abs(this):
    raise NotImplementedError

def op_not(this):
    raise NotImplementedError

def op_0notequal(this):
    raise NotImplementedError

def op_add(this):
    l = this.pop()
    r = this.pop()
    this.push(l+r)

def op_sub(this):
    raise NotImplementedError

def op_booland(this):
    raise NotImplementedError

def op_boolor(this):
    raise NotImplementedError

def op_numequal(this):
    l = this.pop()
    r = this.pop()
    this.push(l==r)

def op_numequalverify(this):
    raise NotImplementedError

def op_numnotequal(this):
    raise NotImplementedError

def op_lessthan(this):
    raise NotImplementedError

def op_greaterthan(this):
    raise NotImplementedError

def op_lessthanorequal(this):
    raise NotImplementedError

def op_greaterthanorequal(this):
    raise NotImplementedError

def op_min(this):
    raise NotImplementedError

def op_max(this):
    raise NotImplementedError

def op_within(this):
    raise NotImplementedError

dispatch_map = {
    OP_FALSE : op_push_0,
    OP_TRUE  : op_push_1,
    OP_1NEGATE : op_1_negate,
    OP_RESERVED : op_reserved,

    #Push data
    OP_PUSHDATA1 : op_pushdata1,
    OP_PUSHDATA2 : op_pushdata2,
    OP_PUSHDATA4 : op_pushdata4,

    #push small numbers onto stack
    OP_0 : op_push_0,
    OP_1 : op_push_1,
    OP_2 : op_push_2,
    OP_3 : op_push_3,
    OP_4 : op_push_4,
    OP_5 : op_push_5,
    OP_6 : op_push_6,
    OP_7 : op_push_7,
    OP_8 : op_push_8,
    OP_9 : op_push_9,
    OP_10 : op_push_10,
    OP_11 : op_push_11,
    OP_12 : op_push_12,
    OP_13 : op_push_13,
    OP_14 : op_push_14,
    OP_15 :  op_push_15,
    OP_16 :  op_push_16,


    #arithmetic operations
    OP_1ADD             : op_1add,
    OP_1SUB             : op_1sub,
    OP_NEGATE           : op_negate,
    OP_ABS              : op_abs,
    OP_NOT              : op_not,
    OP_0NOTEQUAL        : op_0notequal,
    OP_ADD              : op_add,
    OP_SUB              : op_sub,
    OP_BOOLAND          : op_booland,
    OP_BOOLOR           : op_boolor,
    OP_NUMEQUAL         : op_numequal,
    OP_NUMEQUALVERIFY   : op_numequalverify,
    OP_NUMNOTEQUAL      : op_numnotequal,
    OP_LESSTHAN         : op_lessthan,
    OP_GREATERTHAN      : op_greaterthan,
    OP_LESSTHANOREQUAL  : op_lessthanorequal,
    OP_GREATERTHANOREQUAL : op_greaterthanorequal,
    OP_MIN              : op_min,
    OP_MAX              : op_max,
    OP_WITHIN           : op_within,

    OP_NOP              : op_nop,
    OP_VER              : op_ver,
    OP_IF               : op_if,
    OP_NOTIF            : op_notif,
    OP_VERIF            : op_verif,
    OP_VERNOTIF         : op_vernotif,
    OP_ELSE             : op_else,
    OP_ENDIF            : op_endif,
    OP_VERIFY           : op_verify,
    OP_RETURN           : op_return,

    #Stack operations
    OP_TOALTSTACK : op_toaltstack,
    OP_FROMALTSTACK : op_fromaltstack,
    OP_2DROP : op_2drop,
    OP_2DUP  : op_2dup,
    OP_3DUP  : op3dup,
    OP_2OVER : op_2over,
    OP_2ROT  : op_2rot,
    OP_2SWAP : op_2swap,
    OP_IFDUP : op_ifdup,
    OP_DEPTH : op_depth,
    OP_DROP  : op_drop,
    OP_DUP   : op_dup,
    OP_NIP   : op_nip,
    OP_OVER  : op_over,
    OP_PICK  : op_pick,
    OP_ROLL  : op_roll,
    OP_ROT   : op_rot,
    OP_SWAP  : op_swap,
    OP_TUCK  : op_tuck,
}







