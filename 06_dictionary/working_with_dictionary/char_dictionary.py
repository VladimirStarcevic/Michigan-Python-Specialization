stri = "what can I do"

char_d = {}

for ch in stri:
    if ch not in char_d:
        char_d[ch] = 0
    char_d[ch] += 1

for item in char_d.items():
    print(item)