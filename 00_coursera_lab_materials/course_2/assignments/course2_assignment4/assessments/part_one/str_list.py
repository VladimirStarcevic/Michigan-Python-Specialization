from typing import List

def sublist(list_in: List[str]) -> List[str]:
    if "STOP" not in list_in:
        return list_in

    sub_list = []
    index = 0
    while index < len(list_in):
        if list_in[index] == "STOP":
            break
        sub_list.append(list_in[index])
        index += 1

    return sub_list


# Test Case 1: "STOP" is in the middle of the list
list1 = ["apple", "banana", "cherry", "STOP", "date"]
expected1 = ["apple", "banana", "cherry"]
result1 = sublist(list1)
print(f"Test Case 1 Passed: {result1 == expected1}")
assert result1 == expected1

# Test Case 2: "STOP" is the first element
list2 = ["STOP", "apple", "banana"]
expected2 = []
result2 = sublist(list2)
print(f"Test Case 2 Passed: {result2 == expected2}")
assert result2 == expected2

# Test Case 3: The list does not contain "STOP"
list3 = ["apple", "banana", "cherry"]
# We expect the ORIGINAL list object back, not a copy
result3 = sublist(list3)
print(f"Test Case 3 Passed: {result3 == list3 and result3 is list3}")
assert result3 is list3

# Test Case 4: The list is empty
list4 = []
expected4 = []
result4 = sublist(list4)
print(f"Test Case 4 Passed: {result4 == expected4 and result4 is list4}")
assert result4 is list4

print("\nAll tests passed successfully!")