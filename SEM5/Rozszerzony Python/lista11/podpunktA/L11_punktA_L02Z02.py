# python3 -m unittest L11-punktA-L02Z02.py

import unittest
import L02Z02

class TestSqrt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(L02Z02.pierwiastek(2), 1)
    
    def test_2(self):
        self.assertEqual(L02Z02.pierwiastek(4), 2)
        
    def test_3(self):
        self.assertEqual(L02Z02.pierwiastek(16), 4)
        
    def test_4(self):
        self.assertEqual(L02Z02.pierwiastek(20), 4)
        
    def test_5(self):
        self.assertEqual(L02Z02.pierwiastek(220), 14)
        
    def test_6(self):
        self.assertEqual(L02Z02.pierwiastek(225), 15)
        
    def test_7(self):
        self.assertEqual(L02Z02.pierwiastek(227), 15)
        
    def test_8(self):
        self.assertEqual(L02Z02.pierwiastek(5), 2)
        
    def test_9(self):
        self.assertEqual(L02Z02.pierwiastek(8), 2)
        
    def test_10(self):
        self.assertEqual(L02Z02.pierwiastek(13), 3)

# na wykładzie
    result = [
       (2, 1), (4, 2),
       (5, 2), (8, 2),
       (16, 4), (20, 4),
       (220, 14), (227, 15)
    ]

    def test_11(self):
        for(n, res) in self.result:
            ans = L02Z02.pierwiastek(n)
            self.assertEqual(ans, res)

if __name__ == '__main__':
    unittest.main()
