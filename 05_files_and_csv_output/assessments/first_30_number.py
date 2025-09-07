import os

data = "cache_folder"
file_name = "travel_plans.txt"
file_path = os.path.join("..", data, file_name)

beginning_chars = ""

try:
    with open(file_path, "r") as f_input:

       beginning_chars += f_input.read(30)

except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(beginning_chars)