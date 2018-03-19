import unittest
import csv
from itertools import combinations


input = 'day2.txt'

def checksum_original(filename):
    sum = 0
    with open(filename) as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            nums = [int(cell) for cell in row]
            sum = sum + (max(nums) - min(nums))
    return sum

def find_checksum_original(nums):
    i = 1
    for c in nums:
        for d in nums[i:]:
            if c % d == 0 or d % c == 0:
                return max(c//d, d//c)
        i += 1
    return 0

def checksum2_original(filename):
    sum = 0
    with open(filename) as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            nums = [int(cell) for cell in row]
            c_sum = find_checksum(nums)
            sum = sum + c_sum 
    return sum

def checksum(filename):
    with open(filename) as f:
        lines = [list(map(int, line.split())) for line in f]
        return sum(max(l) - min(l) for l in lines)

def checksum2(filename):
    with open(filename) as f:
        lines = [list(map(int, line.split())) for line in f]
        return sum(y//x for l in lines for x,y in combinations(sorted(l),2) if y % x == 0)

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(checksum('day2-test.txt'), 18)
    def test2(self):
        self.assertEqual(checksum2('day2-test2.txt'), 9)
    def test1_input(self):
        self.assertEqual(checksum('day2.txt'), 43074)
    def test1_input(self):
        self.assertEqual(checksum2('day2.txt'), 280)

print("Result:", checksum(input))
print("Result 2:", checksum2(input))
unittest.main()

