import unittest
from app import add
from app import sub

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add1(self):
        self.assertEqual(add(4, 3), 7)
    
    def test_add2(self):
        self.assertAlmostEqual(add(-1,9),8)
    
    def test_sub1(self):
        self.assertAlmostEqual(sub(-1,9),-10)

    def testsub2(self):
        self.assertAlmostEqual(sub(2,9),-7)

if __name__ == "__main__":
    unittest.main()