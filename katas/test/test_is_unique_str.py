import unittest
from katas.is_unique_str import is_unique


class TestIsUnique(unittest.TestCase):
    def test_unique_characters(self):
        """Test strings with all unique characters."""
        self.assertTrue(is_unique("World"))
        self.assertTrue(is_unique("Python"))

    def test_non_unique_characters(self):
        """Test strings with repeated characters."""
        self.assertFalse(is_unique("Hello"))  # Repeated 'l'
        self.assertFalse(is_unique("Aa"))     # Case-insensitive match
        self.assertFalse(is_unique("Test"))   # Repeated 't'

    def test_empty_string(self):
        """Test an empty string."""
        self.assertTrue(is_unique(""))  # No characters, hence unique

    def test_single_character(self):
        """Test a string with a single character."""
        self.assertTrue(is_unique("A"))  # Single character is always unique

    def test_special_characters(self):
        """Test strings with special characters."""
        self.assertTrue(is_unique("!@#$%^&*()"))  # All unique special characters
        self.assertFalse(is_unique("!!"))         # Repeated '!'

    def test_numbers(self):
        """Test strings with numbers."""
        self.assertTrue(is_unique("1234567890"))  # All unique numbers
        self.assertFalse(is_unique("112345"))    # Repeated '1'


if __name__ == '__main__':
    unittest.main()
