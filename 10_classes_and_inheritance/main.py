from config_manager import ConfigManager


config_path = "data/config.json"

manager = ConfigManager(config_path)
print(manager)

manager.load_config()

print("\nLoaded Data:")
print(manager.data)

print("\n--- Testing get_value method ---")

api_timeout = manager.get_value("api_settings.timeout")
print(f"API Timeout: {api_timeout}")


retry_count = manager.get_value("api_settings.retries.count")
print(f"Retry Count: {retry_count}")

non_existent = manager.get_value("database.user.password")
print(f"Non-existent value: {non_existent}")

print("\n--- Testing recursive find_first method ---")
retry_count_rec = manager.find_first("count")
print(f"Recursively found 'count': {retry_count_rec}")

db_path_rec = manager.find_first("path")
print(f"Recursively found 'path': {db_path_rec}")

