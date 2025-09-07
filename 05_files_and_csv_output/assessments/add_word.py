import os

data = "cache_folder"
file_name = "school_prompt.txt"
file_path = os.path.join("..", data, file_name)

p_words = []

try:

    with open(file_path, "r") as f_input:
        for line in f_input:

            word_list = line.strip().split()

            for word in word_list:
                if "p" in word:
                  p_words.append(word)


except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(p_words)