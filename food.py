import random
import pygame

RED = (255, 0, 0)


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 14)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(
            self.x * 40, self.y * 40, 40, 40))

    def check_collision(self, snake):
        if self.x == snake.x and self.y == snake.y:
            self.move()
            snake.length += 1
            return True
        return False
