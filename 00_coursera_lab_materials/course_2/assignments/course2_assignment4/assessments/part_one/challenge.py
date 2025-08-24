from typing import List


def beginning(list_in: List[str]) -> List[str]:
    sub_list = []
    index = 0
    while index < len(list_in) and len(sub_list) < 10:

        current_item = list_in[index]

        if current_item == 'bye':
            break
        sub_list.append(current_item)
        index += 1

    return sub_list

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'bye']
list2 = ['a', 'b', 'bye', 'c']
list3 = ['a', 'b', 'c']

print(f"Test 1 : {beginning(list1)}")
print(f"Test 2 : {beginning(list2)}")
print(f"Test 3 : {beginning(list3)}")
