import pytest
from katas.true_counter import count_true_values

def test_count_true_values():
    # Test case 1: Normal case with mixed True and False
    assert count_true_values([True, False, True, True, False]) == 3

    # Test case 2: All True values
    assert count_true_values([True, True, True, True]) == 4

    # Test case 3: All False values
    assert count_true_values([False, False, False, False]) == 0

    # Test case 4: Empty list
    assert count_true_values([]) == 0

    # Test case 5: Single True value
    assert count_true_values([True]) == 1

    # Test case 6: Single False value
    assert count_true_values([False]) == 0
