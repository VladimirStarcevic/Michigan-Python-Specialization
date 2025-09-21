class Letter:
    letter: str
    in_correct_place: bool
    in_word: bool

    def __init__(self, letter: str) -> None:
        self.letter = letter
        self.in_correct_place = False
        self.in_word = False

    def is_in_correct_place(self) -> bool:
        return self.in_correct_place

    def is_in_word(self) -> bool:
        return  self.in_word