from typing import Dict, List, Any
import os

file_name = "scarlet.txt"
data = "cache_folder"
file_path = os.path.join("..", data, file_name)

def clean_text(text: str) -> str:

    cleaned_text = text.lower()
    punctuation_to_remove = ".,!?'\";:0123456789"

    for punc_char in punctuation_to_remove:
        cleaned_text = cleaned_text.replace(punc_char, "")

    return cleaned_text

def get_list(text: str) -> List:
    return text.strip().split()

def get_only_seven_list(words: List) -> List:
    word_of_seven = []
    for word in words:
        if len(word) == 7:
            word_of_seven.append(word)
    return word_of_seven

def get_frequency_of_words(words: List) -> Dict[str, int]:
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

def get_word_of_max_frequency(frequency_map: Dict) -> Any | None:
    if not frequency_map:
        return None

    key_list = list(frequency_map.keys())
    best_key_so_far = key_list[0]

    for key in key_list:
        if frequency_map[key] > frequency_map[best_key_so_far]:
            best_key_so_far = key
    return best_key_so_far

try:
    with open(file_path, "r") as f_in:

        string_in = f_in.read()
        text_in = clean_text(string_in)
        word_list = get_list(text_in)
        word_seven_list = get_only_seven_list(word_list)

        words_dictionary = get_frequency_of_words(word_seven_list)
        key_max_frequency = get_word_of_max_frequency(words_dictionary)


        print(f"Key: '{key_max_frequency}' appear exact {words_dictionary[key_max_frequency]} times.")



except FileNotFoundError:
    print(f"ERROR: File {file_name} not found")
except Exception as e:
    print(f"An unexpected error occurred: {e}")