import random

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 14)
