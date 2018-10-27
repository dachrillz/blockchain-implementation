##############################################################
### This file containts constants defined for the script machine.
##############################################################

##############################################################
### Stack operations
##############################################################

OP_0 = 0x00
OP_FALSE =  0x00 #An empty array is pushed onto the stack (corresponds to false)

_1 =  0x01 #Push 1 bytes ono stack
_2 =  0x02 #Push 2 bytes onto stack
_3 =  0x03 #Push 3 bytes onto stack
_4 =  0x04 #Push 4 bytes onto stack
_5 =  0x05 #Push 5 bytes onto stack
_6 =  0x06 #Push 6 bytes onto stack
_7 =  0x07 #Push 7 bytes onto stack
_8 =  0x08 #Push 8 bytes onto stack
_9 =  0x09 #Push 9 bytes onto stack
_10 = 0x0a #Push 10 bytes onto stack
_11 = 0x0b #Push 11 bytes onto stack
_12 = 0x0c #Push 12 bytes onto stack
_13 = 0x0d #Push 13 bytes onto stack
_14 = 0x0e #Push 14 bytes onto stack
_15 = 0x0f #Push 15 bytes onto stack
_16 = 0x10 #Push 16 bytes onto stack
_17 = 0x11 #Push 17 bytes onto stack
_18 = 0x12 #Push 18 bytes onto stack
_19 = 0x13 #Push 19 bytes onto stack
_20 = 0x14 #Push 20 bytes onto stack
_21 = 0x15 #Push 21 bytes onto stack
_22 = 0x16 #Push 22 bytes onto stack
_23 = 0x17 #Push 23 bytes onto stack
_24 = 0x18 #Push 24 bytes onto stack
_25 = 0x19 #Push 25 bytes onto stack
_26 = 0x1a #Push 26 bytes onto stack
_27 = 0x1b #Push 27 bytes onto stack
_28 = 0x1c #Push 28 bytes onto stack
_29 = 0x1d #Push 29 bytes onto stack
_30 = 0x1e #Push 30 bytes onto stack
_31 = 0x1f #Push 31 bytes onto stack
_32 = 0x20 #Push 32 bytes onto stack
_33 = 0x21 #Push 33 bytes onto stack
_34 = 0x22 #Push 34 bytes onto stack
_35 = 0x23 #Push 35 bytes onto stack
_36 = 0x24 #Push 36 bytes onto stack
_37 = 0x25 #Push 37 bytes onto stack
_38 = 0x26 #Push 38 bytes onto stack
_39 = 0x27 #Push 39 bytes onto stack
_40 = 0x28 #Push 40 bytes onto stack
_41 = 0x29 #Push 41 bytes onto stack
_42 = 0x2a #Push 42 bytes onto stack
_43 = 0x2b #Push 43 bytes onto stack
_44 = 0x2c #Push 44 bytes onto stack
_45 = 0x2d #Push 45 bytes onto stack
_46 = 0x2e #Push 46 bytes onto stack
_47 = 0x2f #Push 47 bytes onto stack
_48 = 0x30 #Push 48 bytes onto stack
_49 = 0x31 #Push 49 bytes onto stack
_50 = 0x32 #Push 50 bytes onto stack
_51 = 0x33 #Push 51 bytes onto stack
_52 = 0x34 #Push 52 bytes onto stack
_53 = 0x35 #Push 53 bytes onto stack
_54 = 0x36 #Push 54 bytes onto stack
_55 = 0x37 #Push 55 bytes onto stack
_56 = 0x38 #Push 56 bytes onto stack
_57 = 0x39 #Push 57 bytes onto stack
_58 = 0x3a #Push 58 bytes onto stack
_59 = 0x3b #Push 59 bytes onto stack
_60 = 0x3c #Push 60 bytes onto stack
_61 = 0x3d #Push 61 bytes onto stack
_62 = 0x3e #Push 62 bytes onto stack
_63 = 0x3f #Push 63 bytes onto stack
_64 = 0x40 #Push 64 bytes onto stack
_65 = 0x41 #Push 65 bytes onto stack
_66 = 0x42 #Push 66 bytes onto stack
_67 = 0x43 #Push 67 bytes onto stack
_68 = 0x44 #Push 68 bytes onto stack
_69 = 0x45 #Push 69 bytes onto stack
_70 = 0x46 #Push 70 bytes onto stack
_71 = 0x47 #Push 71 bytes onto stack
_72 = 0x48 #Push 72 bytes onto stack
_73 = 0x49 #Push 73 bytes onto stack
_74 = 0x4a #Push 74 bytes onto stack
_75 = 0x4b #Push 75 bytes onto stack

OP_PUSHDATA1 = 0x4c #Push the next script byte containts N, push the following N bytes onto the stack
OP_PUSHDATA2 = 0x4d #The next to script bytes contain N, push the following N bytes onto the stack
OP_PUSHDATA4 = 0x4e #The next four scipt bytes contain N, push the following N bytes onto the stack
OP_1NEGATE = 0x4f   #Push the value "-1" into the stack
OP_RESERVED = 0x50 #Halt - Invalid transaction unless found in an unexecuted OP_IF clause

