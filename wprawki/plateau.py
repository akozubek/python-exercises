import unittest
"""
Finds the longest plateau in a list

    if list == []:
        raise EmptyListError()
    min = list[0]
    for val in list:
         if val < min:
             min = val
    return min         

"""
def plateau(list):
    if list == []:
        return 0

    max_len = 1
    len = 1
    cur = list[0]
    for val in list[1:]:
        if val == cur:
            len += 1
        else:
            if len > max_len:
                max_len = len            
            cur = val
            len = 1
    if len > max_len:
        max_len = len            
    return max_len

class TestPlateau(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(plateau([]), 0)
    def test_len1(self):
        self.assertEqual(plateau([1]), 1)
    def test_len2(self):
        self.assertEqual(plateau([1,0]), 1)
    def test_len2_asc(self):
        self.assertEqual(plateau([0,1]), 1)
    def test_len3_desc(self):
        self.assertEqual(plateau([1,1,-1]), 2)
    def test_len3_asc(self):
        self.assertEqual(plateau([-1,1,1]), 2)
    def test_len3_med(self):
        self.assertEqual(plateau([1,1,1]), 3)
    def test_len3_med(self):
        self.assertEqual(plateau([1,1,1,0]), 3)

if __name__ == '__main__':
    unittest.main()
