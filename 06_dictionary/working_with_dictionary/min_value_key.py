from typing import Dict, Any

def create_frequency_dict(text: str) -> Dict[str, int]:
    new_dict = {}
    for ch in text:
        new_dict[ch] = new_dict.get(ch, 0) + 1
    return new_dict

def find_key_for_min_value(dict_in: Dict) -> Any:
    if not dict_in:
        return None
    key_list = list(dict_in.keys())
    min_key = key_list[0]

    for key in key_list:
        if dict_in[key] < dict_in[min_key]:
            min_key = key
    return min_key
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = create_frequency_dict(placement)
key_with_min_value = find_key_for_min_value(d)

print(f"The character with the lowest frequency is: '{key_with_min_value}'")