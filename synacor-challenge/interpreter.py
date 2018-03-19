import struct
import sys

size = 32768

HALT = 0 
SET = 1
PUSH = 2
POP = 3
EQ = 4
GT = 5
JMP = 6
JT = 7
JF = 8
ADD = 9
MULT = 10
MOD = 11
AND = 12
OR = 13
NOT = 14
RMEM = 15
WMEM = 16
CALL = 17
RET = 18
OUT = 19
IN = 20
NOOP = 21


def load_program():
    with open('challenge.bin', 'rb') as f:
        mem = []
        bin = f.read(2)
        while bin != b"":
            instr = struct.unpack('<H', bin)[0] 
            mem.append(instr)
            bin = f.read(2)
        return mem

def value(registers, num):
    if num <= 32767:
        return num
    if 32768 <= num <= 32775:
        return registers[num - size
    ]
    raise ValueError("Invalid number", num)

def register(num):
    return num - size

mem = load_program()
registers = {i:0  for i in range(8)}
stack = list()

pos = 0

while pos < len(mem):
    instr = mem[pos]
    if instr == HALT:
       sys.exit()
    elif instr == OUT: 
        val = value(registers, mem[pos+1])
        print(chr(val), end='')
        pos += 2
    elif instr == NOOP: 
        pos += 1
    elif instr == JMP: 
        a = mem[pos+1]
        pos = value(registers, a)
    elif instr == JT: 
        a = value(registers, mem[pos+1])
        if a != 0:
            pos = value(registers, mem[pos+2])
        else: 
            pos += 3
    elif instr == JF: 
        a = value(registers, mem[pos+1])
        if a == 0:
            pos = value(registers, mem[pos+2])
        else: 
            pos += 3
    elif instr == RET: 
        try:
            pos = stack.pop()
        except:
            sys.exit()
    elif instr == PUSH: 
        a = value(registers, mem[pos+1])
        stack.append(a) 
        pos += 2
    elif instr == POP: 
        a = register(mem[pos+1])
        registers[a] = stack.pop()
        pos += 2
    elif instr == CALL: 
        stack.append(pos+2)
        pos = value(registers, mem[pos+1])
    elif instr == IN: 
        val = sys.stdin.read(1)
        a = register(mem[pos+1])
        registers[a] = ord(val)
        pos += 2
    elif instr == SET: 
        a = register(mem[pos+1])
        b = value(registers, mem[pos+2])
        registers[a] = b
        pos += 3
    elif instr == NOT: 
        a = register(mem[pos+1])
        b = value(registers, mem[pos+2])
        registers[a] = (~b) % size
        pos += 3
    elif instr == RMEM: 
        a = register(mem[pos+1])
        b = mem[value(registers, mem[pos+2])]
        registers[a] = b
        pos += 3
    elif instr == WMEM: 
        a = value(registers, mem[pos+1])
        b = value(registers, mem[pos+2])
        mem[a] = b
        pos += 3
    elif instr == EQ: 
        a = register(mem[pos+1])
        b = value(registers, mem[pos+2])
        c = value(registers, mem[pos+3])
        if b == c:
                registers[a] = 1
        else: 
                registers[a] = 0
        pos += 4
    elif instr == GT: 
        a = register(mem[pos+1])
        b = value(registers, mem[pos+2])
        c = value(registers, mem[pos+3])
        if b > c:
                registers[a] = 1
        else: 
                registers[a] = 0
        pos += 4
    elif instr == ADD: 
        a = register(mem[pos+1])
        b = value(registers, mem[pos+2])
        c = value(registers, mem[pos+3])
        registers[a] = (b + c) % size
        pos += 4
    elif instr == MULT: 
        a = register(mem[pos+1])
        b = value(registers, mem[pos+2])
        c = value(registers, mem[pos+3])
        registers[a] = (b * c) % size
        pos += 4
    elif instr == MOD: 
        a = register(mem[pos+1])
        b = value(registers, mem[pos+2])
        c = value(registers, mem[pos+3])
        registers[a] = (b % c) % size
        pos += 4
    elif instr == AND: 
        a = register(mem[pos+1])
        b = value(registers, mem[pos+2])
        c = value(registers, mem[pos+3])
        registers[a] = (b & c) % size
        pos += 4
    elif instr == OR: 
        a = register(mem[pos+1])
        b = value(registers, mem[pos+2])
        c = value(registers, mem[pos+3])
        registers[a] = (b | c) % size
        pos += 4

