import unittest
import average

class Testcube(unittest.TestCase):
    def test_av(self):
        v = average.avg([1,2,3,4,5])
        self.assertEqual(v,3.0)
    def test_empty(self):
        n = average.avg([])
        self.assertEqual(n,'error') #can't be empty
    def test_complexnumber(self):
        v = average.avg([-30,40,50])
        self.assertEqual(v,20)
    
if __name__ == '__main__':
    unittest.main()