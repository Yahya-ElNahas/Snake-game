class Snake:
    def __init__(self):
        self.size = 1
        x = 1
        y = 1
        self.dirX = 0
        self.dirY = 0
        self.body = [Body(x, y)]

    def incr(self):
        x = self.body[-1].x - self.dirX
        y = self.body[-1].y - self.dirY
        b = Body(x, y)
        self.body.append(b)
        self.size += 1

    def move(self):
        self.moveBody(len(self.body) - 1)
        self.body[0].x += self.dirX
        self.body[0].y += self.dirY

    def changeDirection(self, dirX, dirY):
        if(self.dirX + dirX != 0):
            self.dirX = dirX
        if(self.dirY + dirY != 0):
            self.dirY = dirY
    
    def moveBody(self, i):
        if(i == 0):
            return
        self.body[i].x = self.body[i - 1].x
        self.body[i].y = self.body[i - 1].y
        self.moveBody(i - 1)

    def checkPosition(self, x, y):
        for i in range(0, len(self.body)):
            if x == self.body[i].x and y == self.body[i].y:
                return True
        return False
    
    def checkCollision(self):
        for i in range(1, len(self.body)):
            if self.body[0].x == self.body[i].x and self.body[0].y == self.body[i].y:
                return True
        return False

class Body:
    def __init__(self, x, y):
        self.x = x
        self.y = y
