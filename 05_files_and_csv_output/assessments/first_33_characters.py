import os

data = "data"
file_name = "travel_plans.txt"
file_path = os.path.join("..", data, file_name)

first_chars = ""

try:
    with open(file_path, "r") as f_input:

       first_chars += f_input.read(33)

except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(first_chars)