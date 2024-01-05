import unittest

from kata import BowlingScorer


class BowlingTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BowlingTest, self).__init__(*args, **kwargs)
        self.test_scorer = BowlingScorer()

    def test_can_print_score_with_no_rolls(self):
        score = self.test_scorer.get_score()

        self.assertEqual(score, 0)

    def test_can_print_score_if_strike(self):
        self.test_scorer.set_frames("X")
        score = self.test_scorer.get_score()

        self.assertEqual(score, 10)

    def test_can_print_score_if_two_valid_rolls(self):
        self.test_scorer.set_frames("12")
        score = self.test_scorer.get_score()

        self.assertEqual(score, 3)

    def test_can_print_score_if_spare(self):
        self.test_scorer.set_frames("1/")
        score = self.test_scorer.get_score()

        self.assertEqual(score, 10)

    def test_can_print_score_from_list_of_frames_basic(self):
        self.test_scorer.set_frames("46 32 46")
        score = self.test_scorer.get_score()

        self.assertEqual(score, 25)

    def test_can_print_score_from_list_of_frames_spare(self):
        self.test_scorer.set_frames("46 3/ 32")
        score = self.test_scorer.get_score()

        self.assertEqual(score, 30)