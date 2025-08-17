sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

def get_num_of_words(list_of_words):
    words_repetitions = {}
    for word in list_of_words:
        words_repetitions[word] = words_repetitions.get(word, 0) + 1
    return words_repetitions


word_list = sentence.strip().split()
word_counts = get_num_of_words(word_list)

for item in word_counts.items():
    print(item)

