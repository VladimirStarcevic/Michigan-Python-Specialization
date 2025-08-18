from typing import List, Dict
english_words_str = """
sir
hotel
student
boy
madam
professor
restaurant
your
excuse
students
are
lawyer
the
restroom
my
hello
is
man
"""

pirate_words_str = """
matey
fleabag inn
swabbie
matey
proud beauty
foul blaggart
galley
yer
arr
swabbies
be
foul blaggart
th'
head
me
avast
be
matey
"""
def create_list_from_text(text: str) -> List:
    word_list = text.strip().split('\n')
    return word_list

def create_translation_dict(english_list, pirate_list: List) -> Dict[str, str]:
    translation_dict = {}

    size_eng = len(english_list)
    size_pir = len(pirate_list)

    if size_eng == size_pir:
        for i in range(size_eng):
            current_key = english_list[i]
            if not current_key in translation_dict:
                translation_dict.setdefault(current_key, pirate_list[i])
    return translation_dict

def translate_word(word: str, translate_dict: Dict[str, str]) -> str:
    if word in translate_dict:
        return translate_dict[word]
    else:
        return word

def main_translator_loop() -> None:
    english_list = create_list_from_text(english_words_str)
    pirate_list = create_list_from_text(pirate_words_str)

    pirate_dictionary = create_translation_dict(english_list, pirate_list)
    print("Avast! Welcome to the Pirate Translator!")
    english_sentence = input("Enter a sentence to translate: ")

    clean_word = english_sentence.lower().strip()
    translated_word = pirate_dictionary.get(clean_word, "I don't know that word, matey!")

    print(f"In pirate speak, '{english_sentence}' is: {translated_word}")



main_translator_loop()