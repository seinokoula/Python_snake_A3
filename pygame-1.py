import sys
import pygame


from snake import Snake
from food import Food

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake A3 Python')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
snake = Snake(10, 10, 'up')
food = Food(5, 5)
speed = 5
game = True
while True:

    while game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
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
                elif snake.length > 1:
                    speed += 1
                elif snake.length > 2:
                    speed += 2
                elif snake.length > 3:
                    speed += 3

        screen.fill(BLACK)

        for pos in snake.body:
            pygame.draw.rect(screen, WHITE, pygame.Rect(
                pos[0] * 40, pos[1] * 40, 40, 40))
        pygame.draw.rect(screen, RED, pygame.Rect(
            food.x * 40, food.y * 40, 40, 40))

        for i in range(21):
            pygame.draw.line(screen, GREY, (i * 40, 0), (i * 40, 600))
        for i in range(16):
            pygame.draw.line(screen, GREY, (0, i * 40), (800, i * 40))

        snake.check_collision(food)
        if snake.check_wall_collision() or snake.check_self_collision():
            break

        snake.move()

        pygame.display.flip()
        pygame.display.update()

        clock.tick(speed)

    font = pygame.font.SysFont('Poppins', 30)
    text = font.render('Score: ' + str(snake.length - 1), True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (400, 250)
    screen.blit(text, text_rect)
    pygame.display.flip()

    score = 0
    high_score = 0
    if snake.length - 1 > score:
        score = snake.length - 1
        text = font.render('High Score: ' + str(score), True, BLUE)
        text_rect = text.get_rect()
        text_rect.center = (400, 300)
        screen.blit(text, text_rect)
        pygame.display.flip()

    if score > high_score:
        high_score = score
        text = font.render('High Score: ' + str(high_score), True, BLUE)
        text_rect = text.get_rect()
        text_rect.center = (400, 300)
        screen.blit(text, text_rect)
        pygame.display.flip()

    font = pygame.font.SysFont('Poppins', 30)
    text = font.render('Play Again? yes press y and quit press n', True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (400, 350)
    screen.blit(text, text_rect)
    pygame.display.flip()
    stop = True
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_y:
                    snake = Snake(10, 10, 'up')
                    food = Food(5, 5)
                    game = True
                    stop = False
                    break
