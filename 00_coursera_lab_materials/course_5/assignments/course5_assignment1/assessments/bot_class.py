from typing import List
from letter_class import Letter
import random
class Bot:
    word_list: List[str]

    def __init__(self, word_list_file: str) -> None:
        try:
            with open(word_list_file, encoding='UTF-8') as f_in:

                lines = f_in.readlines()
                self.word_list = [line.strip().upper() for line in lines]


        except FileNotFoundError:
            print(f"File not found")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        self.known_letters = ['_'] * 5
        self.unused_letters = set()
        self.misplaced_letters = set()


    def make_guess(self) -> str:
        size = len(self.word_list) - 1
        random_element = random.randint(0, size)
        return self.word_list[random_element]

    def record_guess_results(self, guess: str, guess_results: List['Letter']) -> None:

        for i, letter_obj in enumerate(guess_results):

            if letter_obj.is_in_correct_place():

                self.known_letters[i] = letter_obj.letter
