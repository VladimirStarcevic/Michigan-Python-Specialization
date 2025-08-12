import os

data = "data"
file_name = "studentdata.txt"

file_path = os.path.join("..", data, file_name)

try:
    with open(file_path, "r") as f_input:

        student_list = f_input.readlines()

        for student in student_list:
            student_info = student.strip().split()
            if len(student_info[1:]) > 6:
                print(student_info[0])
except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")