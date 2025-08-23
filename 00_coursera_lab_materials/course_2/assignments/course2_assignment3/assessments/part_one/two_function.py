def divide(num: int | float) -> int | float:
    return num / 2

def add(num: int | float) -> int | float:
    div_by_two = divide(num)
    return div_by_two + 6

num1 = 10

result = add(num1)
print(f"Result: {result}")