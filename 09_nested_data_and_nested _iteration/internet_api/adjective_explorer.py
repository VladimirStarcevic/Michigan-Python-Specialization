import json
import requests


BASE_URL = "https://api.datamuse.com/words"
adjective_explorer = input("Enter Adjective Explorer for exp(ocean,sky,car): ")

query_params = {
    "rel_jjb": adjective_explorer,
    "max": 5
}

def count_vowels(word: str) -> int:
    count = 0
    vowels = "aeiou"
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count


try:

    response = requests.get(BASE_URL, params=query_params, timeout=5)
    response.raise_for_status()
    adjective_words = response.json()

    print(json.dumps(adjective_words, indent=5))

    adjective_words_list = [item['word'] for item in adjective_words if count_vowels(item['word']) > 1]
    print(adjective_words_list)



except requests.exceptions.RequestException as e:
    print(f"\nThere is error on communication with server: {e}")
except json.JSONDecodeError:
    print("\nERROR: Server did not return valid JSON.")