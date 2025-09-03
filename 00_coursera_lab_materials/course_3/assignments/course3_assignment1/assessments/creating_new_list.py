# Create a new list called thirds by iterating through the contents of list__of_lists,
# collecting the third element of each sublist.

list__of_lists = [
    ['purple', 'mauve', 'blue'],
    ['red', 'maroon', 'blood orange', 'crimson'],
    ['sea green', 'cornflower', 'lavender', 'indigo'],
    ['yellow', 'amarillo', 'mac n cheese', 'golden rod']
]

thirds = []

for i in range(len(list__of_lists)):
    for j in range(len(list__of_lists[i])):

        if j == 2:
            element = list__of_lists[i][j]
            thirds.append(element)
print(thirds)

thirds_pythonic = []
for sub_list in list__of_lists:
    thirds_pythonic.append(sub_list[2])

print(thirds_pythonic)

