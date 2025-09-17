from typing import List, Any

def get_remainders_list(list_in: List[int], divisor) -> List[Any]:

    if len(list_in) == 0:
        return []
    list_out = []
    for num in list_in:
        try:
            list_out.append(divisor % num)
        except ZeroDivisionError:
            list_out.append("Error")
    return list_out

numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainders = get_remainders_list(numbers, 36)
print(remainders)