import os

data_folder = 'data'
file_name = 'olympics.txt'
file_path = os.path.join('..', data_folder, file_name)

try:
    with open(file_path, "r") as file_object:
        print(f"====== File '{file_name}' opened successfully. ======")

        for line in file_object:
            print(line.strip())

        print("=== End of File ===")

except FileNotFoundError:
    print(f"ERROR: File not found at '{file_path}'")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
