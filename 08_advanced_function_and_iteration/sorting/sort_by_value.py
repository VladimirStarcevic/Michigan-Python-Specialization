
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_keys = sorted(dictionary, key=lambda k: dictionary[k], reverse=True)
sorted_values = sorted_keys

print("--- Sorted by Value (Highest to Lowest) ---")
for key in sorted_values:
    print(f"{key} => {dictionary[key]}")