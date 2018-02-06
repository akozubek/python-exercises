
import unittest

def isleap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False
    #  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

class Test(unittest.TestCase):
    def test2000(self):
        self.assertEqual(isleap(2000), True)
    def test1982(self):
        self.assertEqual(isleap(1982), False)
    def test1981(self):
        self.assertEqual(isleap(1981), False)
    def test1981(self):
        self.assertEqual(isleap(1983), False)
    def test1900(self):
        self.assertEqual(isleap(1900), False)
    def test1800(self):
        self.assertEqual(isleap(1800), False)
    def test1700(self):
        self.assertEqual(isleap(1700), False)
    def test1600(self):
        self.assertEqual(isleap(1600), True)

if __name__ == '__main__':
    unittest.main()
