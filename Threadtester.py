import time
import threading

class Threadtester (threading.Thread):
    moving = False
    def __init__(self, ball):
        threading.Thread.__init__(self)
        self.ball = ball
        self.prevXCor = self.ball.xcor()
        self.prevYCor = self.ball.ycor()
        

    def run(self):
        while True:
            time.sleep(0.01)
            #print(self.prevXCor)
            #print(self.ball.xcor())
            if self.prevXCor != self.ball.xcor() or self.prevYCor != self.ball.ycor():
                Threadtester.moving = True
                self.prevXCor = self.ball.xcor()
                self.prevYCor = self.ball.ycor()
            #if self.prevXCor == self.ball.xcor():
                #Threadtester.moving = False
                



