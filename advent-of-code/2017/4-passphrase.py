import unittest

def isvalid(passphrase):
    words = passphrase.split()
    return len(set(words)) == len(words)

def isvalid2(passphrase):
    words = passphrase.split()
    canonic_words = [''.join(sorted(w)) for w in words]
    return len(set(canonic_words)) == len(canonic_words)

def countvalid(filename, valid_function):
    with open(filename) as file:
        return sum([1 for line in file if valid_function(line) ])


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(isvalid('aa bb cc dd ee'), True)
    def test2(self):
        self.assertEqual(isvalid('aa bb cc dd aa'), False)
    def test3(self):
        self.assertEqual(isvalid('aa bb cc dd aaa'), True)

    def test21(self):
        self.assertEqual(isvalid2('abcde fghij'), True)
    def test22(self):
        self.assertEqual(isvalid2('abcde xyz ecdab'), False)
    def test23(self):
        self.assertEqual(isvalid2('a ab abc abd abf abj'), True)
    def test24(self):
        self.assertEqual(isvalid2('iiii oiii ooii oooi'), True)
    def test25(self):
        self.assertEqual(isvalid2('oiii ioii iioi iiio'), False)


print('Result:', countvalid('day4.txt', isvalid))
print('Result:', countvalid('day4.txt', isvalid2))
unittest.main()
