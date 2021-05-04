import unittest
import name

class Testcube(unittest.TestCase):
    def test_works(self):
        v = name.n('dulla', 'o')
        self.assertEqual(v,'dulla o')
    def test_notstring(self):
        n = name.n('james', 3)
        self.assertEqual(n,'error') #can't input a number
    def test_empty(self):
        v = name.n('yooo', ' ')
        self.assertEqual(v,'yooo  ')
    
if __name__ == '__main__':
    unittest.main()