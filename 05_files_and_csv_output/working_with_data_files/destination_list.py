import os

data = "data"
file_name = "travel_plans.txt"
file_path = os.path.join("..", data, file_name)


destination = []
try:
    with open(file_path, "r") as f_input:

        lines = f_input.readlines()
        for line in lines:
            if ":" in line:
                destination.append(line.strip())

except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(destination)
