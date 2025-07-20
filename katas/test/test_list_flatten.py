import unittest
from katas.list_flatten import flatten_list

class TestFlattenList(unittest.TestCase):
    def test_flatten_simple(self):
        """Verifies flattening of a simple, non-nested list."""
        nested_list = [1, 2, 3]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3])

    def test_flatten_nested(self):
        """Checks flattening of a list with nested sublists."""
        nested_list = [1, [2, 3], [4, [5, 6]], 7]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4, 5, 6, 7])

    def test_flatten_empty(self):
        """Ensures flattening an empty list returns an empty list."""
        nested_list = []
        self.assertEqual(flatten_list(nested_list), [])

    def test_flatten_deeply_nested(self):
        """Tests flattening of a deeply nested list structure."""
        nested_list = [[[[1]]], 2, [[3, [4]]]]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4])

    def test_flatten_with_non_list_elements(self):
        """Confirms flattening works with mixed element types (e.g., integers and strings)."""
        nested_list = [1, "string", [2, 3], [4, [5, 6]], 7]
        self.assertEqual(flatten_list(nested_list), [1, "string", 2, 3, 4, 5, 6, 7])

    def test_flatten_with_empty_lists(self):
        """Validates flattening when the list contains empty sublists."""
        nested_list = [[], [1, [], [2, [3]]], []]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
