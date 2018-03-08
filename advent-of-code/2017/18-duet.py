import unittest

def get_value(reg, registers):
    if reg.isalpha():
        try:
            return registers[reg]
        except:
            return 0
    else:
        return int(reg)

def sound_played(instructions):
    registers = dict()
    last_sound = 0
    i = 0
    while True:
        instr = instructions[i]
        elems = instr.split(' ')
        reg = elems[1]
        if instr.startswith('set'):
           value = get_value(elems[2], registers)
           registers[reg] = value
        elif instr.startswith('add'):
           value = get_value(elems[2], registers)
           registers[reg] = get_value(reg, registers) + value
        elif instr.startswith('mul'):
           value = get_value(elems[2], registers)
           registers[reg] = get_value(reg, registers) * value
        elif instr.startswith('mod'):
           value = get_value(elems[2], registers)
           registers[reg] = get_value(reg, registers) % value
        elif instr.startswith('snd'):
           last_sound = get_value(reg, registers)
        elif instr.startswith('rcv'):
           value = get_value(reg, registers)
           if value != 0:
               return last_sound
        elif instr.startswith('jgz'):
           x = get_value(reg, registers)
           y = get_value(elems[2], registers)
           if x > 0:
               # perform jump, subtract -1 so that you can safely add 1 later
               i = i + y - 1
        i += 1

    return last_sound

class Test(unittest.TestCase):
    def test1(self):
        test_input = [
        'set a 1',
        'add a 2',
        'mul a a',
        'mod a 5',
        'snd a',
        'set a 0',
        'rcv a',
        'jgz a -1',
        'set a 1',
        'jgz a -2'
        ]
        self.assertEqual(sound_played(test_input), 4)

with open("day18.txt") as file:
    print("Result:", sound_played([ line[:-1] for line in file.readlines() ]))

unittest.main()
