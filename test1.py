import unittest
import cube

class Testcube(unittest.TestCase):
    def test_perf(self):
        v = cube.c(1,2,3)
        self.assertEqual(v,6)
    def test_negative(self):
        n = cube.c(-2,-4,-10)
        self.assertEqual(n,'error') #can't be a negative number 
    def test_complexnumber(self):
        v = cube.c(3.4,5,1.5)
        self.assertEqual(v,25.5)
    
if __name__ == '__main__':
    unittest.main()