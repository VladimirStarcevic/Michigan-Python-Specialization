from typing import List

def get_even_list() -> List[int]:
    even_list = []
    counter = 0
    while counter <= 15:
        if counter % 2 == 0:
            even_list.append(counter)

        counter += 1
    return even_list

even_numbs = get_even_list()
print(even_numbs)