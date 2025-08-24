from typing import List

def sublist(list_in: List[int | float]) -> List[int | float]:
    sub_list = []
    index = 0
    while index < len(list_in):
        current_num = list_in[index]
        if current_num == 5:
            break
        sub_list.append(current_num)
        index += 1
    return sub_list

list1 = [2, 4, 5, 6, 7, 9]
result = sublist(list1)
print(result)

