from typing import Dict, Any


def create_dictionary(text: str) -> Dict[str, int]:
    new_dict = {}

    for ch in text:
        new_dict[ch] = new_dict.get(ch, 0) + 1
    return new_dict

def get_highest_value_key(dict_in: Dict) -> Any:
    if not dict_in:
        return None

    key_list = list(dict_in.keys())
    max_value_key = key_list[0]

    for key in key_list:
        if dict_in[key] > dict_in[max_value_key]:
            max_value_key = key
    return max_value_key

product = "iphone and android phones"
lett_d = create_dictionary(product)
key_with_max_value = get_highest_value_key(lett_d)

print(f"Key: '{key_with_max_value}' has max value of: {lett_d[key_with_max_value]}")

