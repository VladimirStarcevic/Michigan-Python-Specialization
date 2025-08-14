import os

assets = "assets"
file_name = "school_prompt.txt"
file_path = os.path.join("..", assets, file_name)

beginning_chars = ""
try:
    with open(file_path, "r") as f_in:

        beginning_chars += f_in.read(30)


except FileNotFoundError:
    print(f"ERROR: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"First 30 chars:\n{beginning_chars}")