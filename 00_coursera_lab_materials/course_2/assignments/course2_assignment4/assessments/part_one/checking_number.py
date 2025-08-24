from typing import List

def check_nums(list_in: List[int]) -> List[int]:
    if 7 not in list_in:
        return list_in
    list_out = []
    index = 0
    while index < len(list_in):
        current_num = list_in[index]
        if current_num == 7:
            break
        list_out.append(current_num)
        index += 1
    return list_out

list_with_7 = [1, 2, 3, 4, 5, 6, 7, 8]
list_without_7 = [1, 2, 3, 4]

output1 = check_nums(list_with_7)
output2 = check_nums(list_without_7)

print(f"For list with 7: {output1}")
print(f"For list without 7: {output2}")
print(f"Is output2 original? {output2 is list_without_7}")

