import unittest

def dance(programs, moves):
    moves = moves.split(',')
    programs_list = list(programs)
    for move in moves: 
        if move.startswith('s'):
             steps = len(programs_list) - int(move[1:])
             programs_list = programs_list[steps:] + programs_list[:steps]
        elif move.startswith('x'):
             p1 = int(move[1:].split('/')[0])
             p2 = int(move[1:].split('/')[1])
             letter1 = programs_list[p1]
             letter2 = programs_list[p2]
             programs_list[p1] = letter2
             programs_list[p2] = letter1
        elif move.startswith('p'):
             letter1 = move[1:].split('/')[0]
             letter2 = move[1:].split('/')[1]
             p1 = programs_list.index(letter1)
             p2 = programs_list.index(letter2)
             programs_list[p1] = letter2
             programs_list[p2] = letter1
    return ''.join(programs_list)

def dance2(programs, moves):
    orig_programs = programs
    limit = 1000000000 
    for i in range(0, limit):
        programs = dance(programs, moves)
        if orig_programs == programs:
             break
    print("Period is", i+1)
    remainder = limit % (i+1)
    print("Remainder is ", remainder)

    for i in range(0, remainder):
        programs = dance(programs, moves)
    return programs

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(dance('abcde', 's1,x3/4,pe/b'), 'baedc')

with open("day16.txt") as file:
   for line in file:
       print("Result", dance('abcdefghijklmnop', line))

with open("day16.txt") as file:
   for line in file:
       print("Result2", dance2('abcdefghijklmnop', line))
unittest.main()
