class Mumble:

    ERROR_MESSAGE = 'Mumble needs an input'

    def __init__(self, *args, **kwargs):
        super(Mumble, self).__init__(*args, **kwargs)

        self.input = ''
        self.converted = []
        self.result = ''

    def clean(self):
        self.input = ''
        self.converted = []
        self.result = ''

    def __convert_repeats(self):
        for pos, letter in enumerate(self.input):
            self.converted.append(
                letter.lower() * (pos + 1)
            )

    def __capitalize_converted(self):
        self.converted = [
            seq.capitalize() for seq in self.converted
        ]

    def __format_converted(self):
        self.result = "-".join(self.converted)

    def mumble_letters(self, sequence):
        if sequence is None:
            return Mumble.ERROR_MESSAGE

        if not len(sequence):
            return sequence

        self.input = sequence

        self.__convert_repeats()
        self.__capitalize_converted()
        self.__format_converted()

        return self.result
