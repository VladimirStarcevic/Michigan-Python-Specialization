from typing import List

def get_total(list_in: List[int | float]) -> int | float:
    tot = 0
    idx = 0
    while idx < len(list_in):
        current_num = list_in[idx]
        tot += current_num
        idx += 1

    return tot


list1 = [8, 3, 4, 5, 6, 7, 9]

accum = get_total(list1)
print(f"Sum of all elements: {accum}")