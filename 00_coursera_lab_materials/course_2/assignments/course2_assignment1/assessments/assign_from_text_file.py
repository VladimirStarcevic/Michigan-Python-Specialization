import os
assets = "assets"
file_name = "travel_plans.txt"
file_path = os.path.join("..", assets, file_name)

first_chars = ""
try:
    with open(file_path, "r") as f_in:

        first_chars += f_in.read(33)

except FileNotFoundError:
    print(f"ERROR: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
print(first_chars)

