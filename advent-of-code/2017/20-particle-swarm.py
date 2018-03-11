import unittest
import collections
import math

class NoCollision(Exception):
    pass

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

def valid_round_number(x):
    if x >= 0 and x.is_integer():
         return x
    else:
         raise NoCollision

def find_colliding_rounds(idx, x1, v1, a1, x2, v2, a2):
    # We solve equation (in positive integers)
    # x1 + v1 *n + a1 * (n^2+n)/2 = x2 + v2*n + a2 * (n^2 + n)/2
    # x1+ v1 * n1 + a1/2 * n^2 + a1 * n / 2 = x2+ v2 * n2 + a2/2 * n^2 + a2 * n / 2 
    # (a1-a2)/2 * n^2 + (v1 + a1 / 2 - v2 - a2/2) * n + x1 - x2 = 0

    a = (a1[idx] - a2[idx])/2
    b = (v1[idx] + a1[idx]/2 - v2[idx] - a2[idx]/2)
    c = x1[idx] - x2[idx]

    round_numbers = set()
    if a == 0:
        if b == 0:
            if c == 0:
                 return round_numbers
            else:
                 raise NoCollision
        else:
            round_numbers.add(valid_round_number(-c/b))
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            raise NoCollision
        
        try:
            n = (-b - math.sqrt(delta))/(2*a)
            round_numbers.add(valid_round_number(n))
        except NoCollision:
            pass
 
        try:
            n = (-b + math.sqrt(delta))/(2*a)
            round_numbers.add(valid_round_number(n))
        except NoCollision:
            pass

    if not round_numbers:
        raise NoCollision
    return round_numbers


def when_collide(p1, p2, particles, velocities, accelerations):
    # We want to solve vector equation for integer n
    # x1 + v1 *n + a1 * (n^2+n)/2 = x2 + v2*n + a2 * (n^2 + n)/2

    x1, x2 = particles[p1], particles[p2]
    v1, v2 = velocities[p1], velocities[p2]
    a1, a2 = accelerations[p1], accelerations[p2]
  
    n0 = find_colliding_rounds(0, x1, v1, a1, x2, v2, a2)
    n1 = find_colliding_rounds(1, x1, v1, a1, x2, v2, a2)
    n2 = find_colliding_rounds(2, x1, v1, a1, x2, v2, a2)
   
    nmaxs = {max(n0, default = None), max(n1, default = None), max(n2, default = None)}
    nmins = {min(n0, default = None), min(n1, default = None), min(n2, default = None)}
    if None in nmaxs:
         nmaxs.remove(None)
    if None in nmins:
         nmins.remove(None)

    if len(nmaxs) == 1: 
        return int(max(nmaxs))
    if len(nmins) == 1:
        return int(max(nmins))
    raise NoCollision

def count_particles(input):
    specs = [line.split(', ') for line in input ] 
    particles = [ list(map(int, spec[0][3:-1].split(","))) for spec in specs ]
    velocities = [ list(map(int, spec[1][3:-1].split(","))) for spec in specs ]
    accelerations = [ list(map(int, spec[2][3:-1].split(","))) for spec in specs ]

    remaining_particles = list(range(0, len(specs)))
    collisions = collections.defaultdict(set)

    for p1 in remaining_particles:
        for p2 in range(p1+1, len(particles)):
            print("Collision between", p1, p2)
            try:
               round_num = when_collide(p1, p2, particles, velocities, accelerations)
               collisions[round_num].add((p1,p2))
            except NoCollision:  
               print("No collision")
               pass
    print("Collisions:", collisions)
    
    # Remove colliding particles for each round
    for r in sorted(collisions):
        removed = set()
        for p1, p2 in collisions[r]:
            if p1 in remaining_particles and p2 in remaining_particles:
                 removed.add(p1)
                 removed.add(p2)
        for p in removed:
            remaining_particles.remove(p)

    return len(remaining_particles)

class Test(unittest.TestCase):
    def test1(self):
        test_input = [
          'p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>',
          'p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>'
        ]

        self.assertEqual(min_particle(test_input), 0)
    def test2(self):
        test_input = [
           'p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>',
           'p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>',
           'p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>',
           'p=< 3,0,0>, v=<-1,0,0>, a=<0,0,0>',
        ]

        self.assertEqual(count_particles(test_input), 1)

with open("day20.txt") as file:
     print("Result:", min_particle([line[:-1] for line in file.readlines()]))

with open("day20.txt") as file:
     print("Result 2:", count_particles([line[:-1] for line in file.readlines()]))

unittest.main()
