import unittest

'''
The program can only move with 6 vectors (steps):
(0, +-sqrt(3)), (+- 1.5, +- sqrt(3)/2)

Change the coordinate system: x axis unit is 1.5, y axis unit is sqrt(3)
'''

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

def distance(point):
'''
First make steps along x-axis; number of steps abs(point[0]).
Arrive at point (0, y).
Then make steps along y-axis (vertical vector), number of steps = abs(y-coordinate)
after point[0] steps.
'''
    r = reverse(point)
    return abs(point[0]) + abs(point[1] + r[1] * abs(point[0]))

def shortest_path(input):
    moves = input.split(',')
    current = [0,0]
    m = 0
    for move in moves:
         v = vector(move)
         current[0] += v[0]
         current[1] += v[1]
         d = distance(current)
         m = max(m,d)
    return (distance(current), m) 

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(shortest_path('ne,ne,ne')[0], 3)
    def test2(self):
        self.assertEqual(shortest_path('ne,ne,sw,sw')[0], 0)
    def test3(self):
        self.assertEqual(shortest_path('ne,ne,s,s')[0], 2)
    def test4(self):
        self.assertEqual(shortest_path('se,sw,se,sw,sw')[0], 3)

with open("day11.txt") as file:
    line = file.readline().rstrip('\n')
    print("Result: ", shortest_path(line))

unittest.main()
