from random import randrange as rn
from random import choice as rc
import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 100  # frames per second setting
fpsClock = pygame.time.Clock()

pygame.mixer.music.load(r'C:\Users\Abid Sheri\Music\Music\TXL\01_-_Wiz_Khalifa_-_Outsiders--(MixJoint.com).mp3')
pygame.mixer.music.play(-1, 0.0)


DISPLAYSURF = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption('Animation')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF.fill(BLACK)

catImg = pygame.image.load('spaceship01.png')
catx = 10
caty = 10
direction = 'right'

liz = []

pixObj = pygame.PixelArray(DISPLAYSURF)

for i in range(1000):
    n = rn(700)
    liz.append(n)
    a = rc(liz)
    b = rc(liz)
    pixObj[a][b] = WHITE

del pixObj

while True:

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
