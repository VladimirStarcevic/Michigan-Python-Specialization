import json
import requests

BASE_URL = "https://api.datamuse.com/words"

user_word = input("Enter your first word: ")
user_step_number = int(input("Enter number of steps: "))

word_chain_list = [user_word]

next_word_to_search = user_word

try:

    for _ in range(user_step_number):

        query_params = {
            'rel_trg': next_word_to_search,
            'max': "1"
        }

        response = requests.get(BASE_URL, params=query_params, timeout=5)
        response.raise_for_status()
        words_chain_data = response.json()

        if not words_chain_data:
            print(f"There is not word '{next_word_to_search}'.")
            break
        found_word = words_chain_data[0]['word']

        word_chain_list.append(found_word)
        next_word_to_search = found_word

except requests.exceptions.RequestException as e:
    print(f"\nThere is error on communication with server: {e}")
except json.JSONDecodeError:
    print("\nERROR: Server did not return valid JSON.")

print(f"\nFinal chain of words: {word_chain_list}")