import unittest

from kata import WordleChecker


class WordleTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(WordleTest, self).__init__(*args, **kwargs)
        self.test_wordle = WordleChecker()

    def test_checker_returns_0_if_guess_not_in_target(self):
        self.test_wordle.check_wordle("a", "b")
        result = self.test_wordle.get_result()
        self.assertEqual(result, "0")

    def test_checker_returns_1_if_guess_in_target_not_in_position(self):
        self.test_wordle.check_wordle("ab", "ba")
        result = self.test_wordle.get_result()
        self.assertEqual(result, "11")

    def test_checker_returns_2_if_guess_in_target_in_position(self):
        self.test_wordle.check_wordle("a", "a")
        result = self.test_wordle.get_result()
        self.assertEqual(result, "2")

    def test_checker_returns_full_sequence_if_guess_in_target_in_position(self):
        self.test_wordle.check_wordle("abcaa", "acbax")
        result = self.test_wordle.get_result()
        self.assertEqual(result, "21120")
