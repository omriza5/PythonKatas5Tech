import unittest
from katas.longest_common_prefix import longest_common_prefix

class TestLongestCommonPrefix(unittest.TestCase):
    def test_normal_case_with_common_prefix(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")

    def test_no_common_prefix(self):
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_common_prefix_with_longer_strings(self):
        self.assertEqual(longest_common_prefix(["interspecies", "interstellar", "interstate"]), "inters")

    def test_common_prefix_with_short_strings(self):
        self.assertEqual(longest_common_prefix(["apple", "apricot", "ape"]), "ap")

    def test_single_string_in_list(self):
        self.assertEqual(longest_common_prefix(["single"]), "single")

    def test_empty_list(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_list_with_empty_strings(self):
        self.assertEqual(longest_common_prefix(["", "", ""]), "")

    def test_mixed_empty_and_nonempty_strings(self):
        self.assertEqual(longest_common_prefix(["", "nonempty", "none"]), "")

if __name__ == "__main__":
    unittest.main()
