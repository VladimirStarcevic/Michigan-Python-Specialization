import requests
import json

BASIC_URL = "https://api.chucknorris.io/jokes/random"
categories = ["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music","political","religion","science","sport","travel"]

print("Jokes categories available")
for i in range(len(categories)):
    print(f"{i + 1}. {categories[i]}")

category = input("Select category: ")

if category not in categories:
    print("You are selected not existing category!")
else:
    query_params = {
        "category": category
    }
    try:

        response = requests.get(BASIC_URL, query_params, timeout=5)
        response.raise_for_status()
        norris_jokes = response.json()
        print(json.dumps(norris_jokes, indent=5))
        print(norris_jokes["value"])

    except requests.exceptions.RequestException as e:
        print(f"\nThere is error on communication with server: {e}")
    except json.JSONDecodeError:
        print("\nERROR: Server did not return valid JSON.")