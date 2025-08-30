# Extract the value associated with the key color and assign it to the variable color. Do not hard code this.
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

info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }


color = find_key_universal(info, 'color')
print(type(color))
print(color)

