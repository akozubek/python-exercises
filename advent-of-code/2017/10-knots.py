import unittest

def reverse_sublist(l, current, length):
    lower_a = current
    lower_b = min(current+length, len(l))
    lower_list = l[lower_a:lower_b]

    upper_a = 0
    upper_b = max(0,(current+length-len(l)))
    upper_list = l[upper_a:upper_b]

    sublist = lower_list + upper_list
    sublist = list(reversed(sublist))

    index = current
    for v in sublist:
        l[index] = v
        index = (index + 1) % len(l)

def tie_knots(l, lengths, current, skip):

    for length in lengths:
        reverse_sublist(l, current, length)
        current = (current + length + skip) % len(l)
        skip += 1

    return (l, current, skip)

def xor(l):
    res = 0
    for x in l:
        res = res ^ x
    return res

def hex0(n):
    h = hex(n)[2:]
    if len(h) == 1:
        return '0'+h
    return h

def compute_lengths(line):
    return [ord(c) for c in line] + [17, 31, 73, 47, 23]

def compute_string_hash(dense_hash):
    return "".join([hex0(n) for n in dense_hash])

def compute_hash(line):
    lengths = compute_lengths(line)
    current = 0
    skip = 0
    l = list(range(0, 256))
    for i in range(0, 64):
         (l, current, skip) = tie_knots(l, lengths, current, skip)
    sparse_hash = l
    dense_hash = list(range(0,16))
    for i in range(0, 16):
        index = 16 * i
        dense_hash[i] = xor(sparse_hash[index:(index+16)])
    
    return compute_string_hash(dense_hash)

class Test(unittest.TestCase):
    def test1(self):
        l = list(range(0, 5))
        result = tie_knots(l, [3,4,1,5], 0, 0)
        self.assertEqual(result[0][0] * result[0][1], 12)

    def test2(self):
        self.assertEqual(compute_hash(''), 'a2582a3a0e66e6e86e3812dcb672a272')

    def test3(self):
        self.assertEqual(compute_hash('AoC 2017'), '33efeb34ea91902bb2f59c9920caa6cd')

    def test4(self):
        self.assertEqual(compute_hash('1,2,3'), '3efbe78a8d82f29979031a4aa0b16a9d')

    def test5(self):
        self.assertEqual(compute_hash('1,2,4'), '63960835bcdc130f0b66d7ff4f6a5a8e')

    def testXor(self):
        self.assertEqual(xor([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]), 64)

    def testLengths(self):
        self.assertEqual(compute_lengths('1,2,3'), [49,44,50,44,51,17, 31, 73, 47, 23])
    def testHash(self):
        self.assertEqual(compute_string_hash([64, 7, 255]), '4007ff')

with open("day10.txt") as file:
    for line in file:
        l = list(range(0, 256))
        result = tie_knots(l, [int(n) for n in line.split(",")], 0, 0)
        print("Result:", result[0][0] * result[0][1])

with open("day10.txt") as file:
    for line in file:
        print(line)
        print("Result 2:", compute_hash('34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167'))

unittest.main()
