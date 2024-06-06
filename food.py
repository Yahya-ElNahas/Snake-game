import random
from util import *

class Food:
    def __init__(self):
        self.generate()

    def generate(self):
        x = random.randint(0, Game_WIDTH / TILE_SIZE - 1)
        y = random.randint(0, Game_HEIGHT / TILE_SIZE - 1)
        self.x = x
        self.y = y

    def move(self, snake):
        x = random.randint(0, Game_WIDTH / TILE_SIZE - 1)
        y = random.randint(0, Game_HEIGHT / TILE_SIZE - 1)
        while snake.checkPosition(x, y):
            x = random.randint(0, Game_WIDTH / TILE_SIZE - 1)
            y = random.randint(0, Game_HEIGHT / TILE_SIZE - 1)
        self.x = x
        self.y = y
