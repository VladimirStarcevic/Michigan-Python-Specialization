import os

data = "data"
file_name = "emotion_words.txt"

file_path = os.path.join("..", data, file_name)

num_words = 0
try:
    with open(file_path, "r") as f_input:

        for line in f_input:
            words_list = line.strip().split()
            for word in words_list:
                num_words += 1

except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"Total number of words in file {file_name} is: {num_words}")