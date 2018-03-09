import unittest

'''
Advent of Code Day 18, Part 2
'''

def get_value(reg, registers):
    if reg.isalpha():
        try:
            return registers[reg]
        except:
            return 0
    else:
        return int(reg)

def run_instructions(instructions, i, registers, read_queue, write_queue):
    writes = 0
    while i < len(instructions):
        instr = instructions[i]
        elems = instr.split(' ')
        reg = elems[1]
        i += 1
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
            write_queue.append(get_value(reg, registers))
            writes += 1
        elif instr.startswith('rcv'):
            if len(read_queue) == 0:
                 i -= 1
                 break
            registers[reg] = read_queue.pop(0)
        elif instr.startswith('jgz'):
            x = get_value(reg, registers)
            y = get_value(elems[2], registers)
            if x > 0:
                # perform jump, subtract -1 so that you can safely add 1 later
                i = i + y - 1
    if i == len(instructions):
         result = "terminated"
    else:
         result = "block_rcv"
    return (i, writes, result)


def count_sends(instructions):
    registers_0 = { 'p' : 0 }
    registers_1 = { 'p' : 1 }
    i_0 = 0
    i_1 = 0
    # queue for 0 to write
    queue_0 = list()
    # queue for 1 to write
    queue_1 = list()
    total_writes_1 = 0
    while True:
        i_0, writes_0, result_0 = run_instructions(instructions, i_0, registers_0, queue_1, queue_0)
        i_1, writes_1, result_1 = run_instructions(instructions, i_1, registers_1, queue_0, queue_1)
        total_writes_1 += writes_1
        blocked_0 = (result_0 == "block_rcv" and queue_1 == [])
        blocked_1 = (result_1 == "block_rcv" and queue_0 == [])
        if blocked_0 and blocked_1:
            #deadlock
            break
        # There should be conditions for either program terminating
        # but I'm too lazy to implement them since they are not needed
        

    return total_writes_1

class Test(unittest.TestCase):
    def test1(self):
        test_input = [
          'snd 1',
          'snd 2',
          'snd p',
          'rcv a',
          'rcv b',
          'rcv c',
          'rcv d',
        ]
        self.assertEqual(count_sends(test_input), 3)

with open("day18.txt") as file:
    print("Result:", count_sends([ line[:-1] for line in file.readlines() ]))

unittest.main()
