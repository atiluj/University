# python3 -m unittest L11-punktA-L01Z02.py
# http://pep8online.com/

import unittest
import L01Z02


class TestPalindrom(unittest.TestCase):
    def test_1(self):
        self.assertEqual(L01Z02.is_palindrom("Kobyła ma mały bok"), True, "ok")

    def test_2(self):
        self.assertEqual(L01Z02.is_palindrom(
            "Eine gulden gute Tugned Luge nie"),
            True,
            "ok")

    def test_3(self):
        self.assertEqual(L01Z02.is_palindrom(
            "Eine gulden, gute Tugned: Luge nie!"),
            True,
            "ok")

    def test_4(self):
        self.assertEqual(L01Z02.is_palindrom("Hello world"), False, "ok")

    def test_5(self):
        self.assertEqual(L01Z02.is_palindrom("OKO"), True, "ok")

    # def test_6(self):
    #     self.assertEqual(L01Z02.is_palindrom("OKO"), False, "NOT ok")

if __name__ == '__main__':
    unittest.main()
