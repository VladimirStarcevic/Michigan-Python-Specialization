import os

data_folder = "cache_folder"
file_name = "school_prompt2.txt"

file_path = os.path.join("..", data_folder, file_name)

try:
    with open(file_path, "r") as file_object:

        content = file_object.read()
        num_char = len(content)



except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"The file has {num_char} characters.")

