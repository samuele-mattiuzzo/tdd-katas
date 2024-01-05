class BowlingScorer:

    def __init__(self, *args, **kwargs):
        super(BowlingScorer, self).__init__(*args, **kwargs)
        self.frames = ""

    def set_frames(self, frames):
        self.frames = frames

    def sum_frame(self, frame):
        return sum(
            [int(num) for num in frame]
        )

    def get_score(self):
        score = 0
        all_frames = self.frames.split(" ")

        for idx, frame in enumerate(all_frames):
            if frame == "X":
                score += 10
                if idx < len(all_frames) - 2:
                    first_frame = all_frames[idx + 1]
                    second_frame = all_frames[idx + 2]
                    score += self.sum_frame(first_frame)
                    score += self.sum_frame(second_frame)
            elif "/" in frame:
                score += 10
                if idx < len(all_frames) - 1:
                    next_frame = all_frames[idx + 1]
                    score += self.sum_frame(next_frame)
            else:
                score += self.sum_frame(frame)

        return score
