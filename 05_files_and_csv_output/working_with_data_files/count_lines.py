import os

data_folder = "data"
file_name = "emotion_words.txt"
file_path = os.path.join("..", data_folder, file_name)


try:
    with open(file_path, "r") as file_object:
        print(f"====== File: {file_name} opened successfully. ======")
        num_lines = 0
        for line in file_object:
            line.strip()
            num_lines += 1

except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"Number of lines in file: {file_name} is: {num_lines}")