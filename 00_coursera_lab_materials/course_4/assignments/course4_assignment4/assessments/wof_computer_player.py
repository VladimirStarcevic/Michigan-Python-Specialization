from wof_player import WOFPlayer
import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
VOWEL_COST = 250


class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

    def smartCoinFlip(self):
        roll = random.randint(1, 10)
        return roll <= self.level

    def getPossibleLetters(self, guessed):
        possible_letters = []
        for letter in LETTERS:
            if letter not in guessed:
                if letter in VOWELS:
                    if self.prize_money >= VOWEL_COST:
                        possible_letters.append(letter)
                else:
                    possible_letters.append(letter)
        return possible_letters

    def getMove(self, category, obscured_phrase, guessed):
        possible_letters = self.getPossibleLetters(guessed)

        if not possible_letters:
            return 'pass'

        if self.smartCoinFlip():
            for letter in reversed(self.SORTED_FREQUENCIES):
                if letter in possible_letters:
                    return letter
            return None
        else:
            return random.choice(possible_letters)