from typing import Dict, List, Tuple

def get_tuple_list(dict_in: Dict[str, int]) -> Tuple[List[str], List[int]]:

    events = []
    medals_count = []
    for key, value in dict_in.items():
        events.append(key)
        medals_count.append(value)
    return  events, medals_count

track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}

track_events, medals = get_tuple_list(track_medal_counts)
print(track_events)