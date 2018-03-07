import unittest

def spinlock2017(steps):
    buf = [0]
    current = 0
    
    for i in range(1, 2018):
        current = (current + steps) % len(buf) + 1
        buf.insert(current, i)

    return buf[(current + 1) % len(buf)]

def spinlock2017_part2(steps):
    '''
    We're only interested in value inserted at position 1. All others
    can be disregarded
    '''
    current = 0
    value = 0
    
    for i in range(1, 50000000):
        current = (current + steps) % i + 1
        if current == 1:
             value = i

    return value
    

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(spinlock2017(3),638)

input = 312
print("Result:", spinlock2017(input))
print("Result 2:", spinlock2017_part2(input))
unittest.main()
