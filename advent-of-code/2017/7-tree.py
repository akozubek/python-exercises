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
        program, weight, children = parse(line)
        try: 
            t[program][0] = weight
        except:
            t[program] = [weight, dict()]
        program_tree = t[program]
        for child in children:
            child_node = t.setdefault(child, [0, dict()])
            program_tree[1][child] = child_node
    return t

def depth(t,k):
    _, tree = t[k]
    if tree == {}:
        return 0
    return max([depth(t,child) for child in tree])+1

def root(t):
    max = 0
    r = ''
    for k in t:
        d = depth(t,k)
        if d > max:
             max = d
             r = k
    return r

def build_tree_with_weights(label, current_node):
    (weight, children) = current_node
    if len(children) == 0:
        return (label, weight, weight, dict())
    # there are children
    total_weight = weight
    new_children = dict()
    for child in children:
        new_child_tree = build_tree_with_weights(child, children[child])
        (child_label, child_weight, child_total_weight, child_tree) = new_child_tree
        total_weight += child_total_weight
        new_children[child] = new_child_tree
    return (label, weight, total_weight, new_children)

def tree_with_weights(t):
    r = root(t)
    new_tree = build_tree_with_weights(r, t[r])
    return new_tree

def find_imbalance(t):
     #print(t)
    (label, weight, total, children) = t
    if (len(children) == 0):
       return None    

    weights = dict()
    for c in children:
        (child_label, child_weigth, child_total, child_tree) = children[c]        
        child_imbalance = find_imbalance(children[c])
        if (child_imbalance != None):
           return child_imbalance
        s = weights.setdefault(child_total, set())
        s.add(child_label)

    if (len(weights) == 1):
        # tree are balanced
        return None
    else: 
        # trees are not balanced
        for w in weights:
            if len(weights[w]) == 1:
                odd_label = list(weights[w])[0]
            else: 
                normal_weight = w
        (_, odd_weight, odd_total, _) = children[odd_label]
        return odd_weight + normal_weight - odd_total
        
def balance(t):
    weighted_tree = tree_with_weights(t)
    return find_imbalance(weighted_tree)

class Test(unittest.TestCase):
    def test1(self):
       with open("day7-test.txt") as file:
         self.assertEqual(root(tree([line for line in file])), 'tknk')

    def test2(self):
       with open("day7-test.txt") as file:
         self.assertEqual(balance(tree([line for line in file])), 60)

with open("day7.txt") as file:
    print("Result", root(tree([line for line in file])))

with open("day7.txt") as file:
    print("Result 2", balance(tree([line for line in file])))

unittest.main()
