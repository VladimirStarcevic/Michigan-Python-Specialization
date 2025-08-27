# Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable sorted_keys

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}


sorted_keys = sorted(dictionary.keys())

for key in sorted_keys:
    print(f"{key} => {dictionary[key]}")