import unittest

# Global dictionaries to make matching faster
# Ugly, I know
flip_dict = dict()
rot_dict = dict()
matches_dict = dict()
matching_patterns_dict = dict()

def str(square):
    return "/".join(square)

def flip(square):
    try:
        flip_dict[str(square)]
    except:
        pass

    r = []
    for i in range(0, len(square)):
        line = ""
        for j in range(1, len(square)+1):
            line += square[i][len(square)-j]
        r.append(line)
    flip_dict[str(square)] = tuple(r)
    return tuple(r)

def rot(square):
    try:
        rot_dict[str(square)]
    except:
        pass

    r = []
    for i in range(0, len(square)):
        line = ""
        for j in range(1, len(square)+1):
            line += square[len(square)-j][i]
        r.append(line)
    rot_dict[str(square)] =  tuple(r)
    return tuple(r)

def matches(pattern, square):
    try:
       return matches_dict[(pattern,str(square))]
    except:
       pass

    psq = tuple(pattern.split("/"))
    if len(psq) != len(square):
        return False
    # else: same size of pattern and square
    rotations = { psq, rot(psq), rot(rot(psq)), rot(rot(rot(psq))), flip(psq), rot(flip(psq)), rot(rot(flip(psq))), rot(rot(rot(flip(psq)))), rot(flip(psq))}
    result = tuple(square) in rotations
    matches_dict[(pattern, str(square))] = result
    return result

def apply_pattern(patterns, square):
    try:
        return matching_patterns_dict[str(square)]
    except:
        pass
    
    for pattern in patterns:
        if matches(pattern, square):
             result = patterns[pattern].split("/")
             matching_patterns_dict[str(square)] = result
             return result
    raise ValueError("No match found!", square)

def merge(new_grid):
    grid = []
    size = len(new_grid[0][0][0])
    for i in range(0, len(new_grid)):
        for x in range(0, size):
             grid.append("")
        for j in range(0, len(new_grid)):
            for k in range(0, size):
                grid[size*i+k] += new_grid[i][j][k]
    return grid

def print_grid(grid):
    for line in grid:
        print(line)

def pixels(input, iterations):
    grid = ['.#.', '..#', '###']
    patterns = {elem[0]:elem[1] for elem in (line.split(' => ') for line in input)}
    for x in range (0, iterations):
        print("Round", x)
        new_grid = []
        if len(grid) % 2 == 0:
           size = 2
        else:
           size = 3
        for i in range(0, int(len(grid)/size)):
            new_grid.append([])
            for j in range(0, int(len(grid)/size)):
                square = [line[size*j:size*(j+1)] for line in grid[size*i:size*(i+1)]]
                new_grid[i].append(apply_pattern(patterns, square))
        grid = merge(new_grid)
    return sum([1 for line in grid for elem in line if elem == '#'])

class Test(unittest.TestCase):
    def setUp(self):
        global matches_dict, matching_patterns_dict, rot_dict, flip_dict
        matches_dict = dict()
        matching_patterns_dict = dict()
        rot_dict = dict()
        flip_dict = dict()

    def test1(self):
        test_input = [
            '../.# => ##./#../...',
            '.#./..#/### => #..#/..../..../#..#'
        ]
        self.assertEqual(pixels(test_input, 2), 12)


with open("day21.txt") as file:
    input = [line[:-1] for line in file.readlines()]
    print("Result:", pixels(input, 18))

unittest.main()

