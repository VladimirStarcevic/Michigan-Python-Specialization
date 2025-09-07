import os

data = "cache_folder"
file_name = "school_prompt.txt"

file_path = os.path.join("..", data, file_name)
num_lines = 0
try:

    with open(file_path, "r") as f_input:

        for line in f_input:
            num_lines += 1


except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"Number of lines in file {file_name} is: {num_lines}")