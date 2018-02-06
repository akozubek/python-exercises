import unittest
"""
Finds minimum in a list.

We need:
- know what to do with empty list!
- exceptions
- for loop
- if
- lists
"""
def minimum(list):
    if list == []:
        raise EmptyListError()
    min = list[0]
    for val in list:
         if val < min:
             min = val
    return min         

class EmptyListError(Exception):
    pass

class TestMinimum(unittest.TestCase):
    def test_empty(self):
        self.assertRaises(EmptyListError, minimum, [])
    def test_len1(self):
        self.assertEqual(minimum([1]), 1)
    def test_len2_desc(self):
        self.assertEqual(minimum([1,0]), 0)
    def test_len2_asc(self):
        self.assertEqual(minimum([0,1]), 0)
    def test_len3_desc(self):
        self.assertEqual(minimum([1,0,-1]), -1)
    def test_len3_asc(self):
        self.assertEqual(minimum([-1,0,1]), -1)
    def test_len3_med(self):
        self.assertEqual(minimum([1,-4,1]), -4)

if __name__ == '__main__':
    unittest.main()
