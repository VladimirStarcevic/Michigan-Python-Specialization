from typing import List

def accum(numbers: List[int | float]) -> int | float:
    total = 0
    for num in numbers:
        total += num
    return total

nums = [2, 6,5]
element_sum = accum(nums)
print(f"Total sum of elements: {element_sum}")