import json
from typing import Dict, List, Any

def find_key_universal(data: Dict | List, target_key: str) -> Any:

    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                return value
            result = find_key_universal(value, target_key)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_key_universal(item, target_key)
            if result is not None:
                return result
    return None

def update_users_status(user_data: dict, key_to_update: str, value_to_add: int):

    if key_to_update in user_data:
        user_data[key_to_update] += value_to_add
    else:
        print(f"Warning: Key '{key_to_update}' not found for this user.")

def interactive_update_session(user_data: dict):
    print("--- Starting interactive update session ---")
    print("Enter 'key value' to update (e.g., 'tweets 5'), or 'END' to finish.")

    while True:

        command = input("> ")
        if command.upper() == "END":
            print("--- Session finished ---")
            break

        try:
            key, value_str = command.split()
            value = int(value_str)
            update_users_status(user_data, key, value)
            print("Updated data:", user_data)
        except ValueError:
           print("Invalid format. Please use 'key value' (e.g., 'tweets 5').")



userProfilesString = '{"profiles": \n{"Iman"\n\n: {"tweets": 450, "likes": 2500, "followers": 190, "following": 300},\n\n"Allan"\n\n: {"tweets": 200, "likes": 700, "followers": 150, "following": 100},\n\n"Xinyan"\n\n: {"tweets": 1135, "likes": 3000, "followers": 400, "following": 230},\n\n"Hao"\n\n: {"tweets": 645, "likes": 800, "followers": 300, "following": 500},\n"Harman"\n\n: {"tweets": 300, "likes": 1750, "followers": 200, "following": 400}}}'


user_profiles_data = json.loads(userProfilesString)
assert isinstance(user_profiles_data, dict)

iman_data = find_key_universal(user_profiles_data, "Iman")
if iman_data:
    interactive_update_session(iman_data)
allan_data = find_key_universal(user_profiles_data, "Allan")
if allan_data:
    interactive_update_session(allan_data)
xinyan_data = find_key_universal(user_profiles_data, "Xinyan")
if xinyan_data:
    interactive_update_session(xinyan_data)

updated_json_string = json.dumps(user_profiles_data, sort_keys=True, indent=4)
print(updated_json_string)




