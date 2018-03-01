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

def create_layers(spec):
    layers = list()
    index = 0
    for line in spec:
        [layer, depth] = [ int(l) for l in (line.split(": ")) ]
        for i in range(index, layer): 
            layers.append([])
            index += 1
        layers.append([0] * depth)
        layers[layer][0] = 1
        index += 1
    return layers

def severity(spec):
   layers = create_layers(spec)

   sev = 0
   for i in range(0, len(layers)):
       if len(layers[i]) > 0 and layers[i][0] != 0:
           # caught!
           sev += i * len(layers[i])
       # move scanners
       for l in layers:
           move(l)
   return sev

def severity2(spec):
    # create layers
    layers = create_layers(spec)

    delays = []
    picosecond = 0
    while True:
        delays.append(picosecond)
        # check if any delays are caught
        for d in delays[:]:
            # where in this picosecond is the packet with delay d
            position = picosecond - d
            if position == len(layers):
                 # finally found it!
                 return d
           
            if len(layers[position]) > 0 and layers[position][0] != 0:
                # caught! => remove
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

unittest.main()
