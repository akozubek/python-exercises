import unittest
import operator


def add(t1, t2):
    return tuple(map(operator.add, t1, t2))

def dist(t1, t2):
    return max(abs(t1[0]-t2[0]),abs(t1[1]-t2[1]))

def new_direction(pos, direction):
    x, y = pos
    if x > 0 and x == y:
	# left
        return (-1,0)
    elif x < 0 and -x == y:
        # down
        return (0,-1)
    elif x < 0 and x == y:
        # right
        return (1,0)
    elif x > 0 and y == -x + 1:
        # up
        return (0,1)
    else: 
        return direction

def spiral_steps(n):
    position = (0,0)
    direction = (1,0) # right
    for i in range(n-1):
        position = add(position, direction)
        direction = new_direction(position, direction)
    return abs(position[0]) + abs(position[1])

def value(grid, pos):
    return 

def spiral2_value(n):
    pos = (0,0)
    direction = (1,0) # right
    grid = {pos: 1}

    while grid[pos] < n:
        pos = add(pos, direction)
        direction = new_direction(pos, direction)
        grid[pos] = sum(grid[x] for x in grid if dist(x, pos) == 1)

    return grid[pos]

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(spiral_steps(1),0)
    def test2(self):
        self.assertEqual(spiral_steps(12),3)
    def test3(self):
        self.assertEqual(spiral_steps(23),2)
    def test4(self):
        self.assertEqual(spiral_steps(1024),31)
    def test_input(self):
        inp = 289326
        self.assertEqual(spiral_steps(inp), 419)

    def test2_input(self):
        inp = 289326
        self.assertEqual(spiral2_value(inp), 295229)

inp = 289326
print("Result: ", spiral_steps(inp))
print("Result 2: ", spiral2_value(inp))
unittest.main()
