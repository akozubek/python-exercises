import unittest

def is_infected(grid, x, y):
    try: 
       return grid[(x,y)] == 1
    except:
       # no tuple in grid
       return False

def status(grid, x, y):
    try: 
       return grid[(x,y)]
    except:
       # no tuple in grid
       return 0

def right(dir):
    if dir == [0, -1]: #up
        return [1,0]
    elif dir == [1,0]: #right
        return [0,1]
    elif dir == [0,1]: #down
        return [-1,0]
    elif dir == [-1,0]: #left
        return [0,-1]

def left(dir):
    if dir == [0, -1]: #up
        return [-1,0]
    elif dir == [1,0]: #right
        return [0,-1]
    elif dir == [0,1]: #down
        return [1,0]
    elif dir == [-1,0]: #left
        return [0,1]

def infect(grid, x, y):
    grid[(x,y)] = 1

def weaken(grid, x, y):
    grid[(x,y)] = 2

def flag(grid, x, y):
    grid[(x,y)] = 3

def clean(grid, x, y):
    if (x,y) in grid:
        del grid[(x,y)]

def epidemy(input, iterations):
    infections = 0
    grid = dict()
    # the grid is square
    for i, a in enumerate(input):
        for j, b in enumerate(a):
            grid[(j,i)] = 1 if b == '#' else 0

    x = len(input)//2
    y = x
    dir = [0, -1]
    
    for i in range(iterations):
        if is_infected(grid,x,y):
            dir = right(dir)
            clean(grid, x, y)
        else:  
            dir = left(dir)
            infect(grid, x, y)
            infections += 1
        x = x + dir[0]
        y = y + dir[1]

    return infections

def epidemy2(input, iterations):
    # 0 = clean, 1 = infected, 2 = weakened, 3 = flagged
    infections = 0
    grid = dict()
    # the grid is square
    for i, a in enumerate(input):
        for j, b in enumerate(a):
            grid[(j,i)] = 1 if b == '#' else 0

    x = len(input)//2
    y = x
    dir = [0, -1]
    
    for i in range(iterations):
        s = status(grid, x, y)
        if s == 1:
            # infected
            dir = right(dir)
            flag(grid, x, y)
        elif s == 0:  
            # clean
            dir = left(dir)
            weaken(grid, x, y)
        elif s == 2:
            # weakened
            infect(grid, x, y)
            infections += 1
        elif s == 3:
            # flagged
            dir = [dir[0] * (-1), dir[1] * (-1)]
            clean(grid, x, y)
        x = x + dir[0]
        y = y + dir[1]

    return infections

class Test(unittest.TestCase):
    def test0(self):
       test_input = ['..#', '#..', '...']
       self.assertEqual(epidemy(test_input, 7),5)

    def test1(self):
       test_input = ['..#', '#..', '...']
       self.assertEqual(epidemy(test_input, 70),41)

    def test2(self):
       test_input = ['..#', '#..', '...']
       self.assertEqual(epidemy(test_input, 10000),5587)

    def test20(self):
       test_input = ['..#', '#..', '...']
       self.assertEqual(epidemy2(test_input, 100),26)

    def test21(self):
       test_input = ['..#', '#..', '...']
       self.assertEqual(epidemy2(test_input, 10000000),2511944)

with open("day22.txt") as file:
     input = [line[:-1] for line in file.readlines()]
     print("Result:", epidemy(input, 10000))
     print("Result:", epidemy2(input, 10000000))

unittest.main()
