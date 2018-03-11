import unittest
import collections
import math

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

def solve_equation(idx, x1, v1, a1, x2, v2, a2):
#    print("x1=", x1[idx], "v1=", v1[idx], "a1=", a1[idx], "x2=", x2[idx], "v2=", v2[idx], "a2=", a2[idx])
    # x1 + v1 *n + a1 * (n^2+n)/2 = x2 + v2*n + a2 * (n^2 + n)/2
    # x1+ v1 * n1 + a1/2 * n^2 + a1 * n / 2 = x2+ v2 * n2 + a2/2 * n^2 + a2 * n / 2 
    # (a1-a2)/2 * n^2 + (v1 + a1 / 2 - v2 - a2/2) * n + x1 - x2 = 0
    # Delta = b^2 - 4ac

    a = (a1[idx] - a2[idx])/2
    b = (v1[idx] + a1[idx]/2 - v2[idx] - a2[idx]/2)
    c = x1[idx] - x2[idx]

    if a == 0:
        if b == 0:
            if c == 0:
                 return (0.0,)
            else:
                 return (-1.0,)
        else:
            return (-c/b,) if (c/b).is_integer() else (-1.0,)
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            return (-1.0,)
        n1 = (-b - math.sqrt(delta))/(2*a)
        n2 = (-b + math.sqrt(delta))/(2*a)
        
        if n1 >= 0 and n1.is_integer():
             if n2 >= 0 and n2.is_integer():
                 return (n1,n2)
             else:
                return (n1,)
        else:
             if n2 >= 0 and n2.is_integer():
                 return (n2,)
             else:
                return (-1.0,)


def when_collide(p1, p2, particles, velocities, accelerations):
    # We want to solve vector equation for integer n
    # x1 + v1 *n + a1 * (n^2+n)/2 = x2 + v2*n + a2 * (n^2 + n)/2
    # x1+ v1 * n1 + a1/2 * n^2 + a1 * n / 2 = x2+ v2 * n2 + a2/2 * n^2 + a2 * n / 2 
    # (a1-a2)/2 * n^2 + (v1 + a1 / 2 - v2 - a2/2) * n + x1 - x2 = 0
    # Delta = b^2 - 4ac

    x1, x2 = particles[p1], particles[p2]
    v1, v2 = velocities[p1], velocities[p2]
    a1, a2 = accelerations[p1], accelerations[p2]
  
    n0 = solve_equation(0, x1, v1, a1, x2, v2, a2)
    n1 = solve_equation(1, x1, v1, a1, x2, v2, a2)
    n2 = solve_equation(2, x1, v1, a1, x2, v2, a2)
    print(n0, n1, n2)
   
    #if n0.is_integer() and n1.is_integer() and n2.is_integer():
    nmaxs = {max(n0), max(n1), max(n2)}
    nmins = {min(n0), min(n1), min(n2)}
    if -1.0 in nmaxs:
         return -1
    if len(nmaxs) == 1 or (0 in nmaxs and len(nmaxs) == 2):
        return int(max(nmaxs))
    if (0 in nmins and len(nmins) == 2) or len(nmins) == 1:
        return int(max(nmins))
    return -1

def count_particles(input):
    specs = [line.split(', ') for line in input ] 
    particles = [ list(map(int, spec[0][3:-1].split(","))) for spec in specs ]
    velocities = [ list(map(int, spec[1][3:-1].split(","))) for spec in specs ]
    accelerations = [ list(map(int, spec[2][3:-1].split(","))) for spec in specs ]
    remaining_particles = list(range(0, len(specs)))
    collisions = collections.defaultdict(set)
    for p1 in remaining_particles:
        for p2 in range(p1+1, len(particles)):
            print("Check for collisions between", p1, "and", p2)
            round_num = when_collide(p1, p2, particles, velocities, accelerations)
            print("collision at round", round_num)
            if round_num != -1:
                 collisions[round_num].add((p1,p2))
    print("Collisions:", collisions)
    
    for r in sorted(collisions):
        removed = set()
        print("Removing particles coliding in round", r)
        for p1, p2 in collisions[r]:
            print("Collision", p1, "and", p2)
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
