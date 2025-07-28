import pytest
from katas.two_sum import two_sum

def test_two_sum():
    # Test case 1: Normal case with a solution
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Test case 2: Normal case with a solution
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Test case 3: Case with duplicate numbers
    assert two_sum([3, 3], 6) == [0, 1]

    # Test case 4: Case with no solution
    assert two_sum([1, 2, 3, 4, 5], 10) == []

    # Test case 5: Case with negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    # Test case 6: Case with mixed positive and negative numbers
    assert two_sum([-10, 20, 10, -20], 0) == [0, 2]

    # Test case 7: Case with a single element (no solution)
    assert two_sum([1], 1) == []

    # Test case 8: Empty list (no solution)
    assert two_sum([], 0) == []
