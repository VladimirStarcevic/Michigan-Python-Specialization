# Below, we have provided a list of tuples that contain students' names and their final grades in PYTHON 101.
# Using a list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).
# passed should be a list of strings (names without final grades) in the same order as students.

students = [('Tamara', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [name for name, garde in students if garde >= 70]

print(passed)
assert 'Tamara' in passed
assert 'Linda' not in passed