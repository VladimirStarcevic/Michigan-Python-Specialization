import os
assets = "assets"
file_name = "emotion_words.txt"
file_path = os.path.join("..", assets, file_name)


emotions = []
try:
    with open(file_path, "r") as f_in:

        for line in f_in:

            lines = line.strip().split()
            if len(lines) >= 1:
                first_word = lines[0]
                emotions.append(first_word)


except FileNotFoundError:
    print(f"ERROR: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(emotions)