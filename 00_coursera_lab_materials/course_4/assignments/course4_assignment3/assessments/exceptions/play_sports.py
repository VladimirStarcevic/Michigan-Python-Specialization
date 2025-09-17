from typing import List, Dict

def get_people_in_sports(dict_in: Dict[str, int], list_in: List[str]):

    for item in list_in:
        try:
            print(dict_in[item])
        except KeyError:
            dict_in[item] = 1
            print(dict_in[item])

sports = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]
ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

get_people_in_sports(ppl_play, sports)