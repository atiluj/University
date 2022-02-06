# python3 -m unittest TestSuite.py 

import unittest
from L11_punktA_L01Z02 import TestPalindrom
from L11_punktA_L02Z02 import TestSqrt

if __name__ == '__main__':
    list = []
    list.append(unittest.TestLoader().loadTestsFromTestCase(TestPalindrom))
    list.append(unittest.TestLoader().loadTestsFromTestCase(TestSqrt))
    suite = unittest.TestSuite(list)