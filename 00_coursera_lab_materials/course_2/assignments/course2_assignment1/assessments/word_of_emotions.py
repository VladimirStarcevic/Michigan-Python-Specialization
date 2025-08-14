import os
assets = "assets"
file_name = "emotion_words.txt"
file_path = os.path.join("..", assets, file_name)



num_words = 0
try:
    with open(file_path, "r") as f_in:

        for line in f_in:
            word_list = line.strip().split()
            num_words += len(word_list)



except FileNotFoundError:
    print(f"ERROR: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
print(f"Number of word is: {num_words}")