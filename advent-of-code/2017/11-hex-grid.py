import unittest

def vector(move):
    if move == 'n':
        return [0,1]
    elif move == 's':
        return [0,-1]
    elif move == 'ne':
        return [1,1/2]
    elif move == 'se':
        return [1,-1/2]
    elif move == 'nw':
        return [-1,1/2]
    elif move == 'sw':
        return [-1,-1/2]

def sign(x):
    if x < 0:
       return -1
    elif x > 0:
       return 1
    else:
       return 0

def reverse(v):
    return [ sign(v[0]) * (-1) , sign(v[1]) * (-1/2) ]

def shortest_path(input):
    moves = input.split(',')
    current = [0,0]
    for move in moves:
         v = vector(move)
         current[0] += v[0]
         current[1] += v[1]
    r = reverse(current)
    return abs(current[0]) + abs(current[1] + r[1] * abs(current[0]))


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(shortest_path('ne,ne,ne'), 3)
    def test2(self):
        self.assertEqual(shortest_path('ne,ne,sw,sw'), 0)
    def test3(self):
        self.assertEqual(shortest_path('ne,ne,s,s'), 2)
    def test4(self):
        self.assertEqual(shortest_path('se,sw,se,sw,sw'), 3)

with open("day11.txt") as file:
    line = file.readline().rstrip('\n')
    print("Result: ", shortest_path(line))

unittest.main()
