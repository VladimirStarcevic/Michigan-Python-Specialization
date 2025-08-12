import os

data = "data"
file_name = "emotion_words.txt"
file_path = os.path.join("..", data, file_name)

j_emotions = []

try:
    with open(file_path, "r") as f_input:

        for line in f_input:
            words_in_line = line.strip().split()
            for word in words_in_line:
                if word.startswith('j'):
                    j_emotions.append(word)

except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred {e}")

print(j_emotions)