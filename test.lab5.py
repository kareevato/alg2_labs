import unittest
from labyrinth import bfs

class TestLabyrinth(unittest.TestCase):
    def test_shortest_path(self):
        matrix = [
            [1, 1, 1],
            [0, 1, 0],
            [1, 1, 1]
        ]
        start = (0, 0)
        end = (2, 2)
        rows, cols = 3, 3
        self.assertEqual(bfs(matrix, start, end, rows, cols), 4)

    def test_no_path(self):
        matrix = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 1, 1]
        ]
        start = (0, 0)
        end = (2, 2)
        rows, cols = 3, 3
        self.assertEqual(bfs(matrix, start, end, rows, cols), -1)

if __name__ == '__main__':
    unittest.main()
