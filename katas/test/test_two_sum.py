import unittest
from katas.two_sum import two_sum

class TestTwoSum(unittest.TestCase):
    def test_normal_case_with_solution_1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_normal_case_with_solution_2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_case_with_duplicate_numbers(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_case_with_no_solution(self):
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 10), [])

    def test_case_with_negative_numbers(self):
        self.assertEqual(two_sum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_case_with_mixed_positive_and_negative_numbers(self):
        self.assertEqual(two_sum([-10, 20, 10, -20], 0), [0, 2])

    def test_case_with_single_element(self):
        self.assertEqual(two_sum([1], 1), [])

    def test_case_with_empty_list(self):
        self.assertEqual(two_sum([], 0), [])

if __name__ == "__main__":
    unittest.main()
