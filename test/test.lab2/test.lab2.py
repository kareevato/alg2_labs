# test_main.py

import unittest
from eating_speed import minEatingSpeed  

class TestMinEatingSpeed(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(minEatingSpeed([3, 6, 7, 11], 8), 4)
        self.assertEqual(minEatingSpeed([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(minEatingSpeed([30, 11, 23, 4, 20], 6), 23)

if __name__ == "__main__":
    unittest.main()
