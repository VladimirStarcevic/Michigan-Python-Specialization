from typing import Dict, List, Any

# Provided is a buggy for loop that tries to accumulate some values out of some dictionaries.
# Insert a try/except so that the code executes without error and produces the correct total.


def get_total(list_in: List[dict], key_to_search) -> int:

    if len(list_in) == 0:
        return 0
    total_result = 0
    for item in list_in:
        if isinstance(item, dict):
            try:
                total_result += item[key_to_search]
            except KeyError:
                pass
    return total_result



di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]


key = "Puppies"
total = get_total(di, key)
print(f"Total of {key}: {total}")

