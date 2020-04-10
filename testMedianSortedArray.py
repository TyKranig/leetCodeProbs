import unittest
from medianSortedArray import Solution


class TestSubstring(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_meage_array(self):
        self.assertEqual([1,2,3,4,5], self.sol.mergeArray([1,3,5],[2,4]))

    def test_merge_array2(self):
        self.assertEqual([1,2,3,4,5], self.sol.mergeArray([1,2,3],[4,5]))
    
    def test_median_array(self):
        self.assertEqual(2.5, self.sol.findMedianSortedArrays([1, 2], [3, 4]))

if __name__ == "__main__":
    unittest.main()
