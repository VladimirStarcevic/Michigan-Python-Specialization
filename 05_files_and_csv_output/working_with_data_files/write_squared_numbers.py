import os

data_folder = "cache_folder"
file_name = "squared_numbers.txt"

file_path = os.path.join("..", data_folder, file_name)


try:
    with open(file_path, "w") as file_object:
        print(f"======== File {file_name} is open for work ========")

        for num in range(1, 13):
            square = num * num
            file_object.write(str(square) + "\n")

    print("Finished writing to file.")

    print(f"\n======== Opening {file_name} for reading... ========")
    with open(file_path, "r") as file_to_read:
        for line in file_to_read:
            print(line.strip())

    print("\n====== Program Ended =======")


except FileNotFoundError:
    print(f"ERROR: File {file_name} is not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
