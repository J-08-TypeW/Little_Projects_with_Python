import turtle
import random
from turtle import *

bgcolor("lightblue")
screen = turtle.Screen()
screen.setup(800, 600)

nieve = turtle.Turtle()
nieve.shape("circle")
nieve.color("white")
nieve.speed("fastest")
nieve.up()

for m in range(100):
    corrdd = random.randint(-700,500)
    cooor = random.randint(-700,500)
    nieve.goto(corrdd,cooor)
    nieve.stamp()

circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()

square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()

circle.goto(0, 280)
circle.stamp()

k = 0
for i in range(1, 17):
    y = 30 * i
    for j in range(i - k):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()

    if i % 4 == 0:
        x = 30 * (j + 1)
        circle.color('red')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()
        k += 2

    if i % 4 == 3:
        x = 30 * (j + 1)
        circle.color('yellow')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()

square.color('brown')
for i in range(17, 20):
    y = 30 * i
    for j in range(3):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()

turtle.color("red")
texto = "Feliz Navidad :D"
turtle.up()
turtle.goto(0,280)
turtle.write(texto, align="center", font=("Arial", 50, "bold"))

turtle.color("lime")
texto2 = "Les desea Python B)"
#texto.goto(0, -700)
turtle.goto(0,-350)
turtle.write(texto2, align="center", font=("Arial", 50, "bold"))


turtle.exitonclick()
