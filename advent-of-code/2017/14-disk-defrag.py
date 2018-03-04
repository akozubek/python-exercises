import unittest

# Day 10 code

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

# end of Day 10 code

def compute_binary(hash):
    scale = 16
    bits = 4
    res = ''
    for d in hash:
        res += (bin(int(d, scale))[2:].zfill(bits))
    return res

def disk(input):
    inputs = [ input + '-' + str(i) for i in range(0,128)]
    hashes = [ compute_hash(i) for i in inputs ]
    binary = [ compute_binary(h) for h in hashes ]
    return binary

def disk_count(input):
    binary = disk(input)
    sum = 0
    for row in binary:
        for s in row:
            sum += int(s)
    return sum

def neighbors(square, squares):
    (x,y) = square
    neighbors = set()
    for i in range(-1,1):
        for j in range(-1,1):
            nx = x + i
            ny = y + j
            if i * j == 0 and 0 <= nx < 128 and 0 <= ny < 128:
                 if (nx, ny) in squares:
                     neighbors.add((nx, ny))
    return neighbors 

def disk_groups(input):
    binary = disk(input)
    squares = dict()
    for i in range(0, 128):
        for j in range(0, 128):
            if binary[i][j] == '1':
                 squares[(i,j)] = { (i,j) }
    for square in squares:
        ns = neighbors(square, squares)
        squares[square].update(ns)
        for n in squares[square].copy():
            squares[square].update(squares[n])
        for n in squares[square]:
            squares[n].update(squares[square])

    sorted_groups = [ sorted(group) for group in squares.values() ]
    labels = []
    for group in sorted_groups:
        labels.append(",".join([str(t) for t in group ]))
    return len(set(labels))

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(disk_count('flqrgnkx'), 8108)

    def test2(self):
        self.assertEqual(disk_groups('flqrgnkx'), 1242)

input = 'nbysizxe'
print("Result:", disk_count(input))
print("Result 2:", disk_groups(input))

unittest.main()
