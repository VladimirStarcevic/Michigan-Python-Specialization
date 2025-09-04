# Use a list comprehension to create a list called lst2 that "doubles" each element in the list, lst.
# Use * 2 to "double" numbers (5 * 2 == 10),
# strings ("xyz" * 2 == "xyzxyz"), and lists (['a', 'b'] * 2 == ['a', 'b', 'a', 'b']).

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [element * 2 for element in lst]

print(lst2)
assert "hellohello" in lst2