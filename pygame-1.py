import sys
import pygame
import random
import time

from snake import Snake
from food import Food


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
