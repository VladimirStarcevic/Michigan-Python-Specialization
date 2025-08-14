import os
assets = "assets"
file_name = "school_prompt.txt"
file_path = os.path.join("..", assets, file_name)


def get_only_p_words(word_list, char):
    words_with_char = []
    for word in word_list:
        if char in word:
            words_with_char.append(word)
    return words_with_char


p_words = []

try:
    with open(file_path, "r") as f_in:

        for line in f_in:
            lines = line.strip().split()
            p_words_from_line = get_only_p_words(lines, "p")
            p_words.extend(p_words_from_line)

except FileNotFoundError:
    print(f"ERROR: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(p_words)
