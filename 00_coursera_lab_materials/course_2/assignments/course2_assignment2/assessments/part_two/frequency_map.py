from typing import Dict, List

def calculate_frequency_of_char(str_in: str) -> Dict[str, int]:
    freq_map = {}
    for ch in str_in:
        freq_map[ch] = freq_map.get(ch, 0) + 1
    return freq_map



str1 = "peter piper picked a peck of pickled peppers"
freq = calculate_frequency_of_char(str1)
print(freq)

