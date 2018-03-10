import unittest

def right(dir):
    if dir == [-1,0]:
        return [0, -1]
    elif dir == [1,0]:
        return [0, 1]
    elif dir == [0,-1]:
        return [1,0]
    elif dir == [0,1]:
        return [-1,0]

def left(dir):
    return right(right(right(dir)))

def can_go_forward(i,j,dir,tubes):
    ni, nj = i + dir[0], j + dir[1]
    if ni < 0 or ni >= len(tubes):
        return False
    if nj < 0 or nj >= len(tubes[ni]):
        return False
    if tubes[ni][nj] == ' ':
        return False
    return True

def follow_tube(tubes):
    i, j = 0, tubes[0].index('|')
    dir = [1, 0]
    word = ''
    steps = 0
    while True:
        steps += 1
        if tubes[i][j].isalpha():
            word += tubes[i][j]

        if not can_go_forward(i, j, dir, tubes):
            # change direction, can't go forward, can't go back,
            # must rotate to right or to left
            rdir = right(dir)
            ldir = left(dir)
            if can_go_forward(i, j, rdir, tubes):
                dir = rdir
            elif can_go_forward(i, j, ldir, tubes):
                dir = ldir
            else: 
                # the end?
                return (word, steps)
        # go forward in new or old dir
        i, j = i + dir[0], j + dir[1]
    return (word, steps)

class Test(unittest.TestCase):
    def test1(self):
        test_input = [
          '     |          ',
          '     |  +--+    ',
          '     A  |  C    ',
          ' F---|----E|--+ ',
          '     |  |  |  D ',
          '     +B-+  +--+ ']
        self.assertEqual(follow_tube(test_input), ('ABCDEF', 38))

with open("day19.txt") as file:
     input = [line[:-1] for line in file]
     print("Result:", follow_tube(input))

unittest.main()
