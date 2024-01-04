POINTS_INT = [
    0, 1, 2, 3
]


INT_TO_STR_MAPPING = {
    0: 'love',
    1: 'fifteen',
    2: 'thirty',
    3: 'fourty'
}

SCORE_TEMPLATE = '%s - %s'


class TennisScorer(object):

    def __init__(self, *args, **kwargs):
        super(TennisScorer, self).__init__(*args, **kwargs)
        self.p1_points = 0
        self.p2_points = 0

    def score_point(self, player):
        if player == 'p1':
            self.p1_points += 1
        elif player == 'p2':
            self.p2_points += 1

    def get_score(self):
        if (self.p1_points >= 3 or self.p2_points >= 3) and \
           self.p1_points + self.p2_points >= 4:
            if self.p1_points == self.p2_points + 1:
                return 'advantage p1'
            if self.p2_points == self.p1_points + 1:
                return 'advantage p2'
            if self.p1_points >= self.p2_points + 2:
                return 'victory p1'
            if self.p2_points >= self.p1_points + 2:
                return 'victory p2'
            if self.p1_points == self.p2_points:
                return 'deuce'

        p1_str = INT_TO_STR_MAPPING[self.p1_points]
        p2_str = INT_TO_STR_MAPPING[self.p2_points]
        return SCORE_TEMPLATE % (p1_str, p2_str)
