from typing import Dict, Union


def check_key(test_key: int, check: bool = True, dict1: Dict = None) -> Union[int, bool, None]:
    if dict1 is None:
        dict1 = {2: 3, 4: 5, 6: 8}

    if not check:
        return False
    return dict1.get(test_key)


print(check_key(2))


