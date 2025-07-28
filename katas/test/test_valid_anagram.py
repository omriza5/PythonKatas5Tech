import unittest
from katas.valid_anagram import is_anagram

class TestIsAnagram(unittest.TestCase):

    def test_valid_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("elbow", "below"))
        self.assertTrue(is_anagram("study", "dusty"))
        self.assertTrue(is_anagram("The Eyes", "They See"))

    def test_invalid_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))

    def test_case_insensitivity(self):
        self.assertTrue(is_anagram("Listen", "Silent"))
        self.assertTrue(is_anagram("Elbow", "Below"))

    def test_ignore_spaces(self):
        self.assertTrue(is_anagram("The Eyes", "They See"))
        self.assertTrue(is_anagram("New York Times", "Monkeys Write"))

    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))

    def test_different_lengths(self):
        self.assertFalse(is_anagram("abc", "abcd"))

    def test_special_characters(self):
        self.assertTrue(is_anagram("a!b@c", "c@b!a"))
        self.assertFalse(is_anagram("a!b@c", "c@b!d"))

if __name__ == "__main__":
    unittest.main()
