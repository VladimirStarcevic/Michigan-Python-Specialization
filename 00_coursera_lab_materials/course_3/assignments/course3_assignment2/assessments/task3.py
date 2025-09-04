# Below, we have provided a list of tuples that contain the names of Game of Thrones characters.
# The first item in each tuple is their last (family) name.
# The second item is their first (given) name.
# Using a list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [f_name for l_name, f_name in people]

print(first_names)


assert 'Jon'  in first_names
assert 'Snow' not in first_names