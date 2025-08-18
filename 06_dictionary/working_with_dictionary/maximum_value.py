from typing import Dict, Any

def find_key_for_max_value(dicti_in: Dict[Any, int]) -> Any:

    if not dicti_in:
        return None

    keys_list = list(dicti_in.keys())
    best_so_far = keys_list[0]
    for key in keys_list:
        if dicti_in[key] > dicti_in[best_so_far]:
            best_so_far = key

    return best_so_far


d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

max_key = find_key_for_max_value(d)

if max_key is not None:
    max_value = d[max_key]
    print(f"Key '{max_key}' has the highest value, which is {max_value}.")
else:
    print("The dictionary is empty.")

