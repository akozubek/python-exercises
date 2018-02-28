import unittest

def move(layer):
    if len(layer) <= 1:
        return
    try: 
        index = layer.index(1)
        layer[index] = 0
        if index == len(layer) - 1:
            layer[index - 1] = -1
        else: 
            layer[index + 1] = 1
    except:
        index = layer.index(-1)
        layer[index] = 0
        if index == 0:
            layer[1] = 1
        else: 
            layer[index - 1] = -1

def severity(spec):
   layers = list()
   index = 0
   for line in spec:
       [layer, depth] = [ int(l) for l in (line.split(": ")) ]
       print(layer, depth)
       for i in range(index, layer): 
           layers.append([])
           index += 1
       layers.append([0] * depth)
       layers[layer][0] = 1
       index += 1

   sev = 0
   for i in range(0, len(layers)):
       print("Picosecond", i)
       print(layers)
       if len(layers[i]) > 0 and layers[i][0] != 0:
           # caught!
           sev += i * len(layers[i])
       # move scanners
       for l in layers:
           move(l)

       # move packet
   return sev

class Test(unittest.TestCase):
    def test1(self):
        input = ['0: 3','1: 2', '4: 4', '6: 4']
        self.assertEqual(severity(input), 24)

with open("day13.txt") as file:
    print("Result:", severity(file.readlines()))

unittest.main()
