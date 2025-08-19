from typing import Dict

def get_char_map(str_in:str) -> Dict[str, int]:
    chars = {}
    for ch in str_in:
        chars[ch] = chars.get(ch, 0) + 1
    return chars


def get_key_with_min(dict_in: Dict[str, int]) -> str:
    if not dict_in:
        return ""

    key_list = list(dict_in.keys())

    worst_char_so_far = key_list[0]

    for key in key_list:
        if dict_in[key] < dict_in[worst_char_so_far]:
            worst_char_so_far = key

    return worst_char_so_far


sally = "sally sells sea shells by the sea shore and by the road"
characters = get_char_map(sally)
worst_char = get_key_with_min(characters)

if worst_char != "":
    print(f"Worst key: '{worst_char}' has min value of: {characters[worst_char]}")
else:
    print("Dictionary is empty!")