from typing import Union

def mult(num1: int, multiplier: Union[int, float, str] = 6) -> Union[int, float, str]:
    return num1 * multiplier

print(mult(5))
print(mult(5, 10))
print(mult(5, "A"))
print(mult(3, "Go"))