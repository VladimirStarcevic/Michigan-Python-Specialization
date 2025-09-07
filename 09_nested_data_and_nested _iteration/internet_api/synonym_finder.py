import json
import requests


BASE_URL = "https://api.datamuse.com/words"
sinonym_to_search = input("Enter word to search sinonym for: ")
query_params = {
    "rel_syn": sinonym_to_search,
    "max": 5
}


try:


    response = requests.get(BASE_URL,params=query_params, timeout=5)
    response.raise_for_status()
    words_of_sinonym = response.json()
    print(json.dumps(words_of_sinonym, indent=5))

    list_of_sinonym_for_happy = [item["word"] for item in words_of_sinonym]
    print("\n ==============================")
    for word in list_of_sinonym_for_happy:
        print(f"For word: {sinonym_to_search} => {word}")

except requests.exceptions.RequestException as e:
    print(f"\nThere is error on communication with server: {e}")
except json.JSONDecodeError:
    print("\nERROR: Server did not return valid JSON.")