import pygame as pg
import sys
import expy as ex

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

# preset colours
black = (0,0,0)
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 

# start pg, open a screen with preset size.
pg.init()
screen = pg.display.set_mode((screenx,screeny)) #set your window size, (x,y)
pg.display.set_caption("Let's get scrolling!!!")

clock = pg.time.Clock()

#load background image and show on screen
bg = pg.image.load("bgbgbg.png")
player = pg.image.load("Player.png")

fps = 60

bgx = 0
bgy = 0

#def update():
 

while True:
    QUIT = False

    #inputs
    mx,my = pg.mouse.get_pos()
    L,M,R = pg.mouse.get_pressed() #1/0 : 1-pressed
    keys = pg.key.get_pressed()

    #update()
    
    if keys[pg.K_d] ==True:
        bgx -= 5
    if keys[pg.K_a] ==True:
        bgx += 5
    if keys[pg.K_s] ==True:
        bgy -= 5
    if keys[pg.K_w] ==True:
        bgy += 5

    for event in pg.event.get():
        if event.type == pg.locals.QUIT:
            QUIT = True
            
    screen.fill(black)
    screen.blit(bg, (bgx,bgy))
    pg.display.flip()
    clock.tick(fps)

    if QUIT == True:
        pg.quit()
        break
