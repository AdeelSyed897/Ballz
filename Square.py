import turtle
import random
class Square:
    
    colors = ['red','green','blue','orange','purple']
    coords = [[(-200,300), None], [(-100, 300,), None], [(0, 300), None], [(100,300), None], [(200,300), None]]
    #edges = [ [ [-150,-250, 250,250], [-250,-250,250,350], [], [] ] ]
    tiles = []
    def __init__(self):
        #bob = turtle.Turtle()
        #bob.goto(-200,250)
        tile = turtle.Turtle()
        tile.penup()
        tile.speed(0)
        tile.color('white',Square.colors[random.randint(0,4)])
        tile.shape('square')
        tile.shapesize(5,5)
        condition = True
        while condition:
            x = random.randint(0,4)
            y = Square.coords[x]
            print('y[0][0]', y[0][0])
            print('y[0][1]', y[0][1])
            Square.tiles.append([tile, Square.calcEdges(y[0][0], y[0][1]) ])
            if y[1] is None:
                tile.clear()
                tile.goto(y[0])
                tile.write('50',align = 'center',font=("Arial", 30))
                y[1] = 1
                condition = False
        print(Square.tiles)

    @staticmethod
    def moveDown():
        for tile in Square.tiles:
            if tile.ycor() != -300:
                tile.sety(tile.ycor()-100)
            return True
        else:
            return False
    @staticmethod
    def calcEdges(x, y): #-200, 250
        edges = []
        #top
        x1 = x-50 #-150
        y1 = y+50 #300
        x2 = x+50 #-250
        y2 = y+50 # 300

        edges.append( [x1, x2, y1, y2] )


        #right
        x1 = x+50 #-150
        y1 = y-50 #300
        x2 = x+50 #-250
        y2 = y+50 # 300

        
        edges.append( [x1, x2, y1, y2] )


        #bottom
        x1 = x-50 #-150
        y1 = y-50 #300
        x2 = x+50 #-250
        y2 = y-50 # 300
        edges.append( [x1, x2, y1, y2] )

        #left
        x1 = x-50 #-150
        y1 = y-50 #300
        x2 = x-50 #-250
        y2 = y+50 # 300
        edges.append( [x1, x2, y1, y2] )
        return edges
    
        
