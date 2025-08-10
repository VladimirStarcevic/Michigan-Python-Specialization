import os

data_folder = "data"
file_name = "olympics.txt"

output_file_name = 'medal_winners.csv'

file_path = os.path.join("..", data_folder, file_name)
output_file_path = os.path.join("..", data_folder, output_file_name)


try:

    winners_data_list = []

    with open(file_path, "r") as file_object:
        lines = file_object.readlines()

        for data_line in lines[1:]:
            values = data_line.strip().split(",")
            if values[5] != "NA":
                winner_info = [values[0], values[4], values[5]]
                winners_data_list.append(winner_info)


    with open(output_file_path, "w") as write_file:

        write_file.write("Name,Event,Medal\n")

        for winner_info_list in winners_data_list:
            csv_line = ",".join(winner_info_list)
            write_file.write(csv_line + "\n")

        print(f"Successfully created and saved data to {output_file_name}")



except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")