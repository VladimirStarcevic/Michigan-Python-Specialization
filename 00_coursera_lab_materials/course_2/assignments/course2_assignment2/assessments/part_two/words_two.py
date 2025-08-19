from typing import  Dict, List

def get_word_frequency(str_in: str) -> Dict[str, int]:
    words_list = str_in.strip().split()
    words_count = {}
    for word in words_list:
        words_count[word] = words_count.get(word, 0) + 1
    return words_count


sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = get_word_frequency(sent)
print(wrd_d)