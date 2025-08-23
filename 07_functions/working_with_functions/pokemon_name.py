from typing import Dict, List, Tuple

def get_lists_from_dict(dict_in: Dict[str, int]) -> Tuple[List[str], List[int]]:

    key_list = []
    value_list = []
    for key, value in dict_in.items():
        key_list.append(key)
        value_list.append(value)
    return key_list, value_list

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

p_names, p_number = get_lists_from_dict(pokemon)
print(f"{p_names} {p_number}")