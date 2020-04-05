from roman import Solution
import unittest


class TestRoman(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one_letter(self):
        self.assertEqual(1, self.sol.romanToInt("I"))

    def test_five(self):
        self.assertEqual(5, self.sol.romanToInt("V"))

    def test_ten(self):
        self.assertEqual(10, self.sol.romanToInt("X"))

    def test_fifty(self):
        self.assertEqual(50, self.sol.romanToInt("L"))

    def test_mult_one(self):
        self.assertEqual(3, self.sol.romanToInt("III"))

    def test_four(self):
        self.assertEqual(4, self.sol.romanToInt("IV"))

    def test_nine(self):
        self.assertEqual(9, self.sol.romanToInt("IX"))

    def test_nine_nine_five(self):
        self.assertEqual(995, self.sol.romanToInt("VM"))

    def test_add(self):
        self.assertEqual(58, self.sol.romanToInt("LVIII"))

    def test_fifty_three(self):
        self.assertEqual(53, self.sol.romanToInt("VLVIII"))

    def test_pieces(self):
        self.assertEqual(["IV","IV","IV"], self.sol.romanPieces("IVIVIV"))


if __name__ == "__main__":
    unittest.main()
