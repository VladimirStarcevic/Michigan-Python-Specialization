from typing import List

def length(list_in: List) -> str:
    if len(list_in) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"

input_list = [1, 5, "Pop_OS", "Ubuntu", 6, 1.2]

print(length(input_list))