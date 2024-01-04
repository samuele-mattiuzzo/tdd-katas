import unittest

from kata import TennisScorer


class TennisTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TennisTests, self).__init__(*args, **kwargs)
        self.test_scorer = TennisScorer()

    def scored_points(self, points_list=None):
        if points_list is None:
            return
        for point in points_list:
            self.test_scorer.score_point(point)

    def test_scorer_can_score_without_rounds_played(self):
        self.scored_points()
        score = self.test_scorer.get_score()

        self.assertEqual(score, 'love - love')

    def test_scorer_print_correct_when_p1_scored_once(self):
        points_list = ['p1']
        self.scored_points(points_list)
        score = self.test_scorer.get_score()

        self.assertEqual(score, 'fifteen - love')

    def test_scorer_print_correct_when_p1_scored_twice(self):
        points_list = ['p1', 'p1']
        self.scored_points(points_list)
        score = self.test_scorer.get_score()

        self.assertEqual(score, 'thirty - love')

    def test_scorer_print_correct_when_p1_scored_thrice(self):
        points_list = ['p1', 'p1', 'p1']
        self.scored_points(points_list)
        score = self.test_scorer.get_score()

        self.assertEqual(score, 'fourty - love')

    def test_scorer_print_correct_when_deuce(self):
        points_list = [
            'p1', 'p1', 'p1', 'p2', 'p2', 'p2'
        ]
        self.scored_points(points_list)
        score = self.test_scorer.get_score()

        self.assertEqual(score, 'deuce')

    def test_scorer_print_correct_when_advantage_p1(self):
        points_list = [
            'p1', 'p1', 'p1', 'p2', 'p2', 'p2', 'p1'
        ]
        self.scored_points(points_list)
        score = self.test_scorer.get_score()

        self.assertEqual(score, 'advantage p1')

    def test_scorer_print_correct_when_advantage_p2(self):
        points_list = [
            'p1', 'p1', 'p1', 'p2', 'p2', 'p2', 'p2'
        ]
        self.scored_points(points_list)
        score = self.test_scorer.get_score()

        self.assertEqual(score, 'advantage p2')

    def test_scorer_print_correct_when_victory_p1(self):
        points_list = [
            'p1', 'p1', 'p1', 'p2', 'p1'
        ]
        self.scored_points(points_list)
        score = self.test_scorer.get_score()

        self.assertEqual(score, 'victory p1')

    def test_scorer_print_correct_when_victory_p2(self):
        points_list = [
            'p2', 'p2', 'p2', 'p2'
        ]
        self.scored_points(points_list)
        score = self.test_scorer.get_score()

        self.assertEqual(score, 'victory p2')


if __name__ == '__main__':
    unittest.main()
