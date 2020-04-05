import unittest
from substring import Solution


class TestSubstring(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one_letter(self):
        self.assertEqual(1, self.sol.lengthOfLongestSubstring("bbbbbb"))

    def test_change_start(self):
        self.assertEqual(3, self.sol.lengthOfLongestSubstring("dvdf"))

    def test_empty_string(self):
        self.assertEqual(0, self.sol.lengthOfLongestSubstring(""))

    def test_end_string(self):
        self.assertEqual(4, self.sol.lengthOfLongestSubstring("asdff"))

    def test_start_string(self):
        self.assertEqual(4, self.sol.lengthOfLongestSubstring("ffasd"))

    def test_entire_string(self):
        self.assertEqual(5, self.sol.lengthOfLongestSubstring("tesfg"))

    def test_one_char(self):
        self.assertEqual(2, self.sol.lengthOfLongestSubstring("tsssss"))

    def test_same_size(self):
        self.assertEqual(4, self.sol.lengthOfLongestSubstring("asdfsdfg"))

    def test_early_char(self):
        self.assertEqual(4, self.sol.lengthOfLongestSubstring("asdfsa"))

    def test_begin_repeat(self):
        self.assertEqual(5, self.sol.lengthOfLongestSubstring("tmmzuxt"))


if __name__ == "__main__":
    unittest.main()
