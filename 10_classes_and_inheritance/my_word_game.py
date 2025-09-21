import random
import os
from typing import List

class Letter:
    letter: str
    in_correct_place: bool
    in_word: bool


    def __init__(self, letter):
        self.letter = letter
        self.in_correct_place = False
        self.in_word = False

    def is_in_correct_place(self):
        return self.in_correct_place

    def is_in_word(self):
        return self.in_word

    def __str__(self):
        return f"Letter('{self.letter}')"


class GameEngine:
    word_list: List[str]
    target_word: str
    guesses_left: int

    def __init__(self, word_list_file: str):
        try:
            with open(word_list_file, "r", encoding='UTF-8') as f_in:
                lines = f_in.readlines()

                self.word_list = [line.strip().upper() for line in lines]

                if not self.word_list:
                    raise ValueError("Word file is empty.")

                self.target_word = random.choice(self.word_list)
                self.guesses_left = 6

                print(f"GameEngine initialized. Loaded {len(self.word_list)} words.")

                # print(f"Secret word is: {self.target_word}")

        except FileNotFoundError:
            print(f"ERROR: File not found at '{word_list_file}'")
        except ValueError as e:
            print(f"ERROR: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


data_folder = "data"
temp_file_name = "temp_file.txt"
path_to_temp_file = os.path.join(data_folder, temp_file_name)

print(f"--- Testing GameEngine with temp file: {path_to_temp_file} ---")
game = GameEngine(path_to_temp_file)

try:
    print(f"Game has {game.guesses_left} guesses left.")
    print(f"One of the words in the game is: {game.word_list[0]}")
    print(f"The secret word for this round is: {game.target_word}")
except AttributeError:
    print("Could not test game attributes, GameEngine object probably failed to initialize.")
