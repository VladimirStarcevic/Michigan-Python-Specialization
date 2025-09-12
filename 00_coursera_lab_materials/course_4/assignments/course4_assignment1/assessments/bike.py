class Bike:
    price: float
    color: str

    def __init__(self, price, color):
        self.price = price
        self.color = color

    def get_price(self):
        return self.price

    def get_color(self):
        return self.color

    def set_price(self, new_price):
        if new_price == 0 or new_price < 0:
            print("Price must be positive number. Please enter correct number.")
            return

        self.price = new_price

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return f"Bike color: {self.color}\nPrice: {self.price}"


testOne = Bike(89.99,"blue")
testTwo = Bike(25.0,"purple")

print(testOne)
print(testTwo)


