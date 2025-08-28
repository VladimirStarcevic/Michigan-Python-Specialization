
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key=lambda digit: int(str(digit)[-4:]))
print(sorted_id)