from typing import List, Any

def get_list_of_elements(list_in: List[str]) -> List[Any]:

    if len(list_in) == 0:
        return []

    attempts_list = []
    for elem in list_in:
        try:
            attempts_list.append(elem[1])
        except IndexError:
            attempts_list.append("Error")
    return attempts_list

full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']
attempts = get_list_of_elements(full_lst)
print(attempts)