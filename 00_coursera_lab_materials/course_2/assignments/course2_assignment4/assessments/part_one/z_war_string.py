from typing import List

def stop_at_z(list_in: List[str]) -> List[str]:
    if "z" not in list_in:
        return list_in

    sub_list = []
    index = 0
    while index < len(list_in):
        if list_in[index] == "z":
            break

        sub_list.append(list_in[index])
        index += 1
    return sub_list


# --- Test Cases for the stop_at_z function ---

# Test Case 1: 'z' is in the middle
list1 = ['a', 'b', 'c', 'z', 'd', 'e']
expected1 = ['a', 'b', 'c']
result1 = stop_at_z(list1)
print(f"Test Case 1 Passed: {result1 == expected1}")
assert result1 == expected1

# Test Case 2: The list does not contain 'z'
list2 = ['a', 'b', 'c']
# Expecting the original list object back
result2 = stop_at_z(list2)
print(f"Test Case 2 Passed: {result2 == list2 and result2 is list2}")
assert result2 is list2

# Test Case 3: 'z' is the first element
list3 = ['z', 'a', 'b']
expected3 = []
result3 = stop_at_z(list3)
print(f"Test Case 3 Passed: {result3 == expected3}")
assert result3 == expected3

# Test Case 4: An empty list
list4 = []
result4 = stop_at_z(list4)
print(f"Test Case 4 Passed: {result4 == list4 and result4 is list4}")
assert result4 is list4

print("\nAll tests passed successfully!")