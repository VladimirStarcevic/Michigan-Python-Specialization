from typing import  Dict, List

def get_word_frequency(str_in: str) -> Dict[str, int]:
    words_list = str_in.strip().split()
    words_count = {}
    for word in words_list:
        words_count[word] = words_count.get(word, 0) + 1
    return words_count


str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = get_word_frequency(str1)
print(freq_words)