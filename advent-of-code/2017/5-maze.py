import unittest

def maze(moves):
    index = 0
    steps = 0

    while 0 <= index < len(moves):
        instruction = moves[index]
        steps += 1
        moves[index] += 1
        index = index + instruction
        
    return steps

def maze2(moves):
    length = len(moves)
    index = 0
    steps = 0

    while 0 <= index < len(moves):
        offset = moves[index]
        steps += 1
        if offset >= 3:
             moves[index] -= 1
        else:
             moves[index] += 1
        index = index + offset
        
    return steps

class Test(unittest.TestCase):
    def test1(self):
       self.assertEqual(maze([0, 3, 0, 1, -3]), 5)
    def test2(self):
       self.assertEqual(maze2([0, 3, 0, 1, -3]), 10)

with open("day5.txt") as file:
    input = [int(line) for line in file]
    print("Result:", maze(input))

with open("day5.txt") as file:
    input = [int(line) for line in file]
    print("Result 2:", maze2(input))

unittest.main()
