L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings = []
for items in L:
    for product in items:
        if 'b' in product:
            b_strings.append(product)


print(b_strings)
