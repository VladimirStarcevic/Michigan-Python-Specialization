import json
import time
from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"--- Starting {func.__name__}... ---")
        result = func(self, *args, **kwargs)
        print(f"--- Finished {func.__name__} ---")
        return result
    return wrapper

def measure_time(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Execution of {func.__name__} took {duration:.4f} seconds.")
        return result
    return wrapper

class ConfigManager:
    config_path: str

    def __init__(self, config_path):
        self.config_path = config_path
        self.data = {}

    @measure_time
    @log_activity
    def load_config(self):

        try:
            with open(self.config_path, "r", encoding='UTF-8') as file_in:
                file_data = file_in.read()

                self.data = json.loads(file_data)
                print("Config loaded successfully!")


        except FileNotFoundError:
            print(f"ERROR: Configuration file not found at: {self.config_path}")
        except json.JSONDecodeError:
            print(f"ERROR: Could not decode JSON from file: {self.config_path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_value(self, key_string):
        key_string_list = key_string.split(".")
        current_level = self.data
        for key in key_string_list:
            current_level = current_level.get(key)
            if current_level is None:
                return None
        return current_level

    def find_first(self, key_to_find):
        return _find_key_recursive(self.data, key_to_find)



    def __str__(self):
        return f"Configuration Manager for file: {self.config_path}"

def _find_key_recursive(data_dict, key_to_find):
    if key_to_find in data_dict:
        return data_dict[key_to_find]
    for key, value in data_dict.items():
        if isinstance(value, dict):
            result = _find_key_recursive(value, key_to_find)
            if result is not None:
                return result

    return None

