from typing import Dict

def get_dict(str_in: str) -> Dict[str, int]:
    dict_out = {}
    lower_str = str_in.lower()
    for ch in lower_str:
        if ch.isalpha():
            dict_out[ch] = dict_out.get(ch, 0) + 1
    return dict_out



p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = get_dict(p)
print(low_d)