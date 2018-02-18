import unittest

def parse_command(line):
    command = line.split()
    register = command[0]
    instruction = command[1]
    value = int(command[2])
    condition = command[4:]
    return (register, instruction, value, condition)

def condition_is_true(registers, condition):
    register, operator, cmp_value = condition
    cmp_value = int(cmp_value)
    reg_value = registers.setdefault(register, 0)
    if operator == '==':
        return reg_value == cmp_value
    elif operator == '!=':
        return reg_value != cmp_value
    elif operator == '>':
        return reg_value > cmp_value
    elif operator == '<':
        return reg_value < cmp_value
    elif operator == '>=':
        return reg_value >= cmp_value
    elif operator == '<=':
        return reg_value <= cmp_value

def evaluate(register, instruction, value, registers):
    old_value = registers.setdefault(register, 0)
    if instruction == 'inc':
        registers[register] = old_value + value
    elif instruction == 'dec':
        registers[register] = old_value - value

def run_code(commands):
    registers = dict()
    m = 0
    for command in commands:
        (register, instruction, value, condition) = parse_command(command)
        if condition_is_true(registers, condition):
            evaluate(register, instruction, value, registers)
            if registers[register] > m:
                m = registers[register]
    return (max(registers.values()), m)
        

class Test(unittest.TestCase):
    def test1(self):
        with open("day8-test.txt") as file:
            commands = [ line for line in file]
            self.assertEqual(run_code(commands)[0], 1)
    def test2(self):
        with open("day8-test.txt") as file:
            commands = [ line for line in file]
            self.assertEqual(run_code(commands)[1], 10)

with open("day8.txt") as file:
    commands = [ line for line in file]
    print("Result:", run_code(commands))

unittest.main()

