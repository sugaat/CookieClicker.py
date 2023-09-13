# Cookie Clicker
# @TokyoEdtech
# https://www.youtube.com/watch?v=jXx3acg34S0&t=579s

import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker by @TokyoEdtech")
wn.bgcolor("black")

# introduces the image to the file
wn.register_shape("cookie.gif")

# turtle object:
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)
# animation speef of turtle module
# default appears at the center

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

# function sends x and y coordinates
def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
    
cookie.onclick(clicked)

wn.mainloop()