import os
import csv


data_folder = "data"
file_name = "SP500.txt"
file_path = os.path.join("..", data_folder, file_name)


def get_max_interest(interest_list):
    if not interest_list:
        return None

    get_max = interest_list[0]
    for interest in interest_list[1:]:
        if interest > get_max:
            get_max = interest
    return get_max

def get_average(list_of_prices):
    count = 0
    total = 0
    for price in list_of_prices:
        total += price
        count += 1
    return float(total/count)

try:

    with open(file_path, 'r') as f_in:

        csv_reader = csv.reader(f_in)

        header = next(csv_reader)
        #print(f"Header found: {header}")

        sp500_prices = []
        interest_rates = []


        for row in csv_reader:
            date_str = row[0]
            sp500_price = float(row[1])
            rate = float(row[5])

            #print(f"Date: {date_str} Price: {sp500_price}")


            date_parse = date_str.split("/")
            month = int(date_parse[0])
            day = int(date_parse[1])
            year = int(date_parse[2])

            if (year >= 2016 and month >= 6) or (year <= 2017 and month <= 5):
                sp500_prices.append(sp500_price)
                interest_rates.append(rate)

        max_value = get_max_interest(interest_rates)
        average = get_average(sp500_prices)
        print(f"Max value of interset: {max_value}\nAverage value of prices is: {average}")


except StopIteration:
    print("Error: The CSV file is empty.")
except FileNotFoundError:
    print(f"ERROR: File not found at '{file_path}'")
except Exception as e:
    print(f"An error occurred: {e}")