OP_TRUE = 0x51 #Push the value "1" onto the stack
OP_1 = 0x51
OP_2 = 0x52 #Push the value 2 onto the stack
OP_3 = 0x53 #Push the value 3 onto the stack
OP_4 = 0x54 #Push the value 4 onto the stack
OP_5 = 0x55 #Push the value 5 onto the stack
OP_6 = 0x56 #Push the value 6 onto the stack
OP_7 = 0x57 #Push the value 7 onto the stack
OP_8 = 0x58 #Push the value 8 onto the stack
OP_9 = 0x59 #Push the value 9 onto the stack
OP_10 = 0x5a #Push the value 10 onto the stack
OP_11 = 0x5b #Push the value 11 onto the stack
OP_12 = 0x5c #Push the value 12 onto the stack
OP_13 = 0x5d #Push the value 13 onto the stack
OP_14 = 0x5e #Push the value 14 onto the stack
OP_15 = 0x5f #Push the value 15 onto the stack
OP_16 = 0x60 #Push the value 16 onto the stack

##############################################################
### Conditional Flow
##############################################################

OP_NOP = 0x61 #Do Nothing
OP_VER = 0x62 #Halt - invalid transaction unless found in an unexecuted OP_IF clause.
OP_IF = 0x63 #Execute the statements followin if top of stack is not 0
OP_NOTIF = 0x64 #Execute the statements if top of stack is 0
OP_VERIF = 0x65 #Halt - invalid transaction
OP_VERNOTIF = 0x66 #Halt - invalid transaction
OP_ELSE = 0x67 #Execute only if the previous statements were not executed
OP_ENDIF = 0x68 #End the OP_IF,OP_NOTIF,OP_ELSE block
OP_VERIFY = 0x69 #Check the top of the stack, halt and invalidate transaction if not True
OP_RETURN = 0x6a #Halt and invalidate transaction

##############################################################
###
### Time Lock
###
##############################################################

##############################################################
###
### Stack Operations
###
##############################################################

OP_TOALTSTACK = 0x6b #Pop top item from stack and push to alternative stack
OP_FROMALTSTACK = 0x6c #Pop top item from alternative stack and push to stack
OP_2DROP = 0x6d #Pop top two stack items
OP_2DUP = 0x6e #Duplicate top two stack items
OP_3DUP = 0x6f #Duplicate top three stack items
OP_2OVER = 0x70 #Copy the third and fourth items in the stack to the top
OP_2ROT = 0x71 #Move the fifth and sixth items in the stack to the top
OP_2SWAP = 0x72 #Swap the two top pairs of items in the stack
OP_IFDUP = 0x73 #Duplicate the top item in the stack if it is not 0
OP_DEPTH = 0x74 #Count the items on the stack and push the resulting count
OP_DROP = 0x75 #Pop the top item in the stack
OP_DUP = 0x76 #Duplicate the top item in the stack
OP_NIP = 0x77 #Pop the second item in the stack
OP_OVER = 0x78 #Copy the second item in the stack and push it onto the top
OP_PICK = 0x79 #Pop value N from top, then copy the Nth item to the top of the stack
OP_ROLL = 0x7a #Pop value N from top, then move the Nth item to the top of the stack
OP_ROT = 0x7b #Rotate the top three items in the stack
OP_SWAP = 0x7c #Swap the top three items in the stack
OP_TUCK = 0x7d #Copy the top item and insert it between the top and second item.

##############################################################
###
### String Splice Operations
###
##############################################################


##############################################################
###
### Binary Arithmetic and Conditionals
###
##############################################################

##############################################################
###
### Numeric Operators
###
##############################################################

OP_1ADD = 0x8b #Add 1 to top item of stack
OP_1SUB = 0x8c #Subtract 1 from top item of stack
#OP_2MUL = 0x8d #DISABLED
#OP_2DIV = 0x8e #DISABLED
OP_NEGATE = 0x8f #flip the sign of the top item
OP_ABS = 0x90 #Change the sign of the top item to positive
OP_NOT = 0x91 #If top item is 0 or 1 Boolean flip it, otherwise return 0
OP_0NOTEQUAL = 0x92 #If top item is 0 return 0, otherwise return 1
OP_ADD = 0x93 #Pop top two items, add, push result
OP_SUB = 0x94 #Pop top two items, sub, push result
#OP_MUL = 0x95 #DISABLED
#OP_DIV = 0x96 #DISABLED
#OP_MOD = 0x97 #DISABLED
#OP_LSHIFT = 0x98 #DISABLED
#OP_RSHIFT = 0x99 #DISABLED
OP_BOOLAND = 0x9a #Boolean AND of top two items
OP_BOOLOR = 0x9b #Boolean OR of top two items
OP_NUMEQUAL = 0x9c #Return true if top two items are equal
OP_NUMEQUALVERIFY = 0x9d #Return true if top two items are equal, halt otherwise!
OP_NUMNOTEQUAL = 0x9e #Return TRUE if top tow items are not equal
OP_LESSTHAN = 0x9f #Return true if second item is less than top item
OP_GREATERTHAN = 0xa0 #return true if second item is greater then top item
OP_LESSTHANOREQUAL = 0xa1
OP_GREATERTHANOREQUAL = 0xa2
OP_MIN = 0xa3 #Return the smallest of the two top items
OP_MAX = 0xa4 #return the larger of the two top item
OP_WITHIN = 0xa5 #Return True if the third item is between the second (or equal) and first item.

##############################################################
###
### Cryptographic and Hashing Operators
###
##############################################################

##############################################################
###
### Non Operators
###
##############################################################

##############################################################
###
### Reserved OP
###
##############################################################
