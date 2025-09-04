from typing import List

def doubler(list_in: List[int]) -> List[int]:
    new_list = []
    for num in list_in:
        new_list.append(num * 2)
    return new_list
def num_doubled(number: int): return number * 2

def doubler_with_map(list_in: List[int]) -> List[int]:
    return list(map(num_doubled, list_in))


def doubler_with_map_and_lambda(list_in: List[int]):
    return list(map(lambda num: num * 2, list_in))


nums = [4, 11, 6, 8, 23]
nums_d4 = doubler_with_map_and_lambda(nums)
print(nums_d4)

num_double = num_doubled(9)
print(num_double)