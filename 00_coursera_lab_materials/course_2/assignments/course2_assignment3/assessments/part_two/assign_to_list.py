# The list below, tuples_lst, is a list of tuples.
# Create a list of the second elements of each tuple and assign this list to the variable country.
from typing import Tuple, List

def get_country_list(list_in: List[Tuple]) -> List[str]:

    countries = []
    for items in list_in:
        country_name = items[1]
        countries.append(country_name)
    return countries

tuples_lst = [
    ("Beijing", "China", 2008),
    ("London", "England", 2012),
    ("Rio", "Brazil", 2016, "Current"),
    ("Tokyo", "Japan", 2020, "Future"),
]
country = get_country_list(tuples_lst)
print(country)