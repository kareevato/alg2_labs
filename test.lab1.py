import unittest
from find_kth_largest import find_kth_largest

class TestFindKthLargest(unittest.TestCase):
    def test_find_kth_largest(self):
        self.assertEqual(find_kth_largest([15, 7, 22, 9, 30, 18], 1), (30, 4)) 
        self.assertEqual(find_kth_largest([15, 7, 22, 9, 30, 18], 2), (22, 2))
        self.assertEqual(find_kth_largest([15, 7, 22, 9, 30, 18], 3), (18, 5))
        self.assertEqual(find_kth_largest([4, 1, 3, 2, 5], 5), (1, 1))

    def test_invalid_k(self):
        with self.assertRaises(ValueError):
            find_kth_largest([10, 20, 30], 0)
        with self.assertRaises(ValueError):
            find_kth_largest([10, 20, 30], 4)

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            find_kth_largest([], 1)
if __name__ == "__main__":
    unittest.main() 
