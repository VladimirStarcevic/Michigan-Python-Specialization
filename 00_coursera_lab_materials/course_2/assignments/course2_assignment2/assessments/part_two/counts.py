from typing import Dict

def get_counting_dict(str_in: str) -> Dict[str, int]:
    count = {}
    for ch in str_in:
        count[ch] = count.get(ch, 0) + 1
    return count

s1 = "hello"
counts = get_counting_dict(s1)
print(counts)