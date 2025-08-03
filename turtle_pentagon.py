import turtle

wn = turtle.Screen()
wn.title("Turtle Pentagon")
wn.bgcolor("darkgreen")

hillary = turtle.Turtle()
hillary.color("yellow")
hillary.shape("turtle")
hillary.pensize(3)


for _ in range(5):
    hillary.forward(100)
    hillary.right(72)



