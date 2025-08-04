import  turtle


wn = turtle.Screen()
wn.title("My first turtle!")
wn.bgcolor("darkgreen")

tess = turtle.Turtle()
tess.color("gold")
tess.shape("turtle")
tess.pensize(3)


tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(100)


wn.mainloop()