
class Guess:

    def __init__(self, word):
        self.numTries = int()
        self.secretWord = word

    def display(self):
        print('Current:', '')
        print('Tries:', '')

    def guess(self, character):
        self.guessedChars |= {character}
        if character not in self.secretWord:
            return False
        else:
            currentStatus = ''
            matches = 0
            for c in self.secretWord:
                if c in self.guessedChars:
                    currentStatus += c
                else:
                    currentStatus += '_'

            self.currentStatus = currentStatus