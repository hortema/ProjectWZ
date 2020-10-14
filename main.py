import pygame as pg
import sys

from sys import path
from sys import exit
import os

from pygame.locals import QUIT

# setup path information for python to find files by name
my_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(my_path)
path.append(my_path)

# preset screen size is 800 x 600
screenx = 800
screeny = 600

# start pygame, open a screen with preset size.
pg.init()
screen = pg.display.set_mode((screenx,screeny)) #set your window size, (x,y)
pg.display.set_caption("Let's get scrolling!!!")

clock = pg.time.Clock()

#load background image and show on screen
bg = pg.image.load("GiantBackground.png")

bgx = 0
bgy = 0

while True:
    QUIT = False

    for event in pg.event.get():
        if event.type == pg.locals.QUIT:
            QUIT = True

    screen.blit(bg, (bgx,bgy))
    pg.display.flip()
    clock.tick(30)
    
    if QUIT == True:
        pg.quit()
        break
