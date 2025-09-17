from typing import Dict, List, Any

def get_golden_list(dict_in: Dict[str, int], list_in: List[str]) -> List[Any]:

    if not dict_in:
        return []
    if len(list_in) == 0:
        return []

    list_out = []
    for country_name in list_in:
        try:
            num_of_gold = dict_in[country_name]
            list_out.append(num_of_gold)
        except KeyError as key:
            #print(f"Key not found {key}")
            list_out.append("Did not get gold")
    return list_out

gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = get_golden_list(gold, country)
for item in country_gold:
    print(item)