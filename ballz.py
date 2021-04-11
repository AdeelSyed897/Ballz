import turtle
import random
from Square import Square
from Ball import Ball
import math

canvas = turtle.getcanvas()

#scren setting
screen = turtle.Screen()
screen.setup(550,750)
screen.bgcolor('black')


#board making
board = turtle.Turtle()
board.penup()
board.speed(0)
board.goto(-250,-350)
board.pendown()
board.pensize(3)
board.color('white')
board.goto(250,-350)
board.goto(250,350)
board.goto(-250,350)
board.goto(-250,350)
board.goto(-250,-350)
board.ht()



for i in range(random.randint(1,5)):
    square = Square()

ball = Ball()

xclick = 1
yclick = 1

def getcoordinates():
    turtle.onscreenclick(modifyglobalvariables)

def modifyglobalvariables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)




while True:
    getcoordinates()
    if not (yclick == ball.ball.ycor() and xclick == ball.ball.xcor()):
        opp = abs(yclick - ball.ball.ycor())
        adj = abs(xclick - ball.ball.xcor())
        angle = (math.atan(opp/adj) * 180)/math.pi
        if angle < 90:
            angle += 90
        print(angle)
        ball.ball.setheading(angle)
    

