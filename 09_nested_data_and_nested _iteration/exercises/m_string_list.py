from typing import List, Any

def find_m_strings_recursively(list_in: List[Any], results_list: List) -> None:

    for item in list_in:
        if isinstance(item, str):
            if 'm' in item:
                results_list.append(item)
        elif isinstance(item, list):
            find_m_strings_recursively(item, results_list)

d = ['good morning', 'hello', 'chair', 'python',
        ['music', 'flowers', 'facebook', 'instagram', 'snapchat',
           ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']
        ],
     'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']
m_list = []

find_m_strings_recursively(d, m_list)

print(m_list)
