import pygame
from pygame.locals import *
import random
import sys
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
pygame.init()

win = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Mission 'Game'")


bg = pygame.image.load('Night.png')
x = 630
y = 500 #550
x_map = 630
y_map = 465
x_map2 = 200
y_map2 = 200
x_map3 = 640
y_map3 = 510
width = 40
height = 60
vel = 5

GRAVITY = 0.3

isJump = False
jumpCount = 10
screen = pygame.display.set_mode((1280, 720))

run = True

def redrawGameWindow():
    win.blit(bg, (0,0))
    
def map():
    pygame.draw.rect(win, (156,156,156), (x_map, y_map + 150, 500, 150))
    pygame.draw.rect(win, (156,156,156), (x_map, y_map + 150, -500, 150))
    pygame.draw.rect(win, (156,156,156), (x_map, y_map + 100, 450, 150))
    pygame.draw.rect(win, (156,156,156), (x_map, y_map + 100, -450, 150))
    
def map2():
    pygame.draw.rect(win, (156,156,156), (x_map2, y_map2 - 200, 940, 150))
    pygame.draw.rect(win, (156,156,156), (x_map2, y_map2 - 200, -75, 150))
    
def map3():
    pygame.draw.rect(win, (156,156,156), (x_map3 + 200, y_map3 - 50, 125, 25))
    pygame.draw.rect(win, (156,156,156), (x_map3 - 300, y_map3 - 50, 125, 25))
    pygame.draw.rect(win, (156,156,156), (x_map3 - 40, y_map3 - 150, 125, 25))
    pygame.draw.rect(win, (156,156,156), (x_map3 + 200, y_map3 - 250, 125, 25))
    pygame.draw.rect(win, (156,156,156), (x_map3 - 300, y_map3 - 250, 125, 25))
        
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel

    if keys[pygame.K_RIGHT] and x < 1277 - vel - width:  
        x += vel
        
    if not(isJump): 
        if keys[pygame.K_SPACE]:
            isJump = True
        if keys[pygame.K_SPACE] * 2:
            isJump = True * 2
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    
    
    pygame.draw.rect(win, (255, 255, 255), (x, y, 65, 65))
    pygame.display.update()
    redrawGameWindow()
    map()
    map2()
    map3()

pygame.quit()

