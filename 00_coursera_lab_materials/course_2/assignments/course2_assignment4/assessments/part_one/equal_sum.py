sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

sum2 = 0
idx = 0
while idx < len(lst):
    sum2 += lst[idx]
    idx += 1

print(sum1 == sum2)