import unittest

def min_particle(input):
    specs = [line.split(', ') for line in input ] 
    particles = [ list(map(int, spec[0][3:-1].split(","))) for spec in specs ]
    velocities = [ list(map(int, spec[1][3:-1].split(","))) for spec in specs ]
    accelerations = [ list(map(int, spec[2][3:-1].split(","))) for spec in specs ]
    min_i = 0
    min_dist = sum([abs(x) for x in accelerations[0]] )
    for i in range(0, len(accelerations)):
        dist = sum([abs(x) for x in accelerations[i]] )
        if dist < min_dist:
             min_dist = dist
             min_i = i
    return min_i

class Test(unittest.TestCase):
    def test1(self):
        test_input = [
          'p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>',
          'p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>'
        ]

        self.assertEqual(min_particle(test_input), 0)

with open("day20.txt") as file:
     print("Result:", min_particle([line[:-1] for line in file.readlines()]))

unittest.main()
