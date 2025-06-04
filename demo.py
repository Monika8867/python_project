import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral Drawing")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# List of colors to use
colors = ["red", "blue", "green", "yellow", "cyan", "magenta", "orange", "white"]

# Drawing a spiral pattern
for i in range(200):
    pen.color(random.choice(colors))  # Random color
    pen.forward(i * 2)                # Move forward
    pen.left(59)                      # Turn left
    pen.circle(i / 10)                # Draw a small circle

# Hide turtle and keep window open
pen.hideturtle()
screen.mainloop()

