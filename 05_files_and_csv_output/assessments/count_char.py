import os

data = "data"
file_name = "travel_plans.txt"
file_path = os.path.join("..", data, file_name)

num = 0

try:

    with open(file_path, "r") as f_input:

        content = f_input.read()
        for ch in content:
            num += 1

except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"the total number of characters in {file_name} is: {num}")