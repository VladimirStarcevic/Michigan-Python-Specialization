import requests
import json
import os

BASE_URL = "https://api.datamuse.com/words"
CACHE_FILENAME = "my_api_cache.json"
cache_folder = "cache_folder"
file_cache_path = os.path.join("..", cache_folder, CACHE_FILENAME)

def make_cache_key(base_url, params_dict):

    sorted_key = sorted(params_dict.keys())

    string_parts = []
    for key in sorted_key:
        key_value = params_dict[key]
        part = f"{key}-{key_value}"
        string_parts.append(part)

    final_part = '_'.join(string_parts)
    return f"{base_url}_{final_part}"

def read_cache_from_file(cache_path):
    try:

        with open(file_cache_path, "r", encoding="UTF-8") as file_in:

            file_data = file_in.read()
            return json.loads(file_data)

    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

def write_cache_to_file(cache_path, cache_data):
    try:

        with open(file_cache_path, "w", encoding="UTF-8") as file_out:

            formated_json_string = json.dumps(cache_data, indent=4)
            file_out.write(formated_json_string)


    except Exception as e:
        print(f"An unexpected error occurred: {e}")


sinonym_to_search = input("Enter word to search sinonym for: ")
query_params = {
    "rel_syn": sinonym_to_search,
    "max": 5
}

cache_key = make_cache_key(BASE_URL,query_params)
print(cache_key)
print("=================  TEST  ========================")

my_test_cache = {'test_key': 'test_value'}


write_cache_to_file(CACHE_FILENAME, my_test_cache)
print(f"Write data in file: {CACHE_FILENAME}")


reade_data = read_cache_from_file(CACHE_FILENAME)
print(f"Reading data: {reade_data}")


assert my_test_cache == reade_data
