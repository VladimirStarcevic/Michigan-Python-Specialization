import os

data_folder = "data"
file_name = "olympics.txt"
file_path = os.path.join("..", data_folder, file_name)

try:
    with open(file_path, "r") as file_object:
        lines = file_object.readlines()
        header_line = lines[0]
        column_names = header_line.strip().split(',')
        print("Column Names:", column_names)
        print("-" * 62)

        for data_line in lines[1:]:
            values = data_line.strip().split(",")

            if values[5] != "NA":
                print("{}: {}; {}".format(
                    values[0],
                    values[4],
                    values[5]
                ))



except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")