import unittest

from kata import WordleChecker


class WordleTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(WordleTest, self).__init__(*args, **kwargs)
        self.test_wordle = WordleChecker()

    def test_checker_returns_0_if_guess_not_in_target(self):
        result = self.test_wordle.get_result()
        self.assertEqual(result, "0")

    def test_checker_returns_1_if_guess_in_target_not_in_position(self):
        result = self.test_wordle.get_result()
        self.assertEqual(result, "0")
