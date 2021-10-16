import pygame
import random
from collections import Counter

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.update()

gameOver = False

xPos = WIDTH // 2
yPos = HEIGHT // 2

xStep = 0
yStep = 10

STEP = 10
blockSize = 15

snakeColor = [0, 255, 0]
snakeHeadColor = [255, 255, 0]

yellow = [255, 255, 0]
blue = [0, 0, 255]
pink = [255, 98, 226]
foodColor = [255, 0, 0]

clock = pygame.time.Clock()

def getFoodPos(snake):
    found = False
    while not found:
        xFoodPos = round(random.randrange(0, WIDTH - blockSize) / 10) * 10
        yFoodPos = round(random.randrange(0, HEIGHT - blockSize) / 10) * 10
        if not [xFoodPos, yFoodPos] in snake:
            found = True
    return [xFoodPos, yFoodPos]

def checkSnakePos(snake):
    for item in snake:
        if snake.count(item) > 1:
            return True
        
    return False

def drawText(screen, string, pos, color):
    font = pygame.font.SysFont('arial', 15)
    label = font.render(string, 0.5, color)
    screen.blit(label, pos)

snake = []
snakeLength = 1

[xFoodPos, yFoodPos] = getFoodPos(snake)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                xStep = 0
                yStep = - STEP
            elif event.key == pygame.K_DOWN:
                xStep = 0
                yStep = STEP
            elif event.key == pygame.K_LEFT:
                xStep = -STEP
                yStep = 0
            elif event.key == pygame.K_RIGHT:
                xStep = STEP
                yStep = 0
        elif event.type == pygame.QUIT:
            gameOver = True

    if xPos >= WIDTH or xPos < 0 or yPos >= HEIGHT or yPos < 0:
        gameOver = True
    
    xPos += xStep
    yPos += yStep

    snakeHead = [xPos, yPos]
    snake.append(snakeHead)

    if not gameOver:
        gameOver = checkSnakePos(snake)
    
    screen.fill([255, 255, 255])
    pygame.draw.rect(screen, pygame.Color(foodColor), pygame.Rect(xFoodPos, yFoodPos, blockSize, blockSize))

    if len(snake) > snakeLength:
        del snake[0]

    for [xItemPos, yItemPos] in snake:
        pygame.draw.rect(screen, pygame.Color(snakeColor), pygame.Rect(xItemPos, yItemPos, blockSize, blockSize))
    
    for i in range(snakeLength):
        [xItemPos, yItemPos] = snake[i]
        # if i == snakeLength - 1:
        #     pygame.draw.rect(screen, pygame.Color(snakeHeadColor), pygame.Rect(xItemPos, yItemPos, blockSize, blockSize))
        # else:
        #     pygame.draw.rect(screen, pygame.Color(snakeColor), pygame.Rect(xItemPos, yItemPos, blockSize, blockSize))
        if i % 2:
            pygame.draw.rect(screen, pygame.Color(blue), pygame.Rect(xItemPos, yItemPos, blockSize, blockSize))
        else:
            pygame.draw.rect(screen, pygame.Color(pink), pygame.Rect(xItemPos, yItemPos, blockSize, blockSize))


    pygame.display.update()
    checkSnakePos(snake)
    if((abs(xPos - xFoodPos) < blockSize) and (abs(yPos - yFoodPos) < blockSize)):
        [xFoodPos, yFoodPos] = getFoodPos(snake)
        snakeLength += 1

    clock.tick(15)

closedWindow = False
screen.fill([255, 255, 255])

drawText(screen, "Game over", [225, 230], [0,0,0])
pygame.display.update()
while not closedWindow:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closedWindow = True

pygame.quit()