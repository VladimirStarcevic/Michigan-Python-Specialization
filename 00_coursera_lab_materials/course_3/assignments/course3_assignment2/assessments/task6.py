# Write code using zip and filter so that these lists (l1 and l2) are combined into one big list of pairs and assigned to the variable opposites if both elements of the pair are longer than 3 characters.
# Note: be sure to use list to convert the result into a list.


l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

# opposites = [(el1, el2) for el1, el2 in zip(l1, l2) if len(el1) > 3 and  len(el2) > 3]

all_pairs = list(zip(l1, l2))
filtered_pairs = filter(lambda pair: len(pair[0]) > 3 and len(pair[1]) > 3, all_pairs)
opposites = list(filtered_pairs)
print(opposites)

assert ('left', 'right') in opposites
# omit if either word is shorter than 3 characters...
assert ('up', 'down') not in opposites