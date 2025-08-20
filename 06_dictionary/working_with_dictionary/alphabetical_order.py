
from typing import Dict, List


def get_input_dict(user_in: str) -> Dict[str, int]:
    dict_in = {}
    for ch in user_in:
        lower_ch = ch.lower()
        if lower_ch.isalpha():
            dict_in[lower_ch] = dict_in.get(lower_ch, 0) + 1
    return dict_in

def get_sorted_key_list(dict_in: Dict[str, int]) -> List:
    key_list = list(dict_in.keys())
    return sorted(key_list)

def show_by_alphabetical_order(dict_in: Dict[str, int], list_in: List) -> None:
    for key in list_in:
        print(f"{key} {dict_in[key]}")


user_input = input("Enter some text: ")
user_in_dict = get_input_dict(user_input)
sorted_list_of_keys = get_sorted_key_list(user_in_dict)
show_by_alphabetical_order(user_in_dict, sorted_list_of_keys)
