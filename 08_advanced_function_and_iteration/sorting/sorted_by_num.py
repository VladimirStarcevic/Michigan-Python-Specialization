nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(str_in: str) -> str:
    return str_in[-1]

nums_sorted = sorted(nums, key=last_char, reverse=True)
print(nums_sorted)