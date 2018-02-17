import unittest

def parse(line):
    values = line.split()
    program = values[0]
    weight = int(values[1].strip('(').strip(')'))
    try:
        i = values.index('->')
        children = [v.rstrip(',') for v in values[(i+1):]]
    except:
        children = list()
    return (program, weight, children)

def tree(lines):
    t = dict()
    for line in lines:
        program, _, children = parse(line)
        program_tree = t.setdefault(program, dict())
        for child in children:
            child_tree = t.setdefault(child, dict())
            program_tree[child] = child_tree
    return t

def tree(lines):
    t = dict()
    for line in lines:
        program, weight, children = parse(line)
        program_tree = t.setdefault(program, (weight, dict()))
        for child in children:
            child_node = t.setdefault(child, (0, dict()))
            program_tree[child] = child_node
    return t

def depth(t,k):
    if t[k] == {}:
        return 0
    return max([depth(t,child) for child in t[k]])+1

def root(t):
    max = 0
    r = ''
    for k in t:
        d = depth(t,k)
        if d > max:
             max = d
             r = k
    return r

def root2(t2):
    max = 0
    r = ''
    for k in t2:
        d = depth(t,k)
        if d > max:
             max = d
             r = k
    return r
        
def balance(t2):
    return 0

class Test(unittest.TestCase):
    def test1(self):
       with open("day7-test.txt") as file:
         self.assertEqual(root(tree([line for line in file])), 'tknk')

    def test2(self):
       with open("day7-test.txt") as file:
         self.assertEqual(balance(tree2([line for line in file])), 60)

with open("day7.txt") as file:
    print("Result", root(tree([line for line in file])))

with open("day7.txt") as file:
    print("Result 2", balance(tree2([line for line in file])))

unittest.main()
