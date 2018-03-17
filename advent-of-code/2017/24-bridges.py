import unittest

def dfs_strongest(remaining_components, bridge, strength, pin, max_strength):
    for c in remaining_components[:]:
        cpins = list(map(int, c.split("/")))
        if cpins[0] == pin or cpins[1] == pin:
             bridge.append(c)
             cstrength = strength + cpins[0] + cpins[1]
             cpin = cpins[1] if cpins[0] == pin else cpins[0]
             remaining_components.remove(c)
             if cstrength > max_strength:
                 max_strength = cstrength
             max_strength = dfs_strongest(remaining_components, bridge, cstrength, cpin, max_strength)
             remaining_components.append(c)
             bridge.remove(c)
             
    return max_strength

def strongest_bridge(components):
    return dfs_strongest(components, [], 0, 0, 0)

def dfs_longest(remaining_components, bridge, strength, length, pin, longest_strength, max_length):
    for c in remaining_components[:]:
        cpins = list(map(int, c.split("/")))
        if cpins[0] == pin or cpins[1] == pin:
             bridge.append(c)
             cstrength = strength + cpins[0] + cpins[1]
             cpin = cpins[1] if cpins[0] == pin else cpins[0]
             clength = length + 1
             remaining_components.remove(c)
             if clength > max_length:
                 max_length = clength
                 longest_strength = cstrength
             elif clength == max_length:
                 if cstrength > longest_strength:
                     longest_strength = cstrength
             (max_length, longest_strength) = dfs_longest(remaining_components, bridge, cstrength, clength, cpin, longest_strength, max_length)
             remaining_components.append(c)
             bridge.remove(c)
             clength = length - 1
             
    return (max_length, longest_strength)

def longest_bridge(components):
    return dfs_longest(components, [], 0, 0, 0, 0, 0)[1]

class Test(unittest.TestCase):
    def test1(self):
       test_input = [
         '0/2',
         '2/2',
         '2/3',
         '3/4',
         '3/5',
         '0/1',
         '10/1',
         '9/10']
       self.assertEqual(strongest_bridge(test_input), 31)

    def test2(self):
       test_input = [
         '0/2',
         '2/2',
         '2/3',
         '3/4',
         '3/5',
         '0/1',
         '10/1',
         '9/10']
       self.assertEqual(longest_bridge(test_input), 19)

with open("day24.txt") as file:
    print("Result:", strongest_bridge([line[:-1] for line in file.readlines()]))

with open("day24.txt") as file:
    print("Result 2:", longest_bridge([line[:-1] for line in file.readlines()]))


unittest.main()
