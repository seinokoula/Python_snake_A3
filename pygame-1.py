import sys
import pygame
import random
import time


class Snake:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.length = 1
        self.body = [(self.x, self.y)]

    def move(self):
        if self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'right':
            self.x += 1

        self.body.insert(0, (self.x, self.y))
        self.body = self.body[:self.length]

    def check_collision(self, food):
        if self.x == food.x and self.y == food.y:
            self.length += 1
            food.move()

    def check_wall_collision(self):
        if self.x < 0 or self.x > 19 or self.y < 0 or self.y > 14:
            return True
        return False

    def check_self_collision(self):
        if (self.x, self.y) in self.body[1:]:
            return True
        return False


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 14)


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake A3 Python')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
snake = Snake(10, 10, 'up')
food = Food(5, 5)
speed = 10


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_UP:
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN:
                snake.direction = 'down'
            elif event.key == pygame.K_LEFT:
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                snake.direction = 'right'
            elif event.key == pygame.K_y:
                snake = Snake(10, 10, 'up')
                food = Food(5, 5)
                break
            elif event.key == pygame.K_n:
                pygame.quit()
                sys.exit()

    screen.fill(BLACK)

    for pos in snake.body:
        pygame.draw.rect(screen, WHITE, pygame.Rect(
            pos[0] * 40, pos[1] * 40, 40, 40))
    pygame.draw.rect(screen, RED, pygame.Rect(
        food.x * 40, food.y * 40, 40, 40))

    snake.check_collision(food)
    if snake.check_wall_collision() or snake.check_self_collision():
        break

    snake.move()

    pygame.display.flip()

    clock.tick(5)

font = pygame.font.SysFont('Poppins', 30)
text = font.render('Score: ' + str(snake.length - 1), True, WHITE)
text_rect = text.get_rect()
text_rect.center = (400, 300)
screen.blit(text, text_rect)
pygame.display.flip()

high_score = 0
if snake.length - 1 > high_score:
    high_score = snake.length - 1
    text = font.render('High Score: ' + str(high_score), True, BLUE)
    text_rect = text.get_rect()
    text_rect.center = (400, 350)
    screen.blit(text, text_rect)
    pygame.display.flip()

font = pygame.font.SysFont('Poppins', 30)
text = font.render('Play Again? (y/n)', True, WHITE)
text_rect = text.get_rect()
text_rect.center = (400, 400)
screen.blit(text, text_rect)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                snake = Snake(10, 10, 'up')
                food = Food(5, 5)
                break
            elif event.key == pygame.K_n:
                pygame.quit()
                sys.exit()

# pygame.time.wait(5000)
# pygame.quit()
