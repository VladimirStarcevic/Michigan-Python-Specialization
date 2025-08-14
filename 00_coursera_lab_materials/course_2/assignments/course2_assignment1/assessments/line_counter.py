import os

assets = "assets"
file_name = "school_prompt.txt"
file_path = os.path.join("..", assets, file_name)

num_lines = 0
try:
    with open(file_path, "r") as f_in:

        for line in f_in:
            num_lines += 1


except FileNotFoundError:
    print(f"ERROR: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"Total num of lines: {num_lines}")