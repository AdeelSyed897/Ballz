import time
import threading
from Square import Square

class CollisionThread (threading.Thread):
    moving = False
    def __init__(self, ball):
        threading.Thread.__init__(self)
        self.ball = ball
        self.prevXCor = self.ball.xcor()
        self.prevYCor = self.ball.ycor()
        

    def run(self):
        while True:
            time.sleep(0.01)
            for tile in Square.tiles:
                for side in tile[1]:
                  print('ball coords', self.ball.xcor(), self.ball.ycor())
                  print('side', side)
                  print('------------------------------')
                  if side[0] <= self.ball.xcor() <= side[1] and side[2] <= self.ball.ycor() <= side[3]:
                    changeBallDirection(self.ball)
                    print('it half worked')
            if self.ball.ycor() < -335:
                break
                

