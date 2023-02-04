import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("red")



#colors = colorgram.extract("download.jpg", 13)
#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #choice = (r, g, b)
    #colorChoice.append(choice)
#print(colorChoice)


colours = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]


for i in range(5):
    tim.forward(i*20)
    tim.setheading(0)
    tim.showturtle()
    for _ in range(10):
        tim.color(random.choice(colours))
        tim.pendown()
        tim.dot(15)
        tim.penup()
        tim.forward(30)
    tim.hideturtle()
    tim.home()
    tim.setheading(90)













screen = Screen()
screen.exitonclick()