def sum_dictionary_values(any_dictionary: dict) -> int:
    total = 0
    for value in any_dictionary.values():
        total += value
    return total


schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits = sum_dictionary_values(schedule)
print(f"Total number of credits: {total_credits}")