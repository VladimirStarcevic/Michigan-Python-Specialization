# Create a list called emotions that contains the first word of every line in emotion_words.txt.
import os

data = "data"
file_name = "emotion_words.txt"
file_path = os.path.join("..", data, file_name)

emotions = []

try:

    with open(file_path, "r") as f_input:
        for line in f_input:

            word_list = line.strip().split()

            if len(word_list) >= 1:
                third_word = word_list[0]
                emotions.append(third_word)


except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(emotions)