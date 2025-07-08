import unittest
from katas.do_n_times import *


class TestDoNTimes(unittest.TestCase):
    def test_do_n_times(self):
        """
        Tests the do_n_times function by invoking it with the say_hello function and an argument of 1.
        Asserts that the number of times say_hello is invoked matches the expected value.
        """
        self.assertEqual(do_n_times(say_hello,0), 0)
        self.assertEqual(do_n_times(say_hello,1), 1)
        self.assertEqual(do_n_times(say_hello,2), 2)

    def test_do_n_times_argument_validation(self):
        """
        Tests that do_n_times raises TypeError when passed invalid arguments.
        """
        with self.assertRaises(TypeError):
            do_n_times(None, 2)  # Not a function
        with self.assertRaises(TypeError):
            do_n_times(say_hello, "two")  # Not a number
        with self.assertRaises(TypeError):
            do_n_times(say_hello, None)  # Not a number
        with self.assertRaises(TypeError):
            do_n_times(123, 2)  # Not a function

