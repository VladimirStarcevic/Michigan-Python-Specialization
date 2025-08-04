import turtle


wn = turtle.Screen()
wn.bgcolor("black")

painter = turtle.Turtle()
painter.shape("turtle")
painter.color("white")

painter.speed(2)
colors = ["red", "yellow", "blue", "orange", "green", "purple"]

for i in range(36):
    painter.color(colors[i % 6])
    painter.circle(100)
    painter.right(10)


painter.hideturtle()
wn.mainloop()

