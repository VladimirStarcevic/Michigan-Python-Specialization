from typing import Dict

def get_total_credits(dict_in: Dict) -> int:
    if not dict_in:
        return 0

    credits_sum = 0
    for value in dict_in.values():
        credits_sum += value
    return credits_sum

Junior = {
    "SI 206": 4,
    "SI 310": 4,
    "BL 300": 3,
    "TO 313": 3,
    "BCOM 350": 1,
    "MO 300": 3,
}


total_credits = get_total_credits(Junior)
if total_credits is not -1:
    print(f"Junior total credits: {total_credits}")
else:
    print("There is not credits in dictionary")
