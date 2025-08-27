from typing import Dict, List


def get_word_frequency(str_in: str) -> Dict[str, int]:

    dict_out = {}

    lower_str = str_in.lower()

    words = lower_str.split()
    for word in words:
        clean_word = word.strip('.,!?;:"')
        if clean_word:
            dict_out[clean_word] = dict_out.get(clean_word, 0) + 1
    return dict_out

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

word_counts = get_word_frequency(sentence)
print("\n--- Words Sorted Alphabetically ---")

sorted_keys = sorted(word_counts.keys())
for key in sorted_keys:
  print(f"{key} => {word_counts[key]}")

print("\n--- Words Sorted by Frequency (Highest to Lowest) ---")

sorted_keys_by_freq = sorted(word_counts, key=lambda word: word_counts[word], reverse=True)

for word in sorted_keys_by_freq:
    print(f"{word} => {word_counts[word]}")