import os

data_folder = "data"
file_name = "emotion_words2.txt"

file_path = os.path.join("..", data_folder, file_name)

try:
    with open(file_path, "r") as file_object:

            first_forty = file_object.read(40)


except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(first_forty)