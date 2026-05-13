import unittest
from app import add

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add1(self):
        self.assertEqual(add(4, 3), 7)
    
    def test_add2(self):
        self.assertAlmostEqual(add(-1,9),8)

if __name__ == "__main__":
    unittest.main()