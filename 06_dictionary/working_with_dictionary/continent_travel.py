def sum_dictionary_values(any_dictionary: dict) -> int:
    total_sum = 0
    for value in any_dictionary.values():
        total_sum += value
    return total_sum
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}

total = sum_dictionary_values(travel)

print(total)