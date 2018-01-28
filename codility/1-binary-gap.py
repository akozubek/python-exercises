import unittest

'''
Exercise:: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

Assumptions:
        N is an integer within the range [1..2,147,483,647].
1..2^31-1

Complexity:

        expected worst-case time complexity is O(log(N));
        expected worst-case space complexity is O(1). '''


def binary(n):
    digits = [];
    m = n;
    while m > 0:
        if m % 2 == 0:
             digits = [0] + digits
        else: 
             digits = [1] + digits
        m = m//2
    return digits;

def gap(a):
    max_len = 0
    current_len = 0
    for i, val in enumerate(a):
         if val == 0:
             current_len += 1
         else: 	
             if current_len > max_len:
                 max_len = current_len
             current_len = 0
    return max_len

def solution(n):
	binary_digits = binary(n);
	return gap(binary_digits)

class TestBinaryMethod(unittest.TestCase):
    def test_one(self):
        self.assertEqual(binary(1), [1])

    def test_two(self):
        self.assertEqual(binary(2), [1,0])

    def test_three(self):
        self.assertEqual(binary(3), [1,1])

    def test_four(self):
        self.assertEqual(binary(4), [1,0,0])

    def test_ten(self):
        self.assertEqual(binary(10), [1,0,1,0])

    def test_eleven(self):
        self.assertEqual(binary(11), [1,0,1,1])

    def test_max(self):
        self.assertEqual(binary(2147483647), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])


class TestGapMethod(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(gap([]),0)

    def test_1(self):
        self.assertEqual(gap([1]),0)

    def test_0(self):
        self.assertEqual(gap([0]),0)

    def test_101(self):
        self.assertEqual(gap([1,0,1]),1)

    def test_10(self):
        self.assertEqual(gap([1,0]),0)

    def test_10010(self):
        self.assertEqual(gap([1,0,0,1]),2)

    def test_1001000(self):
        self.assertEqual(gap([1,0,0,1,0,0,0]),2)


if __name__ == '__main__':
    unittest.main()
