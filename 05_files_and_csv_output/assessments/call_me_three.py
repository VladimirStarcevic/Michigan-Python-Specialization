import os

data = "cache_folder"
file_name = "travel_plans.txt"
file_path = os.path.join("..", data, file_name)

three = []

try:

    with open(file_path, "r") as f_input:
        for line in f_input:

            word_list = line.strip().split()

            if len(word_list) >= 3:
                third_word = word_list[2]
                three.append(third_word)


except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(three)