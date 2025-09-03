# Below, we have provided a nested list called big_list.
# Use nested iteration to create a dictionary, word_counts,
# that contains all the words in big_list as keys,
# and the number of times they occur as values.
from typing import List, Dict

def get_words_counter_dict(list_in: List) -> Dict[str, int]:

    dict_out = {}
    for l1 in list_in:
        for l2 in l1:
            for element in l2:
                dict_out[element] = dict_out.get(element, 0) + 1
    return dict_out


big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]


word_counts = get_words_counter_dict(big_list)

for key in word_counts.keys():
    print(f"{key}: {word_counts[key]}")

