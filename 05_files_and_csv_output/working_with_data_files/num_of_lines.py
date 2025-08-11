
import os

data_folder = "data"
file_name = "travel_plans2.txt"

file_path = os.path.join("..", data_folder, file_name)

try:
    with open(file_path, "r") as file_object:

        lines = file_object.readlines()
        num_of_lines = len(lines)

except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"There is {num_of_lines} number of lines in the file {file_name}")