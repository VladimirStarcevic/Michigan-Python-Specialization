items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num = 0

for item in items:
    # if 'w' in item:
    for ch in item:
        if ch == 'w':
            acc_num += 1
            break

print(f"Number of words with character 'w' is: {acc_num}")