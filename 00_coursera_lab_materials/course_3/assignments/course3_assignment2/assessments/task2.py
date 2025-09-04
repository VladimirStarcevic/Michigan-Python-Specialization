# Below, we have provided a list of strings called countries.
# Use filter to produce a list called b_countries that only contains the strings from countries that begin with 'B'.
# Note: be sure to use list to convert the result from filter into a list.

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = list(filter(lambda item: item.lower().startswith('b'), countries))

print(b_countries)

assert 'Brazil' in b_countries
assert 'Canada' not in b_countries