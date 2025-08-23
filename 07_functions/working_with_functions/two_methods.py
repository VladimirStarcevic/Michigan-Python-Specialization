
def addit(num: int | float) -> int | float:
    return num + 5

def mult(num: int | float) -> int | float:
    result = addit(num) * num
    return result

output = mult(10)
print(f"Result  is : {output}")

