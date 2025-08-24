import turtle
import random
def is_in_screen(w, t):
    left_bound = -w.window_width() / 2
    right_bound = w.window_width() / 2
    top_bound = w.window_height() / 2
    bottom_bound = -w.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    stillIn = True
    if turtle_x > right_bound or turtle_x < left_bound:
        stillIn = False

    if turtle_y > top_bound or turtle_y < bottom_bound:
        stillIn = False

    return stillIn


wn = turtle.Screen()
wn.bgcolor("black")
hillary = turtle.Turtle()
hillary.color("pink")
hillary.shape("turtle")

while is_in_screen(wn, hillary):
    random_num = random.randint(0, 1)

    if random_num == 0:
        hillary.left(90)
    else:
        hillary.right(90)

    hillary.forward(25)
wn.exitonclick()