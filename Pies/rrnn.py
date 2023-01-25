from random import randrange as rn
from random import choice as rc
import pygame
import sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption('Stars')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF.fill(BLACK)

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
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



