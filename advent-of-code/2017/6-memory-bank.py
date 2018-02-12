import unittest
import csv

def distribute(memory):
    new_memory = list(memory)
    max_value = max(new_memory)
    max_index = new_memory.index(max_value)
    new_memory[max_index] = 0
    for i in range(max_value):
        index = (max_index + 1 + i) % len(new_memory)
        new_memory[index] += 1

    return tuple(new_memory)

def distributions(memory):
    steps = 0
    configurations = set()
    current = tuple(memory)

    while current not in configurations:
       configurations.add(current)
       current = distribute(current)
       steps += 1
    
    return steps

def distributions2(memory):
    steps = 0
    configurations = dict()
    current = tuple(memory)

    while current not in configurations:
       configurations[current] = steps
       current = distribute(current)
       steps += 1
    
    return steps - configurations[current]

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(distributions([0,2,7,0]),5)

    def test2(self):
        self.assertEqual(distributions2([0,2,7,0]),4)

reader = csv.reader(open("day6.txt",'r'),delimiter='\t') 
for row in reader:
    input = [ int(n) for n in row]
    print("Result: ", distributions(input))
    print("Result 2: ", distributions2(input))

unittest.main()
