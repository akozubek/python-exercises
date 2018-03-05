import unittest

def count_matching(start_a, start_b):
    gen_a = start_a
    gen_b = start_b
    total = 0
    for i in range(0, 40000000):
        print("Round",i)
        binary_a = bin(gen_a)[2:].zfill(32)
        binary_b = bin(gen_b)[2:].zfill(32)
        if binary_a[16:] == binary_b[16:]:
            total += 1
        # generate next values
        gen_a = (gen_a * 16807) % 2147483647
        gen_b = (gen_b * 48271) % 2147483647
        
    return total

def count_matching2(start_a, start_b):
    gen_a = start_a
    gen_b = start_b
    total = 0
    for i in range(0, 5000000):
        print("Round",i)
        # find next values
        while gen_a % 4 != 0:
            gen_a = (gen_a * 16807) % 2147483647
        while gen_b % 8 != 0:
            gen_b = (gen_b * 48271) % 2147483647

        #compare
        binary_a = bin(gen_a)[2:].zfill(32)
        binary_b = bin(gen_b)[2:].zfill(32)
        if binary_a[16:] == binary_b[16:]:
            total += 1

        # make one more step
        gen_a = (gen_a * 16807) % 2147483647
        gen_b = (gen_b * 48271) % 2147483647
        
    return total

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_matching(65,8921), 588)
    def test2(self):
        self.assertEqual(count_matching2(65,8921), 309)

print("Result:", count_matching(699, 124))
print("Result2:", count_matching2(699, 124))
unittest.main()
