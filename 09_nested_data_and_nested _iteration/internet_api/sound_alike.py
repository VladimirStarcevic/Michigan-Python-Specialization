import requests
import json

BASE_URL = "https://api.datamuse.com/words"

user_word = input("Enter your word: ")

query_params = {
    'sl': user_word,
    'max': 5
}

try:

    response = requests.get(BASE_URL, params=query_params, timeout=5)
    response.raise_for_status()

    similar_words_data = response.json()
    print("\n=== JSON Response ===")
    print(json.dumps(similar_words_data, indent=4))
    print("============================================")

    words_only = [item['word'] for item in similar_words_data]

except requests.exceptions.RequestException as e:
    print(f"\nThere is error on communication with server: {e}")
except json.JSONDecodeError:
    print("\nERROR: Server is don't give a JSON.")


