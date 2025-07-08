import unittest
from katas.list_diff import find_difference


class TestListDiff(unittest.TestCase):
    def test_positive_numbers(self):
        """Test with a list of positive numbers."""
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)
        self.assertEqual(find_difference([1, 2, 3, 4, 5]), 4)

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        self.assertEqual(find_difference([-10, -20, -30, -40]), 30)
        self.assertEqual(find_difference([-1, -2, -3, -4, -5]), 4)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers."""
        self.assertEqual(find_difference([-10, 0, 10, 20]), 30)
        self.assertEqual(find_difference([-5, 5, -15, 15]), 30)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(find_difference([42]), 0)

    def test_empty_list(self):
        """Test with an empty list (should raise an error)."""
        with self.assertRaises(IndexError):
            find_difference([])


if __name__ == '__main__':
    unittest.main()
