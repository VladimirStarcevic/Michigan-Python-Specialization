from typing import Dict, List

def create_list(dict_in: Dict) -> List:
    return list(dict_in.keys())

golds = {
    "Italy": 12,
    "USA": 33,
    "Brazil": 15,
    "China": 27,
    "Spain": 19,
    "Canada": 22,
    "Argentina": 8,
    "England": 29,
}
countries = create_list(golds)
print(countries)