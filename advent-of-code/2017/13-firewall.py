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
   return sev


def create_layers(spec):
    layers = list()
    index = 0
    for line in spec:
        [layer, depth] = [ int(l) for l in (line.split(": ")) ]
#        print(layer, depth)
#        print(index)
        for i in range(index, layer): 
            layers.append([])
            index += 1
        layers.append([0] * depth)
#        print(layers)
        layers[layer][0] = 1
        index += 1
    return layers

def severity2(spec):
    # create layers
    layers = create_layers(spec)

    delays = []
    picosecond = 0
    while True:
        print("Picosecond:", picosecond)
        delays.append(picosecond)
        # print("Delays:", delays)
        # check if any delays are caught
        for d in delays[:]:
            # gdzie w tej picosekundzie jest pakiet wyruszajacy z opoznieniem
            # d
            position = picosecond - d
            if position == len(layers):
                 # znalezlismy?
                 return d
           
            if len(layers[position]) > 0 and layers[position][0] != 0:
                # caught!
                delays.remove(d)

        # move scanners
        for l in layers:
            move(l)
        picosecond += 1


class Test(unittest.TestCase):
    def test1(self):
        input = ['0: 3','1: 2', '4: 4', '6: 4']
        self.assertEqual(severity(input), 24)

    def test2(self):
        input = ['0: 3','1: 2', '4: 4', '6: 4']
        self.assertEqual(severity2(input), 10)

with open("day13.txt") as file:
    print("Result:", severity(file.readlines()))

with open("day13.txt") as file:
     print("Result:", severity2(file.readlines()))
     pass

unittest.main()
