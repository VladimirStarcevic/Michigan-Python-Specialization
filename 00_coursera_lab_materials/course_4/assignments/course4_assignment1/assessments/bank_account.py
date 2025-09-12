class BankAccount:
    __name: str
    __amt: int

    def __init__(self, initial_name: str, initial_amount: int):
        self.__name = initial_name
        self.__amt = initial_amount

    def __str__(self):
        return f"Your account, {self.__name}, has {self.__amt} dollars."

t1 = BankAccount("Bob", 100)
print(t1)