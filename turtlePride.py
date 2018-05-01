#!/home/leah
import turtle
sally = turtle.Turtle()
a = 12
sally.width(6)
colors = ["red", "pink", "yellow", "green", "purple", "blue", "orange" ]

for i in range (0, 50):
    for items in colors:
        sally.pencolor(items)
        sally.forward(a)
        sally.right(90)
        sally.forward(a)
        sally.pencolor(items)
        a += 2

# import turtle
#
# silly = turtle.Turtle()
#
# silly.forward(50)
# silly.right(90)     # Rotate clockwise by 90 degrees
#
# silly.forward(50)
# silly.right(90)
#
# silly.forward(50)
# silly.right(90)
#
# silly.forward(50)
# silly.right(90)
#
# turtle.done()
