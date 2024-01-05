class BowlingScorer:

    def __init__(self, *args, **kwargs):
        super(BowlingScorer, self).__init__(*args, **kwargs)
        self.frames = ""

    def set_frames(self, frames):
        self.frames = frames

    def get_next_frame(self, frame_idx, all_frames):
        if frame_idx < len(all_frames) - 1:
            return all_frames[frame_idx + 1]
        return None

    def get_first_roll_score(self, frame):
        return int(frame[0])

    def get_full_frame_score(self, frame):
        return sum([int(num) for num in frame])

    def parse_frame_to_score(self, frame, first=False):
        if frame is None:
            return 0

        if frame == "X":
            return 10

        if "/" in frame:
            return 10

        if first:
            return self.get_first_roll_score(frame)

        return self.get_full_frame_score(frame)

    def check_spare(self, frame, frame_idx, all_frames):
        score = 0
        if "/" in frame:
            next_frame = self.get_next_frame(frame_idx, all_frames)
            score += self.parse_frame_to_score(next_frame, True)
        return score

    def check_strike(self, frame, frame_idx, all_frames):
        score = 0
        if frame == "X":
            next_frame = self.get_next_frame(frame_idx, all_frames)
            score += self.parse_frame_to_score(next_frame)
        return score

    def get_score(self):
        if len(self.frames) == 0:
            return 0

        all_frames = self.frames.split(" ")
        score = 0

        for idx, frame in enumerate(all_frames):
            score += self.parse_frame_to_score(frame)
            score += self.check_spare(frame, idx, all_frames)
            score += self.check_strike(frame, idx, all_frames)

        return score
