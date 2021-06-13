import turtle
import random
class Square:
    
    colors = ['red','green','blue','orange','purple']
    coords = [ [(-200,300), None], [(-100, 300,), None], [(0, 300), None], [(100,300), None], [(200,300), None]]
    tiles = []
    def __init__(self):
        tile = turtle.Turtle()
        tile.penup()
        tile.speed(0)
        tile.color('white',Square.colors[random.randint(0,4)])
        tile.shape('square')
        tile.shapesize(5,5)
        Square.tiles.append(tile)
        condition = True
        while condition:
            x = random.randint(0,4)
            y = Square.coords[x]
            if y[1] is None:
                tile.clear()
                tile.goto(y[0])
                tile.write('50',align = 'center',font=("Arial", 30))
                y[1] = 1
                condition = False

    @staticmethod
    def moveDown():
        if tiles.ycor() != -300:
            for tile in Square.tiles:
                tile.sety(tile.ycor()-100)
            return True
        else:
            return False
