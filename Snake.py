import pygame
import random
import time
import keyboard
import sys
pygame.init()

score=0
win_x,win_y=500,560
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((win_x,win_y))

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def drawScore():
    global startTime
    pygame.draw.rect(screen, (211, 238, 255), (0,0,win_x,60))
    pygame.draw.rect(screen, (0,0,0), (1, 1, win_x-2, 58), 1)


    font = pygame.font.Font("C:\Windows\Fonts\ARIALUNI.TTF", 32)
    text = font.render('Score: {}'.format(score), True, (0, 0, 0), (255,255,255))
    textRect = text.get_rect()
    textRect.center = (win_x/2, 30)
    screen.blit(text, textRect)

    gameTime=round(t1-startTime)
    if gameTime//60 >=1:
        m=gameTime//60
        text = font.render('Time: {}:{:0<2d}'.format(m,gameTime-m*60), True, (0, 0, 0), (255, 255, 255))
    else:
        text = font.render('Time: 0:{:0>2d}'.format(gameTime), True, (0, 0, 0), (255,255,255))

    textRect = text.get_rect()
    textRect.center = (100, 30)
    screen.blit(text, textRect)


def drawBoard():
    screen.fill((146, 255, 141))

    for x in range(0,win_x,40):
        for y in range(0,win_y,40):
            pygame.draw.rect(screen, (215, 255, 190), (x,y,20,20))
    for x in range(20,win_x,40):
        for y in range(20,win_y,40):
            pygame.draw.rect(screen, (215, 255, 190), (x,y,20,20))

class Snake:
    def __init__(self):
        self.x = 240
        self.y = 240
        self.grow = False
        self.position = [[240,280],[240,260],[240,240]]


    def draw(self):
        for index,i in enumerate(reversed(self.position)):
            if index==0:
                pygame.draw.rect(screen, (0, 0, 255), (i[0], i[1], 20, 20))
            else:
                pygame.draw.rect(screen, (0, 0,0), (i[0]-1, i[1]-1, 22, 22))
                pygame.draw.rect(screen, (0,255,255), (i[0], i[1], 20,20))

    def collider(self, lunch):
        pos = self.position[len(self.position) - 1]
        if pos[0] == lunch[0] and pos[1] == lunch[1]:
            return True
        return False

    def colliderAll(self, lunch, positions):
        for pos in positions:
            if pos[0]==lunch[0] and pos[1]==lunch[1]:
                return True
        return False


snake = Snake()

direction = 0
t=time.time()

lunch = [random.randrange(0,480,20),random.randrange(100,480,20)]
Start=False

startTime=time.time()
t1 = time.time()
drawBoard()
drawScore()
snake.draw()
pygame.display.update()

while not Start:
    quit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        direction=0
        Start=True
    elif keys[pygame.K_DOWN]:
        direction = 1
        Start = True
    elif keys[pygame.K_LEFT]:
        direction = 2
        Start = True
    elif keys[pygame.K_RIGHT]:
        direction = 3
        Start = True

startTime=time.time()
while Start:

    t1=time.time()
    drawBoard()
    drawScore()
    quit()

    keys = pygame.key.get_pressed()

    if keyboard.is_pressed('p'):
        continue

    if keys[pygame.K_UP]:
        direction=0
    elif keys[pygame.K_DOWN]:
        direction = 1
    elif keys[pygame.K_LEFT]:
        direction = 2
    elif keys[pygame.K_RIGHT]:
        direction = 3


    if t + .10 < t1:
        snakePos = snake.position[len(snake.position)-1]
        # if direction == 0:
        #     snake.position.append([snakePos[0],snakePos[1]-20])
        # elif direction == 1:
        #     snake.position.append([snakePos[0],snakePos[1]+20])
        # elif direction == 2:
        #     snake.position.append([snakePos[0]-20,snakePos[1]])
        # else:
        #     snake.position.append([snakePos[0]+20,snakePos[1]])
        x,y=0,0
        if direction == 0:
            y-=20
        elif direction == 1:
            y+=20
        elif direction == 2:
            x-=20
        else:
            x+=20

        snakePos=[snakePos[0]+x, snakePos[1]+y]
        snake.position.append(snakePos)

        if snake.colliderAll(snakePos, snake.position[:-1]) or snakePos[0]+20>win_x or snakePos[0]<0 or snakePos[1]+20>win_y or snakePos[1]<60:
            print("Youe are deid")
            time.sleep(1)
            exit(0)

        if snake.collider(lunch):
            n=lunch
            score +=1
            while snake.colliderAll(lunch, snake.position) or lunch==n:
                lunch = [random.randrange(0,480,20),random.randrange(100,480,20)]
        else:
            del snake.position[0]

        t = time.time()



    pygame.draw.rect(screen, (255,100,0), (lunch[0], lunch[1], 20 ,20))
    snake.draw()
    pygame.display.update()
