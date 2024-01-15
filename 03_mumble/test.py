import unittest

from kata import Mumble


class MumbleTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MumbleTest, self).__init__(*args, **kwargs)
        self.mumble = Mumble()

    def test_can_handle_empty_string(self):
        self.assertEqual(
            self.mumble.mumble_letters(''),
            ''
        )

    def test_can_handle_null_string(self):
        self.assertEqual(
            self.mumble.mumble_letters(None),
            Mumble.ERROR_MESSAGE
        )

    def test_converts_first_letter_to_uppercase(self):
        self.assertEqual(
            self.mumble.mumble_letters('a'),
            'A'
        )

    def test_repeats_letters_based_on_position(self):
        self.assertEqual(
            self.mumble.mumble_letters('ab'),
            'A-Bb'
        )

    def test_returns_correct_format_and_output(self):
        samples = [
            {'input': 'abC', 'expected': 'A-Bb-Ccc'},
            {'input': 'aBCd', 'expected': 'A-Bb-Ccc-Dddd'},
            {'input': 'QWERTY', 'expected': 'Q-Ww-Eee-Rrrr-Ttttt-Yyyyyy'}
        ]

        for sample in samples:
            self.assertEqual(
                self.mumble.mumble_letters(sample['input']),
                sample['expected']
            )
            self.mumble.clean()


if __name__ == '__main__':
    unittest.main()
