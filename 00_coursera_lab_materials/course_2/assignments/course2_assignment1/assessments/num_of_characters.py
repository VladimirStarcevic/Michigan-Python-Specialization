import os

assets = "assets"
file_name = "travel_plans.txt"
file_path = os.path.join("..", assets, file_name)
num = 0

try:
    with open(file_path, "r") as f_in:

        full_content = f_in.read()
        num = len(full_content)

except FileNotFoundError:
    print(f"ERROR: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"Total characters: {num}")