from typing import Dict

def get_char_map(str_in:str) -> Dict[str, int]:
    chars = {}
    for ch in str_in:
        chars[ch] = chars.get(ch, 0) + 1
    return chars


def get_key_with_max(dict_in: Dict[str, int]) -> str:
    if not dict_in:
        return ""

    key_list = list(dict_in.keys())

    best_char_so_far = key_list[0]

    for key in key_list:
        if dict_in[key] > dict_in[best_char_so_far]:
            best_char_so_far = key

    return best_char_so_far



sally = "sally sells sea shells by the sea shore"
characters = get_char_map(sally)
best_char = get_key_with_max(characters)

if best_char != "":
    print(f"Best key: '{best_char}' has max value of: {characters[best_char]}")
else:
    print("Dictionary is empty!")