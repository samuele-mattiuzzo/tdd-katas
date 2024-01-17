import unittest

from kata import Mumble


class MumbleTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MumbleTest, self).__init__(*args, **kwargs)
        self.samples = [
            {'input': 'a', 'expected': 'A'},
            {'input': 'ab', 'expected': 'A-Bb'},
            {'input': 'abC', 'expected': 'A-Bb-Ccc'},
            {'input': 'aBCd', 'expected': 'A-Bb-Ccc-Dddd'},
            {'input': 'QWERTY', 'expected': 'Q-Ww-Eee-Rrrr-Ttttt-Yyyyyy'}
        ]

    def test_can_handle_empty_string(self):
        mumble = Mumble()
        self.assertEqual(
            mumble.mumble_letters(''),
            ''
        )

    def test_can_handle_null_string(self):
        mumble = Mumble()
        self.assertEqual(
            mumble.mumble_letters(None),
            Mumble.ERROR_MESSAGE
        )

    def test_converts_first_letter_to_uppercase(self):
        mumble = Mumble()
        sample = self.samples[0]
        self.assertEqual(
            mumble.mumble_letters(
                sample['input']
            ),
            sample['expected']
        )

    def test_repeats_letters_based_on_position(self):
        mumble = Mumble()
        sample = self.samples[1]
        self.assertEqual(
            mumble.mumble_letters(
                sample['input']
            ),
            sample['expected']
        )

    def test_returns_correct_format_and_output_abc(self):
        mumble = Mumble()
        sample = self.samples[2]
        self.assertEqual(
            mumble.mumble_letters(
                sample['input']
            ),
            sample['expected']
        )

    def test_returns_correct_format_and_output_abcd(self):
        mumble = Mumble()
        sample = self.samples[3]
        self.assertEqual(
            mumble.mumble_letters(
                sample['input']
            ),
            sample['expected']
        )

    def test_returns_correct_format_and_output_qwerty(self):
        mumble = Mumble()
        sample = self.samples[3]
        self.assertEqual(
            mumble.mumble_letters(
                sample['input']
            ),
            sample['expected']
        )

if __name__ == '__main__':
    unittest.main()
