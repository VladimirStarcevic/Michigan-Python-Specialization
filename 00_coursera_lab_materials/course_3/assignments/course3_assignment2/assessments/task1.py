# Write code that uses map to assign to the variable map_testing all the elements from lst_check,
# prepending the string "Fruit: " to the beginning of each element.
# Note: be sure to use list to convert the result from map into a list.
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']


word = "Fruit: "
map_testing = list(map(lambda item: word + item, lst_check))

for element in map_testing:
    print(element)

assert 'Fruit: plums' in map_testing
assert 'Fruit: kiwi' in map_testing