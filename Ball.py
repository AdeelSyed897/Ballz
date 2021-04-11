import turtle
import random

class Ball:
    balls = []
    colors = ['red','green','blue','orange','purple']
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.color('white', random.choice(Ball.colors))
        self.ball.penup()
        self.ball.speed(1)
        self.ball.shape('square')
        self.ball.sety(-335)
        Ball.balls.append(self)
