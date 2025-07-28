import unittest
from katas.true_counter import count_true_values

class TestCountTrueValues(unittest.TestCase):
    def test_mixed_true_false(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)

    def test_all_true(self):
        self.assertEqual(count_true_values([True, True, True, True]), 4)

    def test_all_false(self):
        self.assertEqual(count_true_values([False, False, False, False]), 0)

    def test_empty_list(self):
        self.assertEqual(count_true_values([]), 0)

    def test_single_true(self):
        self.assertEqual(count_true_values([True]), 1)

    def test_single_false(self):
        self.assertEqual(count_true_values([False]), 0)

if __name__ == '__main__':
    unittest.main()
