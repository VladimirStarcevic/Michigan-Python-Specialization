# Below, we have provided a list of lists that contain information about people.
# Write code to create a new list that contains every person’s last name, and save that list as last_names
from typing import List, Any

def get_lastname_list(list_in: List) -> Any:
    list_out = []
    for item in list_in:
            last_name = item[1]
            list_out.append(last_name)
    return list_out

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = get_lastname_list(info)

print(last_names)
