import os
assets = "assets"
file_name = "school_prompt.txt"
file_path = os.path.join("..", assets, file_name)


three = []
try:
    with open(file_path, "r") as f_in:

        for line in f_in:
            lines = line.strip().split()
            if len(lines) >= 3:

                third_word = lines[2]
                three.append(third_word)


except FileNotFoundError:
    print(f"ERROR: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(three)