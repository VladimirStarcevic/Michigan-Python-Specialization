# Sort the list, lst from largest to smallest.
# Save this new list to the variable lst_sorted

from typing import List

def sort_inverse_list(list_in: List[int]) -> List[int]:
    list_out = sorted(list_in, reverse = True)
    return list_out

lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sort_inverse_list(lst)
print(lst_sorted)
