import pytest
from katas.longest_common_prefix import longest_common_prefix

def test_longest_common_prefix():
    # Test case 1: Normal case with a common prefix
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

    # Test case 2: No common prefix
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""

    # Test case 3: Common prefix with longer strings
    assert longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters"

    # Test case 4: Common prefix with short strings
    assert longest_common_prefix(["apple", "apricot", "ape"]) == "ap"

    # Test case 5: Single string in the list
    assert longest_common_prefix(["single"]) == "single"

    # Test case 6: Empty list
    assert longest_common_prefix([]) == ""

    # Test case 7: List with empty strings
    assert longest_common_prefix(["", "", ""]) == ""

    # Test case 8: Mixed empty and non-empty strings
    assert longest_common_prefix(["", "nonempty", "none"]) == ""
