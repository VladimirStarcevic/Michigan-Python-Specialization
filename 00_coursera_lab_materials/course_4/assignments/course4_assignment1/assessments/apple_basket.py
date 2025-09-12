class AppleBasket:
    color: str
    quantity: int

    def __init__(self, apple_color, apple_quantity):
        self.color = apple_color
        self.quantity = apple_quantity


    def increase(self):
        self.quantity += 1


    def __str__(self):
        return f"A basket of {self.quantity} {self.color} apples."

green_apple = AppleBasket("green", 20)
for i in range(10):
    green_apple.increase()

print(green_apple)