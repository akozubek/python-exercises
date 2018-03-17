import unittest
import collections

def checksum(input):
    iterations = int(input[1].split(" ")[5])
    configuration = dict()
    
    for i in range(3, len(input), 10):
        state = input[i].split(" ")[2][:-1]
        zeroval = int(input[i+2].split(" ")[8][:-1])
        zeromove = 1 if input[i+3].split(" ")[10] == "right." else -1
        zerostate = input[i+4].split(" ")[8][:-1]
        zeroconf = (zeroval, zeromove, zerostate)
        oneval = int(input[i+6].split(" ")[8][:-1])
        onemove =  1 if input[i+7].split(" ")[10] == "right." else -1
        onestate = input[i+8].split(" ")[8][:-1]
        oneconf = (oneval, onemove, onestate)
        configuration[state] = (zeroconf, oneconf)
    
    state = 'A'
    tape = collections.defaultdict(int)
    index = 0
    for i in range(iterations):
        value = tape[index]
        current_conf = configuration[state][value]
        tape[index] = current_conf[0]
        index += current_conf[1]
        state = current_conf[2]
    
    return sum(tape.values())

class Test(unittest.TestCase):
    def test1(self):
        test_input = [
          'Begin in state A.',
          'Perform a diagnostic checksum after 6 steps.',
          '',
          'In state A:',
          '  If the current value is 0:',
          '    - Write the value 1.',
          '    - Move one slot to the right.',
          '    - Continue with state B.',
          '  If the current value is 1:',
          '    - Write the value 0.',
          '    - Move one slot to the left.',
          '    - Continue with state B.',
          '',
          'In state B:',
          '  If the current value is 0:',
          '    - Write the value 1.',
          '    - Move one slot to the left.',
          '    - Continue with state A.',
          '  If the current value is 1:',
          '    - Write the value 1.',
          '    - Move one slot to the right.',
          '    - Continue with state A.'
        ]
        self.assertEqual(checksum(test_input), 3)

with open("day25.txt") as file:
    print("Result: ", checksum([line[:-1] for line in file.readlines()]))

unittest.main()
