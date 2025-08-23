from typing import Dict, List

def get_num_medals(dict_in: Dict[str, int]) -> List[int]:
    gold_list = []
    for key, values in dict_in.items():
        gold_list.append(values)
    return gold_list

gold = {
    "USA": 31,
    "Great Britain": 19,
    "China": 19,
    "Germany": 13,
    "Russia": 12,
    "Japan": 10,
    "France": 8,
    "Italy": 8,
}
num_medals = get_num_medals(gold)
print(num_medals)