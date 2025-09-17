from typing import List

def get_list(list_in: List[list]) -> List[str]:

    if len(list_in) == 0:
        return []
    list_out = []
    for item in list_in:
        if isinstance(item, list):
            try:
                list_out.append(item[2])
            except IndexError:
                list_out.append("Continent does not have 3 countries")
    return list_out



continents = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'],
              ['USA', 'Mexico', 'Canada'],
              ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'],
              ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'],
              ['Australia'],
              ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'],
              ['Antarctica']]

third_countries = get_list(continents)
print(third_countries)