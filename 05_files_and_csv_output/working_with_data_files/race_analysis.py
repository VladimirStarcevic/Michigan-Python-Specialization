import os

data = "cache_folder"
file_name = "monza_2023_results.txt"
output_file_name = "monza_podium.csv"

file_path = os.path.join("..", data, file_name)
output_file_path = os.path.join("..", data, output_file_name)

try:
    with open(file_path, "r") as f_in:
        with open(output_file_path, "w") as f_out:
            header = f_in.readline()
            column = header.strip().split(",")
            header_info = column[:3]
            header_column = ",".join(header_info)
            f_out.write(header_column + "\n")

            drivers_processed = 0
            for line in f_in:

                if drivers_processed >= 3:
                    break

                drivers_processed += 1

                info_line = line.strip().split(",")
                new_info = info_line[:3]

                driver_info = ",".join(new_info)
                f_out.write(driver_info + "\n")

except FileNotFoundError:
    print(f"ERROR: File {file_name} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

