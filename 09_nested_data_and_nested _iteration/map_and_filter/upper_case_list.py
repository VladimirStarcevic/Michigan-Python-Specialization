# Below, we have provided a list of strings called abbrevs.
# Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = list(map(lambda string: string.upper(), abbrevs))

for element in abbrevs_upper:
    print(element)