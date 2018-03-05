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
             l1 = programs_list[p1]
             l2 = programs_list[p2]
             programs_list[p1] = l2
             programs_list[p2] = l1
        elif move.startswith('p'):
             l1 = move[1:].split('/')[0]
             l2 = move[1:].split('/')[1]
             p1 = programs_list.index(l1)
             p2 = programs_list.index(l2)
             programs_list[p1] = l2
             programs_list[p2] = l1
    return ''.join(programs_list)

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(dance('abcde', 's1,x3/4,pe/b'), 'baedc')

with open("day16.txt") as file:
   for line in file:
       print("Result", dance('abcdefghijklmnop', line))
unittest.main()
