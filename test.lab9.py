import unittest
from wchain import longest_chain

class TestLongestChain(unittest.TestCase):
    def test_example_1(self):
        words = [
            "crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"
        ]
        self.assertEqual(longest_chain(words), 2)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        self.assertEqual(longest_chain(words), 2)

    def test_example_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        self.assertEqual(longest_chain(words), 1)

    def test_single_word(self):
        self.assertEqual(longest_chain(["abc"]), 1)

    def test_chain_of_length_5(self):
        words = ["a", "ab", "abc", "abcd", "abcde"]
        self.assertEqual(longest_chain(words), 5)

    def test_multiple_chains(self):
        words = ["a", "ab", "abc", "b", "bc", "bcd", "bcde"]
        self.assertEqual(longest_chain(words), 4)  # abcde > abcd > abc > ab > a

if __name__ == "__main__":
    unittest.main()
