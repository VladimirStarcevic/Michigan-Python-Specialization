punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word: str) -> str:

    clean_word = word

    for punc in punctuation_chars:
        clean_word = clean_word.replace(punc, "")
    return clean_word
