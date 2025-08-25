def greeting(name: str , greeting = "Hello ", excl = "!") -> str:
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl='!!!'))