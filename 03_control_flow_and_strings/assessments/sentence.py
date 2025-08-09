sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

words_list = sentence.split()

same_letter_count = 0

for word in words_list:
    if len(word) > 0 and word[0] == word[-1]:
        same_letter_count += 1


print(f"Number of words that starts and ends with same letter: {same_letter_count}")