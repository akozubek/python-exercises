import unittest

def programs(pipes):
    connected = dict()
    for p in range(0, len(pipes)):
        connected[p] = { p }

    for pipe in pipes: 
        pipe_spec = pipe.split()
        program = int(pipe_spec[0])
        adjacent_programs = { int(p.replace(',','')) for p in pipe_spec[2:] }
        connected[program] = connected[program].union(adjacent_programs)
        for a in connected[program]:
            connected[a] = connected[a].union(connected[program])

    groups = set()
    for p in connected:
        groups.add(",".join(sorted([ str(n) for n in connected[p]] )))
    return (len(connected[0]), len(groups))

class Test(unittest.TestCase):
    def test1(self):
        input = ['0 <-> 2', '1 <-> 1', '2 <-> 0, 3, 4', '3 <-> 2, 4', '4 <-> 2, 3, 6', '5 <-> 6', '6 <-> 4, 5']
        self.assertEqual(programs(input), (6,2))

with open("day12.txt") as file:
    print("Result:", programs(file.readlines()))
    pass

unittest.main()
