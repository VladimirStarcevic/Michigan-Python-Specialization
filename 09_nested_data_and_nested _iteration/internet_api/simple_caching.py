import requests
import json
import os
from typing import Dict, List, Any

BASE_URL = "https://api.datamuse.com/words"
CACHE_FILENAME = "my_api_cache.json"
cache_folder = "cache_folder"
file_cache_path = os.path.join("..", cache_folder, CACHE_FILENAME)

def make_cache_key(base_url: str, params_dict: Dict[str, any]):
    key_list = params_dict.keys()
    sorted_keys_list = sorted(key_list)

    accumulator_list = []
    for key in sorted_keys_list:
        value = params_dict[key]
        query_str = f"{key}-{value}"
        accumulator_list.append(query_str)
    parts = "_".join(accumulator_list)
    return f"{base_url}_{parts}"

def read_cache_from_file(file_path):
    try:
        with open(file_cache_path, "r", encoding='UTF-8') as file_in:

            file_data =  file_in.read()
            return json.loads(file_data)


    except FileNotFoundError:
        print(f"ERROR: File {CACHE_FILENAME} not found!")
        return {}
    except json.JSONDecodeError as e:
        return {}

def write_cache_to_file(file_path, cache_data):
    try:

        with open(file_cache_path, "w", encoding='UTF-8') as file_out:
            cache_data_to_write = json.dumps(cache_data, indent=5)
            file_out.write(cache_data_to_write)

    except IOError as e:
        print(f"Error writing to file: {e}")


def get_with_caching(base_url, params_dict, cache_filepath):
    cache_key = make_cache_key(base_url, params_dict)

    current_cache = read_cache_from_file(cache_filepath)
    if cache_key in current_cache:
        print("Cache Hit!")
        return current_cache[cache_key]
    else:
        print("Cache miss! Fetching from API....")
        try:

            response = requests.get(BASE_URL, params=params_dict, timeout=5)
            response.raise_for_status()
            response_text = response.text
            current_cache[cache_key] = response_text
            write_cache_to_file(cache_filepath, current_cache)
            return response_text


        except requests.exceptions.RequestException as e:
            print(f"\nThere is error on communication with server: {e}")
            return None
        except json.JSONDecodeError:
            print("\nERROR: Server did not return valid JSON.")
            return None




sinonym_to_search = input("Enter word to search sinonym for: ")
query_params = {
    "rel_syn": sinonym_to_search,
    "max": 5
}

print(get_with_caching(BASE_URL, query_params, cache_filepath=file_cache_path))
print("============================================================")
print(get_with_caching(BASE_URL, query_params, cache_filepath=file_cache_path))