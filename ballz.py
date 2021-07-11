import turtle

import random
from Square import Square
from Threadtester import Threadtester
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

ball = Ball()

ball.ball.speed(0)

def shoot():
  ball.ball.forward(15)
  if ball.ball.xcor() > 240:
    changeBallDirection(ball.ball)
  if ball.ball.xcor() < -240:
    changeBallDirection(ball.ball)
  if ball.ball.ycor() > 340:
    changeBallDirection(ball.ball, "topBound")
  if ball.ball.ycor() < -330:
    return False
  for tile in Square.tiles:
    for side in tile[1]:
      if side[0] <= ball.ball.xcor() <= side[1] and side[2] <= ball.ball.ycor() <= side[3]:
        changeBallDirection(ball.ball)
        print('it half worked')
  return True



def changeBallDirection(ball, context=None):
  ballHeading = ball.heading()

  if context == "topBound" or context == "bottomBound":
    ball.setheading(360 - ballHeading)
  elif 0 <= ballHeading < 180:
    ball.setheading(180 - ballHeading)
  elif 180 <= ballHeading < 360:
    ball.setheading(540 - ballHeading)

for i in range(random.randint(1,5)):
    square = Square()



xclick = 1
yclick = 1

def getcoordinates():
    turtle.onscreenclick(modifyglobalvariables)


def modifyglobalvariables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)
    


thread = Threadtester(ball.ball)
thread.start()



ball.ball.left(30)
##while True:
##  ball.ball.forward(10)
##  if ball.ball.xcor() > 240:
##    changeBallDirection(ball.ball)
##  if ball.ball.xcor() < -240:
##    changeBallDirection(ball.ball)
##  if ball.ball.ycor() > 340:
##    print(ball.ball.heading())
##    changeBallDirection(ball.ball, "topBound")
##  #if ball.ball.ycor() == -336:





getcoordinates()
i = 0
while True:
    if ball.ball.ycor() == -336 and Threadtester.moving:
      Square.moveDown()
    print('------------------------------------------')
  
    print(Threadtester.moving)
    print('i', i)
    
    if not (yclick == ball.ball.ycor() and xclick == ball.ball.xcor()):
      if not Threadtester.moving or i < 10:
        print(xclick, yclick)

        opp = abs(yclick - ball.ball.ycor())
        adj = abs(xclick - ball.ball.xcor())
        angle = (math.atan(opp/adj) * 180)/math.pi
        if xclick < 0:
          angle = 90+(90-angle)
        ball.ball.setheading(angle)
        print('angle', angle)
        print(xclick, yclick)
        Threadtester.var = True
    if xclick != 1 and yclick != 1:
      result = shoot()
      if result:
        pass
      else:
        break
    i+=1


    
  
    
  
