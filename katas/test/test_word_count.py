import unittest
from katas.word_count import count_words

class TestCountWords(unittest.TestCase):

    def test_regular_sentence(self):
        sentence = "This is a sample sentence for counting words."
        self.assertEqual(count_words(sentence), 8)

    def test_empty_string(self):
        sentence = ""
        self.assertEqual(count_words(sentence), 0)

    def test_single_word(self):
        sentence = "Hello"
        self.assertEqual(count_words(sentence), 1)

    def test_multiple_spaces(self):
        sentence = "This   is   a   test."
        self.assertEqual(count_words(sentence), 4)

    def test_newlines_and_tabs(self):
        sentence = "This is\na test\twith tabs."
        self.assertEqual(count_words(sentence), 6)

    def test_punctuation(self):
        sentence = "Hello, world! This is a test."
        self.assertEqual(count_words(sentence), 6)

    def test_non_ascii_characters(self):
        sentence = "こんにちは 世界"
        self.assertEqual(count_words(sentence), 2)

if __name__ == "__main__":
    unittest.main()
