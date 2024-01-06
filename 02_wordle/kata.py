class WordleChecker:

    def __init__(self, *args, **kwargs):
        super(WordleChecker, self).__init__(*args, **kwargs)
        self.result = ''

    def get_result(self):
        return self.result

    def check_wordle(self, target, guess):
        tmp_result = ''

        for g_idx, g_symbol in enumerate(guess):
            if g_symbol in target:
                if target[g_idx] != g_symbol:
                    tmp_result += '1'
                else:
                    tmp_result += '2'
            else:
                tmp_result += '0'

        if not len(tmp_result):
            tmp_result = '0'

        self.result = tmp_result
