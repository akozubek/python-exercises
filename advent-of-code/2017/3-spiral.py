import unittest
import operator


def add(t1, t2):
    return tuple(map(operator.add, t1, t2))

def dist(t1, t2):
    return max(abs(t1[0]-t2[0]),abs(t1[1]-t2[1]))

def gen_vector(cur, vector):
    x = cur[0]
    y = cur[1]
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
        return vector

def spiral(n):
    cur = (0,0)
    # right
    vector = (1,0)
    for i in range(n-1):
        cur = add(cur, vector)
        vector = gen_vector(cur, vector)
    return abs(cur[0]) + abs(cur[1])

def value(dict, cur):
    neighbors = [point for point in dict if dist(point, cur) == 1 ]
    val = 0
    for point in neighbors:
        val += dict[point]
    return val

def spiral2(n):
    cur = (0,0)
    # right
    vector = (1,0)
    dict = {cur: 1}
    for i in range(n+1):
        cur = add(cur, vector)
        vector = gen_vector(cur, vector)
        val = value(dict, cur)
        dict[cur] = val
        if val > n:
            print(dict)
            return val

    print(dict)
    return 0

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(spiral(1),0)
    def test2(self):
        self.assertEqual(spiral(12),3)
    def test3(self):
        self.assertEqual(spiral(23),2)
    def test4(self):
        self.assertEqual(spiral(1024),31)

#    def test21(self):
#        self.assertEqual(spiral2(1),2)

input = 289326
print("Result: ", spiral(input))
print("Result 2: ", spiral2(input))
spiral2(1)

unittest.main()
