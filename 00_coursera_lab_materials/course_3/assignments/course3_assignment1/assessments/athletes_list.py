# Given below is a list of lists of athletes.
# Create a list, t_athletes, that includes an athlete's name if it contains a lowercase "t".
# If it does not contain the letter "t", save that athlete's name into list others.
from typing import List

def get_lists_of_athletes(list_in: List, t_list: List, other_list: List) -> None:
    for items in list_in:
        if isinstance(items, list):
            for athlete_name in items:
                if 't' in athlete_name:
                    t_list.append(athlete_name)
                else:
                    other_list.append(athlete_name)

athletes = [
    ['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'],
    ['Felix', 'Bolt', 'Gardner', 'Eaton'],
    ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t_athletes = []
others = []

get_lists_of_athletes(athletes, t_athletes, others)

for t_names in t_athletes:
    print(f"T name: {t_names}")
print("\n========= Others Names List ============")
for name in others:
    print(f"Regular name: {name}")

