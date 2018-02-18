import unittest

def total_score(input):
    total = 0
    score = 0
    garbage = False
    cancel = False
    garbage_count = 0
    for c in input:
        if cancel:
            cancel = False 
            continue
        if garbage:
            if c == "!":
                cancel = True
            elif c == ">":
                garbage = False
            else:
                garbage_count += 1
            continue
        if c == '{':
            score += 1
        elif c == '}':
            # group end
            total += score
            score -= 1
        elif c == "<":
            garbage = True
        
    return (total, garbage_count)

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(total_score("{}")[0], 1)
    def test2(self):
        self.assertEqual(total_score("{{{}}}")[0], 6)
    def test3(self):
        self.assertEqual(total_score("{{},{}}")[0], 5)
    def test4(self):
        self.assertEqual(total_score("{<a>,<a>,<a>,<a>}")[0], 1)
    def test5(self):
        self.assertEqual(total_score("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0], 9)
    def test6(self):
        self.assertEqual(total_score("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0], 9)
    def test7(self):
        self.assertEqual(total_score("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0], 3)

with open("day9.txt") as file:
    for line in file:
        print("Result", total_score(line))
unittest.main()
