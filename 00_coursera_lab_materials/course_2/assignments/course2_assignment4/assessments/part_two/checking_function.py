from typing import Dict, Union

def checking_if_in(str_in: str, direction = True, d = None) -> Union[int, bool, None]:
    if d is None:
        d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}

    if direction:
        if str_in in d:
            return True
        else:
            return False
    else:
        if str_in not in d:
            return True
        else:
            return False



