import pygame
from sys import exit 
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode(((1020,720)))
background = 'gray'
clock = pygame.time.Clock()

class girl:
    def __init__(info,nb_life,nb_bomb,xp,lvl):
         info.nb_life = nb_life 
         info.nb_bomb = nb_bomb
         info.xp = xp 
         info.lvl = lvl
    def __str__(info):
        return f"Life : {info.nb_life}\n Bomb : {nb_bomb} \n Power :{info.xp}"

x = 400
y= 200
rad = 5
vel = 7
shiftvel = 3

projvel = 8
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clef = pygame.key.get_pressed()
    if clef[pygame.K_w]:
        ...
    if clef[pygame.K_LEFT] and x > rad:
        if clef[pygame.K_LSHIFT]:
            x-= shiftvel
        else:
            x -= vel 
    if clef[pygame.K_RIGHT] and x<1020-rad: 
        if clef[pygame.K_LSHIFT]:
            x += shiftvel
        else:
            x += vel 
    if clef[pygame.K_UP] and y>rad:           
        if clef[pygame.K_LSHIFT]:
            y -= shiftvel
        else:
            y -= vel 
    if clef[pygame.K_DOWN] and y<720-rad: 
        if clef[pygame.K_LSHIFT]:
            y += shiftvel
        else:
            y += vel 
    
    screen.fill(background)
    pygame.draw.circle(screen, 'red', [x,y], rad) 
    pygame.display.update()
    clock.tick(60)